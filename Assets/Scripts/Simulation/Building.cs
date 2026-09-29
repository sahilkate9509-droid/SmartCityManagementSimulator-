using UnityEngine;

/// <summary>
/// Attached to every interactive city building.
/// Allows player to select, inspect, and upgrade buildings up to Level 5.
/// </summary>
public class Building : MonoBehaviour
{
    public enum Kind
    {
        Residential, Commercial, Industrial, Park,
        Hospital, School, Police, Fire, Power, Water, Recycling, BusStation
    }

    public Kind kind = Kind.Commercial;
    public string buildingName = "Metropolis Facility";
    public int level = 1;
    public const int MaxLevel = 5;
    public float baseUpgradeCost = 8000f;

    public float GetUpgradeCost() => baseUpgradeCost * level;

    public float GetHappinessBonus() => level * 1.5f;
    public float GetRevenueBonus() => level * 450f;

    public void Upgrade()
    {
        if (level >= MaxLevel)
        {
            CityManager.Instance?.Raise(buildingName + " is already at Maximum Level (Level " + MaxLevel + ")!", CityManager.AlertLevel.Info);
            return;
        }

        float cost = GetUpgradeCost();
        if (CityManager.Instance != null && !CityManager.Instance.Spend(cost, buildingName + " Upgrade"))
            return;

        level++;

        // Visual growth feedback
        transform.localScale = new Vector3(
            transform.localScale.x * 1.05f,
            transform.localScale.y * 1.08f,
            transform.localScale.z * 1.05f
        );

        if (CityManager.Instance != null)
        {
            CityManager.Instance.State.happiness = Mathf.Clamp(CityManager.Instance.State.happiness + 2.0f, 0, 100);
            CityManager.Instance.Raise($"⭐ {buildingName} upgraded to Level {level}! (+Happiness & Revenue)", CityManager.AlertLevel.Success);
            CityManager.Instance.RecalculateScore();
            CityManager.Instance.Notify();
        }
    }
}
