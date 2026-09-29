using System;
using UnityEngine;

public static class ProgressionSystem
{
    public static void Simulate(CityState s, Action<string, CityManager.AlertLevel> alert)
    {
        int newLevel = s.smartCityScore >= 85 ? 5 : s.smartCityScore >= 75 ? 4 : s.smartCityScore >= 65 ? 3 : s.smartCityScore >= 55 ? 2 : 1;
        if (newLevel > s.level)
        {
            s.level = newLevel;
            alert?.Invoke("City level increased to Level " + s.level + ". New technology is available.", CityManager.AlertLevel.Success);
        }
        if (s.level >= 2) s.renewableEnergyUnlocked = true;
        if (s.level >= 3) s.smartTrafficUnlocked = true;
        if (s.level >= 4) s.advancedTransitUnlocked = true;
    }
}
