using UnityEngine;

public class ConstructionSystem : MonoBehaviour
{
    public static ConstructionSystem Instance { get; private set; }
    void Awake() { Instance = this; }

    // ── Build a city building at a confirmed world position ───────────────────
    /// <summary>
    /// Deducts cost, updates CityState counters, and spawns the 3D building at
    /// <paramref name="worldPos"/>.  Called by BuildPlacementController after the
    /// player clicks on a free grid cell.
    /// </summary>
    public void Build(Building.Kind kind, Vector3 worldPos)
    {
        var s = CityManager.Instance.State;
        float cost = Cost(kind);
        if (!CityManager.Instance.Spend(cost, kind.ToString())) return;

        switch (kind)
        {
            case Building.Kind.Residential:  s.houses++;                break;
            case Building.Kind.Commercial:   s.commercialBuildings++;   break;
            case Building.Kind.Industrial:   s.industrialBuildings++;   break;
            case Building.Kind.Park:         s.parks++;                 break;
            case Building.Kind.Hospital:     s.hospitals++;             break;
            case Building.Kind.School:       s.schools++;               break;
            case Building.Kind.Police:       s.policeStations++;        break;
            case Building.Kind.Fire:         s.fireStations++;          break;
            case Building.Kind.Power:        s.powerPlants++;           break;
            case Building.Kind.Water:        s.waterFacilities++;       break;
            case Building.Kind.Recycling:    s.recyclingCenters++;      break;
        }

        CityWorldBuilder.Instance?.SpawnBuilding(kind, worldPos);

        CityManager.Instance.Raise(kind + " construction approved! Rs. " + cost.ToString("N0") + " spent.", CityManager.AlertLevel.Success);
        CityManager.Instance.RecalculateScore();
        CityManager.Instance.Notify();
    }

    // ── Place a city decoration at a confirmed world position ─────────────────
    /// <summary>
    /// Deducts cost, updates decoration counters, and spawns the 3D prop at
    /// <paramref name="worldPos"/>.  Called by BuildPlacementController.
    /// </summary>
    public void BuildDecoration(string type, Vector3 worldPos)
    {
        var s = CityManager.Instance.State;
        float cost = DecorationCost(type);
        if (!CityManager.Instance.Spend(cost, type + " decoration")) return;

        switch (type)
        {
            case "Fountain":   s.fountains++;   break;
            case "Flowerbed":  s.flowerbeds++;  break;
            case "Monument":   s.monuments++;   break;
            case "Bench":      s.benches++;     break;
            case "Sculpture":  s.sculptures++;  break;
        }

        CityWorldBuilder.Instance?.SpawnDecoration(type, worldPos);

        s.happiness = Mathf.Clamp(s.happiness + 1.2f, 0, 100);
        CityManager.Instance.Raise(type + " placed! Happiness and land value boosted.", CityManager.AlertLevel.Success);
        CityManager.Instance.RecalculateScore();
        CityManager.Instance.Notify();
    }

    // ── Road & transit (position-less — auto-placed) ──────────────────────────

    public void AddRoad()
    {
        if (!CityManager.Instance.Spend(12000, "road construction")) return;
        CityManager.Instance.State.roads++;
        CityManager.Instance.State.roadCondition = Mathf.Clamp(CityManager.Instance.State.roadCondition + 6, 0, 100);
        CityWorldBuilder.Instance?.SpawnRoad();
        CityManager.Instance.Raise("New smart road added to the city grid.", CityManager.AlertLevel.Success);
    }

    public void RepairRoads()
    {
        if (!CityManager.Instance.Spend(8000, "road repairs")) return;
        CityManager.Instance.State.roadCondition = 100f;
        CityManager.Instance.Raise("Road network fully repaired to 100% condition.", CityManager.AlertLevel.Success);
    }

    public void AddBusRoute()
    {
        if (!CityManager.Instance.Spend(9000, "bus route")) return;
        CityManager.Instance.State.busRoutes++;
        CityManager.Instance.State.buses += 2;
        CityWorldBuilder.Instance?.SpawnBusStop();
        CityManager.Instance.Raise("New bus route opened with 2 new buses.", CityManager.AlertLevel.Success);
    }

    // ── Shortcut builders (enter placement mode from rich HUD pages) ───────────

    public void BuildWaterFacility()   => BuildPlacementController.Instance?.EnterPlacementMode(Building.Kind.Water,     Cost(Building.Kind.Water));
    public void BuildRecyclingCenter() => BuildPlacementController.Instance?.EnterPlacementMode(Building.Kind.Recycling,  Cost(Building.Kind.Recycling));
    public void BuildSchool()          => BuildPlacementController.Instance?.EnterPlacementMode(Building.Kind.School,     Cost(Building.Kind.School));
    public void BuildPoliceStation()   => BuildPlacementController.Instance?.EnterPlacementMode(Building.Kind.Police,     Cost(Building.Kind.Police));
    public void BuildFireStation()     => BuildPlacementController.Instance?.EnterPlacementMode(Building.Kind.Fire,       Cost(Building.Kind.Fire));
    public void BuildPowerPlant()      => BuildPlacementController.Instance?.EnterPlacementMode(Building.Kind.Power,      Cost(Building.Kind.Power));
    public void BuildHospital()        => BuildPlacementController.Instance?.EnterPlacementMode(Building.Kind.Hospital,   Cost(Building.Kind.Hospital));
    public void PlantPark()            => BuildPlacementController.Instance?.EnterPlacementMode(Building.Kind.Park,       Cost(Building.Kind.Park));

    // ── Cost tables ───────────────────────────────────────────────────────────

    public static float Cost(Building.Kind k) => k switch
    {
        Building.Kind.Residential => 10000,
        Building.Kind.Commercial  => 15000,
        Building.Kind.Industrial  => 18000,
        Building.Kind.Park        =>  6500,
        Building.Kind.Hospital    => 28000,
        Building.Kind.School      => 22000,
        Building.Kind.Police      => 20000,
        Building.Kind.Fire        => 20000,
        Building.Kind.Power       => 38000,
        Building.Kind.Water       => 30000,
        Building.Kind.Recycling   => 24000,
        _                         => 12000
    };

    public static float DecorationCost(string type) => type switch
    {
        "Fountain"  =>  8000,
        "Flowerbed" =>  3500,
        "Monument"  => 14000,
        "Bench"     =>  1500,
        "Sculpture" => 12000,
        _           =>  5000
    };
}
