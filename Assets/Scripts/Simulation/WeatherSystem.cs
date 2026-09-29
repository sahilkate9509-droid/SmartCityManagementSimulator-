using UnityEngine;

public class WeatherSystem : MonoBehaviour
{
    public enum Weather { Clear, Cloudy, Rain, Fog, Storm }
    public Weather current = Weather.Clear;
    float timer = 35f;

    void Start()
    {
        ApplyWeather();
    }

    void Update()
    {
        timer -= Time.deltaTime;
        if (timer > 0) return;
        timer = Random.Range(35f, 70f);
        current = (Weather)Random.Range(0, 5);
        ApplyWeather();
        if (CityManager.Instance) CityManager.Instance.Raise("Weather update: " + current, current == Weather.Storm ? CityManager.AlertLevel.Warning : CityManager.AlertLevel.Info);
    }

    void ApplyWeather()
    {
        RenderSettings.fog = true;
        RenderSettings.fogMode = FogMode.Linear;

        switch (current)
        {
            case Weather.Fog:
                RenderSettings.fogStartDistance = 50f;
                RenderSettings.fogEndDistance   = 240f;
                RenderSettings.fogColor = new Color(0.72f, 0.78f, 0.86f);
                break;
            case Weather.Storm:
                RenderSettings.fogStartDistance = 35f;
                RenderSettings.fogEndDistance   = 190f;
                RenderSettings.fogColor = new Color(0.32f, 0.38f, 0.46f);
                break;
            case Weather.Rain:
                RenderSettings.fogStartDistance = 75f;
                RenderSettings.fogEndDistance   = 270f;
                RenderSettings.fogColor = new Color(0.52f, 0.60f, 0.68f);
                break;
            default: // Clear / Cloudy
                RenderSettings.fogStartDistance = 140f;
                RenderSettings.fogEndDistance   = 360f;
                RenderSettings.fogColor = new Color(0.50f, 0.68f, 0.85f);
                break;
        }
    }
}
