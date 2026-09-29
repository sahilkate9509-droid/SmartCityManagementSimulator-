#if UNITY_EDITOR
using UnityEditor; using UnityEditor.SceneManagement; using UnityEngine; using UnityEngine.SceneManagement;
[InitializeOnLoad]
public static class SmartCityProjectBuilder
{
 const string Key="SmartCityProfessionalBuilt_v10";
 static SmartCityProjectBuilder(){EditorApplication.delayCall+=Auto;}
 static void Auto(){if(EditorPrefs.GetBool(Key,false))return;BuildAll();EditorPrefs.SetBool(Key,true);}
 [MenuItem("Tools/Smart City/Rebuild Professional Project")]
 public static void BuildAll(){EnsureFolders();BuildMainMenu();BuildLogin();BuildCreate();BuildInfo("Instructions","Instructions");BuildInfo("Settings","Settings");BuildSimulation();EditorBuildSettings.scenes=new[]{S("MainMenu"),S("AdminLogin"),S("CreateCity"),S("CitySimulation"),S("Instructions"),S("Settings")};EditorSceneManager.OpenScene("Assets/Scenes/MainMenu.unity");Debug.Log("Smart City Professional project scenes rebuilt successfully.");}
 static EditorBuildSettingsScene S(string n)=>new EditorBuildSettingsScene("Assets/Scenes/"+n+".unity",true);
 static void EnsureFolders(){if(!AssetDatabase.IsValidFolder("Assets/Scenes"))AssetDatabase.CreateFolder("Assets","Scenes");}
 static void Base(string name,out Scene scene){scene=EditorSceneManager.NewScene(NewSceneSetup.EmptyScene,NewSceneMode.Single);var mgr=new GameObject("CityManager");mgr.AddComponent<CityManager>();if(name!="CitySimulation"){var cam=new GameObject("Main Camera");cam.tag="MainCamera";var c=cam.AddComponent<Camera>();c.clearFlags=CameraClearFlags.SolidColor;c.backgroundColor=new Color(.035f,.075f,.105f);cam.AddComponent<AudioListener>();}}
 static void BuildMainMenu(){Base("MainMenu",out var s);new GameObject("MainMenuUI").AddComponent<MainMenuUI>();Save(s,"MainMenu");}
 static void BuildLogin(){Base("AdminLogin",out var s);new GameObject("AdminLoginUI").AddComponent<AdminLoginUI>();Save(s,"AdminLogin");}
 static void BuildCreate(){Base("CreateCity",out var s);new GameObject("CreateCityUI").AddComponent<CreateCityUI>();Save(s,"CreateCity");}
 static void BuildInfo(string sceneName,string title){Base(sceneName,out var s);var i=new GameObject("InfoUI").AddComponent<SimpleInfoUI>();i.title=title;if(title=="Settings")i.body="Settings\n\n• Simulation speed is controlled from the in-game top bar.\n• Resolution and quality can be changed from Unity's launcher/player settings.\n• Backend URL defaults to http://127.0.0.1:8000.\n\nMore audio and graphics options can be added as assets are introduced.";Save(s,sceneName);}
 static void BuildSimulation(){Base("CitySimulation",out var s);new GameObject("CitizenRequestSystem").AddComponent<CitizenRequestSystem>();new GameObject("ConstructionSystem").AddComponent<ConstructionSystem>();new GameObject("CityWorldBuilder").AddComponent<CityWorldBuilder>();new GameObject("WeatherSystem").AddComponent<WeatherSystem>();new GameObject("CityHUD").AddComponent<CityHUD>();new GameObject("ApiClient").AddComponent<CityApiClient>();var sun=new GameObject("Sun").AddComponent<Light>();sun.type=LightType.Directional;sun.intensity=1.1f;sun.transform.rotation=Quaternion.Euler(48,155,0);var dns=new GameObject("DayNightSystem").AddComponent<DayNightSystem>();dns.sun=sun;var cam=new GameObject("Main Camera");cam.tag="MainCamera";cam.AddComponent<Camera>();cam.AddComponent<AudioListener>();cam.AddComponent<CityCameraController>();cam.transform.position=new Vector3(-34,38,-43);cam.transform.rotation=Quaternion.Euler(34,38,0);RenderSettings.ambientLight=new Color(.55f,.62f,.70f);RenderSettings.fog=false;Save(s,"CitySimulation");}
 static void Save(Scene s,string n){EditorSceneManager.SaveScene(s,"Assets/Scenes/"+n+".unity");}
}
#endif

