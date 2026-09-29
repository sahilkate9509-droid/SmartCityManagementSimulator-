using UnityEngine;

/// <summary>
/// Hybrid multi-slot save system with Cloud Database synchronization.
/// Supports up to MAX_SLOTS independent city saves.
/// Saves locally to PlayerPrefs for zero-latency offline play,
/// and automatically synchronizes to the PostgreSQL / SQLite cloud backend.
/// </summary>
public static class SaveSystem
{
    public const int MAX_SLOTS = 5;
    const string PREFIX = "SmartCity_v3_Slot";   // v3 key: old v1/v2 saves ignored

    // ── Low-level slot helpers ────────────────────────────────────────────────

    static string Key(int slot)     => PREFIX + slot;
    static string MetaKey(int slot) => PREFIX + slot + "_Meta";

    /// <summary>Returns display name stored in the meta string, or "" if no save.</summary>
    public static string SlotName(int slot)
    {
        if (!PlayerPrefs.HasKey(MetaKey(slot))) return "";
        return PlayerPrefs.GetString(MetaKey(slot));
    }

    public static bool SlotExists(int slot) => PlayerPrefs.HasKey(Key(slot));

    // ── Save / Load ───────────────────────────────────────────────────────────

    /// <summary>Save the current city into slot (0-based) locally and sync to cloud.</summary>
    public static void Save(int slot = 0)
    {
        if (!CityManager.Instance) return;
        var state = CityManager.Instance.State;
        var ev = state.currentEvent;
        state.currentEvent = null; // can't serialise Action<>
        PlayerPrefs.SetString(Key(slot), JsonUtility.ToJson(state));
        PlayerPrefs.SetString(MetaKey(slot), state.cityName); // display name
        PlayerPrefs.Save();
        state.currentEvent = ev;

        // Sync to cloud database in background
        CityApiClient.EnsureInstance()?.SaveSlotToCloud(slot, state);
    }

    /// <summary>Load city from slot and rebuild the 3D world.</summary>
    public static bool Load(int slot = 0)
    {
        if (!SlotExists(slot)) return false;
        var loaded = JsonUtility.FromJson<CityState>(PlayerPrefs.GetString(Key(slot)));
        if (loaded == null) return false;
        loaded.currentEvent = null; // clear phantom events
        if (CityManager.Instance)
        {
            CityManager.Instance.State = loaded;
            CityWorldBuilder.Instance?.BuildStarterCity();
        }
        return true;
    }

    /// <summary>Delete a save slot locally and in the cloud database.</summary>
    public static void Delete(int slot)
    {
        PlayerPrefs.DeleteKey(Key(slot));
        PlayerPrefs.DeleteKey(MetaKey(slot));
        PlayerPrefs.Save();

        // Delete from cloud database
        CityApiClient.EnsureInstance()?.DeleteSlotFromCloud(slot);
    }

    /// <summary>Load directly from the cloud database and apply to simulation.</summary>
    public static void LoadFromCloudAsync(int slot, System.Action<bool> onComplete)
    {
        CityApiClient.EnsureInstance()?.LoadSlotFromCloud(slot, (success, cloudState) =>
        {
            if (success && cloudState != null)
            {
                cloudState.currentEvent = null;
                // Cache locally
                PlayerPrefs.SetString(Key(slot), JsonUtility.ToJson(cloudState));
                PlayerPrefs.SetString(MetaKey(slot), cloudState.cityName);
                PlayerPrefs.Save();

                if (CityManager.Instance)
                {
                    CityManager.Instance.State = cloudState;
                    CityWorldBuilder.Instance?.BuildStarterCity();
                }
                onComplete?.Invoke(true);
            }
            else
            {
                onComplete?.Invoke(false);
            }
        });
    }

    // ── Legacy compat: CityHUD calls Save() / HasSave() with no arg ──────────

    public static bool HasSave() => SlotExists(0);
}
