using UnityEngine;

/// <summary>
/// Controls autonomous road vehicle movement, wheel spinning, and avenue looping.
/// </summary>
public class TrafficVehicle : MonoBehaviour
{
    public Vector3 direction = Vector3.forward;
    public float speed = 16f;
    public float min = -205f;
    public float max = 205f;

    Transform[] wheels;

    void Start()
    {
        var list = new System.Collections.Generic.List<Transform>();
        foreach (Transform child in transform)
        {
            if (child.name.StartsWith("Wheel"))
                list.Add(child);
        }
        wheels = list.ToArray();
    }

    void Update()
    {
        float efficiency = CityManager.Instance ? CityManager.Instance.State.trafficEfficiency / 100f : 1f;
        float currentSpeed = speed * Mathf.Lerp(0.50f, 1.20f, efficiency);

        transform.position += direction.normalized * currentSpeed * Time.deltaTime;

        if (direction != Vector3.zero)
            transform.rotation = Quaternion.LookRotation(direction);

        // Spin wheels
        if (wheels != null && wheels.Length > 0)
        {
            float rotAngle = (currentSpeed / 0.35f) * Mathf.Rad2Deg * Time.deltaTime;
            for (int i = 0; i < wheels.Length; i++)
            {
                if (wheels[i] != null)
                    wheels[i].Rotate(Vector3.forward, rotAngle, Space.Self);
            }
        }

        // Loop boundaries across the avenue network
        if (direction.z > 0 && transform.position.z > max)
            transform.position = new Vector3(transform.position.x, transform.position.y, min);
        else if (direction.z < 0 && transform.position.z < min)
            transform.position = new Vector3(transform.position.x, transform.position.y, max);

        if (direction.x > 0 && transform.position.x > max)
            transform.position = new Vector3(min, transform.position.y, transform.position.z);
        else if (direction.x < 0 && transform.position.x < min)
            transform.position = new Vector3(max, transform.position.y, transform.position.z);
    }
}

/// <summary>
/// Controls autonomous aerial drone flight and gentle hover motion.
/// </summary>
public class SkyDroneFlight : MonoBehaviour
{
    public Vector3 direction = Vector3.forward;
    public float speed = 18f;
    public float min = -210f;
    public float max = 210f;
    float startY;
    float seed;

    void Start()
    {
        startY = transform.position.y;
        seed = Random.Range(0f, 100f);
    }

    void Update()
    {
        float hover = Mathf.Sin(Time.time * 2.5f + seed) * 0.8f;
        transform.position += direction.normalized * speed * Time.deltaTime;
        transform.position = new Vector3(transform.position.x, startY + hover, transform.position.z);

        if (direction.z > 0 && transform.position.z > max)
            transform.position = new Vector3(transform.position.x, startY, min);
        else if (direction.z < 0 && transform.position.z < min)
            transform.position = new Vector3(transform.position.x, startY, max);

        if (direction.x > 0 && transform.position.x > max)
            transform.position = new Vector3(min, startY, transform.position.z);
        else if (direction.x < 0 && transform.position.x < min)
            transform.position = new Vector3(max, startY, transform.position.z);
    }
}
