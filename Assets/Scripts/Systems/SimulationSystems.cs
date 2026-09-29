using UnityEngine;

public static class EconomySystem
{
    public static void Simulate(CityState s)
    {
        float taxIncome = (s.population * s.residentialTax * 2.4f)
                        + (s.commercialBuildings * s.commercialTax * 18f)
                        + (s.industrialBuildings * s.industrialTax * 32f)
                        + (s.buses * 45f);

        float serviceCost = s.hospitals * 240f + s.schools * 180f + s.policeStations * 160f + s.fireStations * 150f + s.buses * 35f;
        float utilityCost = s.electricityConsumption * 0.045f + s.waterConsumption * 0.025f + s.wasteGenerated * 12f;
        float maintenance = (s.roads * 22f) + (s.bridges * 65f) + (s.parks * 15f) + (s.fountains * 25f) + (s.monuments * 30f);

        s.dailyIncome = taxIncome;
        s.maintenanceCost = maintenance;
        s.utilityExpenses = utilityCost;
        s.serviceExpenses = serviceCost;
        s.dailyExpenses = serviceCost + utilityCost + maintenance;

        s.budget += s.dailyIncome - s.dailyExpenses;

        // Road deterioration from traffic
        s.roadCondition = Mathf.Clamp(s.roadCondition - Random.Range(0.08f, 0.25f), 0, 100);

        // High tax unhappiness penalty
        if (s.residentialTax > 15f) s.happiness -= (s.residentialTax - 15f) * 0.2f;
        if (s.commercialTax > 18f) s.employmentRate -= (s.commercialTax - 18f) * 0.3f;
    }
}

public static class PopulationSystem
{
    public static void Simulate(CityState s)
    {
        int housingCapacity = s.houses * 180;
        float taxPenalty = (s.residentialTax - 10f) * 1.5f;

        float attractiveness = (s.happiness * 0.25f)
                             + (s.healthcareQuality * 0.15f)
                             + (s.educationQuality * 0.15f)
                             + ((100f - s.pollution) * 0.15f)
                             + (s.employmentRate * 0.20f)
                             + ((100f - s.crimeRate) * 0.10f)
                             - taxPenalty;

        float delta = (attractiveness - 50f) * 0.35f;

        // Overcrowding check
        if (s.population >= housingCapacity)
        {
            delta = -Mathf.Abs(delta) * 0.5f;
        }

        s.population = Mathf.Max(100, s.population + Mathf.RoundToInt(delta));

        // Employment rate calculation
        float jobCapacity = s.commercialBuildings * 60 + s.industrialBuildings * 90;
        s.employmentRate = Mathf.Clamp((jobCapacity / Mathf.Max(1f, s.population * 0.7f)) * 100f, 20f, 98f);
    }
}

public static class UtilitySystem
{
    public static void Simulate(CityState s)
    {
        // Base consumption + per capita + commercial + industrial
        s.electricityConsumption = 400 + s.population * 0.48f + s.commercialBuildings * 32 + s.industrialBuildings * 85;
        s.electricityProduction = s.powerPlants * 1800f + (s.renewableEnergyUnlocked ? 650f : 0f);

        s.waterConsumption = 350 + s.population * 0.32f + s.industrialBuildings * 40;
        s.waterSupply = s.waterFacilities * 1800f;

        s.reservoirLevel = Mathf.Clamp(s.reservoirLevel + (s.waterSupply - s.waterConsumption) / 2500f, 0, 100);
        s.wasteGenerated = s.population * 0.018f;
        s.recyclingRate = Mathf.Clamp(25 + s.recyclingCenters * 14 + s.sustainability * 0.12f, 0, 95);

        // Power/Water shortages degrade happiness & service quality
        if (s.electricityConsumption > s.electricityProduction)
        {
            s.happiness -= 1.2f;
            s.healthcareQuality -= 0.5f;
        }

        if (s.waterConsumption > s.waterSupply || s.reservoirLevel < 20)
        {
            s.happiness -= 1.2f;
        }
    }
}

public static class TrafficSystem
{
    public static void Simulate(CityState s)
    {
        float demand = s.population / Mathf.Max(1f, s.roads * 260f);
        float transitRelief = Mathf.Min(24f, s.busRoutes * 2.8f + s.buses * 0.4f);
        float smartBonus = s.smartTrafficUnlocked ? 14f : 0f;

        s.trafficEfficiency = Mathf.Clamp(98f - demand * 23f + transitRelief + smartBonus + (s.roadCondition - 75f) * 0.2f, 5f, 100f);
        s.happiness = Mathf.Clamp(s.happiness + (s.trafficEfficiency - 60f) * 0.006f, 0, 100);
    }
}

public static class EnvironmentSystem
{
    public static void Simulate(CityState s)
    {
        float source = s.industrialBuildings * 3.8f + s.population * 0.0014f + (100f - s.trafficEfficiency) * 0.22f;
        float decorationBonus = s.fountains * 0.8f + s.flowerbeds * 0.5f + s.monuments * 0.6f;
        float mitigation = s.parks * 1.8f + s.greenCoverage * 0.30f + (s.renewableEnergyUnlocked ? 9f : 0f) + decorationBonus;

        s.pollution = Mathf.Clamp(18f + source - mitigation, 0, 100);
        s.greenCoverage = Mathf.Clamp(14f + s.parks * 3.4f + s.flowerbeds * 1.2f, 5, 85);
        s.airQuality = Mathf.Clamp(100f - s.pollution * 0.9f, 0, 100);
        s.sustainability = Mathf.Clamp((s.airQuality + s.recyclingRate + s.greenCoverage + (s.electricityProduction >= s.electricityConsumption ? 80 : 45)) / 4f, 0, 100);
    }
}

public static class PublicServicesSystem
{
    public static void Simulate(CityState s)
    {
        s.healthcareQuality = Mathf.Clamp(42f + s.hospitals * 14f - s.population / 1700f, 15, 100);
        s.educationQuality = Mathf.Clamp(40f + s.schools * 13f - s.population / 1800f, 15, 100);

        float safetyCoverage = s.policeStations * 9.5f + s.fireStations * 6.5f;
        s.crimeRate = Mathf.Clamp(21f + s.population / 2500f - safetyCoverage + (s.industrialTax > 20f ? 2f : 0f), 1, 70);

        float decorationHappiness = s.fountains * 0.4f + s.monuments * 0.5f + s.sculptures * 0.5f;
        float serviceComposite = (s.healthcareQuality + s.educationQuality + (100f - s.crimeRate)) / 3f;

        s.happiness = Mathf.Clamp(s.happiness + (serviceComposite - 60f) * 0.008f - s.pollution * 0.004f + decorationHappiness * 0.01f, 0, 100);
    }
}
