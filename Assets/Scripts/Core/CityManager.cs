using System;
using UnityEngine;
using UnityEngine.SceneManagement;

public class CityManager : MonoBehaviour
{
    public static CityManager Instance { get; private set; }
    public CityState State = new();
    public float secondsPerDay = 10f;
    public int simulationSpeed = 1;
    public bool paused;
    public event Action StateChanged;
    public event Action<string, AlertLevel> AlertRaised;
    float timer;

    public enum AlertLevel { Info, Warning, Critical, Success }

    void Awake()
    {
        if (Instance != null && Instance != this) { Destroy(gameObject); return; }
        Instance = this; DontDestroyOnLoad(gameObject);
        Application.targetFrameRate = 120;
        if (State.populationHistory.Count == 0) SnapshotHistory();
    }

    void Update()
    {
        if (paused || simulationSpeed <= 0 || SceneManager.GetActiveScene().name != "CitySimulation") return;
        timer += Time.deltaTime * simulationSpeed;
        if (timer >= secondsPerDay) { timer = 0f; AdvanceDay(); }
    }

    public void NewCity(string name, string difficulty, float startingBudget)
    {
        State = new CityState();
        State.cityName  = string.IsNullOrWhiteSpace(name) ? "Green Valley" : name.Trim();
        State.difficulty = difficulty;
        State.budget     = Mathf.Max(50000f, startingBudget);

        // Starter population scales with difficulty (tiny settlement, not a metropolis)
        State.population = difficulty == "Hard" ? 80 : difficulty == "Medium" ? 100 : 120;

        SnapshotHistory();
        RecalculateScore();
        Notify();

        // Tear down any previous 3D city and generate a fresh starter city.
        // If CityWorldBuilder is already in the scene it will handle the rebuild;
        // if the CitySimulation scene hasn't loaded yet, Start() will call it.
        if (CityWorldBuilder.Instance != null)
            CityWorldBuilder.Instance.BuildStarterCity();
    }

    public bool Spend(float amount, string reason)
    {
        if (State.budget < amount) { Raise("Insufficient budget for " + reason + ".", AlertLevel.Warning); return false; }
        State.budget -= amount; Notify(); return true;
    }

    public void AddBudget(float amount) { State.budget += amount; Notify(); }
    public void SetSpeed(int speed) { simulationSpeed = Mathf.Clamp(speed, 0, 4); paused = speed == 0; Notify(); }
    public void TogglePause() { paused = !paused; Notify(); }

    public void AdvanceDay()
    {
        State.day++;
        if (State.day > 365) { State.day = 1; State.year++; }
        EconomySystem.Simulate(State);
        PopulationSystem.Simulate(State);
        UtilitySystem.Simulate(State);
        TrafficSystem.Simulate(State);
        EnvironmentSystem.Simulate(State);
        PublicServicesSystem.Simulate(State);
        ProgressionSystem.Simulate(State, Raise);
        CityRandomEventSystem.TryGenerate(State, Raise);
        CitizenRequestSystem.Instance?.TryGenerateRequest(State);
        RecalculateScore();
        SnapshotHistory();
        CheckWinLoss();
        Notify();
    }

    public void RecalculateScore()
    {
        float finance = Mathf.Clamp01(State.budget / 500000f) * 100f;
        float infrastructure = Mathf.Clamp((State.roadCondition + State.trafficEfficiency) * 0.5f, 0, 100);
        float safety = 100f - State.crimeRate;
        State.smartCityScore = Mathf.Clamp((State.happiness + finance + State.sustainability + infrastructure + safety + State.healthcareQuality + State.educationQuality + State.trafficEfficiency) / 8f, 0, 100);
    }

    void SnapshotHistory()
    {
        AddHistory(State.populationHistory, State.population);
        AddHistory(State.budgetHistory, State.budget);
        AddHistory(State.happinessHistory, State.happiness);
        AddHistory(State.trafficHistory, State.trafficEfficiency);
        AddHistory(State.sustainabilityHistory, State.sustainability);
    }

    static void AddHistory(System.Collections.Generic.List<float> list, float v) { list.Add(v); if (list.Count > 30) list.RemoveAt(0); }

    void CheckWinLoss()
    {
        if (State.budget <= -10000f) Raise("CITY BANKRUPT: emergency financial recovery required.", AlertLevel.Critical);
        if (State.happiness < 20f) Raise("Citizen happiness is critically low.", AlertLevel.Critical);
        if (State.smartCityScore >= 90f && State.population >= 10000) Raise("Metropolis objective achieved! Smart City Score 90+.", AlertLevel.Success);
    }

    public void Raise(string message, AlertLevel level) { AlertRaised?.Invoke(message, level); }
    public void Notify() { StateChanged?.Invoke(); }
}
