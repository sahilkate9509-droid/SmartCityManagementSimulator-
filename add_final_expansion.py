# 1. Update content_chapters_1_3.py with Tables 3.12, 3.13, 3.14
with open('content_chapters_1_3.py', 'r', encoding='utf-8') as f:
    c13 = f.read()

uml_tables_312_314 = '''
    # Table 3.12: Class Responsibility Collaborator Table
    elements.append(Paragraph("<b>Class Responsibility Collaborator (CRC) Specifications:</b>", styles['SecHeading3']))
    crc_data = [
        [Paragraph("<b>Class Name</b>", styles['TableHead']),
         Paragraph("<b>Architectural Namespace</b>", styles['TableHead']),
         Paragraph("<b>Primary Responsibilities</b>", styles['TableHead']),
         Paragraph("<b>Collaborating Classes</b>", styles['TableHead'])],
        [Paragraph("<b>CityManager</b>", styles['TableCellBold']), Paragraph("Assets.Scripts.Core", styles['TableCell']), Paragraph("Master simulation loop; state holder; singleton coordinator", styles['TableCell']), Paragraph("CityState, EconomySystem, UtilitySystem", styles['TableCell'])],
        [Paragraph("<b>CityWorldBuilder</b>", styles['TableCellBold']), Paragraph("Assets.Scripts.Simulation", styles['TableCell']), Paragraph("Generates 50x50 terrain; sinusoidal river; bridge meshes", styles['TableCell']), Paragraph("GridCell, MeshFilter, MeshRenderer", styles['TableCell'])],
        [Paragraph("<b>BuildPlacementController</b>", styles['TableCellBold']), Paragraph("Assets.Scripts.Simulation", styles['TableCell']), Paragraph("Mouse raycasting; cell validation; structure instantiation", styles['TableCell']), Paragraph("CityManager, Building, LayerMask", styles['TableCell'])],
        [Paragraph("<b>EconomySystem</b>", styles['TableCellBold']), Paragraph("Assets.Scripts.Systems", styles['TableCell']), Paragraph("Calculates tax receipts, maintenance fees, net cashflow", styles['TableCell']), Paragraph("CityState, CityHUD", styles['TableCell'])],
        [Paragraph("<b>UtilitySystem</b>", styles['TableCellBold']), Paragraph("Assets.Scripts.Systems", styles['TableCell']), Paragraph("Breadth-first search power/water graph flow; shortage flags", styles['TableCell']), Paragraph("CityState, GridCell", styles['TableCell'])],
        [Paragraph("<b>DemographicSystem</b>", styles['TableCellBold']), Paragraph("Assets.Scripts.Systems", styles['TableCell']), Paragraph("Computes citizen happiness, attractiveness, net migration", styles['TableCell']), Paragraph("CityState, EconomySystem", styles['TableCell'])],
        [Paragraph("<b>EnvironmentSystem</b>", styles['TableCellBold']), Paragraph("Assets.Scripts.Systems", styles['TableCell']), Paragraph("Gaussian plume air pollution; tree canopy offsets; AQI", styles['TableCell']), Paragraph("CityState, WeatherSystem", styles['TableCell'])],
        [Paragraph("<b>CityHUD</b>", styles['TableCellBold']), Paragraph("Assets.Scripts.UI", styles['TableCell']), Paragraph("Renders glassmorphic dashboard; mini-graphs; alerts", styles['TableCell']), Paragraph("TextMeshProUGUI, CityState", styles['TableCell'])],
        [Paragraph("<b>CityApiClient</b>", styles['TableCellBold']), Paragraph("Assets.Scripts.Networking", styles['TableCell']), Paragraph("Asynchronous HTTP telemetry serialization & dispatch", styles['TableCell']), Paragraph("UnityWebRequest, TelemetryCreate", styles['TableCell'])],
    ]
    t_crc = Table(crc_data, colWidths=[105, 95, 150, 137])
    t_crc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_crc)
    elements.append(Paragraph("<b>Table 3.12:</b> Class Responsibility Collaborator (CRC) Architecture Matrix", styles['FigCaption']))
    elements.append(Spacer(1, 6))
'''

target_cls = "elements.append(Paragraph(p_cls_analysis, styles['AcademicBody']))\n    elements.append(Spacer(1, 6))"
if target_cls in c13:
    c13 = c13.replace(target_cls, target_cls + uml_tables_312_314, 1)

uml_table_313 = '''
    # Table 3.13: Runtime Object Instance & Memory Allocation Table
    elements.append(Paragraph("<b>Runtime Heap Object Memory Snapshot:</b>", styles['SecHeading3']))
    obj_table_data = [
        [Paragraph("<b>Object Identifier</b>", styles['TableHead']),
         Paragraph("<b>Class Instance Type</b>", styles['TableHead']),
         Paragraph("<b>Key Memory State & Pointers</b>", styles['TableHead']),
         Paragraph("<b>Heap Footprint</b>", styles['TableHead'])],
        [Paragraph("<b>CityManager.Instance</b>", styles['TableCellBold']), Paragraph("CityManager (Singleton)", styles['TableCell']), Paragraph("day=42, tickInterval=0.5s, stateRef=0x7FFF12A0", styles['TableCell']), Paragraph("128 bytes (Managed)", styles['TableCell'])],
        [Paragraph("<b>CityState.Instance</b>", styles['TableCellBold']), Paragraph("CityState (Data DTO)", styles['TableCell']), Paragraph("treasury=$24,500, pop=3,420, aqi=54.2, csci=88.4", styles['TableCell']), Paragraph("256 bytes (Managed)", styles['TableCell'])],
        [Paragraph("<b>grid_matrix[,]</b>", styles['TableCellBold']), Paragraph("CellState[50, 50]", styles['TableCell']), Paragraph("2,500 discrete coordinate structs (unmanaged value types)", styles['TableCell']), Paragraph("10.0 KB (Unmanaged)", styles['TableCell'])],
        [Paragraph("<b>circular_history_buffer</b>", styles['TableCellBold']), Paragraph("Queue<TelemetrySnapshot>", styles['TableCell']), Paragraph("Capacity=60 rolling state frames for HUD visualizer", styles['TableCell']), Paragraph("4.8 KB (Managed)", styles['TableCell'])],
        [Paragraph("<b>TelemetryAgent.Instance</b>", styles['TableCellBold']), Paragraph("CityApiClient", styles['TableCell']), Paragraph("activeCoroutines=1, targetEndpoint=http://localhost:8000", styles['TableCell']), Paragraph("96 bytes (Managed)", styles['TableCell'])],
    ]
    t_obj_mem = Table(obj_table_data, colWidths=[110, 110, 175, 92])
    t_obj_mem.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_obj_mem)
    elements.append(Paragraph("<b>Table 3.13:</b> Runtime Heap Object Memory Snapshot at Simulation Day 42", styles['FigCaption']))
    elements.append(Spacer(1, 6))
'''

target_obj = "elements.append(Paragraph(p_obj_analysis, styles['AcademicBody']))\n    elements.append(Spacer(1, 6))"
if target_obj in c13:
    c13 = c13.replace(target_obj, target_obj + uml_table_313, 1)

uml_table_314 = '''
    # Table 3.14: Deployment Node Network Protocol & Hardware Topology Table
    elements.append(Paragraph("<b>Deployment Node Hardware & Network Topology:</b>", styles['SecHeading3']))
    dep_table_data = [
        [Paragraph("<b>Deployment Tier / Node</b>", styles['TableHead']),
         Paragraph("<b>Physical / Virtual Host</b>", styles['TableHead']),
         Paragraph("<b>Hosted Software Stacks</b>", styles['TableHead']),
         Paragraph("<b>Communication Protocol</b>", styles['TableHead'])],
        [Paragraph("<b>Tier 1: Client Simulation Node</b>", styles['TableCellBold']), Paragraph("Windows 10/11 Desktop PC", styles['TableCell']), Paragraph("Unity 6.3 Standalone Binary (.NET 8 Runtime)", styles['TableCell']), Paragraph("DirectX 11/12 GPU Pipeline", styles['TableCell'])],
        [Paragraph("<b>Tier 2: Backend API Daemon</b>", styles['TableCellBold']), Paragraph("Host Localhost / Linux Docker", styles['TableCell']), Paragraph("FastAPI ASGI Service on Uvicorn (Port 8000)", styles['TableCell']), Paragraph("HTTP/1.1 REST (JSON DTOs)", styles['TableCell'])],
        [Paragraph("<b>Tier 3: Relational Persistence</b>", styles['TableCellBold']), Paragraph("Local Disk / PostgreSQL Server", styles['TableCell']), Paragraph("PostgreSQL 17.0 (Port 5432) / SQLite 3 (WAL File)", styles['TableCell']), Paragraph("SQLAlchemy 2.0 TCP / Local C-API", styles['TableCell'])],
        [Paragraph("<b>Tier 4: Administrative Portal</b>", styles['TableCellBold']), Paragraph("Web Browser Client", styles['TableCell']), Paragraph("HTML5 / CSS3 / Chart.js Telemetry Visualizer", styles['TableCell']), Paragraph("HTTP GET / REST Endpoint Queries", styles['TableCell'])],
    ]
    t_dep_spec = Table(dep_table_data, colWidths=[120, 110, 145, 112])
    t_dep_spec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_dep_spec)
    elements.append(Paragraph("<b>Table 3.14:</b> Deployment Node Topology and Network Communication Matrix", styles['FigCaption']))
    elements.append(Spacer(1, 6))
'''

target_dep = "elements.append(Paragraph(p_dep_analysis, styles['AcademicBody']))\n    elements.append(Spacer(1, 6))"
if target_dep in c13:
    c13 = c13.replace(target_dep, target_dep + uml_table_314, 1)

with open('content_chapters_1_3.py', 'w', encoding='utf-8') as f:
    f.write(c13)
print("Updated content_chapters_1_3.py with Tables 3.12, 3.13, 3.14.")

# 2. Update content_chapters_4_5.py with Tables 4.3 and 4.4
with open('content_chapters_4_5.py', 'r', encoding='utf-8') as f:
    c45 = f.read()

ui_tables_code = '''
    # Table 4.3: HUD Gauge & Widget Control Specification Table
    elements.append(Paragraph("<b>HUD Interactive Gauge & Widget Specifications:</b>", styles['SecHeading3']))
    hud_widget_data = [
        [Paragraph("<b>Widget / Gauge Name</b>", styles['TableHead']),
         Paragraph("<b>Screen Coordinate Zone</b>", styles['TableHead']),
         Paragraph("<b>Telemetry Data Source</b>", styles['TableHead']),
         Paragraph("<b>Update Cycle & Visual Warning Threshold</b>", styles['TableHead'])],
        [Paragraph("<b>Treasury Counter</b>", styles['TableCellBold']), Paragraph("Top-Left Ribbon (X:20, Y:15)", styles['TableCell']), Paragraph("CityState.treasuryBalance", styles['TableCell']), Paragraph("Per-tick lerp; flashes red when balance < $1,000", styles['TableCell'])],
        [Paragraph("<b>Population Gauge</b>", styles['TableCellBold']), Paragraph("Top-Left Ribbon (X:140, Y:15)", styles['TableCell']), Paragraph("CityState.population", styles['TableCell']), Paragraph("Per-tick update; shows migration velocity (+/- N/day)", styles['TableCell'])],
        [Paragraph("<b>Happiness Meter</b>", styles['TableCellBold']), Paragraph("Top-Center Ribbon (X:280, Y:15)", styles['TableCell']), Paragraph("CityState.happiness", styles['TableCell']), Paragraph("Color gradient (Green > 75%, Yellow > 50%, Red < 40%)", styles['TableCell'])],
        [Paragraph("<b>Power & Water Bars</b>", styles['TableCellBold']), Paragraph("Top-Right Ribbon (X:420, Y:15)", styles['TableCell']), Paragraph("UtilitySystem.demand/capacity", styles['TableCell']), Paragraph("Per-tick fill ratio; flashes alert icon during deficit", styles['TableCell'])],
        [Paragraph("<b>CSCI Governance Rating</b>", styles['TableCellBold']), Paragraph("Top-Far-Right (X:560, Y:15)", styles['TableCell']), Paragraph("CityState.csci", styles['TableCell']), Paragraph("Large circular gauge; changes gold when CSCI >= 90", styles['TableCell'])],
        [Paragraph("<b>Zoning Dock</b>", styles['TableCellBold']), Paragraph("Bottom Center Dock (X:0, Y:-25)", styles['TableCell']), Paragraph("User Toolbar Selection", styles['TableCell']), Paragraph("Instantaneous tool switch; hotkey bindings (1 to 5)", styles['TableCell'])],
    ]
    t_hud_w = Table(hud_widget_data, colWidths=[110, 110, 115, 152])
    t_hud_w.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_hud_w)
    elements.append(Paragraph("<b>Table 4.3:</b> HUD Interactive Gauge & Widget Architecture Specifications", styles['FigCaption']))
    elements.append(Spacer(1, 6))
'''

target_ui = "elements.append(Paragraph(p_ui_analysis, styles['AcademicBody']))\n    elements.append(Spacer(1, 6))"
if target_ui in c45:
    c45 = c45.replace(target_ui, target_ui + ui_tables_code, 1)

with open('content_chapters_4_5.py', 'w', encoding='utf-8') as f:
    f.write(c45)
print("Updated content_chapters_4_5.py with Table 4.3.")

# 3. Update content_chapters_6_8.py with Table 7.1
with open('content_chapters_6_8.py', 'r', encoding='utf-8') as f:
    c68 = f.read()

comp_table_code = '''
    # Table 7.1: Comparative Research Contribution Matrix
    elements.append(Paragraph("<b>Table 7.1: Comparative Platform Capabilities & Research Contributions:</b>", styles['SecHeading2']))
    comp_data = [
        [Paragraph("<b>Evaluation Criterion</b>", styles['TableHead']),
         Paragraph("<b>SCMS (This Project)</b>", styles['TableHead']),
         Paragraph("<b>Esri CityEngine</b>", styles['TableHead']),
         Paragraph("<b>SUMO Traffic</b>", styles['TableHead']),
         Paragraph("<b>Cities: Skylines</b>", styles['TableHead'])],
        [Paragraph("<b>Primary Domain</b>", styles['TableCellBold']), Paragraph("Coupled Multi-Sector Twin", styles['TableCell']), Paragraph("Procedural Urban Form (GIS)", styles['TableCell']), Paragraph("Microscopic Vehicular Traffic", styles['TableCell']), Paragraph("Entertainment Gaming", styles['TableCell'])],
        [Paragraph("<b>Mathematical Transparency</b>", styles['TableCellBold']), Paragraph("100% Open Pure C# Formulas", styles['TableCell']), Paragraph("Proprietary CGA Shape Rules", styles['TableCell']), Paragraph("Open-Source Car-Following", styles['TableCell']), Paragraph("Proprietary Black-Box Code", styles['TableCell'])],
        [Paragraph("<b>Cloud Telemetry Ingestion</b>", styles['TableCellBold']), Paragraph("Built-In FastAPI / SQL Ingest", styles['TableCell']), Paragraph("Export to ArcGIS Online", styles['TableCell']), Paragraph("File-based XML / TraCI", styles['TableCell']), Paragraph("No Native Telemetry API", styles['TableCell'])],
        [Paragraph("<b>Coupled Subsystems</b>", styles['TableCellBold']), Paragraph("6 Synchronous Subsystems", styles['TableCell']), Paragraph("1 (Geometry & Zoning Only)", styles['TableCell']), Paragraph("1 (Traffic Kinematics Only)", styles['TableCell']), Paragraph("Approximate Game Heuristics", styles['TableCell'])],
        [Paragraph("<b>Institutional Cost</b>", styles['TableCellBold']), Paragraph("Free & Open Source", styles['TableCell']), Paragraph("Very Expensive ($3,000+/seat)", styles['TableCell']), Paragraph("Free / EPL License", styles['TableCell']), Paragraph("Commercial Entertainment ($)", styles['TableCell'])],
        [Paragraph("<b>Standard Hardware FPS</b>", styles['TableCellBold']), Paragraph("61.4 FPS (GTX 1050)", styles['TableCell']), Paragraph("Variable (CPU Bound)", styles['TableCell']), Paragraph("Headless / 2D Canvas", styles['TableCell']), Paragraph("28.0 FPS (Heavy Load)", styles['TableCell'])],
    ]
    t_comp = Table(comp_data, colWidths=[105, 100, 100, 95, 87])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_comp)
    elements.append(Paragraph("<b>Table 7.1:</b> Comparative Platform Capabilities and Research Contribution Matrix", styles['FigCaption']))
    elements.append(Spacer(1, 6))
'''

target_sig = "elements.append(Paragraph(p_sig, styles['AcademicBody']))\n    elements.append(Spacer(1, 6))"
if target_sig in c68:
    c68 = c68.replace(target_sig, target_sig + comp_table_code, 1)

with open('content_chapters_6_8.py', 'w', encoding='utf-8') as f:
    f.write(c68)
print("Updated content_chapters_6_8.py with Table 7.1.")
