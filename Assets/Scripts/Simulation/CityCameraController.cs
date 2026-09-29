using UnityEngine;

/// <summary>
/// City camera controller.
///
/// Controls:
///   WASD / Arrow keys   — pan (horizontal plane)
///   Mouse Scroll        — zoom forward/back
///   Right Mouse Drag    — rotate (yaw + pitch)
///   Middle Mouse Drag   — pan (drag-to-pan, works without keyboard focus)
///   Shift               — 2.5× speed multiplier
///   High/Med/Low buttons— snap camera to preset height
/// </summary>
public class CityCameraController : MonoBehaviour
{
    public float moveSpeed   = 35f;
    public float rotateSpeed = 90f;
    public float zoomSpeed   = 280f;

    public static Building SelectedBuilding { get; private set; }

    // ── Camera height presets ─────────────────────────────────────────────────
    public enum CameraPreset { None, High, Medium, Low }

    // Preset definitions: (Y height, pitch angle)
    static readonly (float y, float pitch) PresetHigh   = (120f, 60f);
    static readonly (float y, float pitch) PresetMedium = (65f,  45f);
    static readonly (float y, float pitch) PresetLow    = (25f,  28f);

    CameraPreset activePreset = CameraPreset.None;
    Vector3  targetPos;
    float    targetPitch;
    bool     smoothingToPreset;

    float yaw, pitch;
    float defaultYaw, defaultPitch;
    Vector3 defaultPos;

    // Auto-orbit / cinematic rotation
    bool autoRotate = false;
    public float autoRotateSpeed = 16f;

    // Middle-mouse drag state
    bool    mmDragging;
    Vector3 mmDragOrigin;
    Vector3 mmPosOrigin;

    // Mouse rotation state tracking
    bool isMouseRotating = false;
    Vector3 lastMousePos;

    void Start()
    {
        var cam = GetComponent<Camera>();
        if (cam != null)
        {
            cam.farClipPlane = 2000f;
            cam.nearClipPlane = 0.3f;
            cam.clearFlags = CameraClearFlags.SolidColor;
            cam.backgroundColor = new Color(0.38f, 0.62f, 0.88f);
        }

        // If camera is at ground level or default unconfigured origin, snap to city overview
        if (transform.position.y < 8f || transform.position.magnitude < 5f)
        {
            transform.position = new Vector3(-85f, 58f, -95f);
            transform.rotation = Quaternion.Euler(30f, 42f, 0f);
        }

        var angles = transform.eulerAngles;
        pitch = angles.x;
        yaw   = angles.y;

        defaultYaw   = yaw;
        defaultPitch = pitch;
        defaultPos   = transform.position;

        targetPos   = transform.position;
        targetPitch = pitch;
    }

    void OnDisable()
    {
        // Safety: always release cursor lock when disabled or scene unloads
        if (Cursor.lockState != CursorLockMode.None)
        {
            Cursor.lockState = CursorLockMode.None;
            Cursor.visible = true;
        }
    }

    void Update()
    {
        float mult = Input.GetKey(KeyCode.LeftShift) ? 2.5f : 1f;

        // ── Check any user interaction to cancel preset / auto-rotate ───────────
        bool hasMoveInput = Input.GetAxisRaw("Horizontal") != 0f ||
                            Input.GetAxisRaw("Vertical")   != 0f ||
                            Input.mouseScrollDelta.y        != 0f;

        bool hasRotKey = Input.GetKey(KeyCode.Q) || Input.GetKey(KeyCode.E) ||
                         Input.GetKey(KeyCode.F) ||
                         (Input.GetKey(KeyCode.R) && (BuildPlacementController.Instance == null || !BuildPlacementController.Instance.IsPlacing));

        bool mouseRotButton = Input.GetMouseButton(1) ||
                              (Input.GetKey(KeyCode.LeftAlt) && Input.GetMouseButton(0));

        if (hasMoveInput || hasRotKey || mouseRotButton)
        {
            if (smoothingToPreset)
            {
                smoothingToPreset = false;
                activePreset = CameraPreset.None;
            }
            if (autoRotate && (hasMoveInput || hasRotKey || mouseRotButton))
            {
                autoRotate = false;
            }
        }

        // ── Smooth to preset target ───────────────────────────────────────────
        if (smoothingToPreset)
        {
            transform.position = Vector3.Lerp(transform.position, targetPos, Time.deltaTime * 5f);
            pitch = Mathf.Lerp(pitch, targetPitch, Time.deltaTime * 5f);
            transform.rotation = Quaternion.Euler(pitch, yaw, 0f);

            if (Vector3.Distance(transform.position, targetPos) < 0.5f &&
                Mathf.Abs(pitch - targetPitch) < 0.5f)
            {
                transform.position = targetPos;
                pitch = targetPitch;
                smoothingToPreset = false;
            }
            return; // skip normal movement while lerping to preset
        }

        // ── Cinematic Auto-Rotate ─────────────────────────────────────────────
        if (autoRotate)
        {
            yaw = (yaw + autoRotateSpeed * Time.deltaTime) % 360f;
            transform.rotation = Quaternion.Euler(pitch, yaw, 0f);
        }

        // ── Keyboard / WASD pan ───────────────────────────────────────────────
        Vector3 f = Vector3.ProjectOnPlane(transform.forward, Vector3.up).normalized;
        Vector3 r = Vector3.ProjectOnPlane(transform.right,   Vector3.up).normalized;
        float h = Input.GetAxisRaw("Horizontal");
        float v = Input.GetAxisRaw("Vertical");
        if (h != 0f || v != 0f)
        {
            transform.position += (f * v + r * h) * moveSpeed * mult * Time.deltaTime;
            activePreset = CameraPreset.None;
        }

        // ── Mouse scroll zoom ─────────────────────────────────────────────────
        float scroll = Input.mouseScrollDelta.y;
        if (scroll != 0f)
        {
            transform.position += transform.forward * scroll * zoomSpeed * Time.deltaTime;
            activePreset = CameraPreset.None;
        }

        // ── Keyboard rotation (Q = Left, E = Right, R/F = Tilt) ───────────────
        float keyYaw = 0f;
        if (Input.GetKey(KeyCode.Q)) keyYaw -= 1f;
        if (Input.GetKey(KeyCode.E)) keyYaw += 1f;

        float keyPitch = 0f;
        bool placingNow = BuildPlacementController.Instance != null && BuildPlacementController.Instance.IsPlacing;
        if (!placingNow && Input.GetKey(KeyCode.R)) keyPitch -= 1f; // tilt up
        if (Input.GetKey(KeyCode.F))                keyPitch += 1f; // tilt down

        if (keyYaw != 0f || keyPitch != 0f)
        {
            yaw   += keyYaw   * rotateSpeed * mult * Time.deltaTime;
            pitch += keyPitch * rotateSpeed * mult * Time.deltaTime;
            pitch  = Mathf.Clamp(pitch, 10f, 80f);
            transform.rotation = Quaternion.Euler(pitch, yaw, 0f);
            activePreset = CameraPreset.None;
        }

        // ── Mouse rotation (Right Mouse Drag, Middle Mouse Drag, or Alt + Left Drag) ─
        if (Input.GetMouseButtonDown(1) || Input.GetMouseButtonDown(2))
        {
            lastMousePos = Input.mousePosition;
        }

        if (Input.GetMouseButton(1) || Input.GetMouseButton(2) || (Input.GetKey(KeyCode.LeftAlt) && Input.GetMouseButton(0)))
        {
            Vector3 mouseDelta = Input.mousePosition - lastMousePos;
            lastMousePos = Input.mousePosition;

            float rawX = Input.GetAxisRaw("Mouse X");
            float rawY = Input.GetAxisRaw("Mouse Y");

            float xTurn = Mathf.Abs(rawX) > 0.001f ? rawX * 3.8f : mouseDelta.x * 0.35f;
            float yTurn = Mathf.Abs(rawY) > 0.001f ? rawY * 3.8f : mouseDelta.y * 0.35f;

            if (Mathf.Abs(xTurn) > 0.0001f || Mathf.Abs(yTurn) > 0.0001f)
            {
                yaw   += xTurn;
                pitch -= yTurn;
                pitch  = Mathf.Clamp(pitch, 5f, 85f);
                transform.rotation = Quaternion.Euler(pitch, yaw, 0f);
                activePreset = CameraPreset.None;
                smoothingToPreset = false;
                autoRotate = false;
            }
        }
        else
        {
            lastMousePos = Input.mousePosition;
        }

        // ── Middle mouse button: drag-to-pan ──────────────────────────────────
        if (Input.GetMouseButtonDown(2))
        {
            mmDragging   = true;
            mmDragOrigin = Input.mousePosition;
            mmPosOrigin  = transform.position;
        }
        if (Input.GetMouseButtonUp(2)) mmDragging = false;

        if (mmDragging)
        {
            Vector3 delta = Input.mousePosition - mmDragOrigin;
            float dragScale = transform.position.y * 0.018f * mult;
            transform.position = mmPosOrigin
                - r * delta.x * dragScale
                - f * delta.y * dragScale;
            activePreset = CameraPreset.None;
        }

        // ── Left click: select a building ─────────────────────────────────────
        bool placing = BuildPlacementController.Instance != null
                       && BuildPlacementController.Instance.IsPlacing;

        if (!placing
            && !isMouseRotating
            && Input.GetMouseButtonDown(0)
            && Input.mousePosition.y < Screen.height - 68
            && Input.mousePosition.x > 230f)
        {
            if (Camera.main != null)
            {
                Ray ray = Camera.main.ScreenPointToRay(Input.mousePosition);
                if (Physics.Raycast(ray, out RaycastHit hit, 600f))
                {
                    var b = hit.collider.GetComponentInParent<Building>();
                    if (b != null) SelectedBuilding = b;
                }
            }
        }

        // ── Camera bounds (match 320×280 terrain) ─────────────────────────────
        transform.position = new Vector3(
            Mathf.Clamp(transform.position.x, -150f, 150f),
            Mathf.Clamp(transform.position.y,    8f, 150f),
            Mathf.Clamp(transform.position.z, -130f, 130f));
    }

    // ── Public API ────────────────────────────────────────────────────────────

    /// <summary>Rotate camera left by given degrees (default 45°).</summary>
    public void RotateLeft(float degrees = 45f)
    {
        yaw = (yaw - degrees) % 360f;
        transform.rotation = Quaternion.Euler(pitch, yaw, 0f);
        activePreset = CameraPreset.None;
        smoothingToPreset = false;
        autoRotate = false;
    }

    /// <summary>Rotate camera right by given degrees (default 45°).</summary>
    public void RotateRight(float degrees = 45f)
    {
        yaw = (yaw + degrees) % 360f;
        transform.rotation = Quaternion.Euler(pitch, yaw, 0f);
        activePreset = CameraPreset.None;
        smoothingToPreset = false;
        autoRotate = false;
    }

    /// <summary>Toggle cinematic continuous auto-orbit around the city.</summary>
    public void ToggleAutoRotate()
    {
        autoRotate = !autoRotate;
        if (autoRotate) smoothingToPreset = false;
    }

    public bool IsAutoRotating => autoRotate;

    /// <summary>Reset camera to starting position and orientation.</summary>
    public void ResetView()
    {
        targetPos   = defaultPos;
        targetPitch = defaultPitch;
        yaw         = defaultYaw;
        activePreset = CameraPreset.None;
        smoothingToPreset = true;
        autoRotate = false;
    }

    /// <summary>Smoothly move camera to a height preset.</summary>
    public void SetPreset(CameraPreset preset)
    {
        (float y, float p) cfg = preset switch
        {
            CameraPreset.High   => PresetHigh,
            CameraPreset.Medium => PresetMedium,
            CameraPreset.Low    => PresetLow,
            _                   => (transform.position.y, pitch)
        };

        activePreset      = preset;
        targetPos         = new Vector3(transform.position.x, cfg.y, transform.position.z);
        targetPitch       = cfg.p;
        smoothingToPreset = true;
        autoRotate        = false;
    }

    public CameraPreset ActivePreset => activePreset;

    public static void ClearSelection() { SelectedBuilding = null; }
}
