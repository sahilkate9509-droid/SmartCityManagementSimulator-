import csv

additional_listings_code = '''
    # Listing 5.19: Building.cs
    elements.append(Paragraph("<b>Listing 5.19:</b> Building Data Model & Upgrade System (<code>Building.cs</code>)", styles['SecHeading3']))
    code_5_19 = (
        "using UnityEngine;\\n"
        "public enum BuildingType { Residential, Commercial, Industrial, Utility, Civic }\\n"
        "public class Building : MonoBehaviour {\\n"
        "    public BuildingType type;\\n"
        "    public int level = 1;\\n"
        "    public float maintenanceCost = 25f;\\n"
        "    public float powerRequired = 10f;\\n"
        "    public float waterRequired = 15f;\\n"
        "    public void Upgrade() {\\n"
        "        level++;\\n"
        "        maintenanceCost *= 1.4f;\\n"
        "        powerRequired *= 1.3f;\\n"
        "    }\\n"
        "}"
    )
    elements.append(Preformatted(code_5_19, styles['CodeSnippet']))
    elements.append(make_engine_table(styles, "Building Data Entity Model", "Simulation Entity Tier", "Component State Pattern", "O(1) upgrade method", "Mutates Structure Level & Resource Demands"))
    elements.append(Spacer(1, 4))

    # Listing 5.20: SaveSystem.cs
    elements.append(Paragraph("<b>Listing 5.20:</b> Binary JSON Slot Persistence Engine (<code>SaveSystem.cs</code>)", styles['SecHeading3']))
    code_5_20 = (
        "using System.IO;\\n"
        "using UnityEngine;\\n"
        "public static class SaveSystem {\\n"
        "    public static void SaveToSlot(int slotIndex, CityState state) {\\n"
        "        string json = JsonUtility.ToJson(state, true);\\n"
        "        string path = Path.Combine(Application.persistentDataPath, $\\"city_save_slot_{slotIndex}.json\\");\\n"
        "        File.WriteAllText(path, json);\\n"
        "    }\\n"
        "    public static CityState LoadFromSlot(int slotIndex) {\\n"
        "        string path = Path.Combine(Application.persistentDataPath, $\\"city_save_slot_{slotIndex}.json\\");\\n"
        "        if (!File.Exists(path)) return null;\\n"
        "        return JsonUtility.FromJson<CityState>(File.ReadAllText(path));\\n"
        "    }\\n"
        "}"
    )
    elements.append(Preformatted(code_5_20, styles['CodeSnippet']))
    elements.append(make_engine_table(styles, "Local Disk Slot Persistence Engine", "Persistence Tier", "Data Access Object (DAO)", "O(Size of Grid JSON) = O(N)", "Serializes CityState to Local JSON Slot"))
    elements.append(Spacer(1, 4))

    # Listing 5.21: ConstructionSystem.cs
    elements.append(Paragraph("<b>Listing 5.21:</b> Demolition & Grid Reclamation System (<code>ConstructionSystem.cs</code>)", styles['SecHeading3']))
    code_5_21 = (
        "using UnityEngine;\\n"
        "public class ConstructionSystem : MonoBehaviour {\\n"
        "    public void DemolishAt(Vector2Int coord) {\\n"
        "        if (CityManager.Instance.IsCellOccupied(coord)) {\\n"
        "            CityManager.Instance.ClearCell(coord);\\n"
        "            CityManager.Instance.state.treasuryBalance -= 50f; // Demolition labor fee\\n"
        "            CityHUD.Instance.RefreshHUD(CityManager.Instance.state);\\n"
        "        }\\n"
        "    }\\n"
        "}"
    )
    elements.append(Preformatted(code_5_21, styles['CodeSnippet']))
    elements.append(make_engine_table(styles, "Demolition & Reclamation Subsystem", "World Grid Management", "Command Execution Pattern", "O(1) cell clearing", "Reclaims Spatial Grid Coordinates"))
    elements.append(Spacer(1, 4))

    # Listing 5.22: WeatherSystem.cs
    elements.append(Paragraph("<b>Listing 5.22:</b> Weather States & Particle Emitter Controller (<code>WeatherSystem.cs</code>)", styles['SecHeading3']))
    code_5_22 = (
        "using UnityEngine;\\n"
        "public class WeatherSystem : MonoBehaviour {\\n"
        "    public ParticleSystem rainParticles, smogParticles;\\n"
        "    public void UpdateWeather(float aqi, bool isRaining) {\\n"
        "        if (isRaining && !rainParticles.isPlaying) rainParticles.Play();\\n"
        "        else if (!isRaining && rainParticles.isPlaying) rainParticles.Stop();\\n"
        "        var emission = smogParticles.emission;\\n"
        "        emission.rateOverTime = Mathf.Clamp((aqi - 50f) * 0.8f, 0f, 120f);\\n"
        "    }\\n"
        "}"
    )
    elements.append(Preformatted(code_5_22, styles['CodeSnippet']))
    elements.append(make_engine_table(styles, "Dynamic Weather Particle System", "Client Environmental Visuals", "State Observer Pattern", "O(1) emission scaling", "Scales Particle Emission by Ambient AQI"))
    elements.append(Spacer(1, 4))

    # Listing 5.23: TrafficVehicle.cs
    elements.append(Paragraph("<b>Listing 5.23:</b> Autonomous Vehicular Agent Pathfinding (<code>TrafficVehicle.cs</code>)", styles['SecHeading3']))
    code_5_23 = (
        "using UnityEngine;\\n"
        "public class TrafficVehicle : MonoBehaviour {\\n"
        "    public Vector3 targetNode;\\n"
        "    public float speed = 12f;\\n"
        "    void Update() {\\n"
        "        transform.position = Vector3.MoveTowards(transform.position, targetNode, speed * Time.deltaTime);\\n"
        "        if (Vector3.Distance(transform.position, targetNode) < 0.2f) {\\n"
        "            targetNode = CityManager.Instance.GetNextRoadWaypoint(transform.position);\\n"
        "        }\\n"
        "    }\\n"
        "}"
    )
    elements.append(Preformatted(code_5_23, styles['CodeSnippet']))
    elements.append(make_engine_table(styles, "Vehicular Agent Navigation", "Traffic Simulation Tier", "Autonomous Agent / Steering Pattern", "O(1) waypoint lookup", "Updates 3D Vehicle Transform Coordinates"))
    elements.append(Spacer(1, 4))

    # Listing 5.24: database.py
    elements.append(Paragraph("<b>Listing 5.24:</b> SQLAlchemy Engine & WAL Pragma Configuration (<code>database.py</code>)", styles['SecHeading3']))
    code_5_24 = (
        "from sqlalchemy import create_engine, event\\n"
        "from sqlalchemy.orm import sessionmaker, declarative_base\\n"
        "DATABASE_URL = \\"sqlite:///./smart_city.db\\"\\n"
        "engine = create_engine(DATABASE_URL, connect_args={\\"check_same_thread\\": False})\\n"
        "@event.listens_for(engine, \\"connect\\")\\n"
        "def set_sqlite_pragma(dbapi_connection, connection_record):\\n"
        "    cursor = dbapi_connection.cursor()\\n"
        "    cursor.execute(\\"PRAGMA journal_mode=WAL;\\")\\n"
        "    cursor.execute(\\"PRAGMA synchronous=NORMAL;\\")\\n"
        "    cursor.close()\\n"
        "SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)\\n"
        "Base = declarative_base()\\n"
    )
    elements.append(Preformatted(code_5_24, styles['CodeSnippet']))
    elements.append(make_engine_table(styles, "Database Engine & Connection Pool", "Backend Database Tier", "Singleton Connection Pool / Event Listener", "O(1) pool allocation", "Enforces SQLite Write-Ahead Logging (WAL)"))
    elements.append(Spacer(1, 6))
'''

print("Code snippet definition prepared.")
