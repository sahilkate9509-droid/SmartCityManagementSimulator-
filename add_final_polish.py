with open('content_code_listings.py', 'r', encoding='utf-8') as f:
    text = f.read()

listings_25_27 = '''
    # Listing 5.25: ProgressionSystem.cs
    elements.append(Paragraph("<b>Listing 5.25:</b> Civic Milestone & Municipal Level Scaling (<code>ProgressionSystem.cs</code>)", styles['SecHeading3']))
    code_5_25 = (
        "using UnityEngine;\\n"
        "public class ProgressionSystem : MonoBehaviour {\\n"
        "    public int cityTier = 1;\\n"
        "    public void EvaluateProgression(CityState s) {\\n"
        "        if (s.population >= 10000 && cityTier < 3) {\\n"
        "            cityTier = 3;\\n"
        "            CityHUD.Instance.ShowAlertBanner(\\"METROPOLIS TIER REACHED: High-density zoning unlocked!\\");\\n"
        "        } else if (s.population >= 2500 && cityTier < 2) {\\n"
        "            cityTier = 2;\\n"
        "            CityHUD.Instance.ShowAlertBanner(\\"TOWN TIER REACHED: Solar power plant unlocked!\\");\\n"
        "        }\\n"
        "    }\\n"
        "}"
    )
    elements.append(Preformatted(code_5_25, styles['CodeSnippet']))
    elements.append(make_engine_table(styles, "Civic Progression & Milestone System", "Gameplay Progression Tier", "State Machine / Observer Pattern", "O(1) condition evaluation", "Unlocks New Structures & Building Prefabs"))
    elements.append(Spacer(1, 4))

    # Listing 5.26: AdminLoginUI.cs
    elements.append(Paragraph("<b>Listing 5.26:</b> Administrator Authentication & Form Validation (<code>AdminLoginUI.cs</code>)", styles['SecHeading3']))
    code_5_26 = (
        "using UnityEngine;\\n"
        "using TMPro;\\n"
        "public class AdminLoginUI : MonoBehaviour {\\n"
        "    public TMP_InputField usernameInput, passwordInput;\\n"
        "    public TextMeshProUGUI statusLabel;\\n"
        "    public void OnLoginClicked() {\\n"
        "        string user = usernameInput.text.Trim();\\n"
        "        string pass = passwordInput.text;\\n"
        "        if (string.IsNullOrEmpty(user) || string.IsNullOrEmpty(pass)) {\\n"
        "            statusLabel.text = \\"<color=red>Error: Credentials cannot be empty.</color>\\";\\n"
        "            return;\\n"
        "        }\\n"
        "        CityApiClient.Instance.Authenticate(user, pass);\\n"
        "    }\\n"
        "}"
    )
    elements.append(Preformatted(code_5_26, styles['CodeSnippet']))
    elements.append(make_engine_table(styles, "Admin Login UI Form Controller", "Client UI Presentation Tier", "Form Validation / Event Controller", "O(1) input validation", "Dispatches JWT Authentication Request"))
    elements.append(Spacer(1, 4))

    # Listing 5.27: test_simulation.py
    elements.append(Paragraph("<b>Listing 5.27:</b> Pytest Automated Backend Verification Suite (<code>test_simulation.py</code>)", styles['SecHeading3']))
    code_5_27 = (
        "import pytest\\n"
        "from fastapi.testclient import TestClient\\n"
        "from main import app\\n"
        "client = TestClient(app)\\n"
        "def test_create_city():\\n"
        "    res = client.post(\\"/api/v1/cities\\", json={\\"city_name\\": \\"TestCity\\", \\"mayor_name\\": \\"Tester\\", \\"difficulty\\": \\"Normal\\"})\\n"
        "    assert res.status_code == 201\\n"
        "    assert res.json()[\\"city_name\\"] == \\"TestCity\\"\\n"
        "def test_telemetry_ingest():\\n"
        "    res = client.post(\\"/api/v1/telemetry\\", json={\\"city_id\\": 1, \\"simulation_day\\": 1, \\"treasury_balance\\": 50000.0, \\"population\\": 100, \\"csci_rating\\": 85.0})\\n"
        "    assert res.status_code == 201\\n"
    )
    elements.append(Preformatted(code_5_27, styles['CodeSnippet']))
    elements.append(make_engine_table(styles, "Automated REST API Test Suite", "Backend Quality Assurance Tier", "Automated Fixture / Unit Test Harness", "O(Tests) automated execution", "Validates HTTP Endpoints & Relational Storage"))
    elements.append(Spacer(1, 6))
'''

target = "elements.append(Paragraph(\"<b>Listing 5.24:</b> SQLAlchemy Engine & WAL Pragma Configuration (<code>database.py</code>)\", styles['SecHeading3']))"
if target in text:
    # Find the end of listing 5.24 spacer
    target_spacer = "elements.append(make_engine_table(styles, \"Database Engine & Connection Pool\", \"Backend Database Tier\", \"Singleton Connection Pool / Event Listener\", \"O(1) pool allocation\", \"Enforces SQLite Write-Ahead Logging (WAL)\"))\n    elements.append(Spacer(1, 6))"
    if target_spacer in text:
        text = text.replace(target_spacer, target_spacer + listings_25_27, 1)
        with open('content_code_listings.py', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Injected listings 5.25 to 5.27 into content_code_listings.py.")
