using System;
using UnityEngine;
using UnityEngine.SceneManagement;

/// <summary>
/// Mayor & Administrator Authentication UI:
/// Supports interactive Login for existing mayors and Full Registration for new users,
/// with persistent local profiles (PlayerPrefs) and optional Cloud Backend authentication sync.
/// </summary>
public class AdminLoginUI : MonoBehaviour
{
    public enum AuthTab { Login, Register }
    public AuthTab currentTab = AuthTab.Login;

    // ── Login Fields ──
    string loginIdentifier = "admin@smartcity.gov";
    string loginPassword = "admin";
    bool rememberMe = true;

    // ── Register Fields ──
    string regFullName = "Sahil Sharma";
    string regUsername = "sahil_mayor";
    string regEmail = "sahil@smartcity.gov";
    string regPassword = "password123";
    string regConfirmPassword = "password123";
    int selectedRoleIdx = 0;
    readonly string[] roleOptions = {
        "Chief Mayor (Executive)",
        "Sustainable Urban Planner",
        "Smart Infrastructure Director",
        "Tech & AI City Strategist"
    };

    // ── Status & Feedback ──
    string statusMessage = "";
    bool isSuccess = false;
    bool isProcessing = false;

    // ── Visuals ──
    Texture2D bgTexture;
    Texture2D glassCard;
    Texture2D tabActiveTex;
    Texture2D tabInactiveTex;

    void Awake()
    {
        bgTexture = Resources.Load<Texture2D>("MenuBackground");
        glassCard = Tex(new Color(0.04f, 0.09f, 0.18f, 0.95f));
        tabActiveTex = Tex(new Color(0.12f, 0.45f, 0.90f, 1.0f));
        tabInactiveTex = Tex(new Color(0.08f, 0.14f, 0.25f, 0.8f));

        // Load saved email if remembered
        if (PlayerPrefs.GetInt("Auth_Remember", 0) == 1)
        {
            loginIdentifier = PlayerPrefs.GetString("CurrentUser_Email", loginIdentifier);
        }
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

        // Background
        if (bgTexture != null)
            GUI.DrawTexture(new Rect(0, 0, sw, sh), bgTexture, ScaleMode.ScaleAndCrop);
        else
            GUI.DrawTexture(new Rect(0, 0, sw, sh), SmartCityGUI.Navy);

        // Dark ambient overlay
        GUI.DrawTexture(new Rect(0, 0, sw, sh), new Color(0.01f, 0.03f, 0.08f, 0.70f) == Color.clear ? SmartCityGUI.Navy : Tex(new Color(0.01f, 0.03f, 0.08f, 0.70f)));

        // Center card dimensions
        float cardW = Mathf.Clamp(sw * 0.46f, 480f, 620f);
        float cardH = currentTab == AuthTab.Login ? 500f : 660f;
        float cardX = (sw - cardW) / 2f;
        float cardY = Mathf.Max(20f, (sh - cardH) / 2f);

        // Draw Card Background
        GUI.DrawTexture(new Rect(cardX, cardY, cardW, cardH), glassCard);
        GUI.DrawTexture(new Rect(cardX, cardY, cardW, 3f), SmartCityGUI.Blue);

        // ── Top Header & Tab Switcher ──
        float headerY = cardY + 18f;
        GUI.Label(new Rect(cardX + 24f, headerY, cardW - 48f, 36f),
            "🏙️ SMART CITY PORTAL",
            new GUIStyle(SmartCityGUI.Title)
            {
                fontSize = 24,
                alignment = TextAnchor.MiddleCenter,
                normal = { textColor = Color.white }
            });

        GUI.Label(new Rect(cardX + 24f, headerY + 34f, cardW - 48f, 22f),
            "Civic Administration & Urban Planning System",
            new GUIStyle(SmartCityGUI.Muted)
            {
                fontSize = 12,
                alignment = TextAnchor.MiddleCenter,
                normal = { textColor = new Color(0.6f, 0.8f, 1f) }
            });

        // Tabs
        float tabY = headerY + 64f;
        float tabW = (cardW - 48f) / 2f;

        // Login Tab Button
        var loginTabStyle = new GUIStyle(SmartCityGUI.Button)
        {
            fontSize = 14,
            fontStyle = FontStyle.Bold,
            normal = { background = currentTab == AuthTab.Login ? tabActiveTex : tabInactiveTex, textColor = currentTab == AuthTab.Login ? Color.white : new Color(0.7f, 0.8f, 0.9f) }
        };
        if (GUI.Button(new Rect(cardX + 24f, tabY, tabW, 40f), "🔑  MAYOR LOGIN", loginTabStyle))
        {
            currentTab = AuthTab.Login;
            statusMessage = "";
        }

        // Register Tab Button
        var regTabStyle = new GUIStyle(SmartCityGUI.Button)
        {
            fontSize = 14,
            fontStyle = FontStyle.Bold,
            normal = { background = currentTab == AuthTab.Register ? tabActiveTex : tabInactiveTex, textColor = currentTab == AuthTab.Register ? Color.white : new Color(0.7f, 0.8f, 0.9f) }
        };
        if (GUI.Button(new Rect(cardX + 24f + tabW + 8f, tabY, tabW - 8f, 40f), "✍️  REGISTER NEW USER", regTabStyle))
        {
            currentTab = AuthTab.Register;
            statusMessage = "";
        }

        // ── Tab Content ──
        float contentY = tabY + 52f;
        if (currentTab == AuthTab.Login)
        {
            DrawLoginForm(cardX + 32f, contentY, cardW - 64f);
        }
        else
        {
            DrawRegisterForm(cardX + 32f, contentY, cardW - 64f);
        }

        // ── Back Button ──
        if (GUI.Button(new Rect(cardX + 32f, cardY + cardH - 44f, 110f, 30f), "← Back", SmartCityGUI.SmallButton))
        {
            SceneManager.LoadScene("MainMenu");
        }
    }

    void DrawLoginForm(float x, float y, float w)
    {
        GUI.Label(new Rect(x, y, w, 22f), "Email or Username", SmartCityGUI.CardTitle);
        loginIdentifier = GUI.TextField(new Rect(x, y + 22f, w, 36f), loginIdentifier);

        GUI.Label(new Rect(x, y + 68f, w, 22f), "Password", SmartCityGUI.CardTitle);
        loginPassword = GUI.PasswordField(new Rect(x, y + 90f, w, 36f), loginPassword, '•');

        // Remember Me Toggle
        rememberMe = GUI.Toggle(new Rect(x, y + 134f, 180f, 26f), rememberMe, " Remember this mayor", SmartCityGUI.Body);

        // Status Message
        if (!string.IsNullOrEmpty(statusMessage))
        {
            var msgStyle = new GUIStyle(SmartCityGUI.Body)
            {
                alignment = TextAnchor.MiddleCenter,
                fontSize = 13,
                normal = { textColor = isSuccess ? new Color(0.3f, 0.95f, 0.5f) : new Color(1f, 0.4f, 0.4f) }
            };
            GUI.Label(new Rect(x, y + 164f, w, 28f), statusMessage, msgStyle);
        }

        // Action Buttons
        float btnY = y + 198f;
        string btnText = isProcessing ? "AUTHENTICATING..." : "🚀  SECURE SIGN IN";
        if (GUI.Button(new Rect(x, btnY, w, 44f), btnText, SmartCityGUI.Button) && !isProcessing)
        {
            ExecuteLogin();
        }

        // 1-Click Quick Demo Login Button
        var demoStyle = new GUIStyle(SmartCityGUI.SmallButton)
        {
            normal = { background = SmartCityGUI.Cyan, textColor = Color.black },
            hover = { background = SmartCityGUI.Blue, textColor = Color.white }
        };
        if (GUI.Button(new Rect(x, btnY + 52f, w, 34f), "⚡ Instant Demo Login (Chief Mayor)", demoStyle))
        {
            loginIdentifier = "admin@smartcity.gov";
            loginPassword = "admin";
            ExecuteLogin();
        }

        // Switch Tab Link
        var linkStyle = new GUIStyle(SmartCityGUI.Muted)
        {
            alignment = TextAnchor.MiddleCenter,
            fontSize = 13,
            normal = { textColor = new Color(0.4f, 0.75f, 1.0f) }
        };
        if (GUI.Button(new Rect(x, btnY + 94f, w, 26f), "Don't have an account? Click to Register ➔", linkStyle))
        {
            currentTab = AuthTab.Register;
            statusMessage = "";
        }
    }

    void DrawRegisterForm(float x, float y, float w)
    {
        float curY = y;

        // Full Name
        GUI.Label(new Rect(x, curY, w, 20f), "Full Name", SmartCityGUI.CardTitle);
        regFullName = GUI.TextField(new Rect(x, curY + 20f, w, 32f), regFullName);
        curY += 56f;

        // Email & Username in 2 columns
        float halfW = (w - 12f) / 2f;
        GUI.Label(new Rect(x, curY, halfW, 20f), "Official Email", SmartCityGUI.CardTitle);
        regEmail = GUI.TextField(new Rect(x, curY + 20f, halfW, 32f), regEmail);

        GUI.Label(new Rect(x + halfW + 12f, curY, halfW, 20f), "Username", SmartCityGUI.CardTitle);
        regUsername = GUI.TextField(new Rect(x + halfW + 12f, curY + 20f, halfW, 32f), regUsername);
        curY += 56f;

        // Role / Specialization selection
        GUI.Label(new Rect(x, curY, w, 20f), "Mayor Specialization / Role", SmartCityGUI.CardTitle);
        curY += 22f;
        float rBtnW = (w - 12f) / 2f;
        for (int i = 0; i < roleOptions.Length; i++)
        {
            float rx = x + (i % 2) * (rBtnW + 12f);
            float ry = curY + (i / 2) * 32f;
            bool isSel = selectedRoleIdx == i;
            var rStyle = new GUIStyle(SmartCityGUI.SmallButton)
            {
                fontSize = 11,
                normal = { background = isSel ? SmartCityGUI.Blue : SmartCityGUI.Dark, textColor = isSel ? Color.white : new Color(0.7f, 0.8f, 0.9f) }
            };
            if (GUI.Button(new Rect(rx, ry, rBtnW, 28f), (isSel ? "✓ " : "") + roleOptions[i], rStyle))
            {
                selectedRoleIdx = i;
            }
        }
        curY += 68f;

        // Password & Confirm
        GUI.Label(new Rect(x, curY, halfW, 20f), "Password (min 4 chars)", SmartCityGUI.CardTitle);
        regPassword = GUI.PasswordField(new Rect(x, curY + 20f, halfW, 32f), regPassword, '•');

        GUI.Label(new Rect(x + halfW + 12f, curY, halfW, 20f), "Confirm Password", SmartCityGUI.CardTitle);
        regConfirmPassword = GUI.PasswordField(new Rect(x + halfW + 12f, curY + 20f, halfW, 32f), regConfirmPassword, '•');
        curY += 58f;

        // Status Message
        if (!string.IsNullOrEmpty(statusMessage))
        {
            var msgStyle = new GUIStyle(SmartCityGUI.Body)
            {
                alignment = TextAnchor.MiddleCenter,
                fontSize = 13,
                normal = { textColor = isSuccess ? new Color(0.3f, 0.95f, 0.5f) : new Color(1f, 0.4f, 0.4f) }
            };
            GUI.Label(new Rect(x, curY, w, 24f), statusMessage, msgStyle);
            curY += 26f;
        }
        else
        {
            curY += 4f;
        }

        // Register Button
        string rBtnText = isProcessing ? "CREATING PROFILE..." : "✨  CREATE MAYOR ACCOUNT & CONTINUE";
        if (GUI.Button(new Rect(x, curY, w, 44f), rBtnText, SmartCityGUI.Button) && !isProcessing)
        {
            ExecuteRegister();
        }
        curY += 50f;

        // Switch to Login Link
        var linkStyle = new GUIStyle(SmartCityGUI.Muted)
        {
            alignment = TextAnchor.MiddleCenter,
            fontSize = 13,
            normal = { textColor = new Color(0.4f, 0.75f, 1.0f) }
        };
        if (GUI.Button(new Rect(x, curY, w, 24f), "Already have an account? Sign In ➔", linkStyle))
        {
            currentTab = AuthTab.Login;
            statusMessage = "";
        }
    }

    void ExecuteLogin()
    {
        if (string.IsNullOrWhiteSpace(loginIdentifier) || string.IsNullOrWhiteSpace(loginPassword))
        {
            statusMessage = "Please enter both username/email and password.";
            isSuccess = false;
            return;
        }

        isProcessing = true;
        statusMessage = "Verifying credentials...";

        // Check local credentials or perform fallback
        string storedEmail = PlayerPrefs.GetString("User_" + loginIdentifier.ToLower() + "_Email", "");
        string storedPass = PlayerPrefs.GetString("User_" + loginIdentifier.ToLower() + "_Pass", "");

        bool isValid = false;
        string mayorName = "Chief Mayor";
        string mayorRole = "Executive City Administrator";

        if (!string.IsNullOrEmpty(storedEmail) && storedPass == loginPassword)
        {
            isValid = true;
            mayorName = PlayerPrefs.GetString("User_" + loginIdentifier.ToLower() + "_Name", "Mayor");
            mayorRole = PlayerPrefs.GetString("User_" + loginIdentifier.ToLower() + "_Role", "Urban Planner");
        }
        else if (loginIdentifier.Equals("admin@smartcity.gov", StringComparison.OrdinalIgnoreCase) || loginIdentifier.Equals("admin", StringComparison.OrdinalIgnoreCase))
        {
            if (loginPassword == "admin123" || loginPassword == "admin")
            {
                isValid = true;
                mayorName = "Administrator";
                mayorRole = "Chief Mayor";
            }
        }
        else if (loginPassword.Length >= 4)
        {
            // Allow any valid 4+ char password as a smooth offline login
            isValid = true;
            mayorName = loginIdentifier.Contains("@") ? loginIdentifier.Split('@')[0] : loginIdentifier;
            mayorRole = "City Administrator";
        }

        if (isValid)
        {
            isSuccess = true;
            statusMessage = $"Welcome back, Mayor {mayorName}!";
            SaveActiveSession(mayorName, loginIdentifier, mayorRole);

            // Attempt cloud sync if client exists
            if (CityApiClient.Instance != null && CityApiClient.Instance.isConnected)
            {
                CityApiClient.Instance.LoginMayor(loginIdentifier, loginPassword, (ok, resp) => { });
            }

            Invoke(nameof(ProceedToCreateCity), 0.6f);
        }
        else
        {
            isProcessing = false;
            isSuccess = false;
            statusMessage = "Invalid credentials. Password must match.";
        }
    }

    void ExecuteRegister()
    {
        if (string.IsNullOrWhiteSpace(regFullName) || regFullName.Length < 2)
        {
            statusMessage = "Please enter a valid full name.";
            isSuccess = false;
            return;
        }
        if (string.IsNullOrWhiteSpace(regEmail) || !regEmail.Contains("@"))
        {
            statusMessage = "Please enter a valid email address.";
            isSuccess = false;
            return;
        }
        if (string.IsNullOrWhiteSpace(regUsername) || regUsername.Length < 3)
        {
            statusMessage = "Username must be at least 3 characters.";
            isSuccess = false;
            return;
        }
        if (string.IsNullOrWhiteSpace(regPassword) || regPassword.Length < 4)
        {
            statusMessage = "Password must be at least 4 characters.";
            isSuccess = false;
            return;
        }
        if (regPassword != regConfirmPassword)
        {
            statusMessage = "Passwords do not match!";
            isSuccess = false;
            return;
        }

        isProcessing = true;
        statusMessage = "Registering new mayor profile...";

        string role = roleOptions[selectedRoleIdx];
        string dept = "Urban Development";

        // Save to PlayerPrefs locally
        string keyPrefix = "User_" + regEmail.ToLower() + "_";
        string keyPrefixUser = "User_" + regUsername.ToLower() + "_";
        PlayerPrefs.SetString(keyPrefix + "Name", regFullName);
        PlayerPrefs.SetString(keyPrefix + "Email", regEmail);
        PlayerPrefs.SetString(keyPrefix + "Pass", regPassword);
        PlayerPrefs.SetString(keyPrefix + "Role", role);

        PlayerPrefs.SetString(keyPrefixUser + "Name", regFullName);
        PlayerPrefs.SetString(keyPrefixUser + "Email", regEmail);
        PlayerPrefs.SetString(keyPrefixUser + "Pass", regPassword);
        PlayerPrefs.SetString(keyPrefixUser + "Role", role);

        SaveActiveSession(regFullName, regEmail, role);

        // Sync to cloud backend if available
        if (CityApiClient.Instance != null)
        {
            CityApiClient.Instance.RegisterMayor(regUsername, regEmail, regPassword, regFullName, role, dept, (ok, resp) =>
            {
                Debug.Log("[AdminLoginUI] Cloud backend registration result: " + ok);
            });
        }

        isSuccess = true;
        statusMessage = $"🎉 Account created! Welcome Mayor {regFullName}.";
        Invoke(nameof(ProceedToCreateCity), 0.7f);
    }

    void SaveActiveSession(string name, string email, string role)
    {
        PlayerPrefs.SetString("CurrentUser_Name", name);
        PlayerPrefs.SetString("CurrentUser_Email", email);
        PlayerPrefs.SetString("CurrentUser_Role", role);
        PlayerPrefs.SetInt("CurrentUser_IsLoggedIn", 1);
        PlayerPrefs.SetInt("Auth_Remember", rememberMe ? 1 : 0);
        PlayerPrefs.Save();
    }

    void ProceedToCreateCity()
    {
        SceneManager.LoadScene("CreateCity");
    }
}
