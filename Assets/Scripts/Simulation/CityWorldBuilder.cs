using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Rendering;

/// <summary>
/// Full-Scale AAA High-Tech Metropolis World Builder & Architecture Engine.
/// Generates a dense, vibrant, living Smart City with active traffic and upgradeable buildings:
/// 1. DOWNTOWN FINANCIAL CLUSTER: Soaring glass skyscrapers (up to 95m), skybridges, neon ribbons, rooftop helipads.
/// 2. CIVIC & ACADEMIC PAVILIONS: Biotech Medical Center, Quantum Academy rotunda, Cyber Police HQ, Emergency Command.
/// 3. WATERFRONT & RESIDENTIAL DISTRICTS: High-rise condo towers, modern luxury villas with swimming pools, marina boardwalk.
/// 4. SPORTS & ENTERTAINMENT: Stadium arena, cinema malls, central reflection lake with fountains and cherry blossoms.
/// 5. ECO-ENERGY: Clean fusion reactor, tracking solar arrays, distant offshore wind turbines.
/// 6. ACTIVE FLOWING TRAFFIC: Autonomous cyber sedans with LED headlights/underglow, transit cyber-buses, flying VTOL drones.
/// 7. FULLY UPGRADEABLE: Every building has an interactive Building component (Levels 1-5).
/// </summary>
public class CityWorldBuilder : MonoBehaviour
{
    public static CityWorldBuilder Instance { get; private set; }

    // ── Procedural Textures ───────────────────────────────────────────────────
    static Texture2D grassTex;
    static Texture2D asphaltTex;
    static Texture2D sidewalkTex;
    static Texture2D plazaPaverTex;
    static Texture2D skyscraperGlassTex;
    static Texture2D skyscraperEmissionTex;
    static Texture2D modernGlassTex;
    static Texture2D waterTex;
    static Texture2D solarTex;
    static Texture2D woodPlankTex;
    static Texture2D stadiumFieldTex;
    static Texture2D billboardTex;

    // ── Materials ────────────────────────────────────────────────────────────
    Material roadMat, curbMat, sidewalkMat, lineMat, yellowLineMat, grassMat, waterMat, oceanMat, parkMat, darkMat,
             metalMat, chromeMat, windowMat, redCrossMat, solarMat, plazaMat, glassRailMat, neonCyanMat, neonAmberMat,
             neonMagentaMat, neonGreenMat, helipadMat, sunMat, cloudMat,
             residentialMat, commercialMat, industrialMat, serviceMat, stadiumMat, billboardMat,
             hospitalMat, schoolMat, policeMat, fireMat, powerMat, tireMat, rimMat, tailLightMat, headLightMat, sirenBlueMat,
             sandMat, woodMat, cherryMat, pierMat, turbineMat, poolMat;
    bool matsInit;

    Transform root;

    int roadSpawnIdx;
    int busStopCount;

    // Avenue grid coordinates (spacing: 50m / 40m across 460x420m terrain)
    public static readonly float[] MainBoulevardsX = { -100f, -50f, 0f, 50f, 100f };
    public static readonly float[] MainBoulevardsZ = { -80f, -40f, 0f, 40f, 80f };

    // ── Public Builder API (Invoked by ConstructionSystem & BuildPlacementController) ─

    public static Shader GetDefaultShader()
    {
        var s = Shader.Find("Standard");
        if (s == null) s = Shader.Find("Universal Render Pipeline/Lit");
        if (s == null) s = Shader.Find("Diffuse");
        return s;
    }

    public void SpawnBuilding(Building.Kind kind, Vector3 pos)
    {
        if (root == null) root = new GameObject("Generated Smart City").transform;
        InitMaterials();

        switch (kind)
        {
            case Building.Kind.Residential:
                BuildLuxuryCondo(pos, 38f, "Residential Suites", root);
                break;
            case Building.Kind.Commercial:
                BuildModernOfficeBlock(pos, 42f, "Commercial Center", root);
                break;
            case Building.Kind.Industrial:
                BuildCleanIndustrialDepot(pos, "Industrial Center", root);
                break;
            case Building.Kind.Park:
                var pObj = new GameObject("City Park");
                pObj.transform.position = pos;
                pObj.transform.SetParent(root, true);
                var pb = pObj.AddComponent<Building>();
                pb.kind = Building.Kind.Park;
                pb.buildingName = "Botanical City Park";
                Cube("Park Lawn", pos + Vector3.up * 0.1f, new Vector3(18f, 0.2f, 18f), parkMat, pObj.transform);
                SpawnParkTree(pos + new Vector3(-4f, 0, -4f), pObj.transform);
                SpawnParkTree(pos + new Vector3(4f, 0, 4f), pObj.transform);
                SpawnCherryBlossom(pos, pObj.transform);
                break;
            case Building.Kind.Hospital:
                BuildBiotechHospital(pos, "Biotech Medical Center", root);
                break;
            case Building.Kind.School:
                BuildQuantumAcademy(pos, "Quantum Academy", root);
                break;
            case Building.Kind.Police:
                BuildCyberPoliceHQ(pos, "Cyber Police HQ", root);
                break;
            case Building.Kind.Fire:
                BuildEmergencyFireCommand(pos, "Emergency Fire Command", root);
                break;
            case Building.Kind.Power:
                BuildFusionReactor(pos, "Fusion Power Plant", root);
                break;
            case Building.Kind.Water:
                BuildWaterFacility(pos, "Hydro Treatment Plant", root);
                break;
            case Building.Kind.Recycling:
                BuildRecyclingCenter(pos, "Eco Recycling Facility", root);
                break;
        }
    }

    public void SpawnDecoration(string type, Vector3 pos)
    {
        if (root == null) root = new GameObject("Generated Smart City").transform;
        InitMaterials();
        var dec = new GameObject(type + " Prop");
        dec.transform.position = pos;
        dec.transform.SetParent(root, true);

        switch (type)
        {
            case "Fountain":
                Cylinder("Basin", pos + Vector3.up * 0.3f, new Vector3(4.5f, 0.6f, 4.5f), chromeMat, dec.transform);
                Cylinder("Water Column", pos + Vector3.up * 1.5f, new Vector3(0.6f, 3.0f, 0.6f), poolMat, dec.transform);
                break;
            case "Flowerbed":
                Cube("Soil Bed", pos + Vector3.up * 0.15f, new Vector3(4.0f, 0.3f, 2.5f), curbMat, dec.transform);
                SpawnCherryBlossom(pos, dec.transform);
                break;
            case "Monument":
                Cube("Plinth", pos + Vector3.up * 0.4f, new Vector3(2.5f, 0.8f, 2.5f), darkMat, dec.transform);
                Cylinder("Obelisk", pos + Vector3.up * 3.5f, new Vector3(0.8f, 6.0f, 0.8f), chromeMat, dec.transform);
                Sphere("Glowing Orb", pos + Vector3.up * 6.8f, new Vector3(0.9f, 0.9f, 0.9f), neonCyanMat, dec.transform);
                break;
            case "Bench":
                Cube("Bench Seat", pos + Vector3.up * 0.4f, new Vector3(2.2f, 0.15f, 0.6f), woodMat, dec.transform);
                Cube("Bench Back", pos + Vector3.up * 0.8f + Vector3.forward * 0.25f, new Vector3(2.2f, 0.5f, 0.1f), woodMat, dec.transform);
                break;
            case "Sculpture":
                Cube("Base", pos + Vector3.up * 0.3f, new Vector3(3.0f, 0.6f, 3.0f), darkMat, dec.transform);
                Sphere("Sphere 1", pos + Vector3.up * 2.0f, new Vector3(1.8f, 1.8f, 1.8f), chromeMat, dec.transform);
                Sphere("Sphere 2", pos + Vector3.up * 3.4f, new Vector3(1.2f, 1.2f, 1.2f), neonMagentaMat, dec.transform);
                break;
        }
    }

    public void SpawnRoad()
    {
        roadSpawnIdx++;
        if (root == null) root = new GameObject("Generated Smart City").transform;
        InitMaterials();

        // Dynamically build high-speed bypass connector or elevated expressway
        float offset = (roadSpawnIdx * 35f) % 360f - 180f;
        if (roadSpawnIdx % 2 == 1)
        {
            // Diagonal Connector Boulevard
            var diag = Cube($"Smart Connector Road {roadSpawnIdx}", new Vector3(offset, 0.40f, offset * 0.75f), new Vector3(10f, 0.24f, 160f), roadMat, root);
            diag.transform.rotation = Quaternion.Euler(0, 35f, 0);
            Cube($"Connector Yellow Line {roadSpawnIdx}", new Vector3(offset, 0.46f, offset * 0.75f), new Vector3(0.2f, 0.02f, 160f), yellowLineMat, diag.transform);
        }
        else
        {
            // Elevated Smart Expressway Overpass
            var overpass = Cube($"Skyway Expressway {roadSpawnIdx}", new Vector3(0, 6.5f, offset), new Vector3(440f, 0.6f, 9.5f), roadMat, root);
            Cube($"Skyway Neon L {roadSpawnIdx}", new Vector3(0, 7.2f, offset + 4.9f), new Vector3(440f, 0.2f, 0.2f), neonCyanMat, root);
            Cube($"Skyway Neon R {roadSpawnIdx}", new Vector3(0, 7.2f, offset - 4.9f), new Vector3(440f, 0.2f, 0.2f), neonCyanMat, root);
            // Support pillars
            for (float px = -180f; px <= 180f; px += 60f)
            {
                Cylinder($"Skyway Pillar {px}", new Vector3(px, 3.2f, offset), new Vector3(2.5f, 6.5f, 2.5f), metalMat, root);
            }
        }
    }

    public void SpawnBusStop()
    {
        busStopCount++;
        float bx = -70f + (busStopCount % 4) * 45f;
        float bz = -30f + (busStopCount % 3) * 35f;
        Vector3 pos = new Vector3(bx, 0.4f, bz);
        Cube("Bus Stop Shelter", pos + Vector3.up * 1.5f, new Vector3(4.0f, 2.8f, 2.0f), darkMat, root);
        Cube("Bus Stop Glass",   pos + Vector3.up * 1.5f + Vector3.forward * 0.9f, new Vector3(3.6f, 2.5f, 0.1f), windowMat, root);
        Cube("LED Shelter Sign", pos + Vector3.up * 2.8f, new Vector3(2.2f, 0.4f, 0.1f), neonAmberMat, root);
    }

    // ── Lifecycle ─────────────────────────────────────────────────────────────

    void Awake()
    {
        Instance = this;
        if (BuildPlacementController.Instance == null)
            gameObject.AddComponent<BuildPlacementController>();
        if (ConstructionSystem.Instance == null)
            gameObject.AddComponent<ConstructionSystem>();
    }

    void Start()
    {
        BuildStarterCity();
    }

    // ── Procedural Texture Generation ─────────────────────────────────────────

    static void EnsureTextures()
    {
        if (grassTex != null) return;

        // 1. Manicured Urban Turf Grass (128x128)
        grassTex = new Texture2D(128, 128, TextureFormat.RGBA32, true);
        grassTex.wrapMode = TextureWrapMode.Repeat;
        Color[] gPix = new Color[128 * 128];
        for (int y = 0; y < 128; y++)
        {
            for (int x = 0; x < 128; x++)
            {
                float n = Mathf.PerlinNoise(x * 0.08f, y * 0.08f);
                float fine = Mathf.PerlinNoise(x * 0.30f, y * 0.30f) * 0.15f;
                float v = Mathf.Clamp01(n * 0.85f + fine);
                gPix[y * 128 + x] = Color.Lerp(new Color(0.18f, 0.48f, 0.24f), new Color(0.28f, 0.60f, 0.28f), v);
            }
        }
        grassTex.SetPixels(gPix);
        grassTex.Apply();

        // 2. High-Tech Dark Asphalt (128x128)
        asphaltTex = new Texture2D(128, 128, TextureFormat.RGBA32, true);
        asphaltTex.wrapMode = TextureWrapMode.Repeat;
        Color[] rPix = new Color[128 * 128];
        for (int y = 0; y < 128; y++)
        {
            for (int x = 0; x < 128; x++)
            {
                float grain = (Random.value - 0.5f) * 0.03f;
                float b = 0.16f + grain;
                rPix[y * 128 + x] = new Color(b, b + 0.01f, b + 0.015f);
            }
        }
        asphaltTex.SetPixels(rPix);
        asphaltTex.Apply();

        // 3. Concrete Paver Sidewalk (128x128)
        sidewalkTex = new Texture2D(128, 128, TextureFormat.RGBA32, true);
        sidewalkTex.wrapMode = TextureWrapMode.Repeat;
        Color[] sPix = new Color[128 * 128];
        for (int y = 0; y < 128; y++)
        {
            for (int x = 0; x < 128; x++)
            {
                bool grout = (x % 32 == 0 || y % 32 == 0);
                sPix[y * 128 + x] = grout ? new Color(0.48f, 0.52f, 0.58f) : new Color(0.82f, 0.84f, 0.86f);
            }
        }
        sidewalkTex.SetPixels(sPix);
        sidewalkTex.Apply();

        // 4. Urban Plaza Granite Pavers (128x128)
        plazaPaverTex = new Texture2D(128, 128, TextureFormat.RGBA32, true);
        plazaPaverTex.wrapMode = TextureWrapMode.Repeat;
        Color[] pPix = new Color[128 * 128];
        for (int y = 0; y < 128; y++)
        {
            for (int x = 0; x < 128; x++)
            {
                bool seam = (x % 16 == 0 || y % 16 == 0);
                pPix[y * 128 + x] = seam ? new Color(0.38f, 0.42f, 0.48f) : (((x / 16 + y / 16) % 2 == 0) ? new Color(0.85f, 0.88f, 0.90f) : new Color(0.76f, 0.79f, 0.82f));
            }
        }
        plazaPaverTex.SetPixels(pPix);
        plazaPaverTex.Apply();

        // 5. Commercial Skyscraper Glass Curtain (256x256)
        skyscraperGlassTex = new Texture2D(256, 256, TextureFormat.RGBA32, true);
        skyscraperGlassTex.wrapMode = TextureWrapMode.Repeat;
        skyscraperEmissionTex = new Texture2D(256, 256, TextureFormat.RGBA32, true);
        skyscraperEmissionTex.wrapMode = TextureWrapMode.Repeat;

        Color[] skyPix = new Color[256 * 256];
        Color[] emPix  = new Color[256 * 256];

        Random.State state = Random.state;
        Random.InitState(101);

        for (int y = 0; y < 256; y++)
        {
            int floor = y / 16;
            bool floorMullion = (y % 16 < 2);

            for (int x = 0; x < 256; x++)
            {
                int bay = x / 16;
                bool colMullion = (x % 16 < 2);
                int idx = y * 256 + x;

                if (floorMullion || colMullion)
                {
                    skyPix[idx] = new Color(0.65f, 0.72f, 0.80f);
                    emPix[idx]  = Color.black;
                }
                else
                {
                    bool isLit = (Mathf.Sin(floor * 4.5f + bay * 7.2f) > -0.2f);
                    if (isLit)
                    {
                        Color litCol = Color.Lerp(new Color(1.0f, 0.92f, 0.65f), new Color(0.30f, 0.88f, 1.0f), (bay % 2 == 0) ? 0.85f : 0.15f);
                        skyPix[idx] = litCol * 0.95f;
                        emPix[idx]  = litCol * 0.85f;
                    }
                    else
                    {
                        skyPix[idx] = new Color(0.08f, 0.18f, 0.32f);
                        emPix[idx]  = Color.black;
                    }
                }
            }
        }
        Random.state = state;

        skyscraperGlassTex.SetPixels(skyPix);
        skyscraperGlassTex.Apply();
        skyscraperEmissionTex.SetPixels(emPix);
        skyscraperEmissionTex.Apply();

        // 6. Modern Glass Texture (64x64)
        modernGlassTex = new Texture2D(64, 64, TextureFormat.RGBA32, true);
        Color[] mPix = new Color[64 * 64];
        for (int i = 0; i < mPix.Length; i++)
            mPix[i] = new Color(0.40f, 0.72f, 0.95f, 0.85f);
        modernGlassTex.SetPixels(mPix);
        modernGlassTex.Apply();

        // 7. Water Ripple Texture (128x128)
        waterTex = new Texture2D(128, 128, TextureFormat.RGBA32, true);
        waterTex.wrapMode = TextureWrapMode.Repeat;
        Color[] wPix = new Color[128 * 128];
        for (int y = 0; y < 128; y++)
        {
            for (int x = 0; x < 128; x++)
            {
                float w = Mathf.Sin(x * 0.12f) * Mathf.Cos(y * 0.12f) * 0.5f + 0.5f;
                wPix[y * 128 + x] = Color.Lerp(new Color(0.08f, 0.38f, 0.68f), new Color(0.20f, 0.62f, 0.88f), w);
            }
        }
        waterTex.SetPixels(wPix);
        waterTex.Apply();

        // 8. Solar Panel Grid (64x64)
        solarTex = new Texture2D(64, 64, TextureFormat.RGBA32, true);
        Color[] solPix = new Color[64 * 64];
        for (int y = 0; y < 64; y++)
        {
            for (int x = 0; x < 64; x++)
            {
                bool grid = (x % 8 == 0 || y % 8 == 0);
                solPix[y * 64 + x] = grid ? new Color(0.70f, 0.75f, 0.85f) : new Color(0.04f, 0.12f, 0.35f);
            }
        }
        solarTex.SetPixels(solPix);
        solarTex.Apply();

        // 9. Wood Planks (64x64)
        woodPlankTex = new Texture2D(64, 64, TextureFormat.RGBA32, true);
        Color[] wdPix = new Color[64 * 64];
        for (int y = 0; y < 64; y++)
        {
            for (int x = 0; x < 64; x++)
            {
                bool groove = (y % 16 == 0);
                wdPix[y * 64 + x] = groove ? new Color(0.35f, 0.22f, 0.12f) : new Color(0.62f, 0.44f, 0.28f);
            }
        }
        woodPlankTex.SetPixels(wdPix);
        woodPlankTex.Apply();

        // 10. Stadium Sports Turf (128x128)
        stadiumFieldTex = new Texture2D(128, 128, TextureFormat.RGBA32, true);
        Color[] stPix = new Color[128 * 128];
        for (int y = 0; y < 128; y++)
        {
            for (int x = 0; x < 128; x++)
            {
                bool stripe = (y / 16) % 2 == 0;
                bool border = (x < 6 || x > 121 || y < 6 || y > 121 || x == 64 || (x >= 50 && x <= 78 && y >= 50 && y <= 78 && ((x-64)*(x-64) + (y-64)*(y-64) > 100 && (x-64)*(x-64) + (y-64)*(y-64) < 160)));
                if (border) stPix[y * 128 + x] = Color.white;
                else stPix[y * 128 + x] = stripe ? new Color(0.18f, 0.58f, 0.22f) : new Color(0.24f, 0.66f, 0.28f);
            }
        }
        stadiumFieldTex.SetPixels(stPix);
        stadiumFieldTex.Apply();

        // 11. Holographic Billboard Graphic (128x64)
        billboardTex = new Texture2D(128, 64, TextureFormat.RGBA32, true);
        Color[] bPix = new Color[128 * 64];
        for (int y = 0; y < 64; y++)
        {
            for (int x = 0; x < 64; x++)
            {
                float grad = (float)x / 128f;
                Color baseC = Color.Lerp(new Color(0.05f, 0.85f, 1.0f), new Color(1.0f, 0.20f, 0.65f), grad);
                bool grid = (x % 8 == 0 || y % 8 == 0);
                bPix[y * 128 + x] = grid ? baseC * 1.3f : baseC * 0.85f;
            }
        }
        billboardTex.SetPixels(bPix);
        billboardTex.Apply();
    }

    void InitMaterials()
    {
        if (matsInit) return;
        EnsureTextures();

        roadMat        = Mat(new Color(0.16f, 0.17f, 0.19f), 0.30f, 0.15f, mainTex: asphaltTex);
        curbMat        = Mat(new Color(0.55f, 0.58f, 0.62f), 0.25f, 0.20f);
        sidewalkMat    = Mat(new Color(0.82f, 0.84f, 0.86f), 0.25f, 0.15f, mainTex: sidewalkTex);
        lineMat        = Mat(Color.white, 0.1f, 0.1f);
        yellowLineMat  = Mat(new Color(1.0f, 0.82f, 0.12f), 0.2f, 0.1f);

        grassMat       = Mat(new Color(0.25f, 0.55f, 0.28f), 0.15f, 0.05f, mainTex: grassTex);
        parkMat        = Mat(new Color(0.20f, 0.65f, 0.28f), 0.15f, 0.05f, mainTex: grassTex);
        plazaMat       = Mat(new Color(0.86f, 0.88f, 0.90f), 0.30f, 0.25f, mainTex: plazaPaverTex);
        sandMat        = Mat(new Color(0.88f, 0.82f, 0.62f), 0.10f, 0.05f);
        woodMat        = Mat(new Color(0.58f, 0.40f, 0.24f), 0.20f, 0.10f, mainTex: woodPlankTex);
        pierMat        = Mat(new Color(0.45f, 0.32f, 0.20f), 0.20f, 0.10f, mainTex: woodPlankTex);

        waterMat       = Mat(new Color(0.12f, 0.45f, 0.72f), 0.80f, 0.95f, new Color(0.04f, 0.20f, 0.35f), waterTex);
        oceanMat       = Mat(new Color(0.08f, 0.35f, 0.62f), 0.85f, 0.95f, new Color(0.03f, 0.15f, 0.30f), waterTex);
        poolMat        = Mat(new Color(0.20f, 0.80f, 0.95f), 0.90f, 0.95f, new Color(0.10f, 0.45f, 0.65f));

        darkMat        = Mat(new Color(0.10f, 0.12f, 0.16f), 0.40f, 0.30f);
        metalMat       = Mat(new Color(0.72f, 0.75f, 0.80f), 0.70f, 0.80f);
        chromeMat      = Mat(new Color(0.92f, 0.94f, 0.96f), 0.90f, 0.95f);
        windowMat      = Mat(new Color(0.55f, 0.85f, 1.0f), 0.60f, 0.95f, new Color(0.25f, 0.50f, 0.85f));
        glassRailMat   = Mat(new Color(0.60f, 0.88f, 1.0f, 0.70f), 0.85f, 0.95f, new Color(0.20f, 0.45f, 0.70f));

        // Neon Accents
        neonCyanMat    = Mat(new Color(0.10f, 0.90f, 1.0f), 0.20f, 0.90f, new Color(0.10f, 0.90f, 1.0f) * 1.6f);
        neonAmberMat   = Mat(new Color(1.0f, 0.70f, 0.10f), 0.20f, 0.90f, new Color(1.0f, 0.70f, 0.10f) * 1.6f);
        neonMagentaMat = Mat(new Color(1.0f, 0.20f, 0.75f), 0.20f, 0.90f, new Color(1.0f, 0.20f, 0.75f) * 1.6f);
        neonGreenMat   = Mat(new Color(0.15f, 1.0f, 0.45f), 0.20f, 0.90f, new Color(0.15f, 1.0f, 0.45f) * 1.6f);

        // Atmosphere
        sunMat         = Mat(new Color(1.0f, 0.98f, 0.90f), 0.0f, 0.0f, new Color(1.0f, 0.98f, 0.90f) * 2.5f);
        cloudMat       = Mat(new Color(1.0f, 1.0f, 1.0f, 0.95f), 0.1f, 0.1f);

        // Building / District themes
        residentialMat = Mat(new Color(0.92f, 0.94f, 0.96f), 0.40f, 0.30f);
        commercialMat  = Mat(new Color(0.20f, 0.45f, 0.75f), 0.65f, 0.90f, emissionTex: skyscraperEmissionTex, mainTex: skyscraperGlassTex);
        industrialMat  = Mat(new Color(0.25f, 0.28f, 0.34f), 0.50f, 0.40f);
        serviceMat     = Mat(new Color(0.85f, 0.88f, 0.92f), 0.50f, 0.40f);

        hospitalMat    = Mat(new Color(0.94f, 0.96f, 0.98f), 0.60f, 0.40f);
        schoolMat      = Mat(new Color(0.90f, 0.86f, 0.78f), 0.35f, 0.20f);
        policeMat      = Mat(new Color(0.12f, 0.22f, 0.42f), 0.65f, 0.60f);
        fireMat        = Mat(new Color(0.65f, 0.15f, 0.15f), 0.55f, 0.40f);
        powerMat       = Mat(new Color(0.25f, 0.28f, 0.34f), 0.65f, 0.60f);

        solarMat       = Mat(new Color(0.10f, 0.20f, 0.50f), 0.80f, 0.90f, new Color(0.05f, 0.15f, 0.35f), solarTex);
        redCrossMat    = Mat(new Color(0.95f, 0.10f, 0.10f), 0.30f, 0.30f, new Color(0.95f, 0.10f, 0.10f) * 1.5f);
        helipadMat     = Mat(new Color(0.22f, 0.25f, 0.30f), 0.40f, 0.20f);
        stadiumMat     = Mat(new Color(0.22f, 0.60f, 0.25f), 0.20f, 0.10f, mainTex: stadiumFieldTex);
        billboardMat   = Mat(Color.white, 0.5f, 0.8f, Color.white * 1.2f, billboardTex);

        // Vehicles
        tireMat        = Mat(new Color(0.10f, 0.10f, 0.10f), 0.15f, 0.05f);
        rimMat         = Mat(new Color(0.88f, 0.90f, 0.92f), 0.85f, 0.95f);
        headLightMat   = Mat(Color.white, 0.2f, 0.9f, Color.white * 2.2f);
        tailLightMat   = Mat(new Color(1f, 0.05f, 0.05f), 0.2f, 0.9f, new Color(1f, 0.05f, 0.05f) * 2.0f);
        sirenBlueMat   = Mat(new Color(0.1f, 0.5f, 1f), 0.2f, 0.9f, new Color(0.1f, 0.5f, 1f) * 2.0f);
        cherryMat      = Mat(new Color(0.95f, 0.65f, 0.78f), 0.20f, 0.10f);
        turbineMat     = Mat(new Color(0.94f, 0.96f, 0.98f), 0.60f, 0.50f);

        matsInit = true;
    }

    Material Mat(Color c, float smoothness = 0.5f, float metallic = 0.0f, Color? emission = null, Texture2D mainTex = null, Texture2D emissionTex = null)
    {
        var s = Shader.Find("Standard");
        if (s == null) s = Shader.Find("Universal Render Pipeline/Lit");
        if (s == null) s = Shader.Find("Diffuse");
        var m = new Material(s);
        m.color = c;
        if (mainTex != null) m.mainTexture = mainTex;
        if (m.HasProperty("_Glossiness")) m.SetFloat("_Glossiness", smoothness);
        if (m.HasProperty("_Smoothness")) m.SetFloat("_Smoothness", smoothness);
        if (m.HasProperty("_Metallic")) m.SetFloat("_Metallic", metallic);

        if (emission.HasValue && emission.Value != Color.black)
        {
            m.EnableKeyword("_EMISSION");
            m.SetColor("_EmissionColor", emission.Value);
            if (emissionTex != null) m.SetTexture("_EmissionMap", emissionTex);
        }
        else if (emissionTex != null)
        {
            m.EnableKeyword("_EMISSION");
            m.SetColor("_EmissionColor", Color.white);
            m.SetTexture("_EmissionMap", emissionTex);
        }
        return m;
    }

    // ── Master Build ──────────────────────────────────────────────────────────

    public void BuildStarterCity()
    {
        var existing = GameObject.Find("Generated Smart City");
        if (existing != null) DestroyImmediate(existing);

        root = new GameObject("Generated Smart City").transform;
        InitMaterials();

        roadSpawnIdx = 0;
        busStopCount = 0;

        // 1. Atmosphere & Ocean Environment
        BuildAtmosphereAndLandscape();

        // 2. Comprehensive Multi-Lane Boulevard Network with Streetlights
        BuildRoadNetwork();

        // 3. DOWNTOWN FINANCIAL & HIGH-TECH CLUSTER (Skyscrapers with Glass Facades & Helipads)
        BuildDowntownMetropolis();

        // 4. CIVIC & ACADEMIC PAVILIONS (High-Tech Police HQ, Fire Command, Medical Center, Quantum Academy)
        BuildCivicAndInnovationCampus();

        // 5. RESIDENTIAL, SPORTS & ENTERTAINMENT DISTRICTS (Stadium, Luxury Residences, Shopping Mall)
        BuildResidentialAndSportsDistricts();

        // 6. CENTRAL METROPOLITAN PARK & BOTANICAL LAKE
        BuildCentralParkAndPlaza();

        // 7. WATERFRONT SILICON PARK, VILLAS & SEASIDE MARINA
        BuildWaterfrontMarinaAndTechPark();

        // 8. ECO-ENERGY PARK & OFFSHORE TURBINES (In Distant Ocean)
        BuildEcoEnergySector();

        // 9. Active Flowing Traffic Fleet & Flying Sky-Drones
        SpawnUrbanLife();
    }

    // ── 1. Atmosphere & Landscape ─────────────────────────────────────────────

    void BuildAtmosphereAndLandscape()
    {
        // Infinite Ocean Surface
        var ocean = Cube("Ocean Surface", new Vector3(0, -0.45f, 0), new Vector3(4000, 0.4f, 4000), oceanMat, root);
        ocean.AddComponent<RiverWaterFlow>();

        // Metropolis Main Island
        Cube("City Island Ground", new Vector3(0, 0.20f, 0), new Vector3(460, 0.40f, 420), grassMat, root);
        Cube("Beach Shoreline",    new Vector3(0, 0.05f, 0), new Vector3(488, 0.30f, 448), sandMat, root);

        // Modern White Concrete Seawalls
        Cube("Seawall North", new Vector3(0, 0.25f,  211f), new Vector3(464, 0.7f, 2.4f), curbMat, root);
        Cube("Seawall South", new Vector3(0, 0.25f, -211f), new Vector3(464, 0.7f, 2.4f), curbMat, root);
        Cube("Seawall West",  new Vector3(-231f, 0.25f, 0), new Vector3(2.4f, 0.7f, 424), curbMat, root);
        Cube("Seawall East",  new Vector3( 231f, 0.25f, 0), new Vector3(2.4f, 0.7f, 424), curbMat, root);

        // Waterfront Promenade with Glass Railings
        Cube("Waterfront Promenade N", new Vector3(0, 0.42f,  206f), new Vector3(460, 0.15f, 7.0f), plazaMat, root);
        Cube("Waterfront Promenade S", new Vector3(0, 0.42f, -206f), new Vector3(460, 0.15f, 7.0f), plazaMat, root);
        Cube("Glass Railing N",        new Vector3(0, 0.95f,  209.5f), new Vector3(460, 0.90f, 0.12f), glassRailMat, root);
        Cube("Glass Railing S",        new Vector3(0, 0.95f, -209.5f), new Vector3(460, 0.90f, 0.12f), glassRailMat, root);

        // Glowing 3D Sun Disc
        Sphere("Sun Disc", new Vector3(450f, 380f, 550f), new Vector3(85f, 85f, 85f), sunMat, root);

        // Dynamic Cumulus Clouds
        Vector3[] cloudCenters = {
            new Vector3(-250f, 170f,  300f),
            new Vector3( 180f, 190f,  380f),
            new Vector3( 320f, 180f, -220f),
            new Vector3(-340f, 200f, -260f),
            new Vector3(   0f, 210f,  450f)
        };

        for (int i = 0; i < cloudCenters.Length; i++)
        {
            var cg = new GameObject($"Cumulus_Cloud_{i}");
            cg.transform.position = cloudCenters[i];
            cg.transform.SetParent(root, true);
            Sphere("Cloud Core", cloudCenters[i], new Vector3(90f, 28f, 55f), cloudMat, cg.transform);
            Sphere("Cloud Puff L", cloudCenters[i] + new Vector3(-32f, 6f, 0), new Vector3(55f, 35f, 45f), cloudMat, cg.transform);
            Sphere("Cloud Puff R", cloudCenters[i] + new Vector3( 32f, 8f, 0), new Vector3(60f, 38f, 48f), cloudMat, cg.transform);
        }
    }

    // ── 2. Road Network ───────────────────────────────────────────────────────

    void BuildRoadNetwork()
    {
        foreach (float x in MainBoulevardsX)
            RoadBoulevard(x, true, 420f);
        foreach (float z in MainBoulevardsZ)
            RoadBoulevard(z, false, 460f);

        // Modern Low-Profile River with glass embankment
        var river = Cube("River Water", new Vector3(0, 0.22f, 130f), new Vector3(460, 0.22f, 28f), waterMat, root);
        river.AddComponent<RiverWaterFlow>();
        Cube("River Embankment N", new Vector3(0, 0.42f, 144.5f), new Vector3(460, 0.40f, 1.6f), curbMat, root);
        Cube("River Embankment S", new Vector3(0, 0.42f, 115.5f), new Vector3(460, 0.40f, 1.6f), curbMat, root);

        foreach (float x in MainBoulevardsX)
            BuildModernBridge(new Vector3(x, 0.45f, 130f));
    }

    void RoadBoulevard(float coord, bool isColumn, float length)
    {
        Vector3 pos = isColumn ? new Vector3(coord, 0.36f, 0) : new Vector3(0, 0.36f, coord);
        Vector3 size = isColumn ? new Vector3(8.0f, 0.22f, length) : new Vector3(length, 0.22f, 8.0f);

        Cube(isColumn ? "Avenue Col Asphalt" : "Avenue Row Asphalt", pos, size, roadMat, root);

        if (isColumn)
        {
            Cube("Curb W", new Vector3(coord - 4.1f, 0.42f, 0), new Vector3(0.24f, 0.28f, length), curbMat, root);
            Cube("Curb E", new Vector3(coord + 4.1f, 0.42f, 0), new Vector3(0.24f, 0.28f, length), curbMat, root);
            Cube("Sidewalk W", new Vector3(coord - 5.3f, 0.40f, 0), new Vector3(2.2f, 0.26f, length), sidewalkMat, root);
            Cube("Sidewalk E", new Vector3(coord + 5.3f, 0.40f, 0), new Vector3(2.2f, 0.26f, length), sidewalkMat, root);
            Cube("Yellow Line L", new Vector3(coord - 0.15f, 0.48f, 0), new Vector3(0.10f, 0.02f, length), yellowLineMat, root);
            Cube("Yellow Line R", new Vector3(coord + 0.15f, 0.48f, 0), new Vector3(0.10f, 0.02f, length), yellowLineMat, root);
        }
        else
        {
            Cube("Curb S", new Vector3(0, 0.42f, coord - 4.1f), new Vector3(length, 0.28f, 0.24f), curbMat, root);
            Cube("Curb N", new Vector3(0, 0.42f, coord + 4.1f), new Vector3(length, 0.28f, 0.24f), curbMat, root);
            Cube("Sidewalk S", new Vector3(0, 0.40f, coord - 5.3f), new Vector3(length, 0.26f, 2.2f), sidewalkMat, root);
            Cube("Sidewalk N", new Vector3(0, 0.40f, coord + 5.3f), new Vector3(length, 0.26f, 2.2f), sidewalkMat, root);
            Cube("Yellow Line S", new Vector3(0, 0.48f, coord - 0.15f), new Vector3(length, 0.02f, 0.10f), yellowLineMat, root);
            Cube("Yellow Line N", new Vector3(0, 0.48f, coord + 0.15f), new Vector3(length, 0.02f, 0.10f), yellowLineMat, root);
        }

        float[] crossCoords = isColumn ? MainBoulevardsZ : MainBoulevardsX;
        foreach (float cr in crossCoords)
        {
            Vector3 center = isColumn ? new Vector3(coord, 0.38f, cr) : new Vector3(cr, 0.38f, coord);
            Cube("Intersection Base", center, new Vector3(8.2f, 0.24f, 8.2f), roadMat, root);

            for (int z = -3; z <= 3; z += 2)
            {
                Cube("Zebra N", center + new Vector3(z * 0.9f, 0.12f, 4.6f), new Vector3(0.5f, 0.02f, 1.2f), lineMat, root);
                Cube("Zebra S", center + new Vector3(z * 0.9f, 0.12f, -4.6f), new Vector3(0.5f, 0.02f, 1.2f), lineMat, root);
            }

            BuildModernStreetLight(center + new Vector3( 5.5f, 0,  5.5f), -45f);
            BuildModernStreetLight(center + new Vector3(-5.5f, 0, -5.5f), 135f);
            BuildTrafficLight(center + new Vector3( 4.8f, 0, -4.8f));
        }
    }

    void BuildModernBridge(Vector3 pos)
    {
        var bridge = new GameObject("Boulevard Skybridge");
        bridge.transform.position = pos;
        bridge.transform.SetParent(root, true);

        Cube("Bridge Deck", pos + Vector3.up * 0.25f, new Vector3(9.2f, 0.6f, 32f), roadMat, bridge.transform);
        Cube("Bridge Arch L", pos + new Vector3(-5.2f, 3.5f, 0), new Vector3(0.6f, 7.0f, 32f), metalMat, bridge.transform);
        Cube("Bridge Arch R", pos + new Vector3( 5.2f, 3.5f, 0), new Vector3(0.6f, 7.0f, 32f), metalMat, bridge.transform);
        Cube("Neon Ribbon L", pos + new Vector3(-5.55f, 7.1f, 0), new Vector3(0.12f, 0.2f, 32f), neonCyanMat, bridge.transform);
        Cube("Neon Ribbon R", pos + new Vector3( 5.55f, 7.1f, 0), new Vector3(0.12f, 0.2f, 32f), neonCyanMat, bridge.transform);
    }

    void BuildModernStreetLight(Vector3 pos, float yaw)
    {
        var pole = new GameObject("StreetLight");
        pole.transform.position = pos;
        pole.transform.rotation = Quaternion.Euler(0, yaw, 0);
        pole.transform.SetParent(root, true);

        Cylinder("Pole", pos + Vector3.up * 3.5f, new Vector3(0.14f, 7.0f, 0.14f), metalMat, pole.transform);
        Cube("Arm", pos + Vector3.up * 7.1f + pole.transform.forward * 0.9f, new Vector3(0.10f, 0.10f, 1.8f), metalMat, pole.transform);
        Cube("Luminaire", pos + Vector3.up * 7.0f + pole.transform.forward * 1.6f, new Vector3(0.35f, 0.12f, 0.70f), chromeMat, pole.transform);
        Cube("LED Emitter", pos + Vector3.up * 6.92f + pole.transform.forward * 1.6f, new Vector3(0.30f, 0.04f, 0.60f), headLightMat, pole.transform);
    }

    void BuildTrafficLight(Vector3 pos)
    {
        var tl = new GameObject("TrafficSignal");
        tl.transform.position = pos;
        tl.transform.SetParent(root, true);

        Cylinder("Pole", pos + Vector3.up * 2.8f, new Vector3(0.12f, 5.6f, 0.12f), darkMat, tl.transform);
        Cube("Housing", pos + Vector3.up * 5.0f, new Vector3(0.35f, 1.2f, 0.35f), darkMat, tl.transform);
        Sphere("Red Light", pos + Vector3.up * 5.4f + Vector3.forward * 0.18f, new Vector3(0.2f, 0.2f, 0.2f), tailLightMat, tl.transform);
        Sphere("Green Light", pos + Vector3.up * 4.6f + Vector3.forward * 0.18f, new Vector3(0.2f, 0.2f, 0.2f), neonGreenMat, tl.transform);
    }

    // ── 3. Downtown Financial Metropolis ──────────────────────────────────────

    void BuildDowntownMetropolis()
    {
        // Central Plaza Podium Block (-25, 0, -20)
        Vector3 cPos = new Vector3(-25f, 0.45f, -20f);
        var basePlaza = Cube("Metropolis Plaza Podium", cPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), plazaMat, root);

        // 1. Apex Cyber Spire (95m Flagship Skyscraper)
        BuildApexSkyscraper(cPos + new Vector3(-10f, 0, 6f), 95f, "Apex Cyber Spire", basePlaza.transform);

        // 2. Nexus Twin Towers with Glass Skybridge (75m each)
        BuildNexusTwinTowers(cPos + new Vector3(10f, 0, -4f), 75f, basePlaza.transform);

        // 3. Cyber Quantum Tower (82m) at Block (25, 0, -20)
        Vector3 ePos = new Vector3(25f, 0.45f, -20f);
        var ePlaza = Cube("East Tech Plaza Podium", ePos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), plazaMat, root);
        BuildApexSkyscraper(ePos + new Vector3(8f, 0, 4f), 82f, "Quantum Core Tower", ePlaza.transform);
        BuildModernOfficeBlock(ePos + new Vector3(-10f, 0, -4f), 48f, "Helix FinTech Center", ePlaza.transform);

        // 4. North Commercial Plaza (Block (25, 0, 20))
        Vector3 nPos = new Vector3(25f, 0.45f, 20f);
        var nPlaza = Cube("North Retail Plaza", nPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), plazaMat, root);
        BuildHolographicMall(nPos, nPlaza.transform);

        // 5. West Financial Tower (Block (-75, 0, 20))
        Vector3 wPos = new Vector3(-75f, 0.45f, 20f);
        var wPlaza = Cube("West Plaza", wPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), plazaMat, root);
        BuildApexSkyscraper(wPos + new Vector3(-6f, 0, 0), 68f, "Vanguard Capital Tower", wPlaza.transform);
        BuildModernOfficeBlock(wPos + new Vector3(10f, 0, 0), 42f, "Cyber Data Systems", wPlaza.transform);
    }

    void BuildApexSkyscraper(Vector3 pos, float height, string name, Transform parent)
    {
        var tower = new GameObject(name);
        tower.transform.position = pos;
        tower.transform.SetParent(parent, true);

        var b = tower.AddComponent<Building>();
        b.kind = Building.Kind.Commercial;
        b.buildingName = name;
        b.baseUpgradeCost = 12000f;

        Cube("Podium", pos + Vector3.up * 5.0f, new Vector3(18f, 10.0f, 18f), darkMat, tower.transform);
        Cube("Glass Lobby", pos + Vector3.up * 3.5f + Vector3.forward * 9.1f, new Vector3(12f, 6.5f, 0.2f), windowMat, tower.transform);

        float bodyH = height * 0.70f;
        Cube("Glass Shaft", pos + Vector3.up * (10f + bodyH * 0.5f), new Vector3(14.5f, bodyH, 14.5f), commercialMat, tower.transform);
        Cube("Corner Pillar NW", pos + Vector3.up * (10f + bodyH * 0.5f) + new Vector3(-7.3f, 0, -7.3f), new Vector3(0.6f, bodyH, 0.6f), chromeMat, tower.transform);
        Cube("Corner Pillar NE", pos + Vector3.up * (10f + bodyH * 0.5f) + new Vector3( 7.3f, 0, -7.3f), new Vector3(0.6f, bodyH, 0.6f), chromeMat, tower.transform);
        Cube("Corner Pillar SW", pos + Vector3.up * (10f + bodyH * 0.5f) + new Vector3(-7.3f, 0,  7.3f), new Vector3(0.6f, bodyH, 0.6f), chromeMat, tower.transform);
        Cube("Corner Pillar SE", pos + Vector3.up * (10f + bodyH * 0.5f) + new Vector3( 7.3f, 0,  7.3f), new Vector3(0.6f, bodyH, 0.6f), chromeMat, tower.transform);

        float crownH = height * 0.22f;
        Vector3 crownPos = pos + Vector3.up * (10f + bodyH + crownH * 0.5f);
        Cube("Crown Shaft", crownPos, new Vector3(10.5f, crownH, 10.5f), commercialMat, tower.transform);

        Vector3 roofPos = pos + Vector3.up * (10f + bodyH + crownH);
        Cylinder("Helipad", roofPos + Vector3.up * 0.3f, new Vector3(9.5f, 0.5f, 9.5f), helipadMat, tower.transform);
        Cube("Heli Cross 1", roofPos + Vector3.up * 0.6f, new Vector3(5.5f, 0.05f, 1.2f), yellowLineMat, tower.transform);
        Cube("Heli Cross 2", roofPos + Vector3.up * 0.6f, new Vector3(1.2f, 0.05f, 5.5f), yellowLineMat, tower.transform);

        Cylinder("Antenna Base", roofPos + Vector3.up * 4.0f, new Vector3(0.8f, 8.0f, 0.8f), metalMat, tower.transform);
        Cylinder("Needle Spire", roofPos + Vector3.up * 12.0f, new Vector3(0.2f, 16.0f, 0.2f), chromeMat, tower.transform);
        Sphere("Beacon Light", roofPos + Vector3.up * 20.0f, new Vector3(0.6f, 0.6f, 0.6f), neonMagentaMat, tower.transform);

        Cube("Neon Ribbon W", pos + Vector3.up * (height * 0.5f) + new Vector3(-7.4f, 0, 0), new Vector3(0.12f, height * 0.88f, 0.35f), neonCyanMat, tower.transform);
        Cube("Neon Ribbon E", pos + Vector3.up * (height * 0.5f) + new Vector3( 7.4f, 0, 0), new Vector3(0.12f, height * 0.88f, 0.35f), neonCyanMat, tower.transform);
    }

    void BuildNexusTwinTowers(Vector3 center, float height, Transform parent)
    {
        var complex = new GameObject("Nexus Twin Towers");
        complex.transform.position = center;
        complex.transform.SetParent(parent, true);

        var b = complex.AddComponent<Building>();
        b.kind = Building.Kind.Commercial;
        b.buildingName = "Nexus Twin Towers";
        b.baseUpgradeCost = 15000f;

        Vector3 posA = center + new Vector3(-7.5f, 0, 0);
        Vector3 posB = center + new Vector3( 7.5f, 0, 0);

        Cube("Tower A", posA + Vector3.up * (height * 0.5f), new Vector3(10.5f, height, 10.5f), commercialMat, complex.transform);
        Cube("Tower B", posB + Vector3.up * (height * 0.5f), new Vector3(10.5f, height, 10.5f), commercialMat, complex.transform);

        float bridgeY = height * 0.62f;
        Vector3 bridgePos = center + Vector3.up * bridgeY;
        Cube("Skybridge Deck", bridgePos, new Vector3(15f, 4.2f, 5.0f), darkMat, complex.transform);
        Cube("Skybridge Glass N", bridgePos + new Vector3(0, 0,  2.55f), new Vector3(15f, 3.8f, 0.1f), windowMat, complex.transform);
        Cube("Skybridge Glass S", bridgePos + new Vector3(0, 0, -2.55f), new Vector3(15f, 3.8f, 0.1f), windowMat, complex.transform);
        Cube("Skybridge Neon N",  bridgePos + new Vector3(0, -2.1f, 2.6f), new Vector3(15f, 0.18f, 0.18f), neonCyanMat, complex.transform);
        Cube("Skybridge Neon S",  bridgePos + new Vector3(0, -2.1f,-2.6f), new Vector3(15f, 0.18f, 0.18f), neonCyanMat, complex.transform);
    }

    void BuildModernOfficeBlock(Vector3 pos, float height, string name, Transform parent)
    {
        var bObj = new GameObject(name);
        bObj.transform.position = pos;
        bObj.transform.SetParent(parent, true);

        var b = bObj.AddComponent<Building>();
        b.kind = Building.Kind.Commercial;
        b.buildingName = name;
        b.baseUpgradeCost = 9000f;

        Cube("Office Body", pos + Vector3.up * (height * 0.5f), new Vector3(14.0f, height, 13.0f), commercialMat, bObj.transform);
        Cube("Glass Facade", pos + Vector3.up * (height * 0.5f) + Vector3.forward * 6.55f, new Vector3(12.5f, height * 0.90f, 0.15f), windowMat, bObj.transform);
        Cube("Roof AC Unit", pos + Vector3.up * (height + 1.5f), new Vector3(4.5f, 2.5f, 3.5f), darkMat, bObj.transform);
    }

    void BuildHolographicMall(Vector3 pos, Transform parent)
    {
        var mall = new GameObject("Cyber Nexus Shopping Mall");
        mall.transform.position = pos;
        mall.transform.SetParent(parent, true);

        var b = mall.AddComponent<Building>();
        b.kind = Building.Kind.Commercial;
        b.buildingName = "Cyber Nexus Mall";
        b.baseUpgradeCost = 10000f;

        Cube("Mall Pavilion", pos + Vector3.up * 8.0f, new Vector3(32f, 16f, 24f), darkMat, mall.transform);
        Cube("Curved Glass Atrium", pos + Vector3.up * 9.0f + Vector3.forward * 12.1f, new Vector3(22f, 14f, 0.3f), windowMat, mall.transform);
        Cube("Holographic Billboard", pos + Vector3.up * 18.0f, new Vector3(18f, 7.0f, 0.3f), billboardMat, mall.transform);
        Cube("Entrance Canopy", pos + Vector3.up * 3.5f + Vector3.forward * 14.0f, new Vector3(16f, 0.5f, 4.0f), chromeMat, mall.transform);
    }

    // ── 4. Civic & Innovation Campus ──────────────────────────────────────────

    void BuildCivicAndInnovationCampus()
    {
        // Block (25, 0, -60): Smart Medical & Quantum Academy
        Vector3 sPos = new Vector3(25f, 0.45f, -60f);
        var sPlaza = Cube("Civic Campus Plaza", sPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), plazaMat, root);

        BuildBiotechHospital(sPos + new Vector3(-10f, 0, 0), "Biotech Medical Center", sPlaza.transform);
        BuildQuantumAcademy(sPos + new Vector3(10f, 0, 0), "Quantum Tech Academy", sPlaza.transform);

        // Block (-25, 0, -60): Cyber Police HQ & Emergency Services
        Vector3 mPos = new Vector3(-25f, 0.45f, -60f);
        var mPlaza = Cube("Municipal Services Plaza", mPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), plazaMat, root);

        BuildCyberPoliceHQ(mPos + new Vector3(-10f, 0, 0), "Cyber Police Headquarters", mPlaza.transform);
        BuildEmergencyFireCommand(mPos + new Vector3(10f, 0, 0), "Emergency Command Station", mPlaza.transform);
    }

    void BuildBiotechHospital(Vector3 pos, string name, Transform parent)
    {
        var hObj = new GameObject(name);
        hObj.transform.position = pos;
        hObj.transform.SetParent(parent, true);

        var b = hObj.AddComponent<Building>();
        b.kind = Building.Kind.Hospital;
        b.buildingName = name;
        b.baseUpgradeCost = 11000f;

        Cube("Podium", pos + Vector3.up * 4.0f, new Vector3(20f, 8f, 18f), hospitalMat, hObj.transform);
        Cube("Main Tower", pos + Vector3.up * 18.0f, new Vector3(16f, 20f, 14f), hospitalMat, hObj.transform);
        Cube("Glass Atrium", pos + Vector3.up * 18.0f + Vector3.forward * 7.1f, new Vector3(13f, 16f, 0.3f), windowMat, hObj.transform);

        Cube("Red Cross H", pos + Vector3.up * 24.0f + Vector3.forward * 7.2f, new Vector3(5.0f, 1.4f, 0.2f), redCrossMat, hObj.transform);
        Cube("Red Cross V", pos + Vector3.up * 24.0f + Vector3.forward * 7.2f, new Vector3(1.4f, 5.0f, 0.2f), redCrossMat, hObj.transform);

        Cylinder("Helipad", pos + Vector3.up * 28.3f, new Vector3(10f, 0.5f, 10f), helipadMat, hObj.transform);
        Cube("Cross 1", pos + Vector3.up * 28.6f, new Vector3(6f, 0.05f, 1.2f), yellowLineMat, hObj.transform);
        Cube("Cross 2", pos + Vector3.up * 28.6f, new Vector3(1.2f, 0.05f, 6f), yellowLineMat, hObj.transform);
    }

    void BuildQuantumAcademy(Vector3 pos, string name, Transform parent)
    {
        var aObj = new GameObject(name);
        aObj.transform.position = pos;
        aObj.transform.SetParent(parent, true);

        var b = aObj.AddComponent<Building>();
        b.kind = Building.Kind.School;
        b.buildingName = name;
        b.baseUpgradeCost = 10000f;

        Cube("Base Plaza", pos + Vector3.up * 2.0f, new Vector3(18f, 4f, 18f), darkMat, aObj.transform);
        Cylinder("Rotunda Glass", pos + Vector3.up * 11f, new Vector3(14f, 14f, 14f), windowMat, aObj.transform);
        Sphere("Quantum Dome", pos + Vector3.up * 19.5f, new Vector3(14.5f, 8.0f, 14.5f), chromeMat, aObj.transform);
        Cylinder("Observatory Telescope", pos + Vector3.up * 24.0f, new Vector3(1.2f, 6.0f, 1.2f), metalMat, aObj.transform);
    }

    void BuildCyberPoliceHQ(Vector3 pos, string name, Transform parent)
    {
        var pObj = new GameObject(name);
        pObj.transform.position = pos;
        pObj.transform.SetParent(parent, true);

        var b = pObj.AddComponent<Building>();
        b.kind = Building.Kind.Police;
        b.buildingName = name;
        b.baseUpgradeCost = 11000f;

        Cube("HQ Podium", pos + Vector3.up * 4.0f, new Vector3(18f, 8f, 16f), darkMat, pObj.transform);
        Cube("Tower Core", pos + Vector3.up * 18.0f, new Vector3(14f, 20f, 12f), policeMat, pObj.transform);
        Cube("Sapphire Facade N", pos + Vector3.up * 18.0f + Vector3.forward * 6.1f, new Vector3(12f, 18f, 0.2f), windowMat, pObj.transform);
        Cube("Sapphire Facade S", pos + Vector3.up * 18.0f - Vector3.forward * 6.1f, new Vector3(12f, 18f, 0.2f), windowMat, pObj.transform);

        Cylinder("Radar Mast", pos + Vector3.up * 30.0f, new Vector3(0.6f, 4f, 0.6f), chromeMat, pObj.transform);
        Sphere("Radar Dome", pos + Vector3.up * 32.5f, new Vector3(3.2f, 3.2f, 3.2f), chromeMat, pObj.transform);
        Sphere("Police Siren Beacon", pos + Vector3.up * 35.0f, new Vector3(1.2f, 1.2f, 1.2f), sirenBlueMat, pObj.transform);
        Cube("Neon Cyan Ribbon", pos + Vector3.up * 18.0f + new Vector3(-7.1f, 0, 0), new Vector3(0.12f, 20f, 0.3f), neonCyanMat, pObj.transform);
    }

    void BuildEmergencyFireCommand(Vector3 pos, string name, Transform parent)
    {
        var fObj = new GameObject(name);
        fObj.transform.position = pos;
        fObj.transform.SetParent(parent, true);

        var b = fObj.AddComponent<Building>();
        b.kind = Building.Kind.Fire;
        b.buildingName = name;
        b.baseUpgradeCost = 9500f;

        Cube("Fire Command Base", pos + Vector3.up * 5.0f, new Vector3(18f, 10f, 16f), fireMat, fObj.transform);
        Cube("Bay Glass 1", pos + Vector3.up * 3.5f + new Vector3(-4.5f, 0, 8.1f), new Vector3(4.5f, 6.0f, 0.2f), windowMat, fObj.transform);
        Cube("Bay Glass 2", pos + Vector3.up * 3.5f + new Vector3( 4.5f, 0, 8.1f), new Vector3(4.5f, 6.0f, 0.2f), windowMat, fObj.transform);

        Cube("Dispatch Tower", pos + new Vector3(-5.0f, 15f, 0), new Vector3(6f, 12f, 6f), darkMat, fObj.transform);
        Cube("Dispatch Glass", pos + new Vector3(-5.0f, 17f, 3.1f), new Vector3(5f, 4f, 0.2f), windowMat, fObj.transform);
        Cylinder("Comms Mast", pos + new Vector3(-5.0f, 23f, 0), new Vector3(0.3f, 6f, 0.3f), chromeMat, fObj.transform);
    }

    // ── 5. Residential & Sports Districts ─────────────────────────────────────

    void BuildResidentialAndSportsDistricts()
    {
        // Block (75, 0, 20): Modern Esports & Athletic Arena Stadium
        Vector3 stPos = new Vector3(75f, 0.45f, 20f);
        var stPlaza = Cube("Stadium District Plaza", stPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), plazaMat, root);

        var arena = new GameObject("Neo Metropolis Stadium Arena");
        arena.transform.position = stPos;
        arena.transform.SetParent(stPlaza.transform, true);

        var b = arena.AddComponent<Building>();
        b.kind = Building.Kind.Commercial;
        b.buildingName = "Metropolis Sports Arena";
        b.baseUpgradeCost = 14000f;

        Cylinder("Arena Outer Ring", stPos + Vector3.up * 6.5f, new Vector3(34f, 13f, 26f), metalMat, arena.transform);
        Cylinder("Arena Inner Bowl", stPos + Vector3.up * 6.6f, new Vector3(28f, 13.2f, 20f), darkMat, arena.transform);
        Cube("Sports Turf", stPos + Vector3.up * 0.5f, new Vector3(24f, 0.2f, 16f), stadiumMat, arena.transform);
        Cube("Floodlight Tower NW", stPos + new Vector3(-16f, 9f, -12f), new Vector3(0.8f, 18f, 0.8f), chromeMat, arena.transform);
        Cube("Floodlight Tower NE", stPos + new Vector3( 16f, 9f, -12f), new Vector3(0.8f, 18f, 0.8f), chromeMat, arena.transform);
        Cube("Floodlight Emitter NW", stPos + new Vector3(-16f, 18.2f, -12f), new Vector3(2.5f, 1.2f, 1.2f), headLightMat, arena.transform);
        Cube("Floodlight Emitter NE", stPos + new Vector3( 16f, 18.2f, -12f), new Vector3(2.5f, 1.2f, 1.2f), headLightMat, arena.transform);

        // Block (75, 0, -20): Luxury Residential Towers & Sky Gardens
        Vector3 rPos = new Vector3(75f, 0.45f, -20f);
        var rPlaza = Cube("Residential Plaza", rPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), grassMat, root);

        BuildLuxuryCondo(rPos + new Vector3(-9f, 0, 0), 52f, "Marina Vista Towers", rPlaza.transform);
        BuildLuxuryCondo(rPos + new Vector3( 9f, 0, 0), 44f, "Sapphire Bay Residences", rPlaza.transform);

        // Block (75, 0, -60): Smart Automated Logistics Depot
        Vector3 logPos = new Vector3(75f, 0.45f, -60f);
        BuildCleanIndustrialDepot(logPos, "Smart Automated Logistics Depot", root);

        // Block (-25, 0, 60): High-Rise Waterfront Condominiums
        Vector3 nResPos = new Vector3(-25f, 0.45f, 60f);
        var nResPlaza = Cube("Waterfront HighRise Plaza", nResPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), plazaMat, root);
        BuildLuxuryCondo(nResPos + new Vector3(-9f, 0, 0), 48f, "Ocean Promenade Residences", nResPlaza.transform);
        BuildLuxuryCondo(nResPos + new Vector3( 9f, 0, 0), 40f, "Azure Harbor Suites", nResPlaza.transform);

        // Block (75, 0, 60): Oceanfront Resort & Spa
        Vector3 resPos = new Vector3(75f, 0.45f, 60f);
        var resPlaza = Cube("Oceanfront Resort Plaza", resPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), plazaMat, root);
        BuildModernOfficeBlock(resPos + new Vector3(-8f, 0, 0), 36f, "Grand Ocean Resort", resPlaza.transform);
        Cube("Resort Pool Deck", resPos + new Vector3(10f, 0.3f, 0), new Vector3(16f, 0.3f, 22f), plazaMat, resPlaza.transform);
        Cube("Resort Pool Water", resPos + new Vector3(10f, 0.4f, 0), new Vector3(12f, 0.2f, 16f), poolMat, resPlaza.transform);
    }

    void BuildLuxuryCondo(Vector3 pos, float height, string name, Transform parent)
    {
        var condo = new GameObject(name);
        condo.transform.position = pos;
        condo.transform.SetParent(parent, true);

        var b = condo.AddComponent<Building>();
        b.kind = Building.Kind.Residential;
        b.buildingName = name;
        b.baseUpgradeCost = 8500f;

        Cube("Main Body", pos + Vector3.up * (height * 0.5f), new Vector3(14.0f, height, 13.0f), residentialMat, condo.transform);

        for (float y = 8f; y < height - 4f; y += 7.0f)
        {
            Cube($"Balcony_{y}", pos + Vector3.up * y + Vector3.forward * 6.8f, new Vector3(14.0f, 0.25f, 1.4f), darkMat, condo.transform);
            Cube($"Glass_{y}",   pos + Vector3.up * (y + 0.5f) + Vector3.forward * 7.45f, new Vector3(13.8f, 0.90f, 0.08f), glassRailMat, condo.transform);
        }

        Vector3 poolPos = pos + Vector3.up * (height + 0.2f);
        Cube("Pool Deck", poolPos, new Vector3(12f, 0.4f, 11f), plazaMat, condo.transform);
        Cube("Pool Water", poolPos + Vector3.up * 0.1f, new Vector3(8f, 0.2f, 6f), poolMat, condo.transform);
    }

    void BuildCleanIndustrialDepot(Vector3 pos, string name, Transform parent)
    {
        var dep = new GameObject(name);
        dep.transform.position = pos;
        dep.transform.SetParent(parent, true);

        var b = dep.AddComponent<Building>();
        b.kind = Building.Kind.Industrial;
        b.buildingName = name;
        b.baseUpgradeCost = 8000f;

        Cube("Depot Base", pos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), roadMat, dep.transform);
        Cube("Depot Hangar 1", pos + new Vector3(-9f, 6.0f, 0), new Vector3(16f, 12f, 24f), industrialMat, dep.transform);
        Cube("Depot Hangar 2", pos + new Vector3( 9f, 6.0f, 0), new Vector3(16f, 12f, 24f), industrialMat, dep.transform);
        Cube("Solar Roof 1", pos + new Vector3(-9f, 12.2f, 0), new Vector3(15f, 0.2f, 22f), solarMat, dep.transform);
        Cube("Solar Roof 2", pos + new Vector3( 9f, 12.2f, 0), new Vector3(15f, 0.2f, 22f), solarMat, dep.transform);
        Cube("Neon Strip 1", pos + new Vector3(-9f, 6.0f, 12.1f), new Vector3(14f, 0.2f, 0.1f), neonCyanMat, dep.transform);
        Cube("Neon Strip 2", pos + new Vector3( 9f, 6.0f, 12.1f), new Vector3(14f, 0.2f, 0.1f), neonCyanMat, dep.transform);
    }

    // ── 6. Central Metropolitan Park & Plaza ──────────────────────────────────

    void BuildCentralParkAndPlaza()
    {
        Vector3 pos = new Vector3(-25f, 0.45f, 20f);
        var park = Cube("Central Park Island", pos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), parkMat, root);

        var b = park.AddComponent<Building>();
        b.kind = Building.Kind.Park;
        b.buildingName = "Central Metropolitan Park";
        b.baseUpgradeCost = 6000f;

        var lake = Cube("Park Lake", pos + new Vector3(0, 0.15f, 0), new Vector3(20f, 0.22f, 16f), waterMat, park.transform);
        lake.AddComponent<RiverWaterFlow>();

        Cube("Lake Bridge", pos + new Vector3(0, 0.35f, 0), new Vector3(3.5f, 0.3f, 18f), plazaMat, park.transform);
        Cube("Bridge Rail L", pos + new Vector3(-1.8f, 0.8f, 0), new Vector3(0.12f, 0.8f, 18f), glassRailMat, park.transform);
        Cube("Bridge Rail R", pos + new Vector3( 1.8f, 0.8f, 0), new Vector3(0.12f, 0.8f, 18f), glassRailMat, park.transform);

        Cylinder("Fountain Basin", pos + new Vector3(0, 0.4f, 0), new Vector3(5.5f, 0.6f, 5.5f), chromeMat, park.transform);
        Cylinder("Water Jet", pos + Vector3.up * 2.5f, new Vector3(0.8f, 4.5f, 0.8f), poolMat, park.transform);

        SpawnCherryBlossom(pos + new Vector3(-14f, 0, -10f), park.transform);
        SpawnCherryBlossom(pos + new Vector3(-14f, 0,  10f), park.transform);
        SpawnCherryBlossom(pos + new Vector3( 14f, 0, -10f), park.transform);
        SpawnCherryBlossom(pos + new Vector3( 14f, 0,  10f), park.transform);

        SpawnParkTree(pos + new Vector3(-7f, 0, -11f), park.transform);
        SpawnParkTree(pos + new Vector3( 7f, 0, -11f), park.transform);
        SpawnParkTree(pos + new Vector3(-7f, 0,  11f), park.transform);
        SpawnParkTree(pos + new Vector3( 7f, 0,  11f), park.transform);
    }

    void SpawnCherryBlossom(Vector3 pos, Transform parent)
    {
        var tree = new GameObject("Sakura Tree");
        tree.transform.position = pos;
        tree.transform.SetParent(parent, true);

        Cylinder("Trunk", pos + Vector3.up * 2.2f, new Vector3(0.4f, 4.4f, 0.4f), darkMat, tree.transform);
        Sphere("Blossoms", pos + Vector3.up * 5.0f, new Vector3(4.5f, 3.8f, 4.5f), cherryMat, tree.transform);
    }

    void SpawnParkTree(Vector3 pos, Transform parent)
    {
        var tree = new GameObject("Park Tree");
        tree.transform.position = pos;
        tree.transform.SetParent(parent, true);

        Cylinder("Trunk", pos + Vector3.up * 2.0f, new Vector3(0.35f, 4.0f, 0.35f), darkMat, tree.transform);
        Sphere("Canopy", pos + Vector3.up * 4.5f, new Vector3(4.0f, 4.2f, 4.0f), parkMat, tree.transform);
    }

    // ── 7. Waterfront Marina & Silicon Tech Park ──────────────────────────────

    void BuildWaterfrontMarinaAndTechPark()
    {
        // Block (-75, 0, -60): Silicon Tech Park
        Vector3 wPos = new Vector3(-75f, 0.45f, -60f);
        var wPlaza = Cube("Silicon Tech Park", wPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), plazaMat, root);

        var tech = new GameObject("Silicon Innovation Pavilion");
        tech.transform.position = wPos;
        tech.transform.SetParent(wPlaza.transform, true);

        var b = tech.AddComponent<Building>();
        b.kind = Building.Kind.Commercial;
        b.buildingName = "Silicon Innovation Pavilion";
        b.baseUpgradeCost = 9500f;

        Cylinder("Innovation Pavilion", wPos + new Vector3(-8f, 6.0f, 0), new Vector3(18f, 12f, 16f), windowMat, tech.transform);
        Sphere("Tech Dome", wPos + new Vector3(-8f, 12.0f, 0), new Vector3(18.2f, 5.0f, 16.2f), chromeMat, tech.transform);
        Cube("Solar Canopy", wPos + new Vector3(9f, 4.5f, 0), new Vector3(12f, 0.3f, 22f), solarMat, tech.transform);
        Cylinder("Lotus Pond", wPos + new Vector3(9f, 0.3f, 0), new Vector3(10f, 0.4f, 10f), waterMat, tech.transform);

        // Block (-75, 0, 60): Luxury Modern Seaside Villas
        Vector3 villaPos = new Vector3(-75f, 0.45f, 60f);
        var villaPlaza = Cube("Seaside Villa Estates", villaPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), grassMat, root);
        BuildModernVilla(villaPos + new Vector3(-9f, 0, 0), "Ocean Villa Alpha", villaPlaza.transform);
        BuildModernVilla(villaPos + new Vector3( 9f, 0, 0), "Ocean Villa Beta", villaPlaza.transform);

        // Block (25, 0, 60): Marina Commercial Promenade
        Vector3 mPos = new Vector3(25f, 0.45f, 60f);
        var mPlaza = Cube("Marina Promenade Plaza", mPos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), plazaMat, root);
        BuildModernOfficeBlock(mPos + new Vector3(-8f, 0, 0), 28f, "Harbor Point Retail", mPlaza.transform);
        BuildModernOfficeBlock(mPos + new Vector3( 8f, 0, 0), 24f, "Seaside Yacht Club", mPlaza.transform);

        // Marina Boardwalk & Yachts in River Water
        Vector3 marinaPos = new Vector3(25f, 0.45f, 115f);
        var marina = Cube("Yacht Marina Pier", marinaPos + Vector3.up * 0.1f, new Vector3(80f, 0.35f, 10f), pierMat, root);

        for (int i = -2; i <= 2; i++)
        {
            Vector3 yp = marinaPos + new Vector3(i * 15f, 0.2f, 10f);
            BuildYacht(yp, marina.transform);
        }
    }

    void BuildModernVilla(Vector3 pos, string name, Transform parent)
    {
        var vObj = new GameObject(name);
        vObj.transform.position = pos;
        vObj.transform.SetParent(parent, true);

        var b = vObj.AddComponent<Building>();
        b.kind = Building.Kind.Residential;
        b.buildingName = name;
        b.baseUpgradeCost = 7500f;

        Cube("Villa Floor 1", pos + Vector3.up * 2.5f, new Vector3(14f, 5f, 12f), residentialMat, vObj.transform);
        Cube("Villa Floor 2", pos + Vector3.up * 6.5f + Vector3.left * 2f, new Vector3(10f, 4f, 10f), darkMat, vObj.transform);
        Cube("Balcony Glass", pos + Vector3.up * 6.8f + Vector3.forward * 5.1f, new Vector3(9.5f, 0.9f, 0.1f), glassRailMat, vObj.transform);
        Cube("Villa Pool", pos + new Vector3(4f, 0.3f, -2f), new Vector3(5f, 0.25f, 6f), poolMat, vObj.transform);
    }

    void BuildYacht(Vector3 pos, Transform parent)
    {
        var yacht = new GameObject("Luxury Yacht");
        yacht.transform.position = pos;
        yacht.transform.SetParent(parent, true);

        Cube("Hull", pos + Vector3.up * 0.6f, new Vector3(3.8f, 1.2f, 11.0f), chromeMat, yacht.transform);
        Cube("Cabin Glass", pos + Vector3.up * 1.6f, new Vector3(2.8f, 1.1f, 6.0f), windowMat, yacht.transform);
        Cube("Radar Arch", pos + Vector3.up * 2.8f, new Vector3(2.5f, 1.2f, 0.3f), darkMat, yacht.transform);
    }

    // ── 8. Eco-Energy & Distant Turbines ──────────────────────────────────────

    void BuildEcoEnergySector()
    {
        Vector3 pos = new Vector3(-75f, 0.45f, -20f);
        BuildFusionReactor(pos, "Clean Fusion Power Facility", root);

        Vector3 turbineSeaA = new Vector3( 200f, 0f, 170f);
        Vector3 turbineSeaB = new Vector3( 240f, 0f, 200f);
        BuildSingleWindTurbine(turbineSeaA, root);
        BuildSingleWindTurbine(turbineSeaB, root);
    }

    void BuildFusionReactor(Vector3 pos, string name, Transform parent)
    {
        var fObj = new GameObject(name);
        fObj.transform.position = pos;
        fObj.transform.SetParent(parent, true);

        var b = fObj.AddComponent<Building>();
        b.kind = Building.Kind.Power;
        b.buildingName = name;
        b.baseUpgradeCost = 13000f;

        Cube("Eco Energy Base", pos + Vector3.up * 0.2f, new Vector3(40f, 0.4f, 32f), grassMat, fObj.transform);
        Cylinder("Reactor Core", pos + new Vector3(-8f, 7.5f, 0), new Vector3(14f, 15f, 14f), powerMat, fObj.transform);
        Cylinder("Plasma Core Ring", pos + new Vector3(-8f, 8.0f, 0), new Vector3(14.6f, 2.5f, 14.6f), neonCyanMat, fObj.transform);
        Sphere("Containment Dome", pos + new Vector3(-8f, 15.0f, 0), new Vector3(14.2f, 7.0f, 14.2f), chromeMat, fObj.transform);

        for (int row = -2; row <= 2; row++)
        {
            for (int col = 0; col <= 1; col++)
            {
                Vector3 sp = pos + new Vector3(6f + col * 6f, 1.2f, row * 5f);
                var panel = Cube($"Solar Panel {row}_{col}", sp, new Vector3(4.5f, 0.15f, 3.2f), solarMat, fObj.transform);
                panel.transform.rotation = Quaternion.Euler(25f, 40f, 0);
            }
        }
    }

    void BuildWaterFacility(Vector3 pos, string name, Transform parent)
    {
        var wObj = new GameObject(name);
        wObj.transform.position = pos;
        wObj.transform.SetParent(parent, true);

        var b = wObj.AddComponent<Building>();
        b.kind = Building.Kind.Water;
        b.buildingName = name;
        b.baseUpgradeCost = 8000f;

        Cylinder("Water Reservoir", pos + Vector3.up * 6f, new Vector3(14f, 12f, 14f), chromeMat, wObj.transform);
        Cube("Filtration Basin", pos + new Vector3(0, 0.2f, 0), new Vector3(18f, 0.3f, 18f), plazaMat, wObj.transform);
    }

    void BuildRecyclingCenter(Vector3 pos, string name, Transform parent)
    {
        var rObj = new GameObject(name);
        rObj.transform.position = pos;
        rObj.transform.SetParent(parent, true);

        var b = rObj.AddComponent<Building>();
        b.kind = Building.Kind.Recycling;
        b.buildingName = name;
        b.baseUpgradeCost = 7500f;

        Cube("Eco Recycling Facility", pos + Vector3.up * 6f, new Vector3(14f, 12f, 14f), industrialMat, rObj.transform);
        Cube("Green Neon", pos + Vector3.up * 12.1f, new Vector3(12f, 0.2f, 12f), neonGreenMat, rObj.transform);
    }

    void BuildSingleWindTurbine(Vector3 pos, Transform parent)
    {
        var turbine = new GameObject("Offshore Wind Turbine");
        turbine.transform.position = pos;
        turbine.transform.SetParent(parent, true);

        Cylinder("Mast", pos + Vector3.up * 20f, new Vector3(1.6f, 40f, 1.6f), turbineMat, turbine.transform);
        Cube("Nacelle", pos + Vector3.up * 40.2f, new Vector3(2.5f, 2.2f, 5.5f), turbineMat, turbine.transform);

        var rotorHub = new GameObject("Rotor Hub");
        rotorHub.transform.position = pos + Vector3.up * 40.2f + new Vector3(0, 0, 2.8f);
        rotorHub.transform.SetParent(turbine.transform, true);
        rotorHub.AddComponent<WindTurbineRotor>().spinSpeed = Random.Range(70f, 110f);

        Sphere("Nosecone", rotorHub.transform.position, new Vector3(1.6f, 1.6f, 1.6f), turbineMat, rotorHub.transform);
        for (int b = 0; b < 3; b++)
        {
            float angle = b * 120f;
            Vector3 dir = Quaternion.Euler(0, 0, angle) * Vector3.up;
            var blade = Cube($"Blade {b}", rotorHub.transform.position + dir * 9.5f, new Vector3(0.5f, 19f, 0.2f), turbineMat, rotorHub.transform);
            blade.transform.rotation = Quaternion.Euler(0, 0, angle);
        }
    }

    // ── 9. Active Urban Life & Cyber Vehicles ─────────────────────────────────

    void SpawnUrbanLife()
    {
        var group = new GameObject("Active Urban Vehicles & Drones").transform;
        group.SetParent(root, true);

        Color[] cyberColors = {
            new Color(0.05f, 0.85f, 1.0f),  // Cyber Cyan
            new Color(1.0f,  0.20f, 0.35f), // Crimson Neon
            new Color(1.0f,  0.80f, 0.10f), // Amber Gold
            new Color(0.95f, 0.95f, 0.95f), // Pearl White
            new Color(0.12f, 0.14f, 0.18f), // Midnight Obsidian
            new Color(0.15f, 0.95f, 0.40f)  // Emerald Green
        };

        // Autonomous Cyber Sedans along Avenue Boulevards
        int carIdx = 0;
        foreach (float x in MainBoulevardsX)
        {
            for (int lane = 0; lane < 4; lane++)
            {
                float z = -150f + lane * 75f;
                Color col = cyberColors[carIdx % cyberColors.Length];
                SpawnCyberSedan(new Vector3(x + 2.0f, 0.45f, z), Vector3.forward, col, group);
                SpawnCyberSedan(new Vector3(x - 2.0f, 0.45f, z + 35f), Vector3.back, cyberColors[(carIdx + 1) % cyberColors.Length], group);
                carIdx++;
            }
        }

        // Transit Cyber-Buses along Main Cross-Boulevards
        foreach (float z in MainBoulevardsZ)
        {
            SpawnCyberBus(new Vector3(-120f, 0.45f, z + 2.0f), Vector3.right, group);
            SpawnCyberBus(new Vector3( 120f, 0.45f, z - 2.0f), Vector3.left, group);
        }

        // Flying VTOL Sky-Drones (with continuous active flight)
        Vector3[] dronePaths = {
            new Vector3(-60f, 32f, -120f),
            new Vector3( 40f, 36f,  120f),
            new Vector3(-20f, 42f, -160f),
            new Vector3( 80f, 34f,  160f)
        };

        for (int i = 0; i < dronePaths.Length; i++)
        {
            var dObj = new GameObject($"VTOL Sky Drone {i}");
            dObj.transform.position = dronePaths[i];
            dObj.transform.SetParent(group, true);

            var flight = dObj.AddComponent<SkyDroneFlight>();
            flight.direction = (i % 2 == 0) ? Vector3.forward : Vector3.back;
            flight.speed = Random.Range(18f, 26f);

            var body = Cube("Drone Fuselage", dObj.transform.position, new Vector3(2.4f, 0.7f, 3.2f), chromeMat, dObj.transform);
            Cube("Canopy Glass", dObj.transform.position + Vector3.up * 0.35f, new Vector3(1.8f, 0.6f, 2.2f), windowMat, body.transform);
            Cube("Left Wing", dObj.transform.position + Vector3.left * 2.2f, new Vector3(2.4f, 0.12f, 0.8f), darkMat, body.transform);
            Cube("Right Wing", dObj.transform.position + Vector3.right * 2.2f, new Vector3(2.4f, 0.12f, 0.8f), darkMat, body.transform);
            Sphere("Nav Light L", dObj.transform.position + Vector3.left * 3.3f, new Vector3(0.3f, 0.3f, 0.3f), neonCyanMat, body.transform);
            Sphere("Nav Light R", dObj.transform.position + Vector3.right * 3.3f, new Vector3(0.3f, 0.3f, 0.3f), neonMagentaMat, body.transform);
        }
    }

    void SpawnCyberSedan(Vector3 pos, Vector3 dir, Color bodyCol, Transform parent)
    {
        var car = new GameObject("Cyber Sedan");
        car.transform.position = pos;
        car.transform.rotation = Quaternion.LookRotation(dir);
        car.transform.SetParent(parent, true);

        var tv = car.AddComponent<TrafficVehicle>();
        tv.direction = dir;
        tv.speed = Random.Range(16f, 25f);

        var cMat = Mat(bodyCol, 0.75f, 0.65f);

        LocalCube("Chassis", new Vector3(0, 0.35f, 0), new Vector3(1.85f, 0.45f, 4.2f), cMat, car.transform);
        LocalCube("Cabin Glass", new Vector3(0, 0.78f, -0.2f), new Vector3(1.55f, 0.55f, 2.2f), windowMat, car.transform);

        LocalCube("Headlights", new Vector3(0, 0.40f, 2.12f), new Vector3(1.65f, 0.12f, 0.08f), headLightMat, car.transform);
        LocalCube("Taillights", new Vector3(0, 0.45f, -2.12f), new Vector3(1.65f, 0.12f, 0.08f), tailLightMat, car.transform);
        LocalCube("Underglow", new Vector3(0, 0.10f, 0), new Vector3(1.5f, 0.04f, 3.6f), neonCyanMat, car.transform);

        Vector3[] wheelOffsets = {
            new Vector3(-0.95f, 0.28f,  1.2f),
            new Vector3( 0.95f, 0.28f,  1.2f),
            new Vector3(-0.95f, 0.28f, -1.2f),
            new Vector3( 0.95f, 0.28f, -1.2f)
        };
        foreach (var wo in wheelOffsets)
        {
            var w = LocalCylinder("Wheel", wo, new Vector3(0.28f, 0.56f, 0.56f), tireMat, car.transform);
            w.transform.localRotation = Quaternion.Euler(0, 0, 90f);
        }
    }

    void SpawnCyberBus(Vector3 pos, Vector3 dir, Transform parent)
    {
        var bus = new GameObject("Autonomous Transit CyberBus");
        bus.transform.position = pos;
        bus.transform.rotation = Quaternion.LookRotation(dir);
        bus.transform.SetParent(parent, true);

        var tv = bus.AddComponent<TrafficVehicle>();
        tv.direction = dir;
        tv.speed = 13f;

        float len = 9.2f;
        LocalCube("Bus Chassis", new Vector3(0, 1.35f, 0), new Vector3(2.5f, 2.2f, len), darkMat, bus.transform);
        LocalCube("Transit Glass", new Vector3(0, 1.45f, 0), new Vector3(2.55f, 1.1f, len * 0.88f), windowMat, bus.transform);
        LocalCube("LED Route Sign", new Vector3(0, 2.3f, len * 0.51f), new Vector3(1.8f, 0.35f, 0.08f), neonAmberMat, bus.transform);
        LocalCube("Amber Underglow", new Vector3(0, 0.15f, 0), new Vector3(2.2f, 0.04f, len * 0.85f), neonAmberMat, bus.transform);

        Vector3[] busWheels = {
            new Vector3(-1.3f, 0.45f,  2.8f),
            new Vector3( 1.3f, 0.45f,  2.8f),
            new Vector3(-1.3f, 0.45f, -2.8f),
            new Vector3( 1.3f, 0.45f, -2.8f)
        };
        foreach (var bwo in busWheels)
        {
            var w = LocalCylinder("Wheel", bwo, new Vector3(0.35f, 0.85f, 0.85f), tireMat, bus.transform);
            w.transform.localRotation = Quaternion.Euler(0, 0, 90f);
        }
    }

    // ── Helper Geometric Primitives ───────────────────────────────────────────

    GameObject LocalCube(string name, Vector3 localPos, Vector3 size, Material mat, Transform parent)
    {
        var go = GameObject.CreatePrimitive(PrimitiveType.Cube);
        go.name = name;
        go.transform.SetParent(parent, false);
        go.transform.localPosition = localPos;
        go.transform.localRotation = Quaternion.identity;
        go.transform.localScale = size;
        if (mat != null) go.GetComponent<Renderer>().material = mat;
        return go;
    }

    GameObject LocalCylinder(string name, Vector3 localPos, Vector3 size, Material mat, Transform parent)
    {
        var go = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
        go.name = name;
        go.transform.SetParent(parent, false);
        go.transform.localPosition = localPos;
        go.transform.localRotation = Quaternion.identity;
        go.transform.localScale = new Vector3(size.x, size.y * 0.5f, size.z);
        if (mat != null) go.GetComponent<Renderer>().material = mat;
        return go;
    }

    GameObject Cube(string name, Vector3 pos, Vector3 size, Material mat, Transform parent)
    {
        var go = GameObject.CreatePrimitive(PrimitiveType.Cube);
        go.name = name;
        go.transform.position = pos;
        go.transform.localScale = size;
        if (mat != null) go.GetComponent<Renderer>().material = mat;
        if (parent != null) go.transform.SetParent(parent, true);
        return go;
    }

    GameObject Cylinder(string name, Vector3 pos, Vector3 size, Material mat, Transform parent)
    {
        var go = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
        go.name = name;
        go.transform.position = pos;
        go.transform.localScale = new Vector3(size.x, size.y * 0.5f, size.z);
        if (mat != null) go.GetComponent<Renderer>().material = mat;
        if (parent != null) go.transform.SetParent(parent, true);
        return go;
    }

    GameObject Sphere(string name, Vector3 pos, Vector3 size, Material mat, Transform parent)
    {
        var go = GameObject.CreatePrimitive(PrimitiveType.Sphere);
        go.name = name;
        go.transform.position = pos;
        go.transform.localScale = size;
        if (mat != null) go.GetComponent<Renderer>().material = mat;
        if (parent != null) go.transform.SetParent(parent, true);
        return go;
    }
}

/// <summary>Rotates wind turbine blades continuously.</summary>
public class WindTurbineRotor : MonoBehaviour
{
    public float spinSpeed = 90f;
    void Update()
    {
        transform.Rotate(0, 0, spinSpeed * Time.deltaTime, Space.Self);
    }
}
