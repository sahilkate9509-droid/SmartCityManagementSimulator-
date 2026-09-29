using UnityEngine;
using UnityEngine.Rendering;

/// <summary>
/// Lighting & Atmosphere Controller:
/// Maintains crisp, vibrant, sunny daylight lighting with rich ambient colors
/// and clear sky for a clean, professional simulation game aesthetic.
/// </summary>
public class DayNightSystem : MonoBehaviour
{
    public Light sun;
    public float cycleSeconds = 300f;
    public float timeOfDay = 0.28f; // Bright sunny morning/noon

    // ── Bright Sunny Atmosphere Colors ────────────────────────────────────────
    static readonly Color ClearSkyColor    = new Color(0.42f, 0.70f, 0.96f); // Crisp sky blue
    static readonly Color BrightSunColor   = new Color(1.00f, 0.98f, 0.92f); // Warm natural sunlight
    static readonly Color SkyAmbientColor  = new Color(0.65f, 0.78f, 0.92f); // Clean skylight
    static readonly Color EquatorAmbient   = new Color(0.70f, 0.74f, 0.78f);
    static readonly Color GroundAmbient    = new Color(0.35f, 0.44f, 0.32f); // Lush ground bounce

    Camera mainCam;

    void Start()
    {
        mainCam = Camera.main;

        if (mainCam != null)
        {
            mainCam.clearFlags = CameraClearFlags.SolidColor;
            mainCam.backgroundColor = ClearSkyColor;
        }

        if (sun == null)
        {
            var l = FindFirstObjectByType<Light>();
            if (l != null && l.type == LightType.Directional) sun = l;
        }

        if (sun != null)
        {
            sun.type = LightType.Directional;
            sun.color = BrightSunColor;
            sun.intensity = 1.35f;
            sun.shadows = LightShadows.Soft;
            sun.shadowResolution = LightShadowResolution.VeryHigh;
            sun.shadowBias = 0.03f;
            sun.shadowNormalBias = 0.3f;
            sun.shadowStrength = 0.65f;
            sun.transform.rotation = Quaternion.Euler(50f, 140f, 0f);
        }

        QualitySettings.shadowDistance = 400f;
        QualitySettings.shadowCascades = 4;
        QualitySettings.shadowProjection = ShadowProjection.CloseFit;

        // Tri-light ambient for bright, balanced visibility
        RenderSettings.ambientMode = AmbientMode.Trilight;
        RenderSettings.ambientSkyColor = SkyAmbientColor;
        RenderSettings.ambientEquatorColor = EquatorAmbient;
        RenderSettings.ambientGroundColor = GroundAmbient;
        
        // Soft atmospheric distance haze that blends distant mountains and sky smoothly
        RenderSettings.fog = true;
        RenderSettings.fogMode = FogMode.Exponential;
        RenderSettings.fogDensity = 0.00075f;
        RenderSettings.fogColor = new Color(0.55f, 0.74f, 0.94f);
    }

    void Update()
    {
        if (sun == null) return;

        // Maintain bright, clean sun and sky at all times
        if (mainCam != null && mainCam.backgroundColor != ClearSkyColor)
        {
            mainCam.backgroundColor = ClearSkyColor;
        }
        if (sun.intensity < 1.1f)
        {
            sun.intensity = 1.35f;
            sun.color = BrightSunColor;
        }
    }
}
