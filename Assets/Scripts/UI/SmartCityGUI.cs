using UnityEngine;

/// <summary>
/// Smart City Simulator UI System:
/// Modern Cyber-Glassmorphism aesthetic with high-contrast glowing typography,
/// translucent frosted cards, neon metric gauges, and dynamic interactive buttons.
/// </summary>
public static class SmartCityGUI
{
    static GUIStyle title, h1, h2, body, muted, button, nav, navActive,
                    cardTitle, value, smallButton, badge,
                    iconLabel, statCardStyle, progressLabel,
                    actionBtn, dangerBtn, successBtn;

    static Texture2D navy, blue, white, soft, green, amber, red, dark,
                     glassPanel, glassDark, transparent,
                     tealTex, purpleTex, orangeTex, cyanTex, indigotex, borderTex;

    static Texture2D Tex(Color c)
    {
        var t = new Texture2D(1, 1);
        t.SetPixel(0, 0, c);
        t.Apply();
        return t;
    }

    public static void Ensure()
    {
        if (navy != null) return;

        // ── Modern Cyber / Frosted Glass Palettes ─────────────────────────────
        navy        = Tex(new Color(0.04f, 0.08f, 0.16f, 0.96f)); // Deep space navy header
        blue        = Tex(new Color(0.08f, 0.48f, 0.90f, 1.0f));  // Electric royal blue
        white       = Tex(new Color(0.08f, 0.14f, 0.26f, 0.88f)); // Frosted dark glass card (replaces glaring white)
        soft        = Tex(new Color(0.12f, 0.20f, 0.35f, 0.70f)); // Translucent progress track
        green       = Tex(new Color(0.10f, 0.75f, 0.42f, 1.0f));  // Emerald neon
        amber       = Tex(new Color(0.98f, 0.65f, 0.10f, 1.0f));  // Cyber amber
        red         = Tex(new Color(0.92f, 0.24f, 0.28f, 1.0f));  // Crimson glow
        dark        = Tex(new Color(0.05f, 0.09f, 0.18f, 0.95f)); // Dark background
        glassPanel  = Tex(new Color(0.05f, 0.10f, 0.20f, 0.92f)); // Translucent floating glass window
        glassDark   = Tex(new Color(0.03f, 0.07f, 0.14f, 0.90f)); // Sidebar glass
        transparent = Tex(new Color(0f, 0f, 0f, 0f));
        borderTex   = Tex(new Color(0.20f, 0.60f, 1.00f, 0.85f)); // Neon cyan border

        // Accents
        tealTex   = Tex(new Color(0.06f, 0.68f, 0.72f, 1.0f));
        purpleTex = Tex(new Color(0.55f, 0.30f, 0.90f, 1.0f));
        orangeTex = Tex(new Color(0.96f, 0.48f, 0.12f, 1.0f));
        cyanTex   = Tex(new Color(0.15f, 0.85f, 0.98f, 1.0f));
        indigotex = Tex(new Color(0.25f, 0.35f, 0.80f, 1.0f));

        // ── Typography Styles ──────────────────────────────────────────────────
        title = new GUIStyle(GUI.skin.label)
        {
            fontSize  = 34,
            fontStyle = FontStyle.Bold,
            alignment = TextAnchor.MiddleCenter,
            normal    = { textColor = Color.white },
            hover     = { textColor = Color.white },
            focused   = { textColor = Color.white }
        };

        h1 = new GUIStyle(GUI.skin.label)
        {
            fontSize  = 24,
            fontStyle = FontStyle.Bold,
            normal    = { textColor = new Color(0.92f, 0.96f, 1.00f) },
            hover     = { textColor = new Color(0.92f, 0.96f, 1.00f) },
            focused   = { textColor = new Color(0.92f, 0.96f, 1.00f) }
        };

        h2 = new GUIStyle(GUI.skin.label)
        {
            fontSize  = 18,
            fontStyle = FontStyle.Bold,
            normal    = { textColor = new Color(0.40f, 0.82f, 1.00f) },
            hover     = { textColor = new Color(0.40f, 0.82f, 1.00f) },
            focused   = { textColor = new Color(0.40f, 0.82f, 1.00f) }
        };

        body = new GUIStyle(GUI.skin.label)
        {
            fontSize  = 15,
            normal    = { textColor = new Color(0.85f, 0.90f, 0.98f) },
            hover     = { textColor = new Color(0.85f, 0.90f, 0.98f) },
            focused   = { textColor = new Color(0.85f, 0.90f, 0.98f) },
            wordWrap  = true
        };

        muted = new GUIStyle(body)
        {
            fontSize = 13,
            normal   = { textColor = new Color(0.60f, 0.70f, 0.84f) },
            hover    = { textColor = new Color(0.60f, 0.70f, 0.84f) },
            focused  = { textColor = new Color(0.60f, 0.70f, 0.84f) }
        };

        cardTitle = new GUIStyle(body)
        {
            fontSize  = 12,
            fontStyle = FontStyle.Bold,
            normal    = { textColor = new Color(0.45f, 0.75f, 1.00f) },
            hover     = { textColor = new Color(0.45f, 0.75f, 1.00f) },
            focused   = { textColor = new Color(0.45f, 0.75f, 1.00f) }
        };

        value = new GUIStyle(body)
        {
            fontSize  = 24,
            fontStyle = FontStyle.Bold,
            normal    = { textColor = new Color(0.20f, 0.95f, 0.70f) },
            hover     = { textColor = new Color(0.20f, 0.95f, 0.70f) },
            focused   = { textColor = new Color(0.20f, 0.95f, 0.70f) }
        };

        badge = new GUIStyle(body)
        {
            fontSize  = 13,
            fontStyle = FontStyle.Bold,
            alignment = TextAnchor.MiddleCenter,
            normal    = { textColor = Color.white },
            hover     = { textColor = Color.white },
            focused   = { textColor = Color.white }
        };

        iconLabel = new GUIStyle(GUI.skin.label)
        {
            fontSize  = 14,
            fontStyle = FontStyle.Bold,
            wordWrap  = false,
            normal    = { textColor = Color.white },
            hover     = { textColor = Color.white },
            focused   = { textColor = Color.white }
        };

        statCardStyle = new GUIStyle(GUI.skin.label)
        {
            fontSize  = 22,
            fontStyle = FontStyle.Bold,
            alignment = TextAnchor.MiddleCenter,
            normal    = { textColor = Color.white },
            hover     = { textColor = Color.white },
            focused   = { textColor = Color.white }
        };

        progressLabel = new GUIStyle(GUI.skin.label)
        {
            fontSize  = 13,
            fontStyle = FontStyle.Bold,
            alignment = TextAnchor.MiddleRight,
            normal    = { textColor = new Color(0.40f, 0.82f, 1.00f) },
            hover     = { textColor = new Color(0.40f, 0.82f, 1.00f) }
        };

        // ── Interactive Buttons ────────────────────────────────────────────────
        button = new GUIStyle(GUI.skin.button)
        {
            fontSize  = 15,
            fontStyle = FontStyle.Bold,
            normal    = { background = blue,      textColor = Color.white },
            hover     = { background = cyanTex,   textColor = new Color(0.02f, 0.05f, 0.10f) },
            active    = { background = dark,      textColor = Color.white },
            focused   = { background = blue,      textColor = Color.white },
            padding   = new RectOffset(14, 14, 8, 8),
            alignment = TextAnchor.MiddleCenter
        };

        smallButton = new GUIStyle(button)
        {
            fontSize = 13,
            normal   = { background = soft,      textColor = new Color(0.85f, 0.92f, 1.0f) },
            hover    = { background = blue,      textColor = Color.white },
            padding  = new RectOffset(10, 10, 5, 5)
        };

        actionBtn = new GUIStyle(button)
        {
            fontSize = 14,
            normal   = { background = tealTex,   textColor = Color.white },
            hover    = { background = cyanTex,   textColor = new Color(0.02f, 0.05f, 0.10f) },
            active   = { background = dark,      textColor = Color.white },
            focused  = { background = tealTex,   textColor = Color.white },
            padding  = new RectOffset(12, 12, 8, 8)
        };

        dangerBtn = new GUIStyle(button)
        {
            fontSize = 14,
            normal   = { background = red,       textColor = Color.white },
            hover    = { background = amber,     textColor = Color.white },
            active   = { background = dark,      textColor = Color.white },
            focused  = { background = red,       textColor = Color.white },
            padding  = new RectOffset(12, 12, 8, 8)
        };

        successBtn = new GUIStyle(button)
        {
            fontSize = 14,
            normal   = { background = green,     textColor = Color.white },
            hover    = { background = cyanTex,   textColor = new Color(0.02f, 0.05f, 0.10f) },
            active   = { background = dark,      textColor = Color.white },
            focused  = { background = green,     textColor = Color.white },
            padding  = new RectOffset(12, 12, 8, 8)
        };

        nav = new GUIStyle(GUI.skin.button)
        {
            alignment = TextAnchor.MiddleLeft,
            fontSize  = 14,
            fontStyle = FontStyle.Bold,
            normal    = { background = dark,     textColor = new Color(0.70f, 0.82f, 0.95f) },
            hover     = { background = blue,     textColor = Color.white },
            active    = { background = green,    textColor = new Color(0.02f, 0.05f, 0.10f) },
            focused   = { background = dark,     textColor = Color.white },
            padding   = new RectOffset(14, 8, 8, 8)
        };

        navActive = new GUIStyle(nav)
        {
            normal = { background = blue, textColor = Color.white }
        };
    }

    // ── Style accessors ───────────────────────────────────────────────────────
    public static GUIStyle Title       { get { Ensure(); return title; } }
    public static GUIStyle H1         { get { Ensure(); return h1; } }
    public static GUIStyle H2         { get { Ensure(); return h2; } }
    public static GUIStyle Body       { get { Ensure(); return body; } }
    public static GUIStyle Muted      { get { Ensure(); return muted; } }
    public static GUIStyle Button     { get { Ensure(); return button; } }
    public static GUIStyle SmallButton{ get { Ensure(); return smallButton; } }
    public static GUIStyle ActionBtn  { get { Ensure(); return actionBtn; } }
    public static GUIStyle DangerBtn  { get { Ensure(); return dangerBtn; } }
    public static GUIStyle SuccessBtn { get { Ensure(); return successBtn; } }
    public static GUIStyle Nav        { get { Ensure(); return nav; } }
    public static GUIStyle NavActive  { get { Ensure(); return navActive; } }
    public static GUIStyle CardTitle  { get { Ensure(); return cardTitle; } }
    public static GUIStyle Value      { get { Ensure(); return value; } }
    public static GUIStyle Badge      { get { Ensure(); return badge; } }
    public static GUIStyle IconLabel  { get { Ensure(); return iconLabel; } }
    public static GUIStyle StatCard   { get { Ensure(); return statCardStyle; } }
    public static GUIStyle ProgressLbl{ get { Ensure(); return progressLabel; } }

    // ── Texture accessors ─────────────────────────────────────────────────────
    public static Texture2D Navy        { get { Ensure(); return navy; } }
    public static Texture2D White       { get { Ensure(); return white; } }
    public static Texture2D Soft        { get { Ensure(); return soft; } }
    public static Texture2D Blue        { get { Ensure(); return blue; } }
    public static Texture2D Green       { get { Ensure(); return green; } }
    public static Texture2D Amber       { get { Ensure(); return amber; } }
    public static Texture2D Red         { get { Ensure(); return red; } }
    public static Texture2D Dark        { get { Ensure(); return dark; } }
    public static Texture2D GlassPanel  { get { Ensure(); return glassPanel; } }
    public static Texture2D GlassDark   { get { Ensure(); return glassDark; } }
    public static Texture2D Transparent { get { Ensure(); return transparent; } }
    public static Texture2D Teal        { get { Ensure(); return tealTex; } }
    public static Texture2D Purple      { get { Ensure(); return purpleTex; } }
    public static Texture2D Orange      { get { Ensure(); return orangeTex; } }
    public static Texture2D Cyan        { get { Ensure(); return cyanTex; } }
    public static Texture2D Indigo      { get { Ensure(); return indigotex; } }
    public static Texture2D Border      { get { Ensure(); return borderTex; } }

    // ── Utility drawing helpers ───────────────────────────────────────────────

    public static void ColorCard(float x, float y, float w, float h, Texture2D col,
                                  string icon, string title, string val)
    {
        GUI.DrawTexture(new Rect(x, y, w, h), col);
        GUI.DrawTexture(new Rect(x, y, w, 2f), Cyan);
        GUI.Label(new Rect(x + 14, y + 8,  w - 28, 22), icon + "  " + title, new GUIStyle(IconLabel) { fontSize = 12 });
        GUI.Label(new Rect(x + 14, y + 30, w - 28, 36), val, StatCard);
    }

    public static void ProgressBar(float x, float y, float w, string label, float pct,
                                    Texture2D barColor = null)
    {
        barColor ??= blue;
        pct = Mathf.Clamp01(pct);
        float barY = y + 22;
        GUI.Label(new Rect(x, y, w - 60, 20), label, new GUIStyle(body) { fontSize = 13 });
        GUI.Label(new Rect(x + w - 58, y, 55, 20), Mathf.RoundToInt(pct * 100) + "%", progressLabel);
        GUI.DrawTexture(new Rect(x, barY, w, 10), soft);
        if (pct > 0f) GUI.DrawTexture(new Rect(x, barY, w * pct, 10), barColor);
    }
}
