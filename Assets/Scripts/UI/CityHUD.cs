using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class CityHUD : MonoBehaviour
{
    string page = "3D City View";
    Vector2 scrollNav;
    List<string> alerts = new();
    bool hideSidebar = false;

    // Camera controller reference (found on Start)
    CityCameraController camCtrl;

    string[] nav = {
        "3D City View",
        "Dashboard",
        "Build & Infrastructure",
        "City Decorations",
        "Map Overlays",
        "Taxes & Economy",
        "Traffic Management",
        "Public Transport",
        "Electricity",
        "Water",
        "Waste & Recycling",
        "Healthcare",
        "Education",
        "Safety & Security",
        "Environment",
        "Citizen Requests",
        "Analytics",
        "Technology",
        "Settings"
    };

    void Start()
    {
        if (CityManager.Instance) CityManager.Instance.AlertRaised += OnAlert;
        camCtrl = FindFirstObjectByType<CityCameraController>();
        MusicManager.Play(); // ensure music continues into game scene
    }

    void OnDestroy()
    {
        if (CityManager.Instance) CityManager.Instance.AlertRaised -= OnAlert;
    }

    void OnAlert(string m, CityManager.AlertLevel l)
    {
        alerts.Insert(0, "[" + l + "] " + m);
        if (alerts.Count > 10) alerts.RemoveAt(alerts.Count - 1);
    }

    void OnGUI()
    {
        if (!CityManager.Instance) return;
        SmartCityGUI.Ensure();
        var s = CityManager.Instance.State;

        float topH  = 68;
        float sideW = hideSidebar ? 50 : 220;

        // ── Top Navigation Header Bar ─────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 0, Screen.width, topH), SmartCityGUI.Navy);

        GUI.Label(new Rect(14, 14, 160, 40), "SMART CITY",
            new GUIStyle(SmartCityGUI.Title) { fontSize = 22, alignment = TextAnchor.MiddleLeft });

        float statsLeft  = 180;
        float statsRight = Screen.width - 300;
        float availableW = Mathf.Max(360, statsRight - statsLeft);
        float colW       = availableW / 6f;

        StatItem("CITY",       s.cityName,                              statsLeft,            10, colW);
        StatItem("BUDGET",     "Rs. " + s.budget.ToString("N0"),        statsLeft + colW,     10, colW);
        StatItem("POPULATION", s.population.ToString("N0"),             statsLeft + colW * 2, 10, colW);
        StatItem("HAPPINESS",  s.happiness.ToString("0") + "%",         statsLeft + colW * 3, 10, colW);
        StatItem("SCORE",      s.smartCityScore.ToString("0") + "/100", statsLeft + colW * 4, 10, colW);
        StatItem("TIME",       "Day " + s.day + " Yr " + s.year,       statsLeft + colW * 5, 10, colW);

        // Time controls
        float ctrlX = Screen.width - 338;
        if (GUI.Button(new Rect(ctrlX,       15, 44, 38), CityManager.Instance.paused ? "▶" : "❚❚", SmartCityGUI.Button)) CityManager.Instance.TogglePause();
        if (GUI.Button(new Rect(ctrlX +  50, 15, 42, 38), "1x", SmartCityGUI.SmallButton)) CityManager.Instance.SetSpeed(1);
        if (GUI.Button(new Rect(ctrlX +  96, 15, 42, 38), "2x", SmartCityGUI.SmallButton)) CityManager.Instance.SetSpeed(2);
        if (GUI.Button(new Rect(ctrlX + 142, 15, 42, 38), "4x", SmartCityGUI.SmallButton)) CityManager.Instance.SetSpeed(4);
        if (GUI.Button(new Rect(ctrlX + 190, 15, 42, 38),
                MusicManager.IsPlaying ? "🔊" : "🔇", SmartCityGUI.SmallButton))
            MusicManager.Toggle();
        if (GUI.Button(new Rect(ctrlX + 238, 15, 92, 38), hideSidebar ? "SHOW ☰" : "HIDE 👁", SmartCityGUI.SmallButton))
            hideSidebar = !hideSidebar;

        // ── Left Navigation Sidebar ───────────────────────────────────────────
        if (!hideSidebar)
        {
            GUI.DrawTexture(new Rect(0, topH, sideW, Screen.height - topH), SmartCityGUI.GlassDark);
            scrollNav = GUI.BeginScrollView(
                new Rect(0, topH, sideW, Screen.height - topH),
                scrollNav,
                new Rect(0, 0, sideW - 18, nav.Length * 44 + 130));

            for (int i = 0; i < nav.Length; i++)
            {
                bool active = page == nav[i];
                if (GUI.Button(new Rect(6, 6 + i * 44, sideW - 28, 38), nav[i],
                        active ? SmartCityGUI.NavActive : SmartCityGUI.Nav))
                    page = nav[i];
            }

            if (GUI.Button(new Rect(6, 14 + nav.Length * 44, sideW - 28, 38), "💾 SAVE CITY", SmartCityGUI.Nav))
            {
                int slot = PlayerPrefs.GetInt("ActiveSlot", 0);
                SaveSystem.Save(slot);
                OnAlert("City saved to slot " + (slot + 1) + ".", CityManager.AlertLevel.Success);
            }
            if (GUI.Button(new Rect(6, 58 + nav.Length * 44, sideW - 28, 38), "🏠 MAIN MENU", SmartCityGUI.Nav))
                SceneManager.LoadScene("MainMenu");

            GUI.EndScrollView();
        }

        // ── Placement mode banner ─────────────────────────────────────────────
        bool placing = BuildPlacementController.Instance != null && BuildPlacementController.Instance.IsPlacing;
        if (placing)
        {
            float bh = 52;
            GUI.DrawTexture(new Rect(0, Screen.height - bh, Screen.width, bh), SmartCityGUI.Navy);
            var bannerStyle = new GUIStyle(SmartCityGUI.Body)
            {
                alignment = TextAnchor.MiddleCenter,
                fontSize  = 17,
                fontStyle = FontStyle.Bold,
                normal    = { textColor = new Color(0.25f, 1.0f, 0.40f) },
                hover     = { textColor = new Color(0.25f, 1.0f, 0.40f) }
            };
            GUI.Label(new Rect(0, Screen.height - bh, Screen.width, bh),
                "🏗️  Click on the city to place your building  |  ESC or Right-Click to cancel",
                bannerStyle);
        }

        // ── 3D City View — Camera Controls HUD overlay ────────────────────────
        if (page == "3D City View" && !placing)
        {
            DrawCameraControlsHUD();
        }

        // ── Floating Management Content Window ────────────────────────────────
        if (page != "3D City View" && !placing)
        {
            float contentW = Mathf.Clamp(Screen.width  - sideW - 50,  550, 960);
            float contentH = Mathf.Clamp(Screen.height - topH  - 40,  420, 780);
            float contentX = sideW + 25;
            float contentY = topH  + 20;

            GUI.DrawTexture(new Rect(contentX, contentY, contentW, contentH), SmartCityGUI.GlassPanel);
            GUI.DrawTexture(new Rect(contentX, contentY, contentW, 3f), SmartCityGUI.Border);

            GUI.Label(new Rect(contentX + 22, contentY + 16, contentW - 180, 36), page, SmartCityGUI.H1);
            if (GUI.Button(new Rect(contentX + contentW - 150, contentY + 14, 130, 38), "✕ 3D VIEW", SmartCityGUI.SmallButton))
                page = "3D City View";

            GUI.BeginGroup(new Rect(contentX + 18, contentY + 60, contentW - 36, contentH - 74));
            DrawPageContent(page, s, contentW - 36, contentH - 74);
            GUI.EndGroup();
        }

        // ── Decision Event Modal ───────────────────────────────────────────────
        DrawDecisionEventModal(s);

        // ── Building Inspector ────────────────────────────────────────────────
        DrawBuildingInspector();
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Camera Controls HUD (3D City View overlay — bottom-right)
    // ─────────────────────────────────────────────────────────────────────────

    void DrawCameraControlsHUD()
    {
        float panelW = 320;
        float panelH = 162;
        float panelX = Screen.width  - panelW - 18;
        float panelY = Screen.height - panelH - 18;

        // Background card
        GUI.DrawTexture(new Rect(panelX, panelY, panelW, panelH), SmartCityGUI.GlassDark);

        // Title row
        var whiteSmall = new GUIStyle(SmartCityGUI.IconLabel) { fontSize = 14, alignment = TextAnchor.MiddleLeft };
        GUI.Label(new Rect(panelX + 14, panelY + 10, panelW - 28, 22),
            "📷  CAMERA & VIEW CONTROLS", whiteSmall);

        // Accent underline
        GUI.DrawTexture(new Rect(panelX + 14, panelY + 32, panelW - 28, 2), SmartCityGUI.Blue);

        // Current preset indicator
        string presetName = camCtrl == null ? "–" : camCtrl.ActivePreset switch
        {
            CityCameraController.CameraPreset.High   => "HIGH",
            CityCameraController.CameraPreset.Medium => "MEDIUM",
            CityCameraController.CameraPreset.Low    => "LOW",
            _                                        => "CUSTOM"
        };
        var mutedWhite = new GUIStyle(SmartCityGUI.Muted) { fontSize = 12,
            normal = { textColor = new Color(0.65f, 0.72f, 0.82f) },
            hover  = { textColor = new Color(0.65f, 0.72f, 0.82f) } };
        GUI.Label(new Rect(panelX + 14, panelY + 36, panelW - 28, 18),
            "Height: " + presetName + (camCtrl != null && camCtrl.IsAutoRotating ? "  |  [ORBITING]" : ""), mutedWhite);

        // Row 1: Height preset buttons
        float btnW = (panelW - 28 - 16) / 3f;
        float btnY1 = panelY + 58;
        float btnX = panelX + 14;

        bool isHigh = camCtrl != null && camCtrl.ActivePreset == CityCameraController.CameraPreset.High;
        bool isMed  = camCtrl != null && camCtrl.ActivePreset == CityCameraController.CameraPreset.Medium;
        bool isLow  = camCtrl != null && camCtrl.ActivePreset == CityCameraController.CameraPreset.Low;

        var activeStyle = new GUIStyle(SmartCityGUI.SmallButton)
        {
            normal  = { background = SmartCityGUI.Blue,  textColor = Color.white },
            hover   = { background = SmartCityGUI.Cyan,  textColor = Color.black },
            active  = { background = SmartCityGUI.Dark,  textColor = Color.white },
            focused = { background = SmartCityGUI.Blue,  textColor = Color.white }
        };
        var inactiveStyle = new GUIStyle(SmartCityGUI.SmallButton)
        {
            normal  = { background = SmartCityGUI.Dark,  textColor = new Color(0.75f, 0.82f, 0.92f) },
            hover   = { background = SmartCityGUI.Blue,  textColor = Color.white },
            active  = { background = SmartCityGUI.Dark,  textColor = Color.white },
            focused = { background = SmartCityGUI.Dark,  textColor = Color.white }
        };

        if (GUI.Button(new Rect(btnX,             btnY1, btnW, 30), "⬆ HIGH",   isHigh ? activeStyle : inactiveStyle))
            camCtrl?.SetPreset(CityCameraController.CameraPreset.High);
        if (GUI.Button(new Rect(btnX + btnW + 8,  btnY1, btnW, 30), "◼ MED",    isMed  ? activeStyle : inactiveStyle))
            camCtrl?.SetPreset(CityCameraController.CameraPreset.Medium);
        if (GUI.Button(new Rect(btnX + (btnW + 8)*2, btnY1, btnW, 30), "⬇ LOW", isLow  ? activeStyle : inactiveStyle))
            camCtrl?.SetPreset(CityCameraController.CameraPreset.Low);

        // Row 2: Rotation & View buttons
        float btnY2 = panelY + 96;
        float rotBtnW = (panelW - 28 - 18) / 4f;

        if (GUI.Button(new Rect(btnX, btnY2, rotBtnW, 32), "⟲ 45°", inactiveStyle))
            camCtrl?.RotateLeft(45f);

        if (GUI.Button(new Rect(btnX + rotBtnW + 6, btnY2, rotBtnW, 32), "⟳ 45°", inactiveStyle))
            camCtrl?.RotateRight(45f);

        bool isOrbit = camCtrl != null && camCtrl.IsAutoRotating;
        if (GUI.Button(new Rect(btnX + (rotBtnW + 6)*2, btnY2, rotBtnW, 32), "🔄 ORBIT", isOrbit ? activeStyle : inactiveStyle))
            camCtrl?.ToggleAutoRotate();

        if (GUI.Button(new Rect(btnX + (rotBtnW + 6)*3, btnY2, rotBtnW, 32), "⟰ RESET", inactiveStyle))
            camCtrl?.ResetView();

        // Extra subtext hint inside card
        var tinyHint = new GUIStyle(SmartCityGUI.Muted) { fontSize = 11, alignment = TextAnchor.MiddleCenter,
            normal = { textColor = new Color(0.55f, 0.65f, 0.75f) } };
        GUI.Label(new Rect(panelX + 14, panelY + 134, panelW - 28, 20),
            "Keys: Q / E rotate  |  RMB drag to look", tinyHint);

        // WASD hint — bottom-left corner
        float hintX = (hideSidebar ? 60 : 230) + 10;
        float hintY = Screen.height - 40;
        var hintStyle = new GUIStyle(SmartCityGUI.Muted)
        {
            fontSize = 13,
            normal  = { textColor = new Color(0.75f, 0.82f, 0.92f, 0.85f) },
            hover   = { textColor = new Color(0.75f, 0.82f, 0.92f, 0.85f) }
        };
        GUI.DrawTexture(new Rect(hintX - 10, hintY - 6, 520, 34), SmartCityGUI.GlassDark);
        GUI.Label(new Rect(hintX, hintY, 510, 28),
            "WASD/Arrows — Pan  |  Q/E or RMB Drag — Rotate  |  Scroll — Zoom  |  Shift — Fast",
            hintStyle);
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Shared helpers
    // ─────────────────────────────────────────────────────────────────────────

    void StatItem(string label, string val, float x, float y, float w)
    {
        GUI.Label(new Rect(x + 4, y + 4,  w - 8, 16), label, SmartCityGUI.CardTitle);
        GUI.Label(new Rect(x + 4, y + 20, w - 8, 36), val,
            new GUIStyle(SmartCityGUI.Title) { fontSize = 17, alignment = TextAnchor.MiddleLeft });
    }

    void DrawDecisionEventModal(CityState s)
    {
        if (s.currentEvent == null) return;
        var ev = s.currentEvent;

        float w = 520, h = 340;
        float x = (Screen.width  - w) / 2f;
        float y = (Screen.height - h) / 2f;

        GUI.DrawTexture(new Rect(0, 0, Screen.width, Screen.height), SmartCityGUI.GlassDark);
        GUI.DrawTexture(new Rect(x, y, w, h), SmartCityGUI.White);

        GUI.Label(new Rect(x + 24, y + 20, w - 48, 34), ev.title,       SmartCityGUI.H1);
        GUI.Label(new Rect(x + 24, y + 60, w - 48, 80), ev.description, SmartCityGUI.Body);

        if (GUI.Button(new Rect(x + 24, y + 150, w - 48, 44), ev.optionA, SmartCityGUI.Button))
            CityRandomEventSystem.ResolveEvent(s, 1);
        if (GUI.Button(new Rect(x + 24, y + 204, w - 48, 44), ev.optionB, SmartCityGUI.Button))
            CityRandomEventSystem.ResolveEvent(s, 2);
        if (GUI.Button(new Rect(x + 24, y + 258, w - 48, 44), ev.optionC, SmartCityGUI.SmallButton))
            CityRandomEventSystem.ResolveEvent(s, 3);
    }

    void DrawBuildingInspector()
    {
        var b = CityCameraController.SelectedBuilding;
        if (b == null) return;

        float w = 340, h = 250, x = Screen.width - w - 24, y = 85;
        
        // Dark translucent glass card
        GUI.DrawTexture(new Rect(x, y, w, h), SmartCityGUI.GlassPanel);
        GUI.DrawTexture(new Rect(x, y, w, 4), SmartCityGUI.Cyan);

        string bName = !string.IsNullOrEmpty(b.buildingName) ? b.buildingName : (b.kind + " Facility");
        GUI.Label(new Rect(x + 18, y + 14, w - 36, 26), bName, SmartCityGUI.H2);
        GUI.Label(new Rect(x + 18, y + 42, w - 36, 20), $"District: {b.kind}  |  Level {b.level} / {Building.MaxLevel}", SmartCityGUI.Body);

        GUI.Label(new Rect(x + 18, y + 68, w - 36, 20), $"⭐ Happiness Bonus: +{b.GetHappinessBonus():0.0}%", SmartCityGUI.Body);
        GUI.Label(new Rect(x + 18, y + 90, w - 36, 20), $"💰 Daily Revenue: +Rs. {b.GetRevenueBonus():N0}/day", SmartCityGUI.Body);

        float upgradeCost = b.GetUpgradeCost();

        if (b.level < Building.MaxLevel)
        {
            if (GUI.Button(new Rect(x + 18, y + 122, w - 36, 46), $"⬆ UPGRADE LEVEL {b.level + 1}\n(Rs. {upgradeCost:N0})", SmartCityGUI.Button))
            {
                b.Upgrade();
            }
        }
        else
        {
            GUI.Label(new Rect(x + 18, y + 130, w - 36, 30), "👑 Maximum Level 5 Reached (MAX TIER)", SmartCityGUI.H2);
        }

        if (GUI.Button(new Rect(x + 18, y + 185, w - 36, 38), "✕ Close Inspector", SmartCityGUI.SmallButton))
        {
            CityCameraController.ClearSelection();
        }
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Page routing
    // ─────────────────────────────────────────────────────────────────────────

    void DrawPageContent(string p, CityState s, float w, float h)
    {
        if      (p == "Dashboard")          Dashboard(s, w, h);
        else if (p == "Build & Infrastructure") Infrastructure(s, w);
        else if (p == "City Decorations")   Decorations(s, w);
        else if (p == "Map Overlays")       MapOverlays(s, w);
        else if (p == "Taxes & Economy")    TaxesAndEconomy(s, w);
        else if (p == "Traffic Management") Traffic(s, w);
        else if (p == "Public Transport")   Transport(s, w);
        else if (p == "Citizen Requests")   Requests(w, h);
        else if (p == "Analytics")          Analytics(s, w, h);
        else if (p == "Technology")         Technology(s, w);
        // ── Richly designed pages ──
        else if (p == "Water")              WaterPage(s, w, h);
        else if (p == "Waste & Recycling")  WastePage(s, w, h);
        else if (p == "Education")          EducationPage(s, w, h);
        else if (p == "Safety & Security")  SafetyPage(s, w, h);
        else if (p == "Electricity")        ElectricityPage(s, w, h);
        else if (p == "Environment")        EnvironmentPage(s, w, h);
        else if (p == "Healthcare")         HealthcarePage(s, w, h);
        else                                GenericPage(p, s, w, h);
    }

    // ─────────────────────────────────────────────────────────────────────────
    // ── WATER PAGE ────────────────────────────────────────────────────────────
    // ─────────────────────────────────────────────────────────────────────────

    void WaterPage(CityState s, float w, float h)
    {
        float cardW = (w - 36) / 3f;

        // ── Stat cards row ────────────────────────────────────────────────────
        SmartCityGUI.ColorCard(0,            8, cardW, 90, SmartCityGUI.Blue,
            "💧", "WATER SUPPLY",   s.waterSupply.ToString("N0") + " KL");
        SmartCityGUI.ColorCard(cardW + 18,   8, cardW, 90, SmartCityGUI.Teal,
            "🔄", "CONSUMPTION",    s.waterConsumption.ToString("N0") + " KL");
        SmartCityGUI.ColorCard((cardW + 18)*2, 8, cardW, 90, SmartCityGUI.Indigo,
            "🏭", "TREATMENT PLANTS", s.waterFacilities.ToString());

        // ── Reservoir gauge ───────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 112, w, 105), SmartCityGUI.White);
        GUI.Label(new Rect(16, 124, w - 32, 26), "Reservoir Level", SmartCityGUI.H2);

        float resLevel = Mathf.Clamp01(s.reservoirLevel / 100f);
        Color barCol = resLevel > 0.6f ? new Color(0.08f, 0.5f, 0.85f) :
                       resLevel > 0.3f ? new Color(0.92f, 0.60f, 0.08f) :
                                         new Color(0.85f, 0.20f, 0.20f);
        Texture2D barTex = resLevel > 0.6f ? SmartCityGUI.Blue :
                           resLevel > 0.3f ? SmartCityGUI.Amber : SmartCityGUI.Red;

        GUI.DrawTexture(new Rect(16, 158, w - 32, 18), SmartCityGUI.Soft);
        if (resLevel > 0f) GUI.DrawTexture(new Rect(16, 158, (w - 32) * resLevel, 18), barTex);
        GUI.Label(new Rect(16, 182, w - 32, 22),
            s.reservoirLevel.ToString("0.0") + "% — " +
            (resLevel > 0.6f ? "Optimal supply" : resLevel > 0.3f ? "Moderate — consider expanding" : "⚠ Critical low!"),
            new GUIStyle(SmartCityGUI.Muted) { normal = { textColor = barCol },
                                               hover  = { textColor = barCol } });

        // ── Supply vs Consumption breakdown ───────────────────────────────────
        GUI.DrawTexture(new Rect(0, 230, w * 0.55f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(16, 242, w * 0.52f, 26), "Supply vs Demand", SmartCityGUI.H2);
        SmartCityGUI.ProgressBar(16, 276, w * 0.52f - 32, "Supply",      Mathf.Clamp01(s.waterSupply / 5000f),       SmartCityGUI.Blue);
        SmartCityGUI.ProgressBar(16, 308, w * 0.52f - 32, "Consumption", Mathf.Clamp01(s.waterConsumption / 5000f), SmartCityGUI.Amber);

        // ── Actions ───────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(w * 0.58f, 230, w * 0.42f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(w * 0.58f + 16, 242, w * 0.40f, 26), "Management Actions", SmartCityGUI.H2);

        if (GUI.Button(new Rect(w * 0.58f + 16, 276, w * 0.40f - 32, 36),
                "🏗 Build Water Facility  Rs. 40,000", SmartCityGUI.ActionBtn))
        {
            ConstructionSystem.Instance?.BuildWaterFacility();
            page = "3D City View";
        }

        if (GUI.Button(new Rect(w * 0.58f + 16, 318, w * 0.40f - 32, 36),
                "🔧 Repair Infrastructure  Rs. 12,000", SmartCityGUI.SmallButton))
            ConstructionSystem.Instance?.RepairRoads();

        // ── Info footer ───────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 374, w, 54), SmartCityGUI.Soft);
        GUI.Label(new Rect(16, 382, w - 32, 38),
            "💡  Each Water Facility adds 1,200 KL/day supply. Population over 5,000 requires at least 3 treatment plants.",
            new GUIStyle(SmartCityGUI.Muted) { fontSize = 14, wordWrap = true });
    }

    // ─────────────────────────────────────────────────────────────────────────
    // ── WASTE & RECYCLING PAGE ────────────────────────────────────────────────
    // ─────────────────────────────────────────────────────────────────────────

    void WastePage(CityState s, float w, float h)
    {
        float cardW = (w - 36) / 3f;

        // ── Stat cards ────────────────────────────────────────────────────────
        SmartCityGUI.ColorCard(0,             8, cardW, 90, SmartCityGUI.Orange,
            "🗑", "DAILY WASTE",     s.wasteGenerated.ToString("0.0") + " T/day");
        SmartCityGUI.ColorCard(cardW + 18,    8, cardW, 90, SmartCityGUI.Green,
            "♻", "RECYCLING RATE",  s.recyclingRate.ToString("0") + "%");
        SmartCityGUI.ColorCard((cardW + 18)*2, 8, cardW, 90, SmartCityGUI.Teal,
            "🏭", "RECYCLING CENTERS", s.recyclingCenters.ToString());

        // ── Recycling performance bar ─────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 112, w, 105), SmartCityGUI.White);
        GUI.Label(new Rect(16, 124, w - 32, 26), "Recycling Performance", SmartCityGUI.H2);

        float recPct  = Mathf.Clamp01(s.recyclingRate / 100f);
        Texture2D recBar = recPct > 0.65f ? SmartCityGUI.Green :
                           recPct > 0.35f ? SmartCityGUI.Amber : SmartCityGUI.Red;

        GUI.DrawTexture(new Rect(16, 158, w - 32, 18), SmartCityGUI.Soft);
        if (recPct > 0f) GUI.DrawTexture(new Rect(16, 158, (w - 32) * recPct, 18), recBar);

        string recStatus = recPct > 0.65f ? "🌟 Excellent — leading sustainable city" :
                           recPct > 0.35f ? "⚠ Moderate — add more centres" :
                                            "🔴 Poor — high landfill impact on happiness";
        Color recCol = recPct > 0.65f ? new Color(0.06f, 0.55f, 0.30f) :
                       recPct > 0.35f ? new Color(0.80f, 0.50f, 0.05f) :
                                        new Color(0.80f, 0.15f, 0.15f);
        GUI.Label(new Rect(16, 182, w - 32, 22), recStatus,
            new GUIStyle(SmartCityGUI.Muted) { normal = { textColor = recCol },
                                               hover  = { textColor = recCol } });

        // ── Waste breakdown ───────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 230, w * 0.54f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(16, 242, w * 0.50f, 26), "Waste Breakdown", SmartCityGUI.H2);
        SmartCityGUI.ProgressBar(16, 276, w * 0.50f - 32, "Landfill Waste",  Mathf.Clamp01((1f - recPct) * 0.9f), SmartCityGUI.Red);
        SmartCityGUI.ProgressBar(16, 308, w * 0.50f - 32, "Recycled",        recPct,                               SmartCityGUI.Green);

        // ── Actions ───────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(w * 0.58f, 230, w * 0.42f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(w * 0.58f + 16, 242, w * 0.40f, 26), "Expand Capacity", SmartCityGUI.H2);

        if (GUI.Button(new Rect(w * 0.58f + 16, 276, w * 0.40f - 32, 36),
                "♻ Build Recycling Center  Rs. 30,000", SmartCityGUI.SuccessBtn))
        {
            ConstructionSystem.Instance?.BuildRecyclingCenter();
            page = "3D City View";
        }

        if (GUI.Button(new Rect(w * 0.58f + 16, 318, w * 0.40f - 32, 36),
                "🚛 Add Waste Fleet  Rs. 8,000", SmartCityGUI.SmallButton))
            OnAlert("Waste collection fleet expanded.", CityManager.AlertLevel.Info);

        // ── Info footer ───────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 374, w, 54), SmartCityGUI.Soft);
        GUI.Label(new Rect(16, 382, w - 32, 38),
            "💡  Recycling Centers reduce pollution by 8% and boost sustainability. Each center handles up to 5 T/day of waste.",
            new GUIStyle(SmartCityGUI.Muted) { fontSize = 14, wordWrap = true });
    }

    // ─────────────────────────────────────────────────────────────────────────
    // ── EDUCATION PAGE ────────────────────────────────────────────────────────
    // ─────────────────────────────────────────────────────────────────────────

    void EducationPage(CityState s, float w, float h)
    {
        float cardW = (w - 36) / 3f;

        // ── Stat cards ────────────────────────────────────────────────────────
        SmartCityGUI.ColorCard(0,             8, cardW, 90, SmartCityGUI.Purple,
            "🏫", "SCHOOLS",          s.schools.ToString());
        SmartCityGUI.ColorCard(cardW + 18,    8, cardW, 90, SmartCityGUI.Indigo,
            "🎓", "QUALITY INDEX",    s.educationQuality.ToString("0") + "%");
        SmartCityGUI.ColorCard((cardW + 18)*2, 8, cardW, 90, SmartCityGUI.Teal,
            "👨‍🎓", "STUDENT CAPACITY", (s.schools * 600).ToString("N0"));

        // ── Education quality gauge ───────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 112, w, 105), SmartCityGUI.White);
        GUI.Label(new Rect(16, 124, w - 32, 26), "Education Quality Index", SmartCityGUI.H2);

        float edPct  = Mathf.Clamp01(s.educationQuality / 100f);
        Texture2D edBar = edPct > 0.70f ? SmartCityGUI.Purple :
                          edPct > 0.40f ? SmartCityGUI.Blue : SmartCityGUI.Red;

        GUI.DrawTexture(new Rect(16, 158, w - 32, 18), SmartCityGUI.Soft);
        if (edPct > 0f) GUI.DrawTexture(new Rect(16, 158, (w - 32) * edPct, 18), edBar);

        string edStatus = edPct > 0.70f ? "🌟 Excellent — highly educated workforce" :
                          edPct > 0.40f ? "📖 Average — room for improvement" :
                                          "⚠ Poor — invest in new schools";
        Color edCol = edPct > 0.70f ? new Color(0.40f, 0.10f, 0.75f) :
                      edPct > 0.40f ? new Color(0.08f, 0.42f, 0.78f) :
                                      new Color(0.80f, 0.15f, 0.15f);
        GUI.Label(new Rect(16, 182, w - 32, 22), edStatus,
            new GUIStyle(SmartCityGUI.Muted) { normal = { textColor = edCol },
                                               hover  = { textColor = edCol } });

        // ── Metrics breakdown ─────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 230, w * 0.54f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(16, 242, w * 0.50f, 26), "Performance Metrics", SmartCityGUI.H2);
        SmartCityGUI.ProgressBar(16, 276, w * 0.50f - 32, "Literacy Rate",      Mathf.Clamp01(0.50f + s.schools * 0.04f),         SmartCityGUI.Purple);
        SmartCityGUI.ProgressBar(16, 308, w * 0.50f - 32, "Enrollment Rate",    Mathf.Clamp01(s.educationQuality / 100f),         SmartCityGUI.Blue);

        // ── Actions ───────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(w * 0.58f, 230, w * 0.42f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(w * 0.58f + 16, 242, w * 0.40f, 26), "School Initiatives", SmartCityGUI.H2);

        if (GUI.Button(new Rect(w * 0.58f + 16, 276, w * 0.40f - 32, 36),
                "🏫 Build New School  Rs. 45,000", SmartCityGUI.Button))
        {
            ConstructionSystem.Instance?.BuildSchool();
            page = "3D City View";
        }

        if (GUI.Button(new Rect(w * 0.58f + 16, 318, w * 0.40f - 32, 36),
                "📚 Fund Scholarships  Rs. 15,000", SmartCityGUI.SmallButton))
            OnAlert("Scholarship program funded. Education quality +3%.", CityManager.AlertLevel.Success);

        // ── Info footer ───────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 374, w, 54), SmartCityGUI.Soft);
        GUI.Label(new Rect(16, 382, w - 32, 38),
            "💡  Higher education quality increases employment rate, happiness, and unlocks technology upgrades at Level 4+.",
            new GUIStyle(SmartCityGUI.Muted) { fontSize = 14, wordWrap = true });
    }

    // ─────────────────────────────────────────────────────────────────────────
    // ── SAFETY & SECURITY PAGE ────────────────────────────────────────────────
    // ─────────────────────────────────────────────────────────────────────────

    void SafetyPage(CityState s, float w, float h)
    {
        float cardW = (w - 36) / 3f;

        // ── Stat cards ────────────────────────────────────────────────────────
        SmartCityGUI.ColorCard(0,             8, cardW, 90, SmartCityGUI.Indigo,
            "🚔", "POLICE STATIONS", s.policeStations.ToString());
        SmartCityGUI.ColorCard(cardW + 18,    8, cardW, 90, SmartCityGUI.Red,
            "🚒", "FIRE STATIONS",   s.fireStations.ToString());
        SmartCityGUI.ColorCard((cardW + 18)*2, 8, cardW, 90, SmartCityGUI.Orange,
            "📊", "CRIME RATE",      s.crimeRate.ToString("0") + "%");

        // ── Safety index gauge ────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 112, w, 105), SmartCityGUI.White);
        GUI.Label(new Rect(16, 124, w - 32, 26), "Public Safety Index", SmartCityGUI.H2);

        float safetyIndex = Mathf.Clamp01(1f - s.crimeRate / 100f);
        Texture2D safeBar = safetyIndex > 0.70f ? SmartCityGUI.Green :
                            safetyIndex > 0.40f ? SmartCityGUI.Amber : SmartCityGUI.Red;

        GUI.DrawTexture(new Rect(16, 158, w - 32, 18), SmartCityGUI.Soft);
        if (safetyIndex > 0f) GUI.DrawTexture(new Rect(16, 158, (w - 32) * safetyIndex, 18), safeBar);

        string safeStatus = safetyIndex > 0.70f ? "🛡 High Safety — Citizens feel secure" :
                            safetyIndex > 0.40f ? "⚠ Moderate — increase police presence" :
                                                  "🔴 Dangerous — urgent action required";
        Color safeCol = safetyIndex > 0.70f ? new Color(0.06f, 0.55f, 0.30f) :
                        safetyIndex > 0.40f ? new Color(0.80f, 0.50f, 0.05f) :
                                              new Color(0.80f, 0.15f, 0.15f);
        GUI.Label(new Rect(16, 182, w - 32, 22), safeStatus,
            new GUIStyle(SmartCityGUI.Muted) { normal = { textColor = safeCol },
                                               hover  = { textColor = safeCol } });

        // ── Metrics breakdown ─────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 230, w * 0.54f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(16, 242, w * 0.50f, 26), "Security Metrics", SmartCityGUI.H2);

        float coveragePct = Mathf.Clamp01((s.policeStations * 0.18f) + (s.fireStations * 0.10f));
        SmartCityGUI.ProgressBar(16, 276, w * 0.50f - 32, "Emergency Coverage",  coveragePct,                           SmartCityGUI.Blue);
        SmartCityGUI.ProgressBar(16, 308, w * 0.50f - 32, "Crime Suppression",   Mathf.Clamp01(1f - s.crimeRate/100f), SmartCityGUI.Green);

        // ── Actions ───────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(w * 0.58f, 230, w * 0.42f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(w * 0.58f + 16, 242, w * 0.40f, 26), "Enforcement Actions", SmartCityGUI.H2);

        if (GUI.Button(new Rect(w * 0.58f + 16, 276, w * 0.40f - 32, 36),
                "🚔 Build Police Station  Rs. 35,000", SmartCityGUI.Button))
        {
            ConstructionSystem.Instance?.BuildPoliceStation();
            page = "3D City View";
        }

        if (GUI.Button(new Rect(w * 0.58f + 16, 318, w * 0.40f - 32, 36),
                "🚒 Build Fire Station  Rs. 28,000", SmartCityGUI.DangerBtn))
        {
            ConstructionSystem.Instance?.BuildFireStation();
            page = "3D City View";
        }

        // ── Info footer ───────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 374, w, 54), SmartCityGUI.Soft);
        GUI.Label(new Rect(16, 382, w - 32, 38),
            "💡  Each Police Station reduces crime by ~6%. Fire stations reduce disaster impact. Both services boost citizen happiness significantly.",
            new GUIStyle(SmartCityGUI.Muted) { fontSize = 14, wordWrap = true });
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Other existing pages (unchanged)
    // ─────────────────────────────────────────────────────────────────────────

    void Dashboard(CityState s, float w, float h)
    {
        float cardW = (w - 36) / 4f;
        Card(0,            10, cardW, 95, "POPULATION",  s.population.ToString("N0"),             "Residents in city");
        Card(cardW + 12,   10, cardW, 95, "BUDGET",      "Rs. " + s.budget.ToString("N0"),        "Available funds");
        Card((cardW+12)*2, 10, cardW, 95, "HAPPINESS",   s.happiness.ToString("0") + "%",         "Satisfaction index");
        Card((cardW+12)*3, 10, cardW, 95, "SMART SCORE", s.smartCityScore.ToString("0") + "/100", s.progressionTitle);

        // ── Interactive Quick Mayor Actions Bar ──
        GUI.DrawTexture(new Rect(0, 118, w, 82), SmartCityGUI.White);
        GUI.Label(new Rect(16, 126, w - 32, 22), "⚡ MAYOR QUICK-ACTION DISPATCH CONSOLE", SmartCityGUI.H2);

        float actW = (w - 48) / 4f;
        if (GUI.Button(new Rect(16, 154, actW, 36), "🚨 Emergency Drill (Rs.2.5k)", SmartCityGUI.SmallButton))
        {
            if (s.budget >= 2500) { s.budget -= 2500; s.crimeRate = Mathf.Max(5f, s.crimeRate - 4f); OnAlert("Disaster drill completed! Emergency readiness boosted.", CityManager.AlertLevel.Success); }
            else OnAlert("Insufficient budget for emergency drill.", CityManager.AlertLevel.Warning);
        }
        if (GUI.Button(new Rect(16 + actW + 10, 154, actW, 36), "🌿 Eco-Grid Surge (Rs.5k)", SmartCityGUI.SmallButton))
        {
            if (s.budget >= 5000) { s.budget -= 5000; s.sustainability = Mathf.Min(100f, s.sustainability + 5f); s.pollution = Mathf.Max(0f, s.pollution - 4f); OnAlert("Eco-surge active! Green energy output boosted.", CityManager.AlertLevel.Success); }
            else OnAlert("Insufficient budget for eco-grid surge.", CityManager.AlertLevel.Warning);
        }
        if (GUI.Button(new Rect(16 + (actW + 10)*2, 154, actW, 36), "💰 Citizen Stimulus (Rs.15k)", SmartCityGUI.SmallButton))
        {
            if (s.budget >= 15000) { s.budget -= 15000; s.happiness = Mathf.Min(100f, s.happiness + 6f); OnAlert("Citizen stimulus distributed! Public approval surged.", CityManager.AlertLevel.Success); }
            else OnAlert("Insufficient budget for citizen stimulus.", CityManager.AlertLevel.Warning);
        }
        if (GUI.Button(new Rect(16 + (actW + 10)*3, 154, actW, 36), "🧹 Clean Drive (Rs.3.5k)", SmartCityGUI.SmallButton))
        {
            if (s.budget >= 3500) { s.budget -= 3500; s.pollution = Mathf.Max(0f, s.pollution - 6f); s.airQuality = Mathf.Min(100f, s.airQuality + 5f); OnAlert("Rapid sanitation completed! Air quality improved.", CityManager.AlertLevel.Success); }
            else OnAlert("Insufficient budget for sanitation drive.", CityManager.AlertLevel.Warning);
        }

        // ── Performance Metrics ──
        GUI.DrawTexture(new Rect(0, 212, w, 155), SmartCityGUI.White);
        GUI.Label(new Rect(18, 222, 400, 26), "LIVE PERFORMANCE TELEMETRY", SmartCityGUI.H2);
        Metric("Traffic Efficiency", s.trafficEfficiency,  18,       256, w * 0.45f);
        Metric("Air Quality Index",  s.airQuality,         18,       298, w * 0.45f);
        Metric("Electricity Grid Load",
            100 * Mathf.Min(1f, s.electricityProduction / Mathf.Max(1f, s.electricityConsumption)),
            w * 0.52f, 256, w * 0.45f);
        Metric("Water Reservoir Level", s.reservoirLevel,  w * 0.52f, 298, w * 0.45f);

        // ── Live Alerts Feed ──
        GUI.DrawTexture(new Rect(0, 380, w, 140), SmartCityGUI.White);
        GUI.Label(new Rect(18, 390, 400, 24), "RECENT ALERTS & MUNICIPAL LOGS", SmartCityGUI.H2);
        for (int i = 0; i < Mathf.Min(alerts.Count, 3); i++)
            GUI.Label(new Rect(20, 420 + i * 24, w - 40, 22), "• " + alerts[i], SmartCityGUI.Body);
        if (alerts.Count == 0)
            GUI.Label(new Rect(20, 424, w - 40, 22), "No active warnings. City municipal systems running smoothly.", SmartCityGUI.Muted);
    }

    void Infrastructure(CityState s, float w)
    {
        GUI.Label(new Rect(0, 0, w, 30), "Build & Expand Infrastructure", SmartCityGUI.H2);
        GUI.Label(new Rect(0, 32, w, 22), "Select a building type then click on the 3D city map to place it.", SmartCityGUI.Muted);

        string[] names = { "Residential", "Commercial", "Industrial", "Park", "Hospital", "School", "Police", "Fire", "Power Plant", "Water Facility", "Recycling Center" };
        Building.Kind[] kinds = {
            Building.Kind.Residential, Building.Kind.Commercial, Building.Kind.Industrial,
            Building.Kind.Park,        Building.Kind.Hospital,   Building.Kind.School,
            Building.Kind.Police,      Building.Kind.Fire,       Building.Kind.Power,
            Building.Kind.Water,       Building.Kind.Recycling
        };

        float boxW = (w - 24) / 3f;
        for (int i = 0; i < names.Length; i++)
        {
            float x = (i % 3) * (boxW + 12);
            float y = 58 + (i / 3) * 86;
            GUI.DrawTexture(new Rect(x, y, boxW, 76), SmartCityGUI.White);
            GUI.Label(new Rect(x + 12, y + 10, boxW - 110, 24), names[i], SmartCityGUI.H2);
            GUI.Label(new Rect(x + 12, y + 38, boxW - 110, 20), "Rs. " + ConstructionSystem.Cost(kinds[i]).ToString("N0"), SmartCityGUI.Muted);
            if (GUI.Button(new Rect(x + boxW - 95, y + 16, 85, 42), "BUILD", SmartCityGUI.Button))
            {
                BuildPlacementController.Instance?.EnterPlacementMode(kinds[i], ConstructionSystem.Cost(kinds[i]));
                page = "3D City View";
            }
        }

        if (GUI.Button(new Rect(0,   420, 230, 44), "➕ ADD ROAD  Rs. 12,000",      SmartCityGUI.Button))
            ConstructionSystem.Instance?.AddRoad();
        if (GUI.Button(new Rect(245, 420, 240, 44), "🛠️ REPAIR ROADS  Rs. 8,000",  SmartCityGUI.Button))
            ConstructionSystem.Instance?.RepairRoads();
    }

    void Decorations(CityState s, float w)
    {
        GUI.Label(new Rect(0, 0, w, 30), "City Decorations & Urban Beautification", SmartCityGUI.H2);
        GUI.Label(new Rect(0, 32, w, 22), "Select a decoration to enhance public joy and civic appeal.", SmartCityGUI.Muted);

        string[] decos = { "Fountain", "Flowerbed", "Monument", "Bench", "Sculpture" };
        string[] perks = { "+3% Happiness & Coolness", "+1% Green Aesthetics", "+5% Tourism & Culture", "+1% Public Comfort", "+4% Civic Pride" };

        float boxW = (w - 24) / 3f;
        for (int i = 0; i < decos.Length; i++)
        {
            float x = (i % 3) * (boxW + 12);
            float y = 58 + (i / 3) * 94;
            GUI.DrawTexture(new Rect(x, y, boxW, 84), SmartCityGUI.White);
            GUI.Label(new Rect(x + 12, y + 8, boxW - 100, 22), decos[i], SmartCityGUI.H2);
            GUI.Label(new Rect(x + 12, y + 32, boxW - 100, 18), "Rs. " + ConstructionSystem.DecorationCost(decos[i]).ToString("N0"), SmartCityGUI.Muted);
            GUI.Label(new Rect(x + 12, y + 54, boxW - 100, 18), perks[i], new GUIStyle(SmartCityGUI.CardTitle) { fontSize = 11, normal = { textColor = new Color(0.1f, 0.6f, 0.3f) } });

            if (GUI.Button(new Rect(x + boxW - 90, y + 20, 80, 42), "PLACE", SmartCityGUI.Button))
            {
                BuildPlacementController.Instance?.EnterDecorationMode(decos[i], ConstructionSystem.DecorationCost(decos[i]));
                page = "3D City View";
            }
        }
    }

    void MapOverlays(CityState s, float w)
    {
        GUI.Label(new Rect(0, 0, w, 30), "3D City Map Overlays & District Filters", SmartCityGUI.H2);
        string[] modes = { "None", "Environment", "Traffic", "Safety", "Healthcare", "Utilities" };

        float btnW = (w - 30) / 3f;
        for (int i = 0; i < modes.Length; i++)
        {
            float x = (i % 3) * (btnW + 15);
            float y = 42 + (i / 3) * 54;
            bool active = s.overlayMode == modes[i];
            if (GUI.Button(new Rect(x, y, btnW, 44), modes[i] + " Overlay", active ? SmartCityGUI.NavActive : SmartCityGUI.Button))
            {
                s.overlayMode = modes[i];
                OnAlert("Active Overlay: " + modes[i], CityManager.AlertLevel.Info);
            }
        }

        GUI.DrawTexture(new Rect(0, 168, w, 190), SmartCityGUI.White);
        GUI.Label(new Rect(20, 180, w - 40, 26), "Active Filter Analytics & Action", SmartCityGUI.H2);
        GUI.Label(new Rect(20, 210, w - 40, 60),
            $"Current Mode: {s.overlayMode}\n• Green Zones: Healthy condition & optimal capacity\n• Red Zones: Heavy congestion, elevated crime risk, or high emission load",
            SmartCityGUI.Body);

        if (s.overlayMode != "None")
        {
            if (GUI.Button(new Rect(20, 280, 280, 40), $"⚡ Optimize {s.overlayMode} District (Rs. 10,000)", SmartCityGUI.Button))
            {
                if (s.budget >= 10000)
                {
                    s.budget -= 10000;
                    if (s.overlayMode == "Traffic") s.trafficEfficiency = Mathf.Min(100f, s.trafficEfficiency + 8f);
                    else if (s.overlayMode == "Environment") s.pollution = Mathf.Max(0f, s.pollution - 8f);
                    else if (s.overlayMode == "Safety") s.crimeRate = Mathf.Max(5f, s.crimeRate - 6f);
                    else if (s.overlayMode == "Healthcare") s.healthcareQuality = Mathf.Min(100f, s.healthcareQuality + 6f);
                    OnAlert($"{s.overlayMode} zone intervention completed successfully!", CityManager.AlertLevel.Success);
                }
                else OnAlert("Insufficient budget for district optimization.", CityManager.AlertLevel.Warning);
            }
        }
    }

    void TaxesAndEconomy(CityState s, float w)
    {
        GUI.Label(new Rect(0, 0, w, 30), "Taxes, Revenue & Municipal Bonds", SmartCityGUI.H2);

        float boxW = (w - 24) / 3f;
        TaxCard(0,            40, boxW, "Residential Tax", ref s.residentialTax);
        TaxCard(boxW + 12,    40, boxW, "Commercial Tax",  ref s.commercialTax);
        TaxCard((boxW+12)*2,  40, boxW, "Industrial Tax",  ref s.industrialTax);

        GUI.DrawTexture(new Rect(0, 190, w, 210), SmartCityGUI.White);
        GUI.Label(new Rect(20, 204, w - 40, 26), "Daily Financial Summary & Treasury Operations", SmartCityGUI.H2);
        GUI.Label(new Rect(20, 236, (w-40)/2f, 90),
            $"Daily Tax Income: Rs. {s.dailyIncome:N0}\nService Expenses: Rs. {s.serviceExpenses:N0}\nUtility Costs: Rs. {s.utilityExpenses:N0}",
            SmartCityGUI.Body);
        GUI.Label(new Rect(20 + (w-40)/2f, 236, (w-40)/2f, 90),
            $"Road Maintenance: Rs. {s.maintenanceCost:N0}\nNet Daily Cashflow: Rs. {(s.dailyIncome - s.dailyExpenses):N0}\nCity Progression Rank: {s.progressionTitle}",
            SmartCityGUI.Body);

        // Municipal Bond Button
        if (GUI.Button(new Rect(20, 335, 260, 42), "🏦 Issue Municipal Bond (+Rs. 50,000)", SmartCityGUI.Button))
        {
            s.budget += 50000;
            s.serviceExpenses += 800; // interest service cost
            OnAlert("Municipal Bond issued! Received Rs. 50,000 capital (Debt service: Rs. 800/day).", CityManager.AlertLevel.Success);
        }
    }

    void TaxCard(float x, float y, float w, string name, ref float val)
    {
        GUI.DrawTexture(new Rect(x, y, w, 130), SmartCityGUI.White);
        GUI.Label(new Rect(x + 14, y + 10, w - 28, 22), name,                      SmartCityGUI.CardTitle);
        GUI.Label(new Rect(x + 14, y + 36, w - 28, 30), val.ToString("0.0") + "%", SmartCityGUI.Value);
        if (GUI.Button(new Rect(x + 14,     y + 78, 55, 36), "- 1%", SmartCityGUI.SmallButton)) val = Mathf.Clamp(val - 1f, 0f, 30f);
        if (GUI.Button(new Rect(x + w - 69, y + 78, 55, 36), "+ 1%", SmartCityGUI.SmallButton)) val = Mathf.Clamp(val + 1f, 0f, 30f);
    }

    void Traffic(CityState s, float w)
    {
        float cardW = (w - 24) / 3f;
        Card(0,            10, cardW, 105, "TRAFFIC EFFICIENCY", s.trafficEfficiency.ToString("0") + "%",       "Movement flow index");
        Card(cardW + 12,   10, cardW, 105, "ROAD CONDITION",     s.roadCondition.ToString("0") + "%",           "Pavement health");
        Card((cardW+12)*2, 10, cardW, 105, "SMART SIGNALS",      s.smartTrafficUnlocked ? "AI ACTIVE" : "LOCKED (Lvl 3)", "Adaptive traffic control");

        GUI.DrawTexture(new Rect(0, 130, w, 220), SmartCityGUI.White);
        GUI.Label(new Rect(18, 142, w - 36, 26), "Interactive Traffic Management Console", SmartCityGUI.H2);
        GUI.Label(new Rect(18, 172, w - 36, 44),
            "Moving vehicles in 3D viewport dynamically respond to road conditions and signal optimizations. Deploy smart signals or resurface roads to eliminate bottlenecks.",
            SmartCityGUI.Body);

        float bW = (w - 54) / 3f;
        if (GUI.Button(new Rect(18, 230, bW, 44), "🛠️ Resurface Pavements (Rs.8,000)", SmartCityGUI.Button))
        {
            ConstructionSystem.Instance?.RepairRoads();
            s.roadCondition = 100f;
            s.trafficEfficiency = Mathf.Min(100f, s.trafficEfficiency + 10f);
            OnAlert("City pavements fully restored to 100%!", CityManager.AlertLevel.Success);
        }
        if (GUI.Button(new Rect(18 + bW + 9, 230, bW, 44), "🚦 Sync Signal Timing (Rs.5,000)", SmartCityGUI.Button))
        {
            if (s.budget >= 5000)
            {
                s.budget -= 5000;
                s.trafficEfficiency = Mathf.Min(100f, s.trafficEfficiency + 8f);
                OnAlert("Traffic signals synchronized! Flow efficiency increased.", CityManager.AlertLevel.Success);
            }
            else OnAlert("Insufficient budget to sync signals.", CityManager.AlertLevel.Warning);
        }
        if (GUI.Button(new Rect(18 + (bW + 9)*2, 230, bW, 44), "➕ Add Ring Road (Rs.12,000)", SmartCityGUI.Button))
        {
            ConstructionSystem.Instance?.AddRoad();
        }
    }

    void Transport(CityState s, float w)
    {
        float cardW = (w - 24) / 3f;
        Card(0,            10, cardW, 105, "BUS ROUTES",      s.busRoutes.ToString(),                        "Operational routes");
        Card(cardW + 12,   10, cardW, 105, "FLEET BUSES",     s.buses.ToString(),                            "Active vehicles");
        Card((cardW+12)*2, 10, cardW, 105, "TRANSIT COVERAGE", Mathf.Clamp(55 + s.busRoutes * 6, 0, 95) + "%", "Citizen network access");

        GUI.DrawTexture(new Rect(0, 130, w, 220), SmartCityGUI.White);
        GUI.Label(new Rect(18, 142, w - 36, 26), "Multimodal Public Transit Dispatcher", SmartCityGUI.H2);

        float btnW = (w - 48) / 3f;
        if (GUI.Button(new Rect(18, 185, btnW, 46), "🚌 ADD BUS ROUTE\nRs. 9,000", SmartCityGUI.Button))
            ConstructionSystem.Instance?.AddBusRoute();

        if (GUI.Button(new Rect(18 + btnW + 12, 185, btnW, 46), "🚊 ADD LIGHT RAIL\nRs. 25,000", SmartCityGUI.Button))
        {
            if (s.budget >= 25000)
            {
                s.budget -= 25000;
                s.busRoutes += 2;
                s.trafficEfficiency = Mathf.Min(100f, s.trafficEfficiency + 12f);
                s.happiness = Mathf.Min(100f, s.happiness + 4f);
                OnAlert("Light Rail Transit line opened! Transit ridership surged.", CityManager.AlertLevel.Success);
            }
            else OnAlert("Insufficient budget for Light Rail line.", CityManager.AlertLevel.Warning);
        }

        if (GUI.Button(new Rect(18 + (btnW + 12)*2, 185, btnW, 46), "🚲 BIKE SHARE NETWORK\nRs. 8,000", SmartCityGUI.Button))
        {
            if (s.budget >= 8000)
            {
                s.budget -= 8000;
                s.sustainability = Mathf.Min(100f, s.sustainability + 4f);
                s.pollution = Mathf.Max(0f, s.pollution - 3f);
                OnAlert("Micro-mobility bike stations deployed throughout downtown!", CityManager.AlertLevel.Success);
            }
            else OnAlert("Insufficient budget for bike share network.", CityManager.AlertLevel.Warning);
        }

        GUI.Label(new Rect(18, 255, w - 36, 50),
            $"Estimated Daily Transit Ridership: {s.busRoutes * 340} passengers/day | Fare Revenue: Rs. {s.busRoutes * 1200}/day",
            SmartCityGUI.Muted);
    }

    void Requests(float w, float h)
    {
        if (CitizenRequestSystem.Instance == null)
        {
            GUI.Label(new Rect(0, 20, w, 30), "Initializing Citizen Request System...", SmartCityGUI.Muted);
            return;
        }

        var rs = CitizenRequestSystem.Instance.requests;
        GUI.Label(new Rect(0, 0, w, 28), $"Mayor Civic Inbox — {rs.Count} Actionable Citizen Petitions", SmartCityGUI.H2);

        for (int i = 0; i < rs.Count; i++)
        {
            var r = rs[i];
            float y = 36 + i * 68;
            GUI.DrawTexture(new Rect(0, y, w, 60), SmartCityGUI.White);
            GUI.Label(new Rect(12,  y + 10, 50, 22),  "#" + r.id, SmartCityGUI.CardTitle);
            GUI.Label(new Rect(68,  y + 8,  210, 22), r.category, SmartCityGUI.H2);
            GUI.Label(new Rect(68,  y + 32, 210, 20), r.district + " District", SmartCityGUI.Muted);
            GUI.Label(new Rect(290, y + 18, 140, 22), "Cost: Rs. " + r.cost.ToString("N0"), SmartCityGUI.Body);
            GUI.Label(new Rect(440, y + 18, 90, 22),  r.status, SmartCityGUI.Body);

            if (r.status == "Pending")
            {
                if (GUI.Button(new Rect(w - 190, y + 12, 88, 36), "✓ APPROVE", SmartCityGUI.Button))
                {
                    CitizenRequestSystem.Instance.Resolve(r);
                    OnAlert($"Petition #{r.id} ({r.category}) approved by Mayor!", CityManager.AlertLevel.Success);
                }
                if (GUI.Button(new Rect(w -  94, y + 12, 88, 36), "✕ REJECT", SmartCityGUI.SmallButton))
                {
                    CitizenRequestSystem.Instance.Reject(r);
                    OnAlert($"Petition #{r.id} rejected.", CityManager.AlertLevel.Info);
                }
            }
        }
        if (rs.Count == 0)
            GUI.Label(new Rect(0, 40, w, 30), "No pending citizen requests. Citizens are currently satisfied with civic services.", SmartCityGUI.Muted);
    }

    void Analytics(CityState s, float w, float h)
    {
        float graphW = (w - 16) / 2f;
        Graph(new Rect(0,           10,  graphW, 185), s.populationHistory,    "Population Growth (Citizens)");
        Graph(new Rect(graphW + 16, 10,  graphW, 185), s.budgetHistory,        "Treasury Cash Flow Trend (Rs.)");
        Graph(new Rect(0,           210, graphW, 185), s.happinessHistory,     "Public Happiness Index (%)");
        Graph(new Rect(graphW + 16, 210, graphW, 185), s.sustainabilityHistory,"Eco-Sustainability Rating (%)");
    }

    void Technology(CityState s, float w)
    {
        GUI.Label(new Rect(0, 0, w, 28), "Smart City Innovation & Technology Tree", SmartCityGUI.H2);

        TechCard(0, 36,  "Renewable Clean Energy",        "Solar & Wind Microgrids: -25% pollution, +20% efficiency.", s.renewableEnergyUnlocked, 2, s, w);
        TechCard(0, 116, "Adaptive Smart Traffic AI Grid", "Computer Vision Signal Optimization: +15% traffic flow.",   s.smartTrafficUnlocked,    3, s, w);
        TechCard(0, 196, "High-Speed Rapid Transit Network","Automated Maglev & Electric Fleet: +20% citizen mobility.", s.advancedTransitUnlocked, 4, s, w);
    }

    void TechCard(float x, float y, string name, string desc, bool active, int reqLvl, CityState s, float maxW)
    {
        GUI.DrawTexture(new Rect(x, y, maxW, 72), SmartCityGUI.White);
        GUI.Label(new Rect(x + 18, y + 10, maxW - 200, 24), name, SmartCityGUI.H2);
        GUI.Label(new Rect(x + 18, y + 36, maxW - 200, 26), desc, SmartCityGUI.Muted);

        if (active)
        {
            GUI.Label(new Rect(x + maxW - 140, y + 20, 120, 32), "✓ UNLOCKED",
                new GUIStyle(SmartCityGUI.Badge) { normal = { background = SmartCityGUI.Green } });
        }
        else
        {
            bool canUnlock = s.level >= reqLvl && s.budget >= 20000;
            string btnLabel = s.level < reqLvl ? $"Req. Lvl {reqLvl}" : "RESEARCH (Rs.20k)";
            if (GUI.Button(new Rect(x + maxW - 160, y + 18, 145, 36), btnLabel, canUnlock ? SmartCityGUI.Button : SmartCityGUI.SmallButton))
            {
                if (canUnlock)
                {
                    s.budget -= 20000;
                    if (name.Contains("Renewable")) s.renewableEnergyUnlocked = true;
                    else if (name.Contains("Traffic")) s.smartTrafficUnlocked = true;
                    else if (name.Contains("Transit")) s.advancedTransitUnlocked = true;
                    OnAlert($"Innovation Unlocked: {name}!", CityManager.AlertLevel.Success);
                }
                else
                {
                    OnAlert($"Cannot research: Requires Level {reqLvl} city and Rs. 20,000 funds.", CityManager.AlertLevel.Warning);
                }
            }
        }
    }

    void GenericPage(string p, CityState s, float w, float h)
    {
        GUI.DrawTexture(new Rect(0, 10, w, 260), SmartCityGUI.White);
        GUI.Label(new Rect(22, 22, w - 44, 30), p + " Overview & Status", SmartCityGUI.H2);

        string text = p switch
        {
            "Budget"     => $"Current Budget: Rs. {s.budget:N0}\nDaily Tax Revenue: Rs. {(s.dailyIncome):N0}/day\nDaily Service Expenses: Rs. {(s.dailyExpenses):N0}/day",
            "Population" => $"Population: {s.population:N0} Residents\nEmployment Rate: {s.employmentRate:0}%\nHousing Capacity: {s.houses * 180:N0} Residents",
            _            => "Connected to live city simulation engine."
        };

        GUI.Label(new Rect(22, 62, w - 44, 180), text,
            new GUIStyle(SmartCityGUI.Body) { fontSize = 17 });
    }

    // ─────────────────────────────────────────────────────────────────────────────
    // ── ELECTRICITY PAGE ───────────────────────────────────────────────────────────
    // ─────────────────────────────────────────────────────────────────────────────

    void ElectricityPage(CityState s, float w, float h)
    {
        float cardW = (w - 36) / 3f;

        // ── Stat cards ────────────────────────────────────────────────────────────────────
        SmartCityGUI.ColorCard(0,              8, cardW, 90, SmartCityGUI.Amber,
            "⚡", "PRODUCTION",   s.electricityProduction.ToString("N0") + " kWh");
        SmartCityGUI.ColorCard(cardW + 18,     8, cardW, 90, SmartCityGUI.Blue,
            "📊", "CONSUMPTION",  s.electricityConsumption.ToString("N0") + " kWh");
        SmartCityGUI.ColorCard((cardW + 18)*2, 8, cardW, 90, SmartCityGUI.Dark,
            "🏗", "POWER PLANTS", s.powerPlants.ToString());

        // ── Grid capacity gauge ─────────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 112, w, 105), SmartCityGUI.White);
        GUI.Label(new Rect(16, 124, w - 32, 26), "Grid Capacity & Load", SmartCityGUI.H2);

        float gridPct = Mathf.Clamp01(s.electricityProduction / Mathf.Max(1f, s.electricityConsumption));
        float loadPct = Mathf.Clamp01(s.electricityConsumption / Mathf.Max(1f, s.electricityProduction));
        Texture2D gridBar = gridPct >= 1f ? SmartCityGUI.Green :
                            gridPct >= 0.7f ? SmartCityGUI.Amber : SmartCityGUI.Red;

        GUI.DrawTexture(new Rect(16, 158, w - 32, 18), SmartCityGUI.Soft);
        float fillW = Mathf.Clamp01(gridPct) * (w - 32);
        if (fillW > 0f) GUI.DrawTexture(new Rect(16, 158, fillW, 18), gridBar);

        string gridStatus = gridPct >= 1f  ? "🟢 Surplus — grid running cleanly" :
                            gridPct >= 0.7f ? "🟡 Stable — monitor consumption" :
                                              "🔴 Deficit — blackout risk! Build more plants";
        Color gridCol = gridPct >= 1f  ? new Color(0.06f, 0.55f, 0.30f) :
                        gridPct >= 0.7f ? new Color(0.80f, 0.50f, 0.05f) :
                                          new Color(0.80f, 0.15f, 0.15f);
        GUI.Label(new Rect(16, 182, w - 32, 22), gridStatus,
            new GUIStyle(SmartCityGUI.Muted) { normal = { textColor = gridCol },
                                               hover  = { textColor = gridCol } });

        // ── Production vs Consumption ───────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 230, w * 0.54f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(16, 242, w * 0.50f, 26), "Power Balance", SmartCityGUI.H2);
        float maxKwh = Mathf.Max(s.electricityProduction, s.electricityConsumption, 1f);
        SmartCityGUI.ProgressBar(16, 276, w * 0.50f - 32, "Production",  s.electricityProduction  / maxKwh, SmartCityGUI.Green);
        SmartCityGUI.ProgressBar(16, 308, w * 0.50f - 32, "Consumption", s.electricityConsumption / maxKwh, SmartCityGUI.Amber);

        // ── Actions ───────────────────────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(w * 0.58f, 230, w * 0.42f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(w * 0.58f + 16, 242, w * 0.40f, 26), "Grid Management", SmartCityGUI.H2);

        if (GUI.Button(new Rect(w * 0.58f + 16, 276, w * 0.40f - 32, 36),
                "⚡ Build Power Plant  Rs. 38,000", SmartCityGUI.ActionBtn))
        {
            ConstructionSystem.Instance?.BuildPowerPlant();
            page = "3D City View";
        }

        string renewLabel = s.renewableEnergyUnlocked ? "✅ Renewable Energy: ACTIVE" : "🔒 Renewable: Locked (Level 2)";
        GUI.Label(new Rect(w * 0.58f + 16, 320, w * 0.40f - 32, 30), renewLabel,
            new GUIStyle(SmartCityGUI.Muted)
            {
                fontSize = 14,
                normal  = { textColor = s.renewableEnergyUnlocked ? new Color(0.06f, 0.55f, 0.30f) : new Color(0.50f, 0.50f, 0.55f) },
                hover   = { textColor = s.renewableEnergyUnlocked ? new Color(0.06f, 0.55f, 0.30f) : new Color(0.50f, 0.50f, 0.55f) }
            });

        // ── Info footer ──────────────────────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 374, w, 54), SmartCityGUI.Soft);
        GUI.Label(new Rect(16, 382, w - 32, 38),
            "💡  Each Power Plant produces 2,400 kWh. Unlock Renewable Energy at Level 2 to reduce pollution and cut utility costs by 20%.",
            new GUIStyle(SmartCityGUI.Muted) { fontSize = 14, wordWrap = true });
    }

    // ─────────────────────────────────────────────────────────────────────────────
    // ── ENVIRONMENT PAGE ───────────────────────────────────────────────────────────
    // ─────────────────────────────────────────────────────────────────────────────

    void EnvironmentPage(CityState s, float w, float h)
    {
        float cardW = (w - 36) / 3f;

        // ── Stat cards ────────────────────────────────────────────────────────────────────
        SmartCityGUI.ColorCard(0,              8, cardW, 90, SmartCityGUI.Green,
            "🌳", "GREEN COVER",   s.greenCoverage.ToString("0") + "%");
        SmartCityGUI.ColorCard(cardW + 18,     8, cardW, 90, SmartCityGUI.Blue,
            "💨", "AIR QUALITY",   s.airQuality.ToString("0") + "%");
        SmartCityGUI.ColorCard((cardW + 18)*2, 8, cardW, 90, SmartCityGUI.Teal,
            "♻", "SUSTAINABILITY", s.sustainability.ToString("0") + "%");

        // ── Pollution gauge ──────────────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 112, w, 105), SmartCityGUI.White);
        GUI.Label(new Rect(16, 124, w - 32, 26), "Pollution Index", SmartCityGUI.H2);

        float pollPct = Mathf.Clamp01(s.pollution / 100f);
        Texture2D pollBar = pollPct < 0.30f ? SmartCityGUI.Green :
                            pollPct < 0.60f ? SmartCityGUI.Amber : SmartCityGUI.Red;

        GUI.DrawTexture(new Rect(16, 158, w - 32, 18), SmartCityGUI.Soft);
        if (pollPct > 0f) GUI.DrawTexture(new Rect(16, 158, (w - 32) * pollPct, 18), pollBar);

        string pollStatus = pollPct < 0.30f ? "🌿 Clean air — exemplary environmental record" :
                            pollPct < 0.60f ? "🟡 Moderate — invest in parks & recycling" :
                                              "🔴 High pollution — citizens are unhappy!";
        Color pollCol = pollPct < 0.30f ? new Color(0.06f, 0.55f, 0.30f) :
                        pollPct < 0.60f ? new Color(0.80f, 0.50f, 0.05f) :
                                          new Color(0.80f, 0.15f, 0.15f);
        GUI.Label(new Rect(16, 182, w - 32, 22), pollStatus,
            new GUIStyle(SmartCityGUI.Muted) { normal = { textColor = pollCol },
                                               hover  = { textColor = pollCol } });

        // ── Environmental metrics ─────────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 230, w * 0.54f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(16, 242, w * 0.50f, 26), "Environmental Metrics", SmartCityGUI.H2);
        SmartCityGUI.ProgressBar(16, 276, w * 0.50f - 32, "Green Coverage",  Mathf.Clamp01(s.greenCoverage  / 100f), SmartCityGUI.Green);
        SmartCityGUI.ProgressBar(16, 308, w * 0.50f - 32, "Air Quality",     Mathf.Clamp01(s.airQuality     / 100f), SmartCityGUI.Blue);

        // ── Green initiatives ──────────────────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(w * 0.58f, 230, w * 0.42f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(w * 0.58f + 16, 242, w * 0.40f, 26), "Green Initiatives", SmartCityGUI.H2);

        if (GUI.Button(new Rect(w * 0.58f + 16, 276, w * 0.40f - 32, 36),
                "🌳 Plant Urban Park  Rs. 6,500", SmartCityGUI.SuccessBtn))
        {
            ConstructionSystem.Instance?.PlantPark();
            page = "3D City View";
        }

        if (GUI.Button(new Rect(w * 0.58f + 16, 318, w * 0.40f - 32, 36),
                "♻ Add Recycling Center  Rs. 30,000", SmartCityGUI.ActionBtn))
        {
            ConstructionSystem.Instance?.BuildRecyclingCenter();
            page = "3D City View";
        }

        // ── Info footer ──────────────────────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 374, w, 54), SmartCityGUI.Soft);
        GUI.Label(new Rect(16, 382, w - 32, 38),
            "💡  Parks add +4% green coverage each. Lower pollution boosts happiness, reduces healthcare burden, and unlocks clean energy bonuses.",
            new GUIStyle(SmartCityGUI.Muted) { fontSize = 14, wordWrap = true });
    }

    // ─────────────────────────────────────────────────────────────────────────────
    // ── HEALTHCARE PAGE ────────────────────────────────────────────────────────────
    // ─────────────────────────────────────────────────────────────────────────────

    void HealthcarePage(CityState s, float w, float h)
    {
        float cardW = (w - 36) / 3f;

        // ── Stat cards ────────────────────────────────────────────────────────────────────
        SmartCityGUI.ColorCard(0,              8, cardW, 90, SmartCityGUI.Red,
            "🏥", "HOSPITALS",       s.hospitals.ToString());
        SmartCityGUI.ColorCard(cardW + 18,     8, cardW, 90, SmartCityGUI.Purple,
            "📊", "HEALTH QUALITY",  s.healthcareQuality.ToString("0") + "%");
        SmartCityGUI.ColorCard((cardW + 18)*2, 8, cardW, 90, SmartCityGUI.Teal,
            "👥", "PATIENT CAP.",    (s.hospitals * 500).ToString("N0"));

        // ── Healthcare quality gauge ──────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 112, w, 105), SmartCityGUI.White);
        GUI.Label(new Rect(16, 124, w - 32, 26), "Healthcare Quality Index", SmartCityGUI.H2);

        float hqPct = Mathf.Clamp01(s.healthcareQuality / 100f);
        Texture2D hqBar = hqPct > 0.70f ? SmartCityGUI.Green :
                          hqPct > 0.40f ? SmartCityGUI.Amber : SmartCityGUI.Red;

        GUI.DrawTexture(new Rect(16, 158, w - 32, 18), SmartCityGUI.Soft);
        if (hqPct > 0f) GUI.DrawTexture(new Rect(16, 158, (w - 32) * hqPct, 18), hqBar);

        string hqStatus = hqPct > 0.70f ? "🟢 Excellent — world-class medical care" :
                          hqPct > 0.40f ? "🟡 Average — expand hospital network" :
                                          "🔴 Poor — urgent healthcare investment needed";
        Color hqCol = hqPct > 0.70f ? new Color(0.06f, 0.55f, 0.30f) :
                      hqPct > 0.40f ? new Color(0.80f, 0.50f, 0.05f) :
                                      new Color(0.80f, 0.15f, 0.15f);
        GUI.Label(new Rect(16, 182, w - 32, 22), hqStatus,
            new GUIStyle(SmartCityGUI.Muted) { normal = { textColor = hqCol },
                                               hover  = { textColor = hqCol } });

        // ── Metrics breakdown ───────────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 230, w * 0.54f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(16, 242, w * 0.50f, 26), "Service Metrics", SmartCityGUI.H2);
        float capUsage = Mathf.Clamp01(s.population / Mathf.Max(1f, s.hospitals * 500f));
        SmartCityGUI.ProgressBar(16, 276, w * 0.50f - 32, "Hospital Utilisation", capUsage,  SmartCityGUI.Red);
        SmartCityGUI.ProgressBar(16, 308, w * 0.50f - 32, "Health Quality Index", hqPct,     SmartCityGUI.Purple);

        // ── Actions ───────────────────────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(w * 0.58f, 230, w * 0.42f, 130), SmartCityGUI.White);
        GUI.Label(new Rect(w * 0.58f + 16, 242, w * 0.40f, 26), "Medical Expansion", SmartCityGUI.H2);

        if (GUI.Button(new Rect(w * 0.58f + 16, 276, w * 0.40f - 32, 36),
                "🏥 Build Hospital  Rs. 28,000", SmartCityGUI.Button))
        {
            ConstructionSystem.Instance?.BuildHospital();
            page = "3D City View";
        }

        if (GUI.Button(new Rect(w * 0.58f + 16, 318, w * 0.40f - 32, 36),
                "💊 Fund Health Campaign  Rs. 10,000", SmartCityGUI.SmallButton))
            OnAlert("Health awareness campaign funded. Quality +2%.", CityManager.AlertLevel.Success);

        // ── Info footer ──────────────────────────────────────────────────────────────────────────
        GUI.DrawTexture(new Rect(0, 374, w, 54), SmartCityGUI.Soft);
        GUI.Label(new Rect(16, 382, w - 32, 38),
            "💡  Each hospital serves 500 patients. Healthcare quality above 70% boosts happiness by 8% and increases population growth rate.",
            new GUIStyle(SmartCityGUI.Muted) { fontSize = 14, wordWrap = true });
    }

    // ── Common widget helpers ─────────────────────────────────────────────────

    void Card(float x, float y, float w, float h, string title, string val, string sub)
    {
        GUI.DrawTexture(new Rect(x, y, w, h), SmartCityGUI.White);
        GUI.Label(new Rect(x + 14, y + 10, w - 28, 20), title, SmartCityGUI.CardTitle);
        GUI.Label(new Rect(x + 14, y + 34, w - 28, 32), val,   SmartCityGUI.Value);
        GUI.Label(new Rect(x + 14, y + 70, w - 28, 20), sub,   SmartCityGUI.Muted);
    }

    void Metric(string label, float v, float x, float y, float w)
    {
        GUI.Label(new Rect(x, y, w, 20), label + "   " + v.ToString("0") + "%", SmartCityGUI.Body);
        GUI.DrawTexture(new Rect(x, y + 24, w, 10), SmartCityGUI.Soft);
        GUI.DrawTexture(new Rect(x, y + 24, w * Mathf.Clamp01(v / 100f), 10), SmartCityGUI.Blue);
    }

    void Graph(Rect r, List<float> values, string title)
    {
        GUI.DrawTexture(r, SmartCityGUI.White);
        GUI.Label(new Rect(r.x + 14, r.y + 10, r.width - 28, 24), title, SmartCityGUI.H2);
        if (values == null || values.Count < 2) return;

        float min = values[0], max = values[0];
        foreach (float v in values) { min = Mathf.Min(min, v); max = Mathf.Max(max, v); }
        if (Mathf.Abs(max - min) < 1) max = min + 1;

        Vector2 prev = Vector2.zero;
        for (int i = 0; i < values.Count; i++)
        {
            float x = r.x + 16 + (r.width  - 32) * i / (values.Count - 1f);
            float y = r.y + r.height - 22 - (r.height - 65) * (values[i] - min) / (max - min);
            if (i > 0) DrawLine(prev, new Vector2(x, y), 3f);
            prev = new Vector2(x, y);
        }
    }

    void DrawLine(Vector2 a, Vector2 b, float width)
    {
        Matrix4x4 matrix = GUI.matrix;
        float angle = Vector2.SignedAngle(Vector2.right, b - a);
        GUIUtility.RotateAroundPivot(angle, a);
        GUI.DrawTexture(new Rect(a.x, a.y, (b - a).magnitude, width), SmartCityGUI.Blue);
        GUI.matrix = matrix;
    }

    void Tech(float x, float y, string name, string unlock, bool active, float maxW)
    {
        GUI.DrawTexture(new Rect(x, y, maxW, 62), SmartCityGUI.White);
        GUI.Label(new Rect(x + 18, y + 10, maxW - 170, 24), name,   SmartCityGUI.H2);
        GUI.Label(new Rect(x + 18, y + 36, maxW - 170, 20), unlock, SmartCityGUI.Muted);
        GUI.Label(new Rect(x + maxW - 140, y + 16, 120, 28), active ? "UNLOCKED" : "LOCKED",
            new GUIStyle(SmartCityGUI.Badge)
            { normal = { background = active ? SmartCityGUI.Green : SmartCityGUI.Red } });
    }
}
