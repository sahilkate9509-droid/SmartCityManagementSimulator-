using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

/// <summary>
/// Production API client for Smart City Management Simulator.
/// Connects to the FastAPI / PostgreSQL cloud backend for cloud save/load,
/// simulation telemetry tracking, and database synchronization.
/// </summary>
public class CityApiClient : MonoBehaviour
{
    public static CityApiClient Instance { get; private set; }

    const string PREF_API_URL = "ApiBaseUrl";
    const string DEFAULT_URL  = "http://127.0.0.1:8000";

    [Header("Connection Settings")]
    public string baseUrl = DEFAULT_URL;
    public bool isConnected;

    [Header("Telemetry Settings")]
    public float telemetryInterval = 45f;
    float timer;

    [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.BeforeSceneLoad)]
    static void AutoBoot()
    {
        EnsureInstance();
    }

    public static CityApiClient EnsureInstance()
    {
        if (Instance != null) return Instance;
        var go = new GameObject("[CityApiClient]");
        DontDestroyOnLoad(go);
        Instance = go.AddComponent<CityApiClient>();
        return Instance;
    }

    void Awake()
    {
        if (Instance != null && Instance != this) { Destroy(gameObject); return; }
        Instance = this;
        DontDestroyOnLoad(gameObject);

        // Load configured URL (default or user-specified)
        baseUrl = PlayerPrefs.GetString(PREF_API_URL, DEFAULT_URL).TrimEnd('/');
        StartCoroutine(PingServer());
    }

    void Update()
    {
        if (!CityManager.Instance || CityManager.Instance.paused) return;
        timer += Time.deltaTime;
        if (timer >= telemetryInterval)
        {
            timer = 0f;
            RecordSimulationTelemetry();
        }
    }

    /// <summary>Set and persist custom cloud API URL (e.g. Render/Railway URL).</summary>
    public void SetBaseUrl(string newUrl)
    {
        if (string.IsNullOrEmpty(newUrl)) newUrl = DEFAULT_URL;
        baseUrl = newUrl.TrimEnd('/');
        PlayerPrefs.SetString(PREF_API_URL, baseUrl);
        PlayerPrefs.Save();
        StartCoroutine(PingServer());
    }

    // ── Health Check ──────────────────────────────────────────────────────────

    public IEnumerator PingServer(Action<bool> callback = null)
    {
        using var req = UnityWebRequest.Get(baseUrl + "/health");
        req.timeout = 5;
        yield return req.SendWebRequest();
        isConnected = (req.result == UnityWebRequest.Result.Success);
        callback?.Invoke(isConnected);
    }

    /// <summary>Sync current active city state to cloud database.</summary>
    public void SyncCurrentCity()
    {
        if (CityManager.Instance?.State != null)
        {
            int activeSlot = PlayerPrefs.GetInt("ActiveSlot", 0);
            SaveSlotToCloud(activeSlot, CityManager.Instance.State);
        }
    }

    // ── Cloud Save Slot API ───────────────────────────────────────────────────

    /// <summary>Upload complete city state to cloud database slot.</summary>
    public void SaveSlotToCloud(int slotIndex, CityState state, Action<bool, string> onComplete = null)
    {
        StartCoroutine(SaveSlotRoutine(slotIndex, state, onComplete));
    }

    IEnumerator SaveSlotRoutine(int slotIndex, CityState state, Action<bool, string> onComplete)
    {
        var ev = state.currentEvent;
        state.currentEvent = null;
        string stateJson = JsonUtility.ToJson(state);
        state.currentEvent = ev;

        var payload = new SaveSlotPayload
        {
            slot_index        = slotIndex,
            city_name         = state.cityName,
            difficulty        = state.difficulty,
            day               = state.day,
            year              = state.year,
            budget            = state.budget,
            population        = state.population,
            happiness         = state.happiness,
            sustainability    = state.sustainability,
            smart_city_score  = state.smartCityScore,
            level             = state.level,
            progression_title = state.progressionTitle,
            state_json        = stateJson
        };

        string json = JsonUtility.ToJson(payload);
        using var req = new UnityWebRequest(baseUrl + "/cities/save-slot", "POST");
        byte[] body = System.Text.Encoding.UTF8.GetBytes(json);
        req.uploadHandler = new UploadHandlerRaw(body);
        req.downloadHandler = new DownloadHandlerBuffer();
        req.SetRequestHeader("Content-Type", "application/json");
        req.timeout = 8;

        yield return req.SendWebRequest();
        bool ok = req.result == UnityWebRequest.Result.Success;
        isConnected = ok;
        if (ok)
            Debug.Log($"[CityApiClient] Cloud save success for slot {slotIndex} ({state.cityName})");
        else
            Debug.LogWarning($"[CityApiClient] Cloud save failed: {req.error}");

        onComplete?.Invoke(ok, req.downloadHandler.text);
    }

    /// <summary>Download complete city state from cloud database slot.</summary>
    public void LoadSlotFromCloud(int slotIndex, Action<bool, CityState> onComplete)
    {
        StartCoroutine(LoadSlotRoutine(slotIndex, onComplete));
    }

    IEnumerator LoadSlotRoutine(int slotIndex, Action<bool, CityState> onComplete)
    {
        using var req = UnityWebRequest.Get(baseUrl + "/cities/slots/" + slotIndex);
        req.timeout = 8;
        yield return req.SendWebRequest();

        if (req.result == UnityWebRequest.Result.Success)
        {
            try
            {
                var detail = JsonUtility.FromJson<SlotDetailResponse>(req.downloadHandler.text);
                if (detail != null && !string.IsNullOrEmpty(detail.state_json))
                {
                    var loadedState = JsonUtility.FromJson<CityState>(detail.state_json);
                    onComplete?.Invoke(true, loadedState);
                    yield break;
                }
            }
            catch (Exception ex)
            {
                Debug.LogWarning("[CityApiClient] Error parsing cloud state JSON: " + ex.Message);
            }
        }
        onComplete?.Invoke(false, null);
    }

    /// <summary>Delete a cloud save slot.</summary>
    public void DeleteSlotFromCloud(int slotIndex, Action<bool> onComplete = null)
    {
        StartCoroutine(DeleteSlotRoutine(slotIndex, onComplete));
    }

    IEnumerator DeleteSlotRoutine(int slotIndex, Action<bool> onComplete)
    {
        using var req = UnityWebRequest.Delete(baseUrl + "/cities/slots/" + slotIndex);
        req.timeout = 5;
        yield return req.SendWebRequest();
        bool ok = req.result == UnityWebRequest.Result.Success;
        onComplete?.Invoke(ok);
    }

    // ── Simulation Telemetry ──────────────────────────────────────────────────

    void RecordSimulationTelemetry()
    {
        if (!CityManager.Instance || CityManager.Instance.State == null) return;
        int activeSlot = PlayerPrefs.GetInt("ActiveSlot", 0);
        StartCoroutine(TelemetryRoutine(activeSlot, CityManager.Instance.State));
    }

    IEnumerator TelemetryRoutine(int slot, CityState s)
    {
        var payload = new TelemetryPayload
        {
            slot_index         = slot,
            in_game_day        = s.day,
            in_game_year       = s.year,
            budget             = s.budget,
            population         = s.population,
            happiness          = s.happiness,
            sustainability     = s.sustainability,
            traffic_efficiency = s.trafficEfficiency,
            pollution          = s.pollution,
            crime_rate         = s.crimeRate,
            power_balance      = s.electricityProduction - s.electricityConsumption,
            water_balance      = s.waterSupply - s.waterConsumption
        };

        string json = JsonUtility.ToJson(payload);
        using var req = new UnityWebRequest(baseUrl + "/cities/telemetry", "POST");
        byte[] body = System.Text.Encoding.UTF8.GetBytes(json);
        req.uploadHandler = new UploadHandlerRaw(body);
        req.downloadHandler = new DownloadHandlerBuffer();
        req.SetRequestHeader("Content-Type", "application/json");
        req.timeout = 5;

        yield return req.SendWebRequest();
        isConnected = (req.result == UnityWebRequest.Result.Success);
    }

    // ── Authentication API ───────────────────────────────────────────────────

    public void RegisterMayor(string username, string email, string password, string fullName, string role, string dept, Action<bool, string> onComplete)
    {
        StartCoroutine(RegisterMayorRoutine(username, email, password, fullName, role, dept, onComplete));
    }

    IEnumerator RegisterMayorRoutine(string username, string email, string password, string fullName, string role, string dept, Action<bool, string> onComplete)
    {
        var payload = new RegisterPayload
        {
            username = username,
            email = email,
            password = password,
            full_name = fullName,
            role = role,
            department = dept
        };
        string json = JsonUtility.ToJson(payload);
        using var req = new UnityWebRequest(baseUrl + "/auth/register", "POST");
        byte[] body = System.Text.Encoding.UTF8.GetBytes(json);
        req.uploadHandler = new UploadHandlerRaw(body);
        req.downloadHandler = new DownloadHandlerBuffer();
        req.SetRequestHeader("Content-Type", "application/json");
        req.timeout = 6;

        yield return req.SendWebRequest();
        bool ok = req.result == UnityWebRequest.Result.Success;
        onComplete?.Invoke(ok, req.downloadHandler.text);
    }

    public void LoginMayor(string userOrEmail, string password, Action<bool, string> onComplete)
    {
        StartCoroutine(LoginMayorRoutine(userOrEmail, password, onComplete));
    }

    IEnumerator LoginMayorRoutine(string userOrEmail, string password, Action<bool, string> onComplete)
    {
        var payload = new LoginPayload
        {
            username_or_email = userOrEmail,
            password = password
        };
        string json = JsonUtility.ToJson(payload);
        using var req = new UnityWebRequest(baseUrl + "/auth/login", "POST");
        byte[] body = System.Text.Encoding.UTF8.GetBytes(json);
        req.uploadHandler = new UploadHandlerRaw(body);
        req.downloadHandler = new DownloadHandlerBuffer();
        req.SetRequestHeader("Content-Type", "application/json");
        req.timeout = 6;

        yield return req.SendWebRequest();
        bool ok = req.result == UnityWebRequest.Result.Success;
        onComplete?.Invoke(ok, req.downloadHandler.text);
    }

    // ── Serializable DTOs ─────────────────────────────────────────────────────

    [Serializable]
    public class RegisterPayload
    {
        public string username;
        public string email;
        public string password;
        public string full_name;
        public string role;
        public string department;
    }

    [Serializable]
    public class LoginPayload
    {
        public string username_or_email;
        public string password;
    }

    [Serializable]
    class SaveSlotPayload
    {
        public int slot_index;
        public string city_name;
        public string difficulty;
        public int day;
        public int year;
        public float budget;
        public int population;
        public float happiness;
        public float sustainability;
        public float smart_city_score;
        public int level;
        public string progression_title;
        public string state_json;
    }

    [Serializable]
    class SlotDetailResponse
    {
        public int slot_index;
        public string city_name;
        public string state_json;
    }

    [Serializable]
    class TelemetryPayload
    {
        public int slot_index;
        public int in_game_day;
        public int in_game_year;
        public float budget;
        public int population;
        public float happiness;
        public float sustainability;
        public float traffic_efficiency;
        public float pollution;
        public float crime_rate;
        public float power_balance;
        public float water_balance;
    }
}

