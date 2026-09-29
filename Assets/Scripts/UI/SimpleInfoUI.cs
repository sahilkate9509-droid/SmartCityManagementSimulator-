using UnityEngine;
using UnityEngine.SceneManagement;

/// <summary>
/// Shared base for the Instructions and Settings screens.
/// Set <see cref="isSettings"/> to true on the Settings GameObject.
/// </summary>
public class SimpleInfoUI : MonoBehaviour
{
    [Header("Screen type")]
    public bool isSettings = false; // false = Instructions, true = Settings

    // Legacy fields used by SmartCityProjectBuilder editor script
    // (kept for compile compatibility — the new UI doesn't render these directly)
    [HideInInspector] public string title = "Instructions";
    [HideInInspector] public string body  = "";

    // Settings sliders state
    float musicVol    = 0.75f;
    float sfxVol      = 0.85f;
    float simSpeed    = 1f;
    bool  fullscreen  = true;
    int   qualityIdx  = 2; // 0=Low 1=Med 2=High

    void Awake()
    {
        // Auto-detect screen type from legacy title field set by the editor builder
        if (title == "Settings") isSettings = true;

        // Load persisted settings
        musicVol   = PlayerPrefs.GetFloat("MusicVol",  0.75f);
        sfxVol     = PlayerPrefs.GetFloat("SfxVol",    0.85f);
        simSpeed   = PlayerPrefs.GetFloat("SimSpeed",  1f);
        fullscreen = PlayerPrefs.GetInt("Fullscreen",  1) == 1;
        qualityIdx = PlayerPrefs.GetInt("Quality",     2);
    }

    void OnGUI()
    {
        SmartCityGUI.Ensure();
        GUI.DrawTexture(new Rect(0, 0, Screen.width, Screen.height), SmartCityGUI.Navy);

        if (isSettings) DrawSettings();
        else            DrawInstructions();
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Instructions — How To Play
    // ─────────────────────────────────────────────────────────────────────────

    void DrawInstructions()
    {
        float sw = Screen.width, sh = Screen.height;
        float pw = Mathf.Min(sw - 60, 980);
        float ph = Mathf.Min(sh - 60, 760);
        float px = (sw - pw) / 2f, py = (sh - ph) / 2f;

        GUI.DrawTexture(new Rect(px, py, pw, ph), SmartCityGUI.GlassPanel);

        // Header
        GUI.Label(new Rect(px + 36, py + 26, pw - 72, 48),
            "📖  How To Play", SmartCityGUI.H1);
        GUI.DrawTexture(new Rect(px + 36, py + 78, pw - 72, 2), SmartCityGUI.Blue);

        float col = (pw - 72) / 2f - 10f;
        float lx1 = px + 36, lx2 = px + 36 + col + 20;
        float ly = py + 94;

        // Left column
        Section(lx1, ly,      col, "🎮  Camera Controls",
            "• Q / E Keys — Rotate view left / right\n" +
            "• WASD / Arrow Keys — Pan across the city\n" +
            "• Hold Right Mouse (or Alt+LMB) — Rotate view\n" +
            "• Mouse Scroll — Zoom in / out\n" +
            "• Camera HUD (bottom-right) — 45° Rotate & Orbit\n" +
            "• Shift — 2.5× movement speed");

        Section(lx1, ly + 162, col, "🏗️  Building",
            "1. Open the Infrastructure panel from the sidebar.\n" +
            "2. Click BUILD next to any building type.\n" +
            "3. A coloured ghost appears on the city map.\n" +
            "   GREEN = free cell | RED = already occupied.\n" +
            "4. Left-click to confirm placement.\n" +
            "   Press ESC or Right-click to cancel.");

        Section(lx1, ly + 360, col, "🌳  Decorations",
            "Open 'City Decorations' in the sidebar.\n" +
            "Click PLACE, then click anywhere on the city.\n" +
            "Decorations boost happiness and land value.");

        Section(lx1, ly + 490, col, "🚌  Transport",
            "Use 'Public Transport' to add bus routes.\n" +
            "Bus stops spawn automatically on the main road.\n" +
            "More routes = lower traffic and higher happiness.");

        // Right column
        Section(lx2, ly,      col, "📊  City Metrics",
            "Budget    — Spend wisely; income comes from taxes.\n" +
            "Population — Grows when happiness is high.\n" +
            "Happiness  — Keep it above 60% for growth.\n" +
            "Sustainability — Build parks, add recycling centres.\n" +
            "Smart City Score — Overall city health (target 80+).");

        Section(lx2, ly + 172, col, "⚡  Events & Crises",
            "Random events appear as decision modals.\n" +
            "Choose wisely — each option has a different cost\n" +
            "and effect on your city metrics.\n" +
            "Ignoring events has penalties!");

        Section(lx2, ly + 330, col, "💾  Saving",
            "Click '💾 SAVE CITY' in the sidebar at any time.\n" +
            "Up to 5 cities can be saved independently.\n" +
            "Resume any city from Main Menu → My Cities.");

        Section(lx2, ly + 460, col, "💡  Pro Tips",
            "• Build roads before buildings in a new zone.\n" +
            "• Power + Water are needed for high population.\n" +
            "• Industrial zones boost income but raise pollution.\n" +
            "• Use 4× speed when waiting for income to grow.");

        // Back button
        if (GUI.Button(new Rect(px + 36, py + ph - 62, 180, 44), "← MAIN MENU", SmartCityGUI.Button))
            SceneManager.LoadScene("MainMenu");
    }

    void Section(float x, float y, float w, string heading, string text)
    {
        GUI.Label(new Rect(x, y, w, 28), heading,
            new GUIStyle(SmartCityGUI.H2) { fontSize = 17 });
        GUI.DrawTexture(new Rect(x, y + 29, w, 1), SmartCityGUI.Blue);
        GUI.Label(new Rect(x, y + 34, w, 120), text,
            new GUIStyle(SmartCityGUI.Body) { fontSize = 15, wordWrap = true });
    }

    // ─────────────────────────────────────────────────────────────────────────
    // Settings
    // ─────────────────────────────────────────────────────────────────────────

    void DrawSettings()
    {
        float sw = Screen.width, sh = Screen.height;
        float pw = Mathf.Min(sw - 60, 820);
        float ph = Mathf.Min(sh - 60, 680);
        float px = (sw - pw) / 2f, py = (sh - ph) / 2f;

        GUI.DrawTexture(new Rect(px, py, pw, ph), SmartCityGUI.GlassPanel);

        GUI.Label(new Rect(px + 36, py + 26, pw - 72, 48), "⚙  Settings", SmartCityGUI.H1);
        GUI.DrawTexture(new Rect(px + 36, py + 78, pw - 72, 2), SmartCityGUI.Blue);

        float fx = px + 36, fw = pw - 72, fy = py + 98;

        // ── Audio ────────────────────────────────────────────────────────────
        SettingHeader(fx, fy, fw, "🔊  Audio");
        float prevVol = musicVol;
        musicVol = SettingSlider(fx, fy + 38, fw, "Music Volume",   musicVol);
        if (!Mathf.Approximately(prevVol, musicVol)) MusicManager.SetVolume(musicVol);
        sfxVol   = SettingSlider(fx, fy + 88, fw, "Sound Effects",  sfxVol);

        // Music toggle button
        string mLabel = MusicManager.IsPlaying ? "🔊  Music: ON" : "🔇  Music: OFF";
        if (GUI.Button(new Rect(fx + fw - 150f, fy + 88, 146, 32), mLabel,
                new GUIStyle(SmartCityGUI.SmallButton)
                {
                    normal  = { background = MusicManager.IsPlaying ? SmartCityGUI.Green : SmartCityGUI.Dark, textColor = Color.white },
                    hover   = { background = SmartCityGUI.Blue, textColor = Color.white },
                    focused = { background = MusicManager.IsPlaying ? SmartCityGUI.Green : SmartCityGUI.Dark, textColor = Color.white }
                }))
            MusicManager.Toggle();

        // ── Gameplay ──────────────────────────────────────────────────────────
        SettingHeader(fx, fy + 148, fw, "🎮  Gameplay");
        simSpeed = SettingSlider(fx, fy + 186, fw, "Default Sim Speed (1×–4×)", (simSpeed - 1f) / 3f);
        simSpeed = Mathf.Round(simSpeed * 3f + 1f); // convert back

        // ── Display ──────────────────────────────────────────────────────────
        SettingHeader(fx, fy + 248, fw, "🖥️  Display");

        GUI.Label(new Rect(fx, fy + 286, 200, 28), "Fullscreen", SmartCityGUI.Body);
        if (GUI.Button(new Rect(fx + 220, fy + 283, 110, 32),
                fullscreen ? "ON  ✔" : "OFF",
                new GUIStyle(SmartCityGUI.SmallButton)
                {
                    normal = { background = fullscreen ? SmartCityGUI.Green : SmartCityGUI.Dark, textColor = Color.white },
                    hover  = { background = SmartCityGUI.Blue, textColor = Color.white }
                }))
        {
            fullscreen = !fullscreen;
            Screen.fullScreen = fullscreen;
        }

        GUI.Label(new Rect(fx, fy + 328, 200, 28), "Graphics Quality", SmartCityGUI.Body);
        string[] qNames = { "Low", "Medium", "High" };
        for (int q = 0; q < qNames.Length; q++)
        {
            bool active = qualityIdx == q;
            if (GUI.Button(new Rect(fx + 220 + q * 90, fy + 325, 82, 32), qNames[q],
                    new GUIStyle(SmartCityGUI.SmallButton)
                    {
                        normal = { background = active ? SmartCityGUI.Blue : SmartCityGUI.Dark, textColor = Color.white },
                        hover  = { background = SmartCityGUI.Green, textColor = new Color(0.05f, 0.05f, 0.05f) }
                    }))
            {
                qualityIdx = q;
                QualitySettings.SetQualityLevel(q == 0 ? 0 : q == 1 ? 2 : 5, true);
            }
        }

        // ── Controls reference ───────────────────────────────────────────────
        SettingHeader(fx, fy + 378, fw, "⌨️  Key Bindings");
        GUI.Label(new Rect(fx, fy + 416, fw, 80),
            "WASD / Arrows — Pan   |   Q / E or Hold RMB — Rotate   |   Mouse Scroll — Zoom\n" +
            "HUD Buttons — 45° Rotate & Orbit   |   Shift — Speed boost   |   ESC — Cancel placement",
            new GUIStyle(SmartCityGUI.Body) { fontSize = 15, wordWrap = true });

        // ── Buttons ──────────────────────────────────────────────────────────
        if (GUI.Button(new Rect(fx, py + ph - 62, 180, 44), "💾 SAVE SETTINGS", SmartCityGUI.Button))
        {
            PlayerPrefs.SetFloat("MusicVol",   musicVol);
            PlayerPrefs.SetFloat("SfxVol",     sfxVol);
            PlayerPrefs.SetFloat("SimSpeed",   simSpeed);
            PlayerPrefs.SetInt("Fullscreen",   fullscreen ? 1 : 0);
            PlayerPrefs.SetInt("Quality",      qualityIdx);
            MusicManager.SetVolume(musicVol); // apply immediately
            PlayerPrefs.Save();
        }
        if (GUI.Button(new Rect(fx + 200, py + ph - 62, 180, 44), "← MAIN MENU", SmartCityGUI.Button))
            SceneManager.LoadScene("MainMenu");

        if (GUI.Button(new Rect(fx + 400, py + ph - 62, 210, 44), "🗑 RESET ALL DATA",
                new GUIStyle(SmartCityGUI.SmallButton)
                { normal = { background = SmartCityGUI.Red, textColor = Color.white },
                  hover  = { background = SmartCityGUI.Amber, textColor = Color.white } }))
        {
            PlayerPrefs.DeleteAll();
            PlayerPrefs.Save();
        }
    }

    void SettingHeader(float x, float y, float w, string text)
    {
        GUI.Label(new Rect(x, y, w, 28), text,
            new GUIStyle(SmartCityGUI.H2) { fontSize = 18 });
        GUI.DrawTexture(new Rect(x, y + 29, w, 1), SmartCityGUI.Blue);
    }

    float SettingSlider(float x, float y, float w, string label, float val)
    {
        GUI.Label(new Rect(x, y, 220, 28), label, SmartCityGUI.Body);
        float newVal = GUI.HorizontalSlider(new Rect(x + 230, y + 6, w - 340, 16), val, 0f, 1f);
        GUI.Label(new Rect(x + w - 100, y, 95, 28),
            Mathf.RoundToInt(newVal * 100) + "%",
            new GUIStyle(SmartCityGUI.Body) { alignment = TextAnchor.MiddleRight });
        return newVal;
    }
}
