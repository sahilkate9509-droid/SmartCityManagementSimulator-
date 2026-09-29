using System;
using UnityEngine;
using UnityEngine.SceneManagement;

/// <summary>
/// Interactive City Creation UI:
/// Allows the authenticated Mayor to configure city name, biome terrain,
/// economic difficulty perks, and starting capital before simulation launch.
/// </summary>
public class CreateCityUI : MonoBehaviour
{
    string cityName = "Neo Metropolis";
    string difficulty = "Easy";
    string budget = "500000";
    int selectedBiomeIdx = 0;
    readonly string[] biomeOptions = { "🌿 Green Valley (Rivers & Grass)", "🌊 Coastal Bay (Harbor & Ocean)", "⚡ Cyber Hub (High-Tech Metro)", "🏜️ Sun Valley (Solar Advantage)" };

    string mayorName = "Chief Mayor";
    string mayorRole = "Executive Urban Planner";

    Texture2D bgImage;
    Texture2D glassCard;
    Texture2D badgeTex;

    void Awake()
    {
        bgImage = Resources.Load<Texture2D>("MenuBackground");
        glassCard = Tex(new Color(0.03f, 0.08f, 0.17f, 0.95f));
        badgeTex = Tex(new Color(0.10f, 0.35f, 0.75f, 0.9f));

        mayorName = PlayerPrefs.GetString("CurrentUser_Name", "Chief Mayor");
        mayorRole = PlayerPrefs.GetString("CurrentUser_Role", "Urban Planner");
    }

    static Texture2D Tex(Color c)
    {
        var t = new Texture2D(1, 1);
        t.SetPixel(0, 0, c);
        t.Apply();
        return t;
    }

    void OnGUI()
    {
        SmartCityGUI.Ensure();
        float sw = Screen.width;
        float sh = Screen.height;

        if (bgImage != null)
            GUI.DrawTexture(new Rect(0, 0, sw, sh), bgImage, ScaleMode.ScaleAndCrop);
        else
            GUI.DrawTexture(new Rect(0, 0, sw, sh), SmartCityGUI.Navy);

        // Dark tint
        GUI.DrawTexture(new Rect(0, 0, sw, sh), Tex(new Color(0.02f, 0.04f, 0.08f, 0.65f)));

        float cardW = Mathf.Clamp(sw * 0.55f, 560f, 720f);
        float cardH = Mathf.Clamp(sh * 0.88f, 560f, 680f);
        float cardX = (sw - cardW) / 2f;
        float cardY = (sh - cardH) / 2f;

        // Draw Card Panel
        GUI.DrawTexture(new Rect(cardX, cardY, cardW, cardH), glassCard);
        GUI.DrawTexture(new Rect(cardX, cardY, cardW, 3f), SmartCityGUI.Blue);

        // ── Mayor Profile Badge Header ──
        float curY = cardY + 20f;
        float innerX = cardX + 36f;
        float innerW = cardW - 72f;

        // Badge banner
        GUI.DrawTexture(new Rect(innerX, curY, innerW, 44f), badgeTex);
        GUI.Label(new Rect(innerX + 16f, curY + 6f, innerW - 160f, 32f),
            $"🎖️  MAYOR IN CHARGE: {mayorName.ToUpper()}  ({mayorRole})",
            new GUIStyle(SmartCityGUI.CardTitle) { fontSize = 13, normal = { textColor = Color.white } });

        if (GUI.Button(new Rect(innerX + innerW - 120f, curY + 7f, 110f, 30f), "Switch Mayor", SmartCityGUI.SmallButton))
        {
            SceneManager.LoadScene("AdminLogin");
        }
        curY += 56f;

        // Title
        GUI.Label(new Rect(innerX, curY, innerW, 36f), "🏙️ FOUND YOUR SMART CITY", SmartCityGUI.H1);
        GUI.Label(new Rect(innerX, curY + 32f, innerW, 22f), "Configure territory specifications and initialize municipal treasury", SmartCityGUI.Muted);
        curY += 60f;

        // ── City Name Input ──
        GUI.Label(new Rect(innerX, curY, innerW, 20f), "CITY NAME", SmartCityGUI.CardTitle);
        cityName = GUI.TextField(new Rect(innerX, curY + 22f, innerW, 36f), cityName);
        curY += 68f;

        // ── Biome & Terrain Style ──
        GUI.Label(new Rect(innerX, curY, innerW, 20f), "TERRAIN BIOME & CLIMATE", SmartCityGUI.CardTitle);
        curY += 24f;
        float bBtnW = (innerW - 12f) / 2f;
        for (int i = 0; i < biomeOptions.Length; i++)
        {
            float bx = innerX + (i % 2) * (bBtnW + 12f);
            float by = curY + (i / 2) * 34f;
            bool isSel = selectedBiomeIdx == i;
            var bStyle = new GUIStyle(SmartCityGUI.SmallButton)
            {
                fontSize = 12,
                normal = { background = isSel ? SmartCityGUI.Blue : SmartCityGUI.Dark, textColor = isSel ? Color.white : new Color(0.75f, 0.82f, 0.92f) }
            };
            if (GUI.Button(new Rect(bx, by, bBtnW, 30f), (isSel ? "✓ " : "") + biomeOptions[i], bStyle))
            {
                selectedBiomeIdx = i;
            }
        }
        curY += 76f;

        // ── Difficulty Cards ──
        GUI.Label(new Rect(innerX, curY, innerW, 20f), "MANAGEMENT DIFFICULTY & GRANTS", SmartCityGUI.CardTitle);
        curY += 24f;
        float diffCardW = (innerW - 20f) / 3f;

        DrawDifficultyCard(innerX, curY, diffCardW, "Easy", "Rs. 150,000", "High citizen tolerance, low disaster frequency, high tax revenue.", SmartCityGUI.Green);
        DrawDifficultyCard(innerX + diffCardW + 10f, curY, diffCardW, "Medium", "Rs. 120,000", "Balanced economy, dynamic demands, realistic maintenance.", SmartCityGUI.Blue);
        DrawDifficultyCard(innerX + (diffCardW + 10f) * 2, curY, diffCardW, "Hard", "Rs. 90,000", "Strict resource margins, higher breakdown rates, high challenge.", SmartCityGUI.Red);
        curY += 105f;

        // ── Initial Budget ──
        GUI.Label(new Rect(innerX, curY, innerW, 20f), "STARTING MUNICIPAL TREASURY (RS.)", SmartCityGUI.CardTitle);
        budget = GUI.TextField(new Rect(innerX, curY + 22f, innerW, 36f), budget);
        curY += 66f;

        // ── Launch Button ──
        if (GUI.Button(new Rect(innerX, curY, innerW, 46f), "🚀  INITIALIZE CITY SIMULATION", SmartCityGUI.Button))
        {
            if (float.TryParse(budget, out float b))
            {
                if (CityManager.Instance)
                {
                    CityManager.Instance.NewCity(cityName, difficulty, b);
                }
                if (CityApiClient.Instance)
                {
                    CityApiClient.Instance.SyncCurrentCity();
                }

                int slot = PlayerPrefs.GetInt("ActiveSlot", FindFreeSlot());
                PlayerPrefs.SetInt("ActiveSlot", slot);
                SaveSystem.Save(slot);
                SceneManager.LoadScene("CitySimulation");
            }
        }
    }

    void DrawDifficultyCard(float x, float y, float w, string name, string amount, string desc, Texture2D accentTex)
    {
        bool isSel = difficulty == name;
        GUI.DrawTexture(new Rect(x, y, w, 95f), isSel ? SmartCityGUI.White : SmartCityGUI.Dark);
        if (isSel)
            GUI.DrawTexture(new Rect(x, y, w, 3f), accentTex);

        var titleStyle = new GUIStyle(SmartCityGUI.H2)
        {
            fontSize = 15,
            normal = { textColor = isSel ? Color.white : new Color(0.7f, 0.8f, 0.9f) }
        };
        GUI.Label(new Rect(x + 10f, y + 8f, w - 20f, 20f), name, titleStyle);

        var amtStyle = new GUIStyle(SmartCityGUI.Value)
        {
            fontSize = 13,
            normal = { textColor = isSel ? new Color(0.2f, 0.9f, 0.4f) : new Color(0.5f, 0.7f, 0.9f) }
        };
        GUI.Label(new Rect(x + 10f, y + 28f, w - 20f, 18f), amount, amtStyle);

        var descStyle = new GUIStyle(SmartCityGUI.Muted)
        {
            fontSize = 10,
            wordWrap = true,
            normal = { textColor = isSel ? new Color(0.8f, 0.85f, 0.95f) : new Color(0.5f, 0.6f, 0.7f) }
        };
        GUI.Label(new Rect(x + 10f, y + 48f, w - 20f, 44f), desc, descStyle);

        if (GUI.Button(new Rect(x, y, w, 95f), GUIContent.none, GUIStyle.none))
        {
            difficulty = name;
            budget = name == "Easy" ? "150000" : name == "Medium" ? "120000" : "90000";
        }
    }

    int FindFreeSlot()
    {
        for (int i = 0; i < SaveSystem.MAX_SLOTS; i++)
            if (!SaveSystem.SlotExists(i)) return i;
        return 0;
    }
}
