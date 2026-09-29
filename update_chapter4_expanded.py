import os

new_chapter_4 = '''    # =========================================================================
    # CHAPTER 4: SYSTEM MODELING USING UML
    # =========================================================================
    elements.append(Paragraph("<b>CHAPTER 4</b><br/><b>SYSTEM MODELING USING UML</b>", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=12, spaceBefore=4))

    # 4.1 Event Table (System Logic & Event Table)
    elements.append(Paragraph("4.1 Event Table (System Logic &amp; Event Table)", styles['SecHeading1']))
    p_ev_intro = (
        "The System Logic and Event Table forms the behavioral foundation of the Smart City Management Simulator. "
        "In modern urban simulation platforms, discrete user inputs, autonomous clock signals, and stochastic environmental "
        "phenomena must be deterministic and synchronized. The simulation operates on an asynchronous event-driven architecture "
        "supplemented by a fixed 2.0 Hz (500 ms) numerical integration tick. Every interaction—from a mayor allocating residential "
        "zones to the spontaneous ignition of an industrial fire—is classified into discrete triggers, processing subsystems, "
        "and architectural destinations.<br/><br/>"
        "Table 4.1 maps the principal system triggers across the user interface layer, the differential mathematical kernel, "
        "and the cloud telemetry persistence pipeline. By decoupling event capture from execution, the simulation ensures that "
        "high-frequency UI interactions (such as mouse raycasting across the 50x50 plot matrix) remain fluid at 60 FPS while "
        "heavy computation tasks execute synchronously within their designated tick cycles."
    )
    elements.append(Paragraph(p_ev_intro, styles['AcademicBody']))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>Table 4.1: System Logic &amp; Event Table</b>", styles['SecHeading2']))
    event_data = [
        [Paragraph("<b>Event</b>", styles['TableHead']),
         Paragraph("<b>Trigger</b>", styles['TableHead']),
         Paragraph("<b>Source</b>", styles['TableHead']),
         Paragraph("<b>Use Case / Activity</b>", styles['TableHead']),
         Paragraph("<b>System Response</b>", styles['TableHead']),
         Paragraph("<b>Destination</b>", styles['TableHead'])],
        
        [Paragraph("User requests login", styles['TableCellBold']),
         Paragraph("Clicks 'Sign In' button", styles['TableCell']),
         Paragraph("Mayor / User", styles['TableCell']),
         Paragraph("User Authentication", styles['TableCell']),
         Paragraph("Validates session credentials, issues auth token, loads city save slots.", styles['TableCell']),
         Paragraph("Dashboard / UI", styles['TableCellBold'])],
        
        [Paragraph("Zone tile clicked", styles['TableCellBold']),
         Paragraph("Mouse click on 50×50 plot", styles['TableCell']),
         Paragraph("Mayor", styles['TableCell']),
         Paragraph("Zoning Allocation", styles['TableCell']),
         Paragraph("Validates coordinates, deducts zoning fee, colors tile (Res/Com/Ind).", styles['TableCell']),
         Paragraph("CityGrid / 3D Scene", styles['TableCellBold'])],
        
        [Paragraph("Facility placed", styles['TableCellBold']),
         Paragraph("Selects clinic/power plant", styles['TableCell']),
         Paragraph("Mayor", styles['TableCell']),
         Paragraph("Building Construction", styles['TableCell']),
         Paragraph("Validates funds, checks obstacle clearance, instantiates 3D mesh.", styles['TableCell']),
         Paragraph("3D Viewport", styles['TableCellBold'])],
        
        [Paragraph("Simulation tick occurs", styles['TableCellBold']),
         Paragraph("Timer reaches 0.50s (2 Hz)", styles['TableCell']),
         Paragraph("System Clock", styles['TableCell']),
         Paragraph("Differential Simulation", styles['TableCell']),
         Paragraph("Executes coupled differential updates across Economy, Utilities, AQI, Traffic.", styles['TableCell']),
         Paragraph("Simulation Engine", styles['TableCellBold'])],
        
        [Paragraph("Utility shortage detected", styles['TableCellBold']),
         Paragraph("Demand exceeds capacity", styles['TableCell']),
         Paragraph("Utility Manager", styles['TableCell']),
         Paragraph("Service Deficit Warning", styles['TableCell']),
         Paragraph("Generates alert icon over unserviced zone, drops citizen happiness.", styles['TableCell']),
         Paragraph("HUD / Citizen Hub", styles['TableCellBold'])],
        
        [Paragraph("Disaster triggered", styles['TableCellBold']),
         Paragraph("Random event condition met", styles['TableCell']),
         Paragraph("Disaster Engine", styles['TableCell']),
         Paragraph("Emergency Incident", styles['TableCell']),
         Paragraph("Displays emergency modal, spreads localized fire/smog, degrades CSCI.", styles['TableCell']),
         Paragraph("Modal / Telemetry", styles['TableCellBold'])],
        
        [Paragraph("Snapshot save triggered", styles['TableCellBold']),
         Paragraph("Manual save or auto-interval", styles['TableCell']),
         Paragraph("Mayor / Clock", styles['TableCell']),
         Paragraph("Cloud Persistence", styles['TableCell']),
         Paragraph("Serializes simulation matrix to JSON, posts async telemetry to FastAPI.", styles['TableCell']),
         Paragraph("FastAPI / Database", styles['TableCellBold'])],
        
        [Paragraph("Analytics hub opened", styles['TableCellBold']),
         Paragraph("Clicks Analytics tab", styles['TableCell']),
         Paragraph("Mayor / Auditor", styles['TableCell']),
         Paragraph("Historical Diagnostics", styles['TableCell']),
         Paragraph("Queries telemetry history, renders Chart.js CSCI trend curves.", styles['TableCell']),
         Paragraph("Analytics Portal", styles['TableCellBold'])],
    ]
    ev_table = Table(event_data, colWidths=[65, 85, 55, 80, 137, 65])
    ev_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    elements.append(ev_table)
    elements.append(Spacer(1, 8))

    p_ev_post = (
        "As illustrated above, event dispatching enforces transactional safety across subsystems. For example, if a "
        "facility construction event fails due to a terrain collision with the procedurally curved river, the transaction "
        "is aborted before deducting funds from the treasury. This eliminates state divergence between the client-side 3D "
        "viewport and the persistent database records."
    )
    elements.append(Paragraph(p_ev_post, styles['AcademicBody']))
    elements.append(PageBreak())

    # =========================================================================
    # 4.2 Class Diagram
    # =========================================================================
    elements.append(Paragraph("4.2 Class Diagram", styles['SecHeading1']))
    p_cd1 = (
        "The static structure of the Smart City Management Simulator is modeled using a rigorous object-oriented design "
        "hierarchy that enforces high cohesion and loose coupling. In complex urban simulation engines, tight coupling between "
        "graphical rendering and physical calculations frequently leads to frame stutter and thread contention. To prevent "
        "these bottlenecks, the simulator divides domain objects into three distinct conceptual layers: Simulation Management, "
        "Spatial Domain Entities, and Subsystem Calculators.<br/><br/>"
        "Key design patterns are embedded directly into the class architecture:<br/>"
        "• <b>Singleton Pattern:</b> Applied to the <code>SimulationEngine</code> class to guarantee a single authoritative "
        "timekeeper, orchestrating numerical ticks, managing simulation speed multipliers (1x, 2x, 3x), and synchronizing subsystem threads.<br/>"
        "• <b>Spatial Partitioning Pattern:</b> The <code>CityGrid</code> class encapsulates a two-dimensional matrix of 2,500 "
        "discrete plots (50x50 grid). Each cell maintains spatial references to zoning types, terrain elevation, and water collision masks, "
        "enabling O(1) query time during placement validation.<br/>"
        "• <b>Multi-Agent State Machine:</b> The <code>CitizenAgent</code> class models individual demographic behaviors. Each agent "
        "maintains home and work plot vectors, transitioning between state states (Resting, Commuting, Working, Recreating) based on time-of-day "
        "signals and road network congestion.<br/>"
        "• <b>Composite Normalization Pattern:</b> Encapsulated within <code>CSCIComputer</code>, which aggregates weighted outputs from the "
        "treasury, utility grid, environment plume simulator, and citizen satisfaction into a single standardized 0-100 index."
    )
    elements.append(Paragraph(p_cd1, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    cd_path = os.path.join(FIG_DIR, "fig4_4_class.png")
    if os.path.exists(cd_path):
        elements.append(Image(cd_path, width=475, height=275))
        elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Figure 4.1:</b> Class Diagram Mapping City Simulation Entities", styles['FigCaption']))
    elements.append(Spacer(1, 6))

    p_cd2 = (
        "<b>Structural Relationships &amp; Multiplicities:</b><br/>"
        "The class diagram establishes clear structural multiplicities and dependencies across the architecture:<br/>"
        "1. <b>SimulationEngine to Subsystems (1 : 1):</b> The simulation engine maintains direct composition links to the "
        "<code>BudgetManager</code>, <code>UtilityNetwork</code>, <code>EnvironmentEngine</code>, and <code>CSCIComputer</code>, "
        "invoking their respective tick routines sequentially on each 2 Hz clock cycle.<br/>"
        "2. <b>CityGrid to ZonePlot (1 : 2500):</b> The 50x50 spatial grid owns exactly 2,500 <code>ZonePlot</code> instances. "
        "Each plot encapsulates zoning attributes, current occupancy, land value, and utility connectivity flags.<br/>"
        "3. <b>ZonePlot to BuildingEntity (1 : 0..1):</b> A plot may host at most one structural building entity. Upgrading a building "
        "modifies the existing instance properties (capacity, power demand, tax output) without reallocating heap memory.<br/>"
        "4. <b>RoadNetwork to CitizenAgent (1 : N):</b> The road network maintains an interconnected graph of segments and intersections, "
        "providing the underlying A* search space traversed by hundreds of concurrent commuting citizen agents.<br/>"
        "5. <b>FastAPIClient to TelemetryLogger (1 : 1):</b> The HTTP service client serializes simulation state dictionaries and "
        "dispatches non-blocking async tasks to the remote FastAPI backend, buffering failed requests in memory during offline sessions."
    )
    elements.append(Paragraph(p_cd2, styles['AcademicBody']))
    elements.append(PageBreak())

    # =========================================================================
    # 4.3 Use Case Diagram
    # =========================================================================
    elements.append(Paragraph("4.3 Use Case Diagram", styles['SecHeading1']))
    p_uc1 = (
        "The Use Case Diagram defines the functional scope of the Smart City Management Simulator by delineating the operational "
        "interactions between system actors and application use cases. It establishes the system boundary and captures both "
        "human-driven administrative operations and automated background computational processes.<br/><br/>"
        "The system identifies four primary and secondary actors:<br/>"
        "• <b>City Mayor / Urban Planner (Primary Human Actor):</b> The central decision-maker who interacts with the 3D viewport, "
        "allocating residential/commercial/industrial zones, constructing civic buildings, laying utility conduits, adjusting municipal tax rates, "
        "and mobilizing emergency responders during urban crises.<br/>"
        "• <b>Simulation Clock (Autonomous System Actor):</b> An automated internal trigger that generates periodic clock ticks at 2 Hz, "
        "driving the continuous differential evaluation of economy, traffic congestion, utility distribution, and environmental pollution.<br/>"
        "• <b>Municipal Telemetry Auditor (Administrative Actor):</b> A secondary stakeholder who accesses analytical dashboards and telemetry "
        "logs to evaluate city performance against standardized smart city benchmarks (CSCI ratings, carbon footprint, fiscal sustainability).<br/>"
        "• <b>Cloud Backend (External Persistence Actor):</b> The remote FastAPI service and PostgreSQL instance that ingests serialized city "
        "snapshots, manages authentication tokens, and provides long-term telemetry persistence."
    )
    elements.append(Paragraph(p_uc1, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    uc_path = os.path.join(FIG_DIR, "fig4_3_usecase.png")
    if os.path.exists(uc_path):
        elements.append(Image(uc_path, width=470, height=290))
        elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Figure 4.2:</b> Use Case Diagram for City Management System", styles['FigCaption']))
    elements.append(Spacer(1, 6))

    p_uc2 = (
        "<b>Use Case Specifications &amp; Relational Dependencies:</b><br/>"
        "The diagram explicitly documents stereotypic relationships governing system execution:<br/>"
        "• <b>&lt;&lt;include&gt;&gt; Relationships:</b> Mandatory procedural dependencies that execute unconditionally. "
        "For example, executing <i>UC-01 (Zone Urban Plots)</i> and <i>UC-02 (Construct Civic Buildings)</i> unconditionally includes "
        "<i>UC-06 (Validate Plot Elevation &amp; Water Bounds)</i> to prevent invalid construction over water bodies or steep terrain. "
        "Similarly, <i>UC-04 (Execute Coupled ODE Simulation Cycle)</i> unconditionally includes <i>UC-07 (Route Utility Grids)</i> and "
        "<i>UC-09 (Calculate Composite CSCI Rating)</i> to ensure metrics reflect real-time infrastructure capacity.<br/>"
        "• <b>&lt;&lt;extend&gt;&gt; Relationships:</b> Conditional execution paths triggered only under specific operational states. "
        "For instance, <i>UC-05 (Deploy Disaster Responders)</i> extends <i>UC-10 (Dispatch Async Telemetry)</i> only when stochastic disaster "
        "probability exceeds the baseline safety threshold, requiring immediate notification dispatch to the mayor and audit logging.<br/>"
        "• <b>Preconditions and Postconditions:</b> Prior to executing budget adjustments (<i>UC-03</i>), the mayor must be authenticated "
        "with an active session. Postcondition enforcement guarantees that treasury deductions are atomic and recorded in the transaction log."
    )
    elements.append(Paragraph(p_uc2, styles['AcademicBody']))
    elements.append(PageBreak())

    # =========================================================================
    # 4.4 Entity-Relationship (ER) & Data Flow Diagrams
    # =========================================================================
    elements.append(Paragraph("4.4 Entity-Relationship (ER) &amp; Data Flow Diagrams (DFD Level 0 &amp; Level 1)", styles['SecHeading1']))
    
    # 4.4.1 ER Diagram
    p_erd = (
        "<b>4.4.1 Entity-Relationship (ER) Diagram:</b><br/>"
        "The relational data architecture of the Smart City Management Simulator is modeled in Third Normal Form (3NF) to eliminate "
        "data redundancy, guarantee entity integrity, and support scalable time-series telemetry analysis. The schema design addresses "
        "two distinct operational requirements: transactional consistency for active gameplay states and append-only partitioning for "
        "high-frequency telemetry metrics.<br/><br/>"
        "The schema centers on the <code>CITIES</code> master entity, which establishes a strict 1:N relationship with child tables via "
        "the <code>city_id</code> foreign key constraint. The <code>CITY_SAVES</code> table stores complete JSON-serialized spatial state "
        "snapshots, accompanied by SHA-256 checksums to detect file corruption during save/load cycles. The <code>ZONING_GRID</code> entity "
        "normalizes the 2,500 terrain plots, tracking coordinate positions, zoning categories, structural upgrade tiers, and utility flags. "
        "The <code>CITY_TELEMETRY</code> table functions as an append-only time-series ledger, capturing macro indicators (population, "
        "happiness, power demand, AQI, traffic efficiency, and CSCI score) on every periodic sync. Citizen grievances and emergency "
        "events are decoupled into <code>CITIZEN_PETITIONS</code> and <code>DISASTER_INCIDENTS</code>, preserving complete audit trails."
    )
    elements.append(Paragraph(p_erd, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    er_path = os.path.join(FIG_DIR, "fig4_9_erd.png")
    if os.path.exists(er_path):
        elements.append(Image(er_path, width=475, height=275))
        elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Figure 4.3:</b> Entity-Relationship (ER) Diagram for City Management Schema", styles['FigCaption']))
    elements.append(PageBreak())

    # 4.4.2 DFD Level 0 (Context Diagram)
    p_dfd0 = (
        "<b>4.4.2 Data Flow Diagram (DFD) – Level 0 (Context Diagram):</b><br/>"
        "The Level 0 Context Diagram establishes the macro data flow boundary of the Smart City Management Simulator. It defines "
        "the external entities that communicate with the central system process (<code>Process 0.0: Smart City Management Simulator System</code>) "
        "without exposing internal algorithmic complexity.<br/><br/>"
        "Four external entities border the system boundary:<br/>"
        "1. <b>City Mayor (Primary User):</b> Streams planning inputs, zoning commands, taxation rate policies, and disaster response "
        "orders into the system, receiving real-time HUD rendering updates, alert warnings, budget balances, and composite CSCI scores.<br/>"
        "2. <b>Citizen Agents (AI Population):</b> Generates autonomous tax contributions, transit route requests, and service deficiency "
        "grievances, receiving allocated municipal services, healthcare treatments, and employment access.<br/>"
        "3. <b>FastAPI Cloud Middleware:</b> Ingests asynchronous HTTP JSON telemetry payloads from the simulation client, providing aggregated "
        "historical analytics, urban performance benchmarks, and multi-session leaderboards.<br/>"
        "4. <b>PostgreSQL 17 Database:</b> Serves as the persistent data sink and source, storing atomic city state saves, full-grid snapshots, "
        "and time-series logs while providing reliable recovery data during session load requests."
    )
    elements.append(Paragraph(p_dfd0, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    dfd0_path = os.path.join(FIG_DIR, "fig4_6_dfd0.png")
    if os.path.exists(dfd0_path):
        elements.append(Image(dfd0_path, width=475, height=280))
        elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Figure 4.4:</b> DFD Level 0 – Context Diagram", styles['FigCaption']))
    elements.append(PageBreak())

    # 4.4.3 DFD Level 1 (Process Breakdown)
    p_dfd1 = (
        "<b>4.4.3 Data Flow Diagram (DFD) – Level 1 (Process Breakdown):</b><br/>"
        "The Level 1 DFD decomposes the monolithic simulation boundary into four cohesive, interconnected functional processes "
        "interacting with four dedicated persistent data stores (<code>D1: CITY_SESSIONS</code>, <code>D2: ZONING_MATRIX_50x50</code>, "
        "<code>D3: METRICS_TIME_SERIES</code>, and <code>D4: GRIEVANCES_INCIDENTS</code>):<br/><br/>"
        "• <b>Process 1.0 (Spatial Matrix &amp; Construction Engine):</b> Intercepts mouse raycast plot coordinates from the mayor, "
        "performs geometric validation against the terrain heightmap and river boundary, verifies available treasury funds, updates "
        "the spatial tile records in <code>D2: ZONING_MATRIX_50x50</code>, and writes session metadata to <code>D1: CITY_SESSIONS</code>.<br/>"
        "• <b>Process 2.0 (Coupled ODE Simulation Loop):</b> Triggered at 2 Hz by the internal clock, this process reads the populated "
        "grid state from <code>D2</code>, executes coupled differential equations for tax revenue, utility distribution (BFS flow), "
        "and atmospheric Gaussian plume dispersion, writing aggregated statistical records to <code>D3: METRICS_TIME_SERIES</code>.<br/>"
        "• <b>Process 3.0 (Civic Grievance &amp; Disaster Manager):</b> Continuously scans metric deficits in <code>D3</code> (such as "
        "prolonged utility outages or high AQI smog). It instantiates citizen petition records in <code>D4: GRIEVANCES_INCIDENTS</code>, "
        "evaluates stochastic disaster probabilities, and triggers localized incident responses.<br/>"
        "• <b>Process 4.0 (FastAPI Cloud Telemetry Dispatch):</b> Extracts time-series packets from <code>D3</code>, serializes them "
        "into compliant JSON schemas, and dispatches asynchronous non-blocking HTTP POST requests to the cloud analytics backend."
    )
    elements.append(Paragraph(p_dfd1, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    dfd1_path = os.path.join(FIG_DIR, "fig4_7_dfd1.png")
    if os.path.exists(dfd1_path):
        elements.append(Image(dfd1_path, width=475, height=275))
        elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Figure 4.5:</b> DFD Level 1 – Process Breakdown", styles['FigCaption']))
    elements.append(PageBreak())

    # =========================================================================
    # 4.5 Object Diagram
    # =========================================================================
    elements.append(Paragraph("4.5 Object Diagram", styles['SecHeading1']))
    p_od1 = (
        "While class diagrams model static types, relationships, and signatures, an Object Diagram models a concrete, "
        "instantaneous snapshot of the system runtime state during active execution. It illustrates actual instantiated objects, "
        "their allocated attribute values, and runtime instance links at a specific execution tick.<br/><br/>"
        "Figure 4.6 captures the simulation runtime state at <b>Tick #12,450</b> (corresponding to approximately 103 minutes of active "
        "in-game urban governance). The diagram demonstrates the hierarchical composition and parameter binding across active entities:<br/>"
        "• <code>activePlayer : MayorPlayer</code> identifies the authenticated user session (<code>playerName = 'Mayor Sahil Kate'</code>, "
        "<code>currentSessionId = 'MUM-SIM-2026-V5'</code>), actively holding the Commercial High-Density zoning tool.<br/>"
        "• <code>metropolisSession : CityGrid</code> represents the master simulation container. At this instant, 1,420 out of 2,500 plots "
        "are actively populated, sustaining a thriving population of 48,650 citizens, a robust municipal treasury of ₹14,820,500.00, and an "
        "impressive Composite Smart City Index of <b>84.6 / 100 [Rating: Grade A]</b>.<br/>"
        "• Subordinate runtime instances model specific spatial and civic entities: <code>resSector4 : ZonePlot</code> (coordinates 18, 24, "
        "8.5% tax yield, 240 occupants), <code>clinicHospital01 : Building</code> (Level 2 facility operating at 94.5% efficiency), "
        "<code>marineDriveCorridor : Road</code> (4-lane avenue handling 840 vehicles/hour with only 32% congestion), "
        "<code>solarSubstation : Utility</code> (650 MW hybrid capacity servicing 480.2 MW peak demand with zero load shedding), and "
        "<code>citizen1041 : CitizenAgent</code> (a 29-year-old Data Engineer with 86.4% happiness contributing ₹4,200 monthly in municipal taxes)."
    )
    elements.append(Paragraph(p_od1, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    od_path = os.path.join(FIG_DIR, "fig_object_diagram.png")
    if os.path.exists(od_path):
        elements.append(Image(od_path, width=475, height=280))
        elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Figure 4.6:</b> Object Diagram Illustrating Runtime Instances", styles['FigCaption']))
    elements.append(Spacer(1, 6))

    p_od2 = (
        "<b>Runtime State Analysis &amp; Memory Allocation:</b><br/>"
        "The object diagram confirms that memory usage remains tightly bounded throughout extended simulation runs. Subordinate domain "
        "entities are allocated once within pre-warmed object pools during scene initialization, preventing runtime garbage collection "
        "spikes. Instance links reflect direct memory pointer references, ensuring that navigational lookups between citizen agents, "
        "road segments, and residential plots operate with sub-millisecond execution times."
    )
    elements.append(Paragraph(p_od2, styles['AcademicBody']))
    elements.append(PageBreak())

    # =========================================================================
    # 4.6 Sequence Diagram
    # =========================================================================
    elements.append(Paragraph("4.6 Sequence Diagram", styles['SecHeading1']))
    p_seq1 = (
        "The Sequence Diagram models the chronological message exchange and execution timeline between collaborating system lifelines. "
        "It provides a time-ordered view of synchronous method calls, asynchronous callback responses, branching conditional frames, "
        "and telemetry dispatch sequences during a core user transaction.<br/><br/>"
        "Figure 4.7 traces the complete lifecycle of a mayor placing a new healthcare facility (District Clinic) on plot (18, 24), "
        "tracing interactions across six distinct lifelines: <code>Mayor (User)</code>, <code>UI Controller</code>, "
        "<code>Simulation Engine</code>, <code>CityGrid Matrix</code>, <code>Budget Treasury</code>, and <code>FastAPI Telemetry</code>.<br/><br/>"
        "The procedural message sequence unfolds systematically:<br/>"
        "1. <b>User Invocation (Messages 1–2):</b> The mayor clicks the clinic building icon and targets plot (18, 24). The UI controller "
        "captures the raycast hit point and dispatches a validated placement request to the simulation engine.<br/>"
        "2. <b>Spatial &amp; Boundary Validation (Message 3):</b> The engine queries <code>CityGrid Matrix</code> to confirm the target plot "
        "is free, non-steep, and does not collide with the river procedural mesh. The grid returns status <code>CellFreeAndBuildable</code>.<br/>"
        "3. <b>Fiscal Solvency Check (Message 4):</b> The engine requests funds approval from <code>Budget Treasury</code> for the ₹45,000 "
        "construction fee. The treasury checks current liquidity and confirms sufficient capital.<br/>"
        "4. <b>Alternative Execution Frame (alt [Valid vs Invalid]):</b><br/>"
        "&nbsp;&nbsp;• <i>Success Path (Messages 5a–5d):</i> If coordinates and funds are valid, the engine deducts ₹45,000 from the treasury, "
        "instantiates the 3D clinic mesh in the scene, registers the structure in the spatial index, and dispatches an asynchronous HTTP POST "
        "telemetry record to the FastAPI backend. The HUD display immediately updates the treasury balance and CSCI score.<br/>"
        "&nbsp;&nbsp;• <i>Error Path (Messages 5e):</i> If the plot is obstructed or funds are insufficient, the engine aborts the transaction, "
        "instructing the UI controller to display a red boundary highlight, play an invalid-action sound, and display a descriptive warning."
    )
    elements.append(Paragraph(p_seq1, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    seq_path = os.path.join(FIG_DIR, "fig4_5_sequence.png")
    if os.path.exists(seq_path):
        elements.append(Image(seq_path, width=475, height=290))
        elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Figure 4.7:</b> Sequence Diagram for Simulation Tick &amp; Telemetry Flow", styles['FigCaption']))
    elements.append(PageBreak())

    # =========================================================================
    # 4.7 Activity Diagram
    # =========================================================================
    elements.append(Paragraph("4.7 Activity Diagram", styles['SecHeading1']))
    p_act1 = (
        "The Activity Diagram models the dynamic control flow, algorithmic decision nodes, and procedural workflows governing "
        "building placement, zoning allocation, and simulation update cycles. Unlike sequence diagrams which emphasize object lifelines, "
        "activity diagrams emphasize the procedural step-by-step logic, branching guard conditions, and swimlane responsibilities.<br/><br/>"
        "Figure 4.8 organizes the simulation workflow across three structural swimlanes:<br/>"
        "• <b>Swimlane 1 (Mayor UI Controller):</b> Encompasses user interaction events, tool selection, cursor raycasting onto the terrain, "
        "and error visualization.<br/>"
        "• <b>Swimlane 2 (Spatial Validation Engine):</b> Contains the mathematical decision nodes that validate spatial feasibility, "
        "evaluating slope thresholds, water mask intersections, and municipal treasury balances.<br/>"
        "• <b>Swimlane 3 (Simulation Kernel &amp; Cloud):</b> Handles transaction commitment, 3D structural instantiation, coupled differential "
        "equation updates (power, water, AQI, traffic), and asynchronous cloud telemetry synchronization.<br/><br/>"
        "The activity flow features rigorous guard conditions: <code>[Terrain Valid? - Water/Steep Collision]</code> and "
        "<code>[Treasury Sufficient? - Fiscal Deficit Check]</code>. Only when both guard conditions evaluate to <i>True</i> does the workflow "
        "commit funds and instantiate the building. The simulation then seamlessly executes its differential update cycle, broadcasting "
        "the updated urban indicators to the cloud and concluding at the terminal activity node."
    )
    elements.append(Paragraph(p_act1, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    act_path = os.path.join(FIG_DIR, "fig4_8_activity.png")
    if os.path.exists(act_path):
        elements.append(Image(act_path, width=475, height=275))
        elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Figure 4.8:</b> Activity Diagram for Building Placement &amp; Zoning Workflow", styles['FigCaption']))
    elements.append(PageBreak())

    # =========================================================================
    # 4.8 Component Model
    # =========================================================================
    elements.append(Paragraph("4.8 Component Model", styles['SecHeading1']))
    p_comp1 = (
        "The Component Diagram models the physical and logical modular decomposition of the Smart City Management Simulator. It defines "
        "the replaceable software components, their encapsulated boundaries, and the explicit interface contracts through which they "
        "collaborate across the three architectural tiers.<br/><br/>"
        "The architecture is partitioned into three decoupled tiers:<br/>"
        "• <b>Tier 1: Presentation &amp; Client Interface (Unity 6.3 LTS):</b> Encompasses the <code>UnityHUDController</code> (providing "
        "the <code>IHeadsUpDisplay</code> and <code>IMayorInputHandler</code> interfaces), the <code>SceneViewportRenderer</code> (governing "
        "camera navigation and shaders), the <code>SimulationClockTimer</code> (providing <code>ITickTrigger</code> at 2 Hz), and the "
        "<code>LocalAudioDialogueManager</code> for civic audio feedback.<br/>"
        "• <b>Tier 2: Simulation Engine Core (C# Multi-Threaded Kernel):</b> Implements the computational heart of the platform. The "
        "<code>SpatialGridManager</code> exposes <code>IZoningAllocator</code> and <code>ICollisionMatrix</code>; the <code>CoupledODEDifferentialEngine</code> "
        "encapsulates <code>IEconomicTaxLoop</code> and <code>IAQIPlumeSimulator</code>; the <code>CitizenAIAgentEngine</code> drives commute routing; "
        "and the <code>DisasterKernelDispatcher</code> manages emergency crisis propagation.<br/>"
        "• <b>Tier 3: Backend Telemetry &amp; Persistence (FastAPI &amp; PostgreSQL):</b> The <code>FastAPITelemetryRouter</code> exposes high-speed "
        "REST endpoints (<code>POST /telemetry</code>, <code>GET /metrics/csci</code>); the <code>SQLAlchemyORMDataLayer</code> provides data repository "
        "contracts; and the <code>PostgreSQLDatabaseEngine</code> provides durable ACID storage, feeding the <code>ChartJSAnalyticsDashboard</code>.<br/><br/>"
        "By enforcing well-defined interface contracts, any tier can be updated or refactored independently without breaking downstream dependencies."
    )
    elements.append(Paragraph(p_comp1, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    comp_path = os.path.join(FIG_DIR, "fig4_2_component_diagram.png")
    if os.path.exists(comp_path):
        elements.append(Image(comp_path, width=475, height=264))
        elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Figure 4.9:</b> Component Diagram Showing Tier Interconnections", styles['FigCaption']))
    elements.append(PageBreak())

    # =========================================================================
    # 4.9 Deployment Diagram
    # =========================================================================
    elements.append(Paragraph("4.9 Deployment Diagram", styles['SecHeading1']))
    p_dep1 = (
        "The Deployment Diagram maps the physical execution nodes, hardware infrastructure, and network communication topologies "
        "required to run the Smart City Management Simulator in production. It depicts how software artifacts are distributed across "
        "client workstations and cloud hosting environments.<br/><br/>"
        "The platform deployment topology comprises three distinct computational nodes:<br/>"
        "• <b>Client Workstation Node (Mayor Hardware):</b> A 64-bit personal computer (Windows 10/11 x64, minimum 8 GB RAM, dedicated DirectX 12 / "
        "Vulkan GPU). It hosts the standalone executable <code>SmartCitySimulator.exe</code>, the Unity 6.3 runtime engine, and an embedded "
        "local SQLite cache (<code>Saves.db</code>) that ensures offline gameplay continuity when network connectivity is disrupted.<br/>"
        "• <b>Cloud Application Server Node:</b> A cloud virtual machine or Docker container running Ubuntu 24.04 LTS. It executes the "
        "asynchronous <code>Uvicorn ASGI Web Server</code>, hosting the FastAPI Python 3.11 runtime, Pydantic validation schemas, JWT authentication "
        "middleware, and the SQLAlchemy 2.0 ORM pooling engine.<br/>"
        "• <b>Enterprise Database Server Node:</b> A dedicated database server instance running PostgreSQL 17.2 on TCP/IP port 5432. It maintains "
        "relational session state, partitioned telemetry tables, Write-Ahead Logging (WAL) archives, and an automated hourly snapshot backup service.<br/><br/>"
        "<b>Network Communication Protocols:</b> Communication between the Client Workstation and Cloud Server utilizes HTTP/2 over TLS (Port 8000/443) "
        "for REST transactions and low-overhead WebSockets for live telemetry streaming. The Application Server communicates with the Database Node "
        "via persistent, pooled TCP/IP database connections, ensuring sub-50ms round-trip latency."
    )
    elements.append(Paragraph(p_dep1, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    dep_path = os.path.join(FIG_DIR, "fig_deployment_diagram.png")
    if os.path.exists(dep_path):
        elements.append(Image(dep_path, width=475, height=275))
        elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Figure 4.10:</b> Deployment Diagram Across Unity Client, FastAPI and Database Cloud", styles['FigCaption']))
    elements.append(PageBreak())
'''

# Read existing content_chapters_4_5.py
with open(r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\content_chapters_4_5.py", "r", encoding="utf-8") as f:
    orig = f.read()

# Locate Chapter 4 start and Chapter 5 start
ch4_start_marker = "    # CHAPTER 4: SYSTEM MODELING USING UML"
ch5_start_marker = "    # CHAPTER 5: SYSTEM ARCHITECTURE DESIGN"

idx_start = orig.find(ch4_start_marker)
idx_end = orig.find(ch5_start_marker)

if idx_start == -1 or idx_end == -1:
    print(f"Error: Markers not found! idx_start={idx_start}, idx_end={idx_end}")
else:
    # Look back a line to catch the comments banner
    banner_start = orig.rfind("    # =========================================================================", 0, idx_start)
    if banner_start != -1:
        idx_start = banner_start
        
    new_content = orig[:idx_start] + new_chapter_4 + orig[idx_end:]
    with open(r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\content_chapters_4_5.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("SUCCESS: content_chapters_4_5.py updated with expanded Chapter 4!")
