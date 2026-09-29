using UnityEngine;
using UnityEngine.SceneManagement;

/// <summary>
/// Main menu UI — simple clean design with city background image.
/// Background loaded from Resources/MenuBackground.
/// </summary>
public class MainMenuUI : MonoBehaviour
{
    enum MenuView { Main, Cities }
    MenuView view = MenuView.Main;

    int    deletePending = -1;
    string statusMsg     = "";

    // ── Cached textures (never create inside OnGUI) ───────────────────────────
    Texture2D bgImage;   // city photo from Resources
    Texture2D overlay;   // dark tint over photo
    Texture2D panelTex;  // center card
    Texture2D divider;   // thin blue line
    Texture2D citiesPanel;

    void Awake()
    {
        // Load game background photo from Resources
        bgImage = Resources.Load<Texture2D>("MenuBackground");

        // Clean light overlay (28% tint) so the futuristic game city art is vibrant
        overlay    = Tex(new Color(0.00f, 0.02f, 0.06f, 0.28f));
        panelTex   = Tex(new Color(0.03f, 0.07f, 0.15f, 0.94f));
        divider    = Tex(new Color(0.20f, 0.55f, 0.95f, 1.00f));
        citiesPanel= Tex(new Color(0.03f, 0.07f, 0.14f, 0.95f));

        MusicManager.EnsurePlaying();
    }

    static Texture2D Tex(Color c)
    {
        var t = new Texture2D(1, 1);
        t.SetPixel(0, 0, c);
        t.Apply();
        return t;
    }

    // ─────────────────────────────────────────────────────────────────────────
    void OnGUI()
    {
        SmartCityGUI.Ensure();
        float sw = Screen.width, sh = Screen.height;

        // Background photo (or navy fallback)
        if (bgImage != null)
            GUI.DrawTexture(new Rect(0, 0, sw, sh), bgImage, ScaleMode.ScaleAndCrop);
        else
            GUI.DrawTexture(new Rect(0, 0, sw, sh), SmartCityGUI.Navy);

        // Dark overlay so text is readable
        GUI.DrawTexture(new Rect(0, 0, sw, sh), overlay);

        if (view == MenuView.Main) DrawMain(sw, sh);
        else                       DrawCities(sw, sh);
    }

    // ─────────────────────────────────────────────────────────────────────────
    // MAIN SCREEN
    // ─────────────────────────────────────────────────────────────────────────
    void DrawMain(float sw, float sh)
    {
        float cx  = sw / 2f;
        float cy  = sh / 2f;
        float pw  = 380f;
        float ph  = 480f;
        float px  = cx - pw / 2f;
        float py  = cy - ph / 2f;

        // Center card
        GUI.DrawTexture(new Rect(px, py, pw, ph), panelTex);
        // Blue top stripe
        GUI.DrawTexture(new Rect(px, py, pw, 3f), divider);

        // ── Logo ─────────────────────────────────────────────────────────────
        GUI.Label(new Rect(px, py + 20f, pw, 52f),
            "🏙  SMART CITY",
            new GUIStyle(SmartCityGUI.Title)
            {
                fontSize  = 34,
                alignment = TextAnchor.MiddleCenter,
                normal    = { textColor = Color.white },
                hover     = { textColor = Color.white }
            });

        GUI.Label(new Rect(px, py + 70f, pw, 26f),
            "Management Simulator — Professional",
            new GUIStyle(SmartCityGUI.Muted)
            {
                fontSize  = 14,
                alignment = TextAnchor.MiddleCenter,
                normal    = { textColor = new Color(0.60f, 0.80f, 1.00f) },
                hover     = { textColor = new Color(0.60f, 0.80f, 1.00f) }
            });

        // Divider
        GUI.DrawTexture(new Rect(px + 40f, py + 104f, pw - 80f, 1f), divider);

        // ── Buttons ───────────────────────────────────────────────────────────
        float bx  = px + 30f;
        float bw  = pw - 60f;
        float by  = py + 120f;
        float bh  = 48f;
        float gap = 12f;

        if (GUI.Button(new Rect(bx, by,                    bw, bh), "▶  START NEW CITY", SmartCityGUI.Button))
            SceneManager.LoadScene("AdminLogin");

        if (GUI.Button(new Rect(bx, by + (bh + gap),       bw, bh), "🏙  MY CITIES  (Continue)", SmartCityGUI.Button))
        { view = MenuView.Cities; deletePending = -1; statusMsg = ""; }

        if (GUI.Button(new Rect(bx, by + (bh + gap) * 2,   bw, bh), "📖  HOW TO PLAY", SmartCityGUI.Button))
            SceneManager.LoadScene("Instructions");

        if (GUI.Button(new Rect(bx, by + (bh + gap) * 3,   bw, bh), "⚙  SETTINGS", SmartCityGUI.Button))
            SceneManager.LoadScene("Settings");

        if (GUI.Button(new Rect(bx, by + (bh + gap) * 4,   bw, bh), "✕  EXIT", SmartCityGUI.Button))
            Application.Quit();

        // Music toggle
        float mby = by + (bh + gap) * 5 + 6f;
        string mLabel = MusicManager.IsPlaying ? "🔊  Music: ON" : "🔇  Music: OFF";
        if (GUI.Button(new Rect(bx, mby, bw, 36f), mLabel, SmartCityGUI.SmallButton))
            MusicManager.Toggle();

        // Status
        if (!string.IsNullOrEmpty(statusMsg))
            GUI.Label(new Rect(px, py + ph - 30f, pw, 24f), statusMsg,
                new GUIStyle(SmartCityGUI.Muted)
                {
                    alignment = TextAnchor.MiddleCenter,
                    normal    = { textColor = new Color(1f, 0.4f, 0.4f) },
                    hover     = { textColor = new Color(1f, 0.4f, 0.4f) }
                });
    }

    // ─────────────────────────────────────────────────────────────────────────
    // MY CITIES SCREEN
    // ─────────────────────────────────────────────────────────────────────────
    void DrawCities(float sw, float sh)
    {
        float pw = Mathf.Min(sw - 60f, 920f);
        float ph = Mathf.Min(sh - 60f, 680f);
        float px = (sw - pw) / 2f;
        float py = (sh - ph) / 2f;

        GUI.DrawTexture(new Rect(px, py, pw, ph), citiesPanel);
        GUI.DrawTexture(new Rect(px, py, pw, 3f), divider);

        // Header
        GUI.Label(new Rect(px + 30f, py + 22f, pw - 180f, 44f),
            "🏙  My Cities", SmartCityGUI.H1);

        if (GUI.Button(new Rect(px + pw - 146f, py + 20f, 126f, 40f), "← BACK", SmartCityGUI.SmallButton))
        { view = MenuView.Main; deletePending = -1; statusMsg = ""; }

        GUI.Label(new Rect(px + 30f, py + 68f, pw - 60f, 24f),
            "Select a city to continue, or start a new one from the main screen.",
            SmartCityGUI.Muted);

        // City slot cards — 2 columns
        float cardW = (pw - 60f) / 2f - 10f;
        float cardH = 122f;
        float startY = py + 102f;
        int   anySave = 0;

        for (int i = 0; i < SaveSystem.MAX_SLOTS; i++)
        {
            float col = i % 2;
            float row = i / 2;
            float cx  = px + 30f + col * (cardW + 20f);
            float cy  = startY + row * (cardH + 14f);

            bool exists = SaveSystem.SlotExists(i);
            if (exists) anySave++;

            GUI.DrawTexture(new Rect(cx, cy, cardW, cardH),
                exists ? SmartCityGUI.White : SmartCityGUI.Soft);

            if (exists)
            {
                string name = SaveSystem.SlotName(i);
                if (string.IsNullOrEmpty(name)) name = "City " + (i + 1);

                GUI.Label(new Rect(cx + 14f, cy + 12f, cardW - 130f, 30f),
                    "🏙  " + name,
                    new GUIStyle(SmartCityGUI.H2) { fontSize = 18 });

                GUI.Label(new Rect(cx + 14f, cy + 46f, cardW - 130f, 22f),
                    "Slot " + (i + 1) + "  •  Tap LOAD to resume", SmartCityGUI.Muted);

                if (deletePending == i)
                {
                    GUI.Label(new Rect(cx + 14f, cy + 76f, cardW - 170f, 22f),
                        "Delete this city?", SmartCityGUI.Body);

                    var redStyle = new GUIStyle(SmartCityGUI.SmallButton)
                    {
                        normal = { background = SmartCityGUI.Red,   textColor = Color.white },
                        hover  = { background = SmartCityGUI.Amber, textColor = Color.white },
                        focused= { background = SmartCityGUI.Red,   textColor = Color.white }
                    };
                    if (GUI.Button(new Rect(cx + cardW - 148f, cy + 70f, 60f, 32f), "YES", redStyle))
                    { SaveSystem.Delete(i); deletePending = -1; }
                    if (GUI.Button(new Rect(cx + cardW - 80f,  cy + 70f, 60f, 32f), "NO", SmartCityGUI.SmallButton))
                        deletePending = -1;
                }
                else
                {
                    if (GUI.Button(new Rect(cx + cardW - 148f, cy + 12f, 66f, 36f), "LOAD", SmartCityGUI.Button))
                    {
                        PlayerPrefs.SetInt("ActiveSlot", i);
                        if (SaveSystem.Load(i)) SceneManager.LoadScene("CitySimulation");
                        else statusMsg = "Failed to load city!";
                    }

                    var delStyle = new GUIStyle(SmartCityGUI.SmallButton)
                    {
                        normal  = { background = SmartCityGUI.Red,   textColor = Color.white },
                        hover   = { background = SmartCityGUI.Amber, textColor = Color.white },
                        focused = { background = SmartCityGUI.Red,   textColor = Color.white }
                    };
                    if (GUI.Button(new Rect(cx + cardW - 74f, cy + 12f, 60f, 36f), "🗑", delStyle))
                        deletePending = i;
                }
            }
            else
            {
                GUI.Label(new Rect(cx + 14f, cy + 20f, cardW - 28f, 28f),
                    "Slot " + (i + 1) + "  —  Empty",
                    new GUIStyle(SmartCityGUI.H2)
                    { normal = { textColor = new Color(0.50f, 0.58f, 0.68f) } });

                GUI.Label(new Rect(cx + 14f, cy + 52f, cardW - 28f, 22f),
                    "No city here yet. Start one from the main screen.", SmartCityGUI.Muted);

                if (GUI.Button(new Rect(cx + 14f, cy + 80f, 180f, 30f), "✚ New City Here", SmartCityGUI.SmallButton))
                {
                    PlayerPrefs.SetInt("ActiveSlot", i);
                    SceneManager.LoadScene("AdminLogin");
                }
            }
        }

        if (anySave == 0)
            GUI.Label(new Rect(px + 30f, startY + 360f, pw - 60f, 30f),
                "No saved cities yet — press START NEW CITY from the main screen!",
                new GUIStyle(SmartCityGUI.Body)
                {
                    alignment = TextAnchor.MiddleCenter,
                    normal    = { textColor = new Color(0.50f, 0.65f, 0.82f) },
                    hover     = { textColor = new Color(0.50f, 0.65f, 0.82f) }
                });

        if (!string.IsNullOrEmpty(statusMsg))
            GUI.Label(new Rect(px + 30f, py + ph - 44f, pw - 60f, 30f), statusMsg,
                new GUIStyle(SmartCityGUI.Body)
                {
                    alignment = TextAnchor.MiddleCenter,
                    normal    = { textColor = new Color(0.95f, 0.40f, 0.40f) },
                    hover     = { textColor = new Color(0.95f, 0.40f, 0.40f) }
                });
    }
}
