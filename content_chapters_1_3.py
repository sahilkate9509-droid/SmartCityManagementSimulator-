import os
from reportlab.platypus import Paragraph, Spacer, Table, PageBreak, HRFlowable, TableStyle, Image
from reportlab.lib import colors

def build_chapters_1_3(styles, PRINTABLE_WIDTH, FIG_DIR):
    elements = []

    # =========================================================================
    # MODULE 1 HEADER
    # =========================================================================
    elements.append(Paragraph("<b>MODULE 1</b><br/><b>PROBLEM IDENTIFICATION, REQUIREMENT ENGINEERING &amp; SYSTEM DESIGN PHASE</b>", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=2.0, color=colors.HexColor("#1e3a8a"), spaceAfter=14, spaceBefore=4))
    elements.append(Spacer(1, 4))

    # =========================================================================
    # CHAPTER 1: PROBLEM IDENTIFICATION & FEASIBILITY STUDY
    # =========================================================================
    elements.append(Paragraph("<b>CHAPTER 1</b><br/><b>PROBLEM IDENTIFICATION &amp; FEASIBILITY STUDY</b>", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=12, spaceBefore=4))

    # Role and Responsibility
    elements.append(Paragraph("<b>Role and Responsibility</b>", styles['SecHeading1']))
    p_meta = (
        "• <b>Project Title:</b> Smart City Management Simulator<br/>"
        "• <b>Student Name:</b> Mr. Sahil Vishal Kate (Roll No. 9041)<br/>"
        "• <b>Class:</b> T.Y.B.Sc. (Computer Science – Sem V)<br/>"
        "• <b>Project Guide:</b> Prof. Aarti Gawai<br/>"
        "• <b>Institutional Department:</b> Department of Computer Science, The D. G. Ruparel College"
    )
    elements.append(Paragraph(p_meta, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    # Table 1.1: Role and Responsibility Across Project Phases
    elements.append(Paragraph("<b>Table 1.1: Role and Responsibility Across Project Phases</b>", styles['SecHeading2']))
    r_table_data = [
        [Paragraph("<b>Module / Phase</b>", styles['TableHead']),
         Paragraph("<b>Key Engineering Responsibilities Executed</b>", styles['TableHead'])],
        
        [Paragraph("<b>Module 1: Problem Identification &amp; Requirement Engineering</b>", styles['TableCellBold']),
         Paragraph("Conducted literature review of existing urban simulation models (SimCity, Cities: Skylines, OpenCity), identified civic management bottlenecks, performed the TELOS feasibility study, and authored IEEE Std 830-1998 Functional and Non-Functional Requirements specifications.", styles['TableCell'])],
        
        [Paragraph("<b>Module 1: SDLC Planning &amp; UML System Modeling</b>", styles['TableCellBold']),
         Paragraph("Structured the 5-Iteration Agile incremental sprint roadmap, constructed the Work Breakdown Structure (WBS) and Gantt Chart, and designed the Event Table, Entity-Relationship (ER) diagram, Data Flow Diagrams (DFD Level 0 &amp; Level 1), Use Case, Class, Object, Sequence, Activity, Component, and Deployment diagrams.", styles['TableCell'])],
        
        [Paragraph("<b>Module 1: 3-Tier Architecture &amp; Database Schema Design</b>", styles['TableCellBold']),
         Paragraph("Architected the decoupled 3-tier simulation and telemetry infrastructure and designed six relational schemas in PostgreSQL 17 / SQLite 3 covering SimulationSession, CityMetrics, ZoningGrid, CitizenPetition, DisasterIncident, and TelemetryLog.", styles['TableCell'])],
        
        [Paragraph("<b>Module 2: Full-Stack Simulation Development</b>", styles['TableCellBold']),
         Paragraph("Engineered the procedural 3D terrain grid, sinusoidal river generation, multi-agent citizen dynamics, pure differential math subsystems (Economy, Utilities, Demographics, AQI dispersion), and developed the FastAPI REST cloud telemetry server with async session logging.", styles['TableCell'])],
        
        [Paragraph("<b>Module 2: System Testing, Cloud Deployment &amp; Documentation</b>", styles['TableCellBold']),
         Paragraph("Executed 25 comprehensive test cases across Unit, Integration, and Black-Box System testing, verified steady 60 FPS rendering (&lt;16.6ms frame time), evaluated SUS usability metrics (87.5/100), configured GitHub CI version control, and authored the User Manual and final technical report.", styles['TableCell'])],
    ]
    r_table = Table(r_table_data, colWidths=[140, 347])
    r_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(r_table)
    elements.append(Spacer(1, 8))

    # 1.1 Background and Motivation
    elements.append(Paragraph("1.1 Background and Motivation", styles['SecHeading1']))
    p_bg = (
        "The twenty-first century is witnessing the most rapid demographic urbanization in recorded human history. "
        "According to projections by the United Nations Department of Economic and Social Affairs (UN DESA), over 68% of the global "
        "population will reside in urban agglomerations by 2050, adding an estimated 2.5 billion urban dwellers. "
        "Metropolises operate as hyper-complex, non-linear socio-technical systems characterized by tightly coupled feedback loops: "
        "a zoning policy or infrastructure expenditure in one municipal sector triggers cascading, counter-intuitive consequences across others.<br/><br/>"
        "Historically, the computational modeling of urban dynamics traces its intellectual origins to Jay W. Forrester's seminal work "
        "at MIT. Forrester's <i>Urban Dynamics</i> (1969) demonstrated that municipal systems exhibit non-intuitive feedback: constructing "
        "subsidized low-income housing without synchronized industrial employment creation often deepens systemic poverty by drawing jobseekers "
        "without expanding the tax base. Subsequent spatial economic theories—including Von Thünen's concentric bid-rent zones (1826), "
        "Christaller's Central Place Theory (1933), Burgess's Concentric Zone Model (1925), and Harris &amp; Ullman's Multiple Nuclei Model (1945)—"
        "further established that spatial equilibrium emerges organically from micro-level agent decisions.<br/><br/>"
        "The fundamental motivation for developing the <b>Smart City Management Simulator (Professional)</b> arises from the urgent need "
        "for an interactive, accessible, and mathematically rigorous computational sandbox—a true <b>urban digital twin</b>. By uniting "
        "real-time 3D spatial simulation in Unity 6.3 LTS with coupled differential mathematical models and an enterprise cloud telemetry "
        "backend powered by FastAPI and PostgreSQL/SQLite, this project provides students, researchers, and planners with an expressive "
        "decision-support environment."
    )
    elements.append(Paragraph(p_bg, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    # 1.2 Objectives
    elements.append(Paragraph("1.2 Objectives", styles['SecHeading1']))
    p_objs = (
        "The primary engineering and pedagogical objectives of the Smart City Management Simulator platform are:<br/>"
        "• <b>Architect a Real-Time Procedural 3D City Engine:</b> Build an interactive 50×50 grid simulation in Unity 6.3 LTS capable of procedural terrain synthesis, dynamic road networks, sinusoidal rivers, modular bridges, and moving citizen traffic at a steady 60 FPS.<br/>"
        "• <b>Formulate Coupled Differential Mathematical Subsystems:</b> Engineer deterministic, pure C# modules modeling Municipal Economy, Demographic Migration, Utility Corridors (Power/Water/Waste), Traffic Congestion, Environmental AQI Plume Dispersion, and Civic Services.<br/>"
        "• <b>Synthesize the Composite Smart City Index (CSCI):</b> Combine multi-sector telemetry into an aggregated, weighted 0–100 benchmark metric evaluating municipal balance, citizen happiness, fiscal solvency, and ecological sustainability.<br/>"
        "• <b>Build an Asynchronous Cloud Telemetry Backend:</b> Implement a decoupled FastAPI REST microservice with non-blocking SQLite/PostgreSQL persistence for automated simulation snapshots, historical charting, and audit logs.<br/>"
        "• <b>Implement Dynamic Citizen Petitions &amp; Emergency Incidents:</b> Provide an interactive event system with citizen grievances, heatwaves, transformer failures, and water main bursts requiring mayoral intervention."
    )
    elements.append(Paragraph(p_objs, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    # 1.3 Identification of a Real-World Problem
    elements.append(Paragraph("1.3 Identification of a Real-World Problem (Industry / Social / Institutional)", styles['SecHeading1']))
    p_prob = (
        "Urban planning institutions, students, and municipal administrative bodies face four critical bottlenecks in existing educational tools:<br/>"
        "• <b>Siloed &amp; Delayed Feedback (Institutional Gap):</b> Traditional urban management training relies on static GIS layers and historical spreadsheets that fail to convey dynamic, real-time causal feedback across municipal sectors.<br/>"
        "• <b>Commercial Software Oparity (Industry Challenge):</b> Commercial entertainment games (such as SimCity or Cities: Skylines) operate as closed-source 'black boxes' with proprietary, opaque math that cannot be mathematically audited or integrated with external data stores.<br/>"
        "• <b>Prohibitive Licensing &amp; Infrastructure Costs (Social Barrier):</b> Enterprise GIS suites (ArcGIS, Bentley OpenCities) require expensive licensing and dedicated server hardware, making them inaccessible to undergraduate students and public institutions.<br/>"
        "• <b>Fiscal-Ecological Blindspots (Pedagogical Bottleneck):</b> Existing simulators treat industrial growth and pollution independently, ignoring the coupled degradation of citizen health, labor productivity, and public healthcare costs."
    )
    elements.append(Paragraph(p_prob, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    # 1.4 Problem Justification and Scope Definition
    elements.append(Paragraph("1.4 Problem Justification and Scope Definition", styles['SecHeading1']))
    p_scope = (
        "• <b>Problem Justification:</b> To bridge the gap between visual game engines and academic decision-support systems, there is a clear need for an open-architecture 3-tier application merging procedural 3D spatial simulation with verified differential equations and cloud telemetry.<br/>"
        "• <b>Current Scope:</b> The simulator models a 50×50 spatial matrix (2,500 developable plots), six coupled mathematical subsystems, dynamic citizen petitions, emergency incidents, slot-based persistence, and historical telemetry auditing via FastAPI.<br/>"
        "• <b>Future Scope:</b> Planned extensions include AI-powered traffic light optimization via Reinforcement Learning, real-world OpenStreetMap GIS geo-importing, multi-player collaborative zoning sessions, and VR/AR mayoral command interfaces."
    )
    elements.append(Paragraph(p_scope, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    # 1.5 Stakeholder Identification & Beneficiary Analysis
    elements.append(Paragraph("1.5 Stakeholder Identification &amp; Beneficiary Analysis", styles['SecHeading1']))
    p_stake = (
        "• <b>Primary Beneficiaries (Undergraduate Students &amp; Self-Learners):</b> Gain zero-cost, interactive access to an authentic urban digital twin where complex policy trade-offs can be explored safely in real time.<br/>"
        "• <b>Secondary Beneficiaries (Urban Planners &amp; Academic Researchers):</b> Utilize the decoupled pure mathematical kernel and FastAPI telemetry stream to benchmark urban planning algorithms, run stress tests, and extract structured simulation datasets.<br/>"
        "• <b>System Administrators &amp; Developers:</b> Benefit from the modular 3-tier architecture, automated migration scripts, and clean separation between client graphics and server telemetry."
    )
    elements.append(Paragraph(p_stake, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    # 1.6 Feasibility Analysis (TELOS)
    elements.append(Paragraph("1.6 Feasibility Analysis (Technical, Economic, Operational, Legal, Schedule)", styles['SecHeading1']))
    p_telos = (
        "A comprehensive feasibility study was conducted using the standard <b>TELOS</b> framework to evaluate project viability:<br/><br/>"
        "1. <b>Technical Feasibility:</b> The client engine is powered by Unity 6.3 LTS and C# with zero-allocation memory loops, achieving a steady 60 FPS. The backend utilizes FastAPI (Python 3.11) with Uvicorn and SQLAlchemy 2.0 ORM for non-blocking asynchronous REST telemetry under 50ms latency.<br/>"
        "2. <b>Economic Feasibility:</b> Developed entirely using open-source SDKs and tools (Unity Personal, Python, FastAPI, SQLite 3, PostgreSQL, VS Code, Git) resulting in ₹0 software licensing expenditures.<br/>"
        "3. <b>Operational Feasibility:</b> Features an intuitive 3D spatial interface with orbit/pan camera controls, tooltips, and an accessible dark HUD that lowers cognitive friction for students and non-technical administrators.<br/>"
        "4. <b>Legal &amp; Ethical Feasibility:</b> Adheres strictly to MIT and Apache 2.0 open-source licenses. Simulation datasets are synthetic, ensuring zero PII (Personally Identifiable Information) exposure.<br/>"
        "5. <b>Schedule Feasibility:</b> Structured across five iterative Agile sprints, ensuring core mechanics, subsystems, telemetry, testing, and documentation were successfully delivered within the academic semester timeline."
    )
    elements.append(Paragraph(p_telos, styles['AcademicBody']))
    elements.append(PageBreak())

    # =========================================================================
    # CHAPTER 2: REQUIREMENT ENGINEERING
    # =========================================================================
    elements.append(Paragraph("<b>CHAPTER 2</b><br/><b>REQUIREMENT ENGINEERING</b>", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=12, spaceBefore=4))

    # 2.1 Functional Requirements Specification
    elements.append(Paragraph("2.1 Functional Requirements Specification", styles['SecHeading1']))
    p_fr_intro = (
        "The functional requirements define the operational capabilities, procedural generations, mathematical evaluations, "
        "and data processing pipelines of the Smart City Management Simulator platform:"
    )
    elements.append(Paragraph(p_fr_intro, styles['AcademicBody']))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>Table 2.1: Functional Requirements Specification Table</b>", styles['SecHeading2']))
    fr_data = [
        [Paragraph("<b>Req ID</b>", styles['TableHead']),
         Paragraph("<b>Module / Feature</b>", styles['TableHead']),
         Paragraph("<b>Functional Description</b>", styles['TableHead']),
         Paragraph("<b>Priority</b>", styles['TableHead'])],
        
        [Paragraph("<b>FR-01</b>", styles['TableCellBold']),
         Paragraph("Procedural Grid Generation", styles['TableCellBold']),
         Paragraph("The system shall procedurally generate a 50×50 terrain coordinate grid (2,500 plots) featuring sinusoidal river channels, dynamic bridge crossings, and coordinate boundary snapping.", styles['TableCell']),
         Paragraph("High", styles['TableCellBold'])],
        
        [Paragraph("<b>FR-02</b>", styles['TableCellBold']),
         Paragraph("Zoning &amp; Building Placement", styles['TableCellBold']),
         Paragraph("The system shall allow users to demarcate Residential, Commercial, and Industrial zones, construct municipal facilities (power, water, police, fire, clinics), and validate placement bounds.", styles['TableCell']),
         Paragraph("High", styles['TableCellBold'])],
        
        [Paragraph("<b>FR-03</b>", styles['TableCellBold']),
         Paragraph("Utility Grid Simulation", styles['TableCellBold']),
         Paragraph("The system shall simulate the generation, BFS graph propagation, and per-building consumption of electrical power and clean water, flagging unserviced structures with warning icons.", styles['TableCell']),
         Paragraph("High", styles['TableCellBold'])],
        
        [Paragraph("<b>FR-04</b>", styles['TableCellBold']),
         Paragraph("Multi-Agent Traffic Engine", styles['TableCellBold']),
         Paragraph("The system shall compute volume-over-capacity ratios across road networks, simulate commuting vehicular agents between zones, and calculate cumulative pavement wear.", styles['TableCell']),
         Paragraph("High", styles['TableCellBold'])],
        
        [Paragraph("<b>FR-05</b>", styles['TableCellBold']),
         Paragraph("Municipal Economy &amp; Tax", styles['TableCellBold']),
         Paragraph("The system shall collect multi-bracket tax revenues across active zones, deduct building operating expenditures, track municipal debt interest, and maintain treasury reserves.", styles['TableCell']),
         Paragraph("High", styles['TableCellBold'])],
        
        [Paragraph("<b>FR-06</b>", styles['TableCellBold']),
         Paragraph("Environmental AQI Dispersion", styles['TableCellBold']),
         Paragraph("The system shall calculate industrial particulate emissions, apply park canopy offsets, simulate wind dispersion plumes, and render real-time Air Quality Index overlays.", styles['TableCell']),
         Paragraph("High", styles['TableCellBold'])],
        
        [Paragraph("<b>FR-07</b>", styles['TableCellBold']),
         Paragraph("Civic Petitions &amp; Disasters", styles['TableCellBold']),
         Paragraph("The system shall dynamically generate citizen grievances upon service deficits and trigger random civic disasters (heatwaves, transformer bursts, water leaks) requiring intervention.", styles['TableCell']),
         Paragraph("Medium", styles['TableCellBold'])],
        
        [Paragraph("<b>FR-08</b>", styles['TableCellBold']),
         Paragraph("FastAPI Cloud Telemetry", styles['TableCellBold']),
         Paragraph("The system shall serialize runtime simulation snapshots and asynchronously transmit telemetry packets to the FastAPI server for persistent database logging.", styles['TableCell']),
         Paragraph("High", styles['TableCellBold'])],
        
        [Paragraph("<b>FR-09</b>", styles['TableCellBold']),
         Paragraph("Analytical Dashboard &amp; CSCI", styles['TableCellBold']),
         Paragraph("The system shall aggregate multi-subsystem telemetry into the normalized Composite Smart City Index (CSCI) and render historical trend lines and diagnostic breakdowns.", styles['TableCell']),
         Paragraph("Medium", styles['TableCellBold'])],
    ]
    fr_table = Table(fr_data, colWidths=[45, 110, 280, 52])
    fr_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    elements.append(fr_table)
    elements.append(Spacer(1, 6))

    # 2.2 Non-Functional Requirements Specification
    elements.append(Paragraph("2.2 Non-Functional Requirements Specification", styles['SecHeading1']))
    elements.append(Paragraph("<b>Table 2.2: Non-Functional Requirements Specification Table</b>", styles['SecHeading2']))
    nfr_data = [
        [Paragraph("<b>Req ID</b>", styles['TableHead']),
         Paragraph("<b>Category</b>", styles['TableHead']),
         Paragraph("<b>Metric / Specification</b>", styles['TableHead']),
         Paragraph("<b>Priority</b>", styles['TableHead'])],
        
        [Paragraph("<b>NFR-01</b>", styles['TableCellBold']),
         Paragraph("Rendering Performance", styles['TableCellBold']),
         Paragraph("The 3D client engine shall maintain a steady frame rate of >= 60 FPS on mid-tier hardware with frame times bounded under 16.6 milliseconds.", styles['TableCell']),
         Paragraph("High", styles['TableCellBold'])],
        
        [Paragraph("<b>NFR-02</b>", styles['TableCellBold']),
         Paragraph("Telemetry Latency", styles['TableCellBold']),
         Paragraph("Asynchronous HTTP telemetry ingestion requests to the FastAPI backend shall complete with round-trip latency under 50 milliseconds.", styles['TableCell']),
         Paragraph("High", styles['TableCellBold'])],
        
        [Paragraph("<b>NFR-03</b>", styles['TableCellBold']),
         Paragraph("Relational Integrity", styles['TableCellBold']),
         Paragraph("The database shall enforce foreign-key constraints, unique session slugs, and ACID compliance across SQLite and PostgreSQL backends.", styles['TableCell']),
         Paragraph("High", styles['TableCellBold'])],
        
        [Paragraph("<b>NFR-04</b>", styles['TableCellBold']),
         Paragraph("Memory Stability", styles['TableCellBold']),
         Paragraph("The client simulation loop shall operate with zero dynamic heap allocations during runtime, demonstrating &lt;0.5% memory drift over 72-hour stress testing.", styles['TableCell']),
         Paragraph("High", styles['TableCellBold'])],
        
        [Paragraph("<b>NFR-05</b>", styles['TableCellBold']),
         Paragraph("Usability &amp; HCI", styles['TableCellBold']),
         Paragraph("The interface shall achieve a standardized System Usability Scale (SUS) score of >= 80.0 / 100, featuring high-contrast typography and tooltips.", styles['TableCell']),
         Paragraph("Medium", styles['TableCellBold'])],
        
        [Paragraph("<b>NFR-06</b>", styles['TableCellBold']),
         Paragraph("Cross-Platform Support", styles['TableCellBold']),
         Paragraph("The simulator shall compile seamlessly to Windows x64 Standalone Executable, macOS, and WebGL browser runtimes.", styles['TableCell']),
         Paragraph("Medium", styles['TableCellBold'])],
    ]
    nfr_table = Table(nfr_data, colWidths=[50, 105, 275, 57])
    nfr_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    elements.append(nfr_table)
    elements.append(Spacer(1, 6))

    # 2.3 Use-Case Analysis & Actor Profiles
    elements.append(Paragraph("2.3 Use-Case Analysis &amp; Actor Profiles", styles['SecHeading1']))
    p_actors = (
        "The system interactions are modeled around four primary actors and five core use-case narratives:<br/>"
        "• <b>Actor Profiles:</b><br/>"
        "1. <b>Mayor / Lead Urban Planner:</b> Authenticates into the simulation session, demarcates zoning, builds municipal infrastructure, balances fiscal tax rates, resolves citizen petitions, and initiates disaster relief actions.<br/>"
        "2. <b>Citizen Multi-Agents:</b> Autonomous algorithmic entities that commute between residential and commercial/industrial zones, consume utility capacities, generate tax receipts, produce solid waste, and file petitions when service thresholds fail.<br/>"
        "3. <b>Cloud Telemetry Auditor:</b> Municipal analyst or academic researcher who queries the FastAPI REST API, inspects historical city snapshots, audits fiscal records, and benchmarks CSCI trends.<br/>"
        "4. <b>System Administrator:</b> Manages database backups, resets test telemetry tables, provisions user accounts, and monitors FastAPI server health.<br/>"
        "• <b>Core Use-Case Narratives:</b><br/>"
        "1. <b>UC-01 (Session Setup &amp; Grid Initialization):</b> The Mayor configures simulation parameters, selects terrain seed, and the engine generates the 50×50 procedural world grid.<br/>"
        "2. <b>UC-02 (Zoning &amp; Infrastructure Construction):</b> The Mayor places roads, residential zones, power plants, and water towers with real-time placement and cost validation.<br/>"
        "3. <b>UC-03 (Subsystem Differential Simulation Tick):</b> Every 0.5 seconds, the engine updates coupled differential equations across Economy, Utilities, Demographics, Traffic, and AQI.<br/>"
        "4. <b>UC-04 (Citizen Petition &amp; Disaster Resolution):</b> The Mayor reviews active grievances (power blackouts, dirty air) and dispatches emergency services or enacts policy reforms.<br/>"
        "5. <b>UC-05 (Cloud Telemetry &amp; Historical Auditing):</b> The client serializes city metrics into JSON and dispatches async telemetry packets to FastAPI for persistent logging."
    )
    elements.append(Paragraph(p_actors, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    # 2.4 Requirement Prioritization (MoSCoW Matrix)
    elements.append(Paragraph("2.4 Requirement Prioritization (MoSCoW Matrix)", styles['SecHeading1']))
    elements.append(Paragraph("<b>Table 2.3: MoSCoW Requirement Prioritization Matrix</b>", styles['SecHeading2']))
    moscow_data = [
        [Paragraph("<b>Priority Level</b>", styles['TableHead']),
         Paragraph("<b>Requirement IDs</b>", styles['TableHead']),
         Paragraph("<b>Deliverable Scope &amp; Justification</b>", styles['TableHead'])],
        
        [Paragraph("<b>Must Have (M)</b>", styles['TableCellBold']),
         Paragraph("FR-01, FR-02, FR-03, FR-04, FR-05, NFR-01, NFR-03", styles['TableCell']),
         Paragraph("Essential core engine: 50×50 procedural grid, zoning/placement, coupled Economy/Utility/Traffic simulation, 60 FPS rendering, and relational SQLite persistence.", styles['TableCell'])],
        
        [Paragraph("<b>Should Have (S)</b>", styles['TableCellBold']),
         Paragraph("FR-06, FR-08, FR-09, NFR-02, NFR-04", styles['TableCell']),
         Paragraph("High-value analytical features: Environmental AQI dispersion overlays, FastAPI REST telemetry ingestion, Composite Smart City Index (CSCI), and zero-leak memory loops.", styles['TableCell'])],
        
        [Paragraph("<b>Could Have (C)</b>", styles['TableCellBold']),
         Paragraph("FR-07, NFR-05, NFR-06", styles['TableCell']),
         Paragraph("Dynamic enhancements: Citizen petition grievances, emergency disasters (heatwaves/outages), dynamic day-night visual cycles, and WebGL browser compilation.", styles['TableCell'])],
        
        [Paragraph("<b>Won't Have (W)</b>", styles['TableCellBold']),
         Paragraph("Future Scope Items", styles['TableCell']),
         Paragraph("Deferred to future releases: Real-world OpenStreetMap GIS geo-importing, Deep Reinforcement Learning traffic controllers, and VR/AR immersive command headsets.", styles['TableCell'])],
    ]
    moscow_table = Table(moscow_data, colWidths=[90, 110, 287])
    moscow_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(moscow_table)
    elements.append(Spacer(1, 6))

    # 2.5 Constraints and Assumptions
    elements.append(Paragraph("2.5 Constraints and Assumptions", styles['SecHeading1']))
    p_ca = (
        "• <b>System Constraints:</b><br/>"
        "o <i>Spatial Matrix Limits:</i> The simulation universe is constrained to a 50×50 discrete spatial matrix (2,500 developable tiles) to guarantee 60 FPS execution on baseline hardware.<br/>"
        "o <i>Discrete Simulation Rate:</i> Subsystem differential calculations update at a fixed 0.5-second tick interval (2 Hz), decoupling simulation physics from rendering frame rates.<br/>"
        "o <i>Network Independence:</i> The client operates autonomously offline, queuing telemetry in memory when disconnected from the FastAPI server.<br/>"
        "• <b>Operational Assumptions:</b><br/>"
        "o Users possess standard desktop hardware with a dedicated GPU (e.g., NVIDIA GTX 1050 or AMD Radeon equivalent) running Windows 10/11.<br/>"
        "o The Mayor understands fundamental urban planning principles (zoning proximity, tax balance, and environmental mitigation)."
    )
    elements.append(Paragraph(p_ca, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    # 2.6 Preliminary Product Description & Technology Stack Survey
    elements.append(Paragraph("2.6 Preliminary Product Description &amp; Technology Stack Survey", styles['SecHeading1']))
    p_tech = (
        "The Smart City Management Simulator is engineered as a decoupled 3-tier architecture uniting high-performance 3D graphics, "
        "pure functional mathematical kernels, and an enterprise cloud telemetry service:<br/><br/>"
        "• <b>Front-End Presentation &amp; Simulation Layer (Unity 6.3 LTS &amp; C#):</b> Handles real-time 3D procedural terrain generation, "
        "mesh batching, raycast building placement, dynamic day-night atmospheric lighting, weather particle systems, and the responsive dark Heads-Up Display (uGUI).<br/>"
        "• <b>Business Logic &amp; Mathematical Engine Layer (C# Static Pure Functions):</b> Houses decoupled, testable mathematical methods "
        "calculating tax revenues, population migration vectors, BFS utility propagation, volume-capacity traffic congestion, and Gaussian AQI dispersion.<br/>"
        "• <b>Cloud Telemetry &amp; Persistence Layer (FastAPI, Python 3.11 &amp; SQLite/PostgreSQL):</b> Ingests asynchronous HTTP snapshot packets, "
        "enforces relational foreign-key integrity via SQLAlchemy 2.0 ORM, and serves historical KPI analytics to interactive web consoles.<br/>"
        "• <b>Development &amp; Testing Tooling:</b> Visual Studio Code, JetBrains Rider, Postman, PyTest, Unity Test Framework, Git, and GitHub."
    )
    elements.append(Paragraph(p_tech, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    # 2.7 Conceptual Models & Literature Review
    elements.append(Paragraph("2.7 Conceptual Models (Literature Review of Existing Urban Systems)", styles['SecHeading1']))
    p_lit = (
        "Prior to architecting the platform, existing urban simulation software and Computer-Assisted Learning tools were analyzed "
        "to identify architectural and educational limitations:"
    )
    elements.append(Paragraph(p_lit, styles['AcademicBody']))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>Table 2.4: Comparative Analysis Matrix of Existing Simulation Systems</b>", styles['SecHeading2']))
    comp_data = [
        [Paragraph("<b>Feature / Capability</b>", styles['TableHead']),
         Paragraph("<b>Smart City Simulator (Proposed)</b>", styles['TableHead']),
         Paragraph("<b>SimCity 4</b>", styles['TableHead']),
         Paragraph("<b>Cities: Skylines</b>", styles['TableHead']),
         Paragraph("<b>OpenCity</b>", styles['TableHead'])],
        
        [Paragraph("<b>Academic Auditability</b>", styles['TableCellBold']),
         Paragraph("Yes (Open pure math kernel)", styles['TableCell']),
         Paragraph("No (Closed proprietary)", styles['TableCell']),
         Paragraph("No (Closed proprietary)", styles['TableCell']),
         Paragraph("Partial (Open source)", styles['TableCell'])],
        
        [Paragraph("<b>Cloud Telemetry API</b>", styles['TableCellBold']),
         Paragraph("Yes (FastAPI REST JSON)", styles['TableCell']),
         Paragraph("No", styles['TableCell']),
         Paragraph("No (Local save files)", styles['TableCell']),
         Paragraph("No", styles['TableCell'])],
        
        [Paragraph("<b>Coupled Differential Math</b>", styles['TableCellBold']),
         Paragraph("Yes (6 coupled subsystems)", styles['TableCell']),
         Paragraph("Partial (Statistical tables)", styles['TableCell']),
         Paragraph("Yes (Agent-based)", styles['TableCell']),
         Paragraph("Basic (Cellular automata)", styles['TableCell'])],
        
        [Paragraph("<b>Composite Index (CSCI)</b>", styles['TableCellBold']),
         Paragraph("Yes (0–100 weighted metric)", styles['TableCell']),
         Paragraph("No (Approval rating only)", styles['TableCell']),
         Paragraph("No (Happiness % only)", styles['TableCell']),
         Paragraph("No", styles['TableCell'])],
        
        [Paragraph("<b>Procedural Water &amp; Bridges</b>", styles['TableCellBold']),
         Paragraph("Yes (Sinusoidal dynamic mesh)", styles['TableCell']),
         Paragraph("No (Static terrain heightmap)", styles['TableCell']),
         Paragraph("Yes (Physics water engine)", styles['TableCell']),
         Paragraph("No (Flat grid)", styles['TableCell'])],
        
        [Paragraph("<b>Licensing &amp; Cost</b>", styles['TableCellBold']),
         Paragraph("Free / Open-Source (₹0)", styles['TableCell']),
         Paragraph("Commercial ($19.99)", styles['TableCell']),
         Paragraph("Commercial ($29.99 + DLCs)", styles['TableCell']),
         Paragraph("Free / Open-Source", styles['TableCell'])],
    ]
    comp_table = Table(comp_data, colWidths=[105, 105, 90, 95, 92])
    comp_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    elements.append(comp_table)
    elements.append(PageBreak())

    # =========================================================================
    # CHAPTER 3: SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC) PLANNING
    # =========================================================================
    elements.append(Paragraph("<b>CHAPTER 3</b><br/><b>SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC) PLANNING</b>", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=12, spaceBefore=4))

    # 3.1 Selection of SDLC Model
    elements.append(Paragraph("3.1 Selection of SDLC Model (Agile Incremental Sprint Model)", styles['SecHeading1']))
    p_sdlc = (
        "The Smart City Management Simulator was engineered using the <b>Agile Incremental Sprint Methodology</b>. "
        "Rather than employing a rigid linear Waterfall process, the Agile model allowed the complex full-stack simulation to be broken "
        "down into five modular, testable iterations. Each two-week sprint delivered a working functional increment—starting from requirement "
        "engineering and spatial grid generation, progressing through coupled mathematical subsystems and building placement, and culminating "
        "in FastAPI telemetry ingestion, automated performance benchmarking, and system testing. This iterative model facilitated continuous "
        "profiling, GC memory optimization, and seamless integration between the Unity client and FastAPI cloud backend."
    )
    elements.append(Paragraph(p_sdlc, styles['AcademicBody']))
    elements.append(Spacer(1, 6))

    # 3.2 Work Breakdown Structure (WBS)
    elements.append(Paragraph("3.2 Work Breakdown Structure (WBS)", styles['SecHeading1']))
    elements.append(Paragraph("<b>Table 3.1: Work Breakdown Structure (WBS) &amp; Sprint Deliverables</b>", styles['SecHeading2']))
    wbs_data = [
        [Paragraph("<b>WBS ID</b>", styles['TableHead']),
         Paragraph("<b>Iteration / Phase</b>", styles['TableHead']),
         Paragraph("<b>Core Engineering Tasks &amp; Deliverables</b>", styles['TableHead']),
         Paragraph("<b>Milestone Output</b>", styles['TableHead'])],
        
        [Paragraph("<b>Iteration 1</b>", styles['TableCellBold']),
         Paragraph("Requirements &amp; Architecture Planning", styles['TableCellBold']),
         Paragraph("Problem identification, TELOS feasibility analysis, IEEE Std 830-1998 SRS specification, and complete StarUML system modeling (ER, DFD, Use Case, Class, Sequence, Activity).", styles['TableCell']),
         Paragraph("Approved SRS &amp; Complete UML Set", styles['TableCellBold'])],
        
        [Paragraph("<b>Iteration 2</b>", styles['TableCellBold']),
         Paragraph("Procedural Grid &amp; World Generation", styles['TableCellBold']),
         Paragraph("Implementing the 50×50 spatial matrix, sinusoidal river generation, procedural bridge instantiation, raycast placement grid, and camera orbit/pan navigation scripts.", styles['TableCell']),
         Paragraph("Interactive 3D Procedural Grid Engine", styles['TableCellBold'])],
        
        [Paragraph("<b>Iteration 3</b>", styles['TableCellBold']),
         Paragraph("Coupled Mathematical Subsystems", styles['TableCellBold']),
         Paragraph("Engineering static pure C# methods for Economy (tax/expenses), Demographics (migration/housing), Utilities (power/water BFS propagation), Traffic, and AQI Gaussian dispersion.", styles['TableCell']),
         Paragraph("Deterministic 6-Subsystem Simulation Kernel", styles['TableCellBold'])],
        
        [Paragraph("<b>Iteration 4</b>", styles['TableCellBold']),
         Paragraph("FastAPI Telemetry &amp; Persistence", styles['TableCellBold']),
         Paragraph("Developing the asynchronous FastAPI telemetry ingestion endpoint, SQLAlchemy database schemas, slot-based persistence, citizen petition triggers, and emergency disaster events.", styles['TableCell']),
         Paragraph("Integrated Telemetry Backend &amp; Event Engine", styles['TableCellBold'])],
        
        [Paragraph("<b>Iteration 5</b>", styles['TableCellBold']),
         Paragraph("Automated Testing &amp; Deployment", styles['TableCellBold']),
         Paragraph("Executing 25 Unit, Integration, and Black-Box test cases, validating 60 FPS performance, calculating SUS usability benchmarks (87.5/100), Standalone build packaging, and final Black Book.", styles['TableCell']),
         Paragraph("Production-Ready Simulator &amp; Black Book", styles['TableCellBold'])],
    ]
    wbs_table = Table(wbs_data, colWidths=[65, 110, 205, 107])
    wbs_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(wbs_table)
    elements.append(Spacer(1, 8))

    # 3.3 Project Timeline & Scheduling (Gantt Chart)
    elements.append(Paragraph("3.3 Project Timeline &amp; Scheduling (Gantt Chart &amp; Sprint Roadmap)", styles['SecHeading1']))
    gantt_path = os.path.join(FIG_DIR, "fig3_1_gantt.png")
    if os.path.exists(gantt_path):
        elements.append(Image(gantt_path, width=470, height=275))
        elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>Figure 3.1:</b> Project Schedule and Agile Development Gantt Chart", styles['FigCaption']))
    elements.append(Spacer(1, 6))

    # 3.4 Resource Planning
    elements.append(Paragraph("3.4 Resource Planning (Hardware &amp; Software Specifications)", styles['SecHeading1']))
    p_res = (
        "To develop, simulate, and benchmark the Smart City Management Simulator efficiently, the following hardware and software resources were provisioned:<br/><br/>"
        "• <b>Hardware Requirements:</b><br/>"
        "o <i>Processor:</i> Intel Core i5 / AMD Ryzen 5 or higher (minimum quad-core 3.0 GHz).<br/>"
        "o <i>Memory (RAM):</i> 8 GB RAM minimum (16 GB recommended for concurrent Unity editor, FastAPI server, and StarUML modeling).<br/>"
        "o <i>Graphics (GPU):</i> NVIDIA GeForce GTX 1050 / AMD Radeon RX 560 or higher with 4 GB VRAM (supporting DirectX 11 / OpenGL 4.5 / Metal).<br/>"
        "o <i>Storage:</i> Minimum 15 GB of available SSD storage.<br/>"
        "• <b>Software Requirements:</b><br/>"
        "o <i>Operating System:</i> Windows 10/11 64-bit, macOS Monterey+, or Linux Ubuntu 22.04 LTS.<br/>"
        "o <i>Game Engine &amp; SDK:</i> Unity 6.3 LTS (Universal Render Pipeline) with C# .NET Standard 2.1.<br/>"
        "o <i>Backend Web Runtime:</i> Python 3.11+ with FastAPI, Uvicorn, and Pydantic v2.<br/>"
        "o <i>Database Engine:</i> SQLite 3 (WAL mode) and PostgreSQL 17.<br/>"
        "o <i>Development &amp; Profiling Tools:</i> Visual Studio Code, JetBrains Rider, Postman, Git &amp; GitHub, Unity Profiler."
    )
    elements.append(Paragraph(p_res, styles['AcademicBody']))
    elements.append(PageBreak())

    return elements
