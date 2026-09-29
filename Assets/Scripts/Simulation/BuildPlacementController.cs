using System.Collections.Generic;
using UnityEngine;

/// <summary>
/// Click-to-place controller for buildings and city decorations.
///
/// Flow:
///   1. CityHUD calls EnterPlacementMode / EnterDecorationMode when player clicks BUILD / PLACE.
///   2. A coloured ghost box appears on the terrain following the mouse, snapped to a 20-unit grid.
///   3. Ghost is GREEN when the cell is free, RED when occupied.
///   4. Left-click on a free cell confirms placement.
///   5. Escape or Right-click cancels without spending budget.
/// </summary>
public class BuildPlacementController : MonoBehaviour
{
    public static BuildPlacementController Instance { get; private set; }

    // Grid occupancy — keyed by (x / CellSize, z / CellSize)
    readonly HashSet<Vector2Int> occupiedCells = new();

    // Placement state
    bool isPlacing;
    bool isDecoration;
    Building.Kind pendingKind;
    string pendingDecoration;
    float pendingCost;

    // Ghost visuals
    GameObject ghost;
    Material matFree;     // bright green — cell is clear
    Material matBlocked;  // bright red   — cell is taken

    const float CellSize = 20f;

    public bool IsPlacing => isPlacing;

    // ── Lifecycle ────────────────────────────────────────────────────────────

    void Awake() { Instance = this; }

    void Start()
    {
        matFree    = BuildMat(new Color(0.10f, 0.92f, 0.22f));
        matBlocked = BuildMat(new Color(0.92f, 0.12f, 0.12f));
    }

    static Material BuildMat(Color c)
    {
        var sh = CityWorldBuilder.GetDefaultShader();
        var m = sh != null ? new Material(sh) : new Material(Shader.Find("Sprites/Default"));
        m.color = c;
        if (m.HasProperty("_BaseColor")) m.SetColor("_BaseColor", c);
        if (m.HasProperty("_EmissionColor"))
        {
            m.EnableKeyword("_EMISSION");
            m.SetColor("_EmissionColor", c * 0.4f);
        }
        return m;
    }

    // ── Update: ghost tracking ────────────────────────────────────────────────

    void Update()
    {
        if (!isPlacing) return;

        // Cancel
        if (Input.GetKeyDown(KeyCode.Escape) || Input.GetMouseButtonDown(1))
        { CancelPlacement(); return; }

        if (Camera.main == null || ghost == null) return;

        // Don't process when mouse is over the sidebar or top bar
        if (Input.mousePosition.x < 230f || Input.mousePosition.y > Screen.height - 68) return;

        Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
        if (!Physics.Raycast(ray, out RaycastHit hit, 600f)) return;

        // Snap to CellSize grid
        float sx = Mathf.Round(hit.point.x / CellSize) * CellSize;
        float sz = Mathf.Round(hit.point.z / CellSize) * CellSize;
        var snapPos = new Vector3(sx, hit.point.y, sz);

        bool free = !occupiedCells.Contains(WorldToCell(snapPos));

        ghost.transform.position = snapPos + Vector3.up * GhostYOffset();
        ApplyGhostMat(free ? matFree : matBlocked);

        // Confirm on left-click
        if (Input.GetMouseButtonDown(0) && free)
            ConfirmPlacement(snapPos);
    }

    // ── Ghost helpers ─────────────────────────────────────────────────────────

    float GhostYOffset()
    {
        if (isDecoration) return 2f;
        return pendingKind switch
        {
            Building.Kind.Residential => 5f,
            Building.Kind.Commercial  => 12f,
            Building.Kind.Industrial  => 4f,
            Building.Kind.Park        => 0.5f,
            Building.Kind.Hospital    => 3.2f,
            Building.Kind.School      => 2.8f,
            Building.Kind.Police      => 2.7f,
            Building.Kind.Fire        => 2.6f,
            Building.Kind.Power       => 4.0f,
            Building.Kind.Water       => 3.0f,
            Building.Kind.Recycling   => 2.5f,
            _ => 3f
        };
    }

    Vector3 GhostScale()
    {
        if (isDecoration) return new Vector3(4f, 3f, 4f);
        return pendingKind switch
        {
            Building.Kind.Residential => new Vector3(14f, 10f, 14f),
            Building.Kind.Commercial  => new Vector3(7f, 24f, 7f),
            Building.Kind.Industrial  => new Vector3(8f,  8f, 8f),
            Building.Kind.Park        => new Vector3(14f,  1f, 14f),
            _ => new Vector3(10f, 6f, 9f)
        };
    }

    void ApplyGhostMat(Material m)
    {
        foreach (var r in ghost.GetComponentsInChildren<Renderer>(true))
            r.material = m;
    }

    void SpawnGhost(Vector3 scale)
    {
        if (ghost != null) Destroy(ghost);
        ghost = GameObject.CreatePrimitive(PrimitiveType.Cube);
        ghost.name = "PlacementGhost";
        ghost.transform.localScale = scale;
        // Remove collider so the ghost doesn't block raycasts to the terrain
        var col = ghost.GetComponent<Collider>();
        if (col) Destroy(col);
        ApplyGhostMat(matFree);
    }

    // ── Placement logic ───────────────────────────────────────────────────────

    void ConfirmPlacement(Vector3 pos)
    {
        // Lock the cell immediately
        occupiedCells.Add(WorldToCell(pos));

        if (isDecoration)
            ConstructionSystem.Instance?.BuildDecoration(pendingDecoration, pos);
        else
            ConstructionSystem.Instance?.Build(pendingKind, pos);

        if (ghost != null) { Destroy(ghost); ghost = null; }
        isPlacing = false;
    }

    // ── Public API ────────────────────────────────────────────────────────────

    /// <summary>Enter placement mode for a city building.</summary>
    public void EnterPlacementMode(Building.Kind kind, float cost)
    {
        if (isPlacing) CancelPlacement();
        pendingKind = kind; pendingCost = cost;
        isDecoration = false; isPlacing = true;
        SpawnGhost(GhostScale());
    }

    /// <summary>Enter placement mode for a city decoration.</summary>
    public void EnterDecorationMode(string type, float cost)
    {
        if (isPlacing) CancelPlacement();
        pendingDecoration = type; pendingCost = cost;
        isDecoration = true; isPlacing = true;
        SpawnGhost(new Vector3(4f, 3f, 4f));
    }

    /// <summary>Cancel placement without spending budget.</summary>
    public void CancelPlacement()
    {
        isPlacing = false;
        if (ghost != null) { Destroy(ghost); ghost = null; }
    }

    /// <summary>
    /// Mark a world-space position as occupied so the grid correctly blocks overlaps.
    /// Called by CityWorldBuilder for every object placed in BuildStarterCity().
    /// </summary>
    public void RegisterOccupied(Vector3 worldPos)
        => occupiedCells.Add(WorldToCell(worldPos));

    static Vector2Int WorldToCell(Vector3 p)
        => new Vector2Int(
            Mathf.RoundToInt(p.x / CellSize),
            Mathf.RoundToInt(p.z / CellSize));
}
