using UnityEngine;

/// <summary>
/// Animates river surface texture coordinates to simulate real flowing water and sunlight ripples.
/// </summary>
public class RiverWaterFlow : MonoBehaviour
{
    Renderer rend;

    void Start()
    {
        rend = GetComponent<Renderer>();
    }

    void Update()
    {
        if (rend != null && rend.material != null)
        {
            float u = Time.time * 0.05f;
            float v = Mathf.Sin(Time.time * 0.8f) * 0.02f;
            rend.material.mainTextureOffset = new Vector2(u, v);
        }
    }
}
