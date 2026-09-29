using System;
using System.Collections.Generic;
using UnityEngine;

[Serializable]
public class DecisionOption
{
    public string title;
    public float cost;
    public string outcomeText;
    public Action<CityState> effect;
}

[Serializable]
public class DecisionEvent
{
    public string id;
    public string title;
    public string description;
    public string optionA;
    public float costA;
    public string optionB;
    public float costB;
    public string optionC;
    public float costC;
}

[Serializable]
public class CityState
{
    public int cityId;
    public string cityName = "Green Valley";
    public string difficulty = "Easy";
    public int day = 1;
    public int year = 2026;
    public float budget = 150000f;
    public int population = 120;         // Starter: tiny settlement
    public float happiness = 55f;         // Low — city needs to grow
    public float sustainability = 30f;
    public float trafficEfficiency = 60f;
    public float pollution = 15f;
    public float airQuality = 85f;
    public float greenCoverage = 10f;

    // Taxes (0% to 30%)
    public float residentialTax = 10f;
    public float commercialTax = 10f;
    public float industrialTax = 10f;

    // Financial Breakdown
    public float dailyIncome = 0f;
    public float dailyExpenses = 0f;
    public float maintenanceCost = 0f;
    public float utilityExpenses = 0f;
    public float serviceExpenses = 0f;

    // Utilities (starter: 1 power plant + 1 water facility pre-built)
    public float electricityProduction = 1800f;
    public float electricityConsumption = 458f;   // 400 base + 120 pop * 0.48
    public float waterSupply = 1800f;
    public float waterConsumption = 388f;          // 350 base + 120 pop * 0.32
    public float reservoirLevel = 60f;
    public float wasteGenerated = 2.2f;
    public float recyclingRate = 20f;

    // Public Services (no civic buildings yet — player must build them)
    public float crimeRate = 28f;
    public float healthcareQuality = 42f;
    public float educationQuality = 40f;
    public float employmentRate = 55f;
    public float roadCondition = 90f;

    // Score & Progression
    public float smartCityScore = 0f;
    public int level = 1;
    public string progressionTitle = "Small Town";

    // Structures & Buildings — starter city is almost empty
    public int houses = 2;                // 2 residential blocks pre-built
    public int commercialBuildings = 0;
    public int industrialBuildings = 0;
    public int hospitals = 0;
    public int schools = 0;
    public int policeStations = 0;
    public int fireStations = 0;
    public int parks = 1;                 // 1 small park pre-built
    public int buses = 0;
    public int busRoutes = 0;
    public int powerPlants = 1;           // 1 power plant pre-built
    public int waterFacilities = 1;       // 1 water facility pre-built
    public int recyclingCenters = 0;
    public int roads = 3;                 // 2 columns + 1 row starter grid
    public int bridges = 1;

    // City Decorations — none placed yet
    public int fountains = 0;
    public int flowerbeds = 0;
    public int monuments = 0;
    public int benches = 0;
    public int sculptures = 0;

    // Technology Unlocks
    public bool renewableEnergyUnlocked;
    public bool smartTrafficUnlocked;
    public bool advancedTransitUnlocked;
    public bool smartGridUnlocked;

    // Map Overlays ("None", "Environment", "Traffic", "Safety", "Healthcare", "Utilities")
    public string overlayMode = "None";

    // Active Random Decision Event
    public DecisionEvent currentEvent;

    // Historical Performance Lists
    public List<float> populationHistory = new();
    public List<float> budgetHistory = new();
    public List<float> happinessHistory = new();
    public List<float> trafficHistory = new();
    public List<float> sustainabilityHistory = new();
}
