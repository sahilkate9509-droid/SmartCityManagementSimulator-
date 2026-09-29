import os
from reportlab.platypus import Paragraph, Spacer, Table, PageBreak, HRFlowable, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.units import inch

def build_frontmatter(styles, PRINTABLE_WIDTH, FIG_DIR, toc_page_dict=None):
    elements = []
    if toc_page_dict is None:
        toc_page_dict = {}

    # Helper for page lookup
    def get_pg(key, default):
        return str(toc_page_dict.get(key, default))

    # =========================================================================
    # PAGE 1: COVER / TITLE PAGE (OFFICIAL RUPAREL COLLEGE FORMAT)
    # =========================================================================
    elements.append(Spacer(1, 24))
    elements.append(Paragraph("<b>A PROJECT REPORT</b>", styles['CoverAuthor']))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("<b>On</b>", styles['CoverDetails']))
    elements.append(Spacer(1, 16))

    # Project Title in Bold Black
    proj_title_html = "<b>SMART CITY MANAGEMENT SIMULATOR</b>"
    elements.append(Paragraph(proj_title_html, styles['CoverTitle']))
    elements.append(Spacer(1, 16))

    elements.append(Paragraph("<i>Submitted by</i>", styles['CoverDetails']))
    elements.append(Spacer(1, 10))

    # Candidate Name in Bold Black
    cand_name_html = "<b>Mr. Sahil Vishal Kate</b>"
    elements.append(Paragraph(cand_name_html, styles['CoverAuthor']))
    elements.append(Spacer(1, 14))

    elements.append(Paragraph("<i>in partial fulfillment for the award of the degree</i>", styles['CoverDetails']))
    elements.append(Spacer(1, 3))
    elements.append(Paragraph("<i>of</i>", styles['CoverDetails']))
    elements.append(Spacer(1, 8))
    elements.append(Paragraph("<b>BACHELOR OF SCIENCE</b>", styles['CoverAuthor']))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("in", styles['CoverDetails']))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>COMPUTER SCIENCE</b>", styles['CoverAuthor']))
    elements.append(Spacer(1, 14))

    elements.append(Paragraph("<i>under the guidance of</i>", styles['CoverDetails']))
    elements.append(Spacer(1, 8))

    # Guide Name in Bold Black
    guide_name_html = "<b>PROF. AARTI GAWAI</b>"
    elements.append(Paragraph(guide_name_html, styles['CoverAuthor']))
    elements.append(Spacer(1, 8))
    elements.append(Paragraph("<b>Department of Computer Science</b>", styles['CoverAuthor']))
    elements.append(Spacer(1, 16))

    # College Crest
    ruparel_logo = os.path.join(FIG_DIR, "ruparel_logo.png")
    if os.path.exists(ruparel_logo):
        elements.append(Image(ruparel_logo, width=72, height=72))
        elements.append(Spacer(1, 14))

    elements.append(Paragraph("<b>Modern Education Society's</b>", styles['CoverAuthor']))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>The D. G. Ruparel College of Arts, Science &amp; Commerce</b>", styles['CoverAuthor']))
    elements.append(Spacer(1, 16))
    elements.append(Paragraph("<b>(Sem - V)</b>", styles['CoverDetails']))
    elements.append(Spacer(1, 4))
    elements.append(Paragraph("<b>(2026 - 2027)</b>", styles['CoverDetails']))
    elements.append(PageBreak())

    # =========================================================================
    # PAGE 2: CERTIFICATE (OFFICIAL RUPAREL COLLEGE CERTIFICATE FORMAT)
    # =========================================================================
    elements.append(Spacer(1, 10))
    if os.path.exists(ruparel_logo):
        elements.append(Image(ruparel_logo, width=65, height=65))
        elements.append(Spacer(1, 10))

    elements.append(Paragraph("<b>Modern Education Society's</b>", styles['CoverAuthor']))
    elements.append(Spacer(1, 3))
    elements.append(Paragraph("<b>The D. G. Ruparel College of Arts, Science &amp; Commerce,</b>", styles['CoverAuthor']))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph("<font size=9 color=\"#1e293b\">senapati bapat marg, opp. Matunga road station (w.r.), mahim, mumbai 400 016</font>", styles['CoverDetails']))
    elements.append(Spacer(1, 16))

    elements.append(Paragraph("<b>Department of Computer Science</b>", styles['CoverAuthor']))
    elements.append(Spacer(1, 18))

    # Certificate Title
    cert_heading_style = styles['CoverAuthor'].clone('CertHeading')
    cert_heading_style.fontSize = 17
    cert_heading_style.leading = 21
    elements.append(Paragraph("<b>CERTIFICATE</b>", cert_heading_style))
    elements.append(Spacer(1, 22))

    cert_body_style = styles['AcademicBody'].clone('CertBody')
    cert_body_style.fontSize = 11.5
    cert_body_style.leading = 21
    cert_body_style.alignment = 4 # Justified

    cert_p1 = (
        "This is to certify that Mr./Ms. "
        "<u><b>Mr. Sahil Vishal Kate.</b></u>"
    )
    elements.append(Paragraph(cert_p1, cert_body_style))
    elements.append(Spacer(1, 10))

    cert_p2 = (
        "Seat no: ________________ of <b>T.Y.B.Sc. (Sem V)</b> class has satisfactorily completed the "
        "Mini Project <u><b>SMART CITY MANAGEMENT SIMULATOR</b></u> , to be "
        "submitted in the partial fulfillment for the award of <b>Bachelor of Science in Computer Science</b> during the academic year <b>2026 - 2027</b>."
    )
    elements.append(Paragraph(cert_p2, cert_body_style))
    elements.append(Spacer(1, 24))

    elements.append(Paragraph("<b>Date of Submission:</b> ____________________", cert_body_style))
    elements.append(Spacer(1, 40))

    # Signatures
    sig_table_data = [
        [Paragraph("<b>PROF. AARTI GAWAI</b><br/>Project Guide", styles['TableCellBold']),
         Paragraph("<b>Head / Incharge,<br/>Department Computer Science</b>", styles['TableRightBold'])],
        [Spacer(1, 45), Spacer(1, 45)],
        [Paragraph("<b>College Seal</b>", styles['TableCellBold']),
         Paragraph("<b>Signature of Examiner</b>", styles['TableRightBold'])]
    ]
    sig_table = Table(sig_table_data, colWidths=[PRINTABLE_WIDTH/2.0, PRINTABLE_WIDTH/2.0])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    elements.append(sig_table)
    elements.append(PageBreak())

    # =========================================================================
    # PAGE 3: ACKNOWLEDGEMENT
    # =========================================================================
    elements.append(Paragraph("<b>ACKNOWLEDGEMENT</b>", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14, spaceBefore=4))

    ack_p1 = (
        "I would like to express my sincere gratitude to all those who provided guidance and support throughout the completion of this project.<br/><br/>"
        "First and foremost, I extend my heartfelt thanks to my project guide, <b>Prof. Aarti Gawai</b>, whose expert advice, encouragement, and constructive feedback were invaluable in shaping this project. Her guidance helped me navigate the technical challenges of developing a multi-agent 3D urban simulation engine, formulating coupled differential mathematical equations for civic subsystems, architecting asynchronous FastAPI telemetry pipelines, and implementing real-time analytical dashboards.<br/><br/>"
        "I am deeply grateful to the Head / Incharge and the faculty members of the Department of Computer Science at Modern Education Society's <b>The D.G. Ruparel College of Arts, Science and Commerce, Mahim, Mumbai</b>, for providing the necessary laboratory resources, computing workstations, and academic environment that facilitated this project's development through the requirement engineering, system design, implementation, testing, and evaluation phases.<br/><br/>"
        "I would also like to thank the creators and maintainers of the open-source tools, libraries, and technologies used in this project, including Unity Technologies (Unity 6.3 LTS), C# Multi-Threading, Python Software Foundation, FastAPI, Uvicorn, PostgreSQL 17, SQLite 3, SQLAlchemy 2.0 ORM, Chart.js, Visual Studio Code, Postman, Git, and GitHub. Their excellent documentation and robust platforms greatly accelerated the development, telemetry verification, and deployment processes.<br/><br/>"
        "I also acknowledge the support received from my classmates, peers, and everyone who contributed suggestions, testing feedback, or encouragement during the development and documentation stages of the Smart City Management Simulator. Their observations helped identify usability issues and refine the simulation gameplay workflow and heads-up display interface of the application.<br/><br/>"
        "The completion of this project has provided valuable practical experience in spatial algorithms, multi-subsystem simulation, database design, REST API integration, software testing, and technical documentation. I am grateful for the opportunity to apply the concepts learned during the Bachelor of Science in Computer Science programme to a complete working project.<br/><br/>"
        "Finally, I would like to thank my family and friends for their continuous support and understanding during the project, which enabled me to dedicate the time and focus required for its successful completion."
    )
    elements.append(Paragraph(ack_p1, styles['AcademicBody']))
    elements.append(PageBreak())

    # =========================================================================
    # PAGE 4: DECLARATION
    # =========================================================================
    elements.append(Paragraph("<b>DECLARATION</b>", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14, spaceBefore=4))

    decl_text = (
        "I, <b>Sahil Vishal Kate</b> (Roll No. <b>9041</b>), student of the <b>T.Y.B.Sc. (Computer Science – Sem V)</b> class, "
        "hereby declare that the project entitled <b>\"Smart City Management Simulator\"</b> submitted in partial fulfillment for the award of the degree of <b>Bachelor of Science in Computer Science</b> "
        "during the academic year <b>2026 - 2027</b> is my original work. The project has been carried out under the guidance of "
        "<b>Prof. Aarti Gawai</b> and represents the work completed by me as part of the prescribed academic project requirements. "
        "Furthermore, this project has not formed the basis for the award of any degree, associateship, fellowship, or any other similar titles.<br/><br/>"
        "I further declare that the problem identification, feasibility study, requirement engineering specifications, 3-tier system architecture design, "
        "database schemas, Unified Modeling Language (UML) diagrams, Data Flow Diagrams (DFD), application implementation, testing records, "
        "user interface operational workflows, and source code excerpts included in this report across Module 1 and Module 2 have been prepared "
        "for the academic evaluation of the Smart City Management Simulator project.<br/><br/>"
        "Wherever external open-source libraries, software frameworks, cloud platforms, or technical documentation—including Unity 6.3 LTS, C#, "
        "FastAPI, Python 3.11, PostgreSQL 17, SQLite 3, SQLAlchemy 2.0, Chart.js, PyTest, and Uvicorn—have been used, they have been acknowledged "
        "appropriately in the References section of this report.<br/><br/>"
        "I understand that the submission is subject to the academic rules and regulations of <b>D.G. Ruparel College of Arts, Science and Commerce, Mahim</b>, "
        "and that the responsibility for the originality and accuracy of the submitted work rests with me.<br/><br/>"
        "<b>Name of the Student:</b> Mr. Sahil Vishal Kate<br/>"
        "<b>Roll No.:</b> 9041<br/>"
        "<b>Class:</b> T.Y.B.Sc. (Computer Science – Sem V)<br/><br/>"
        "<b>Signature of the Student:</b> ______________________<br/><br/>"
        "<b>Place:</b> Mumbai<br/>"
        "<b>Date:</b> ______________________"
    )
    elements.append(Paragraph(decl_text, styles['AcademicBody']))
    elements.append(PageBreak())

    # =========================================================================
    # PAGE 5: LIST OF ABBREVIATIONS (PAGE V - MATCHING REFERENCE TEMPLATE)
    # =========================================================================
    elements.append(Paragraph("<b>LIST OF ABBREVIATIONS</b>", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=12, spaceBefore=4))

    abbrs = [
        ("API", "Application Programming Interface"),
        ("AQI", "Air Quality Index (CPCB / WHO Environmental Standards)"),
        ("BFS", "Breadth-First Search (Utility Corridor Routing Algorithm)"),
        ("CSCI", "Composite Smart City Index (Normalized 0-100 Rating)"),
        ("DFD", "Data Flow Diagram"),
        ("ERD / ER", "Entity-Relationship Diagram"),
        ("FOV", "Field of View"),
        ("FPS", "Frames Per Second (Target: >= 60 FPS)"),
        ("FR", "Functional Requirement"),
        ("GIS", "Geographic Information System"),
        ("GPU", "Graphics Processing Unit"),
        ("HUD", "Heads-Up Display"),
        ("IEEE", "Institute of Electrical and Electronics Engineers"),
        ("JSON", "JavaScript Object Notation"),
        ("JWT", "JSON Web Token"),
        ("LOD", "Level of Detail"),
        ("LTS", "Long Term Support (Unity 6.3 LTS)"),
        ("NFR", "Non-Functional Requirement"),
        ("ORM", "Object-Relational Mapping (SQLAlchemy 2.0)"),
        ("REST", "Representational State Transfer"),
        ("SDLC", "Software Development Life Cycle"),
        ("SRS", "Software Requirements Specification (IEEE Std 830-1998)"),
        ("SUS", "System Usability Scale (Brooke, 1996)"),
        ("UAT", "User Acceptance Testing"),
        ("UML", "Unified Modeling Language"),
        ("URP", "Universal Render Pipeline"),
        ("VRAM", "Video Random Access Memory"),
        ("WAL", "Write-Ahead Logging (SQLite Storage Engine)"),
        ("WBS", "Work Breakdown Structure"),
    ]

    abbr_data = [
        [Paragraph("<b>Abbreviation</b>", styles['TableHead']),
         Paragraph("<b>Full Form / Definition</b>", styles['TableHead'])]
    ]
    for ab, desc in abbrs:
        abbr_data.append([
            Paragraph(f"<b>{ab}</b>", styles['TableCellBold']),
            Paragraph(desc, styles['TableCell'])
        ])
    abbr_table = Table(abbr_data, colWidths=[120, 367])
    abbr_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(abbr_table)
    elements.append(PageBreak())

    # =========================================================================
    # PAGES 6 & 7: TABLE OF CONTENTS (EXACT REFERENCE TEMPLATE FORMAT)
    # =========================================================================
    elements.append(Paragraph("<b>TABLE OF CONTENTS</b>", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=10, spaceBefore=2))

    toc_entries = [
        ("-", "CERTIFICATE", "ii"),
        ("-", "ACKNOWLEDGEMENTS", "iii"),
        ("-", "DECLARATION", "iv"),
        ("-", "LIST OF ABBREVIATIONS", "v"),
        ("-", "TABLE OF CONTENTS", "vi"),
        ("-", "TABLE OF TABLES", "viii"),
        ("-", "TABLE OF FIGURES", "ix"),
        ("MODULE 1", "PROBLEM IDENTIFICATION, REQUIREMENT ENGINEERING & SYSTEM DESIGN PHASE", "1"),
        ("CHAPTER 1", "PROBLEM IDENTIFICATION & FEASIBILITY STUDY", get_pg("CH1", "1")),
        ("1.1", "Background and Motivation", get_pg("1.1", "1")),
        ("1.2", "Objectives", get_pg("1.2", "2")),
        ("1.3", "Identification of a Real-World Problem (Industry / Social / Institutional)", get_pg("1.3", "2")),
        ("1.4", "Problem Justification and Scope Definition", get_pg("1.4", "3")),
        ("1.5", "Stakeholder Identification & Beneficiary Analysis", get_pg("1.5", "3")),
        ("1.6", "Feasibility Analysis (Technical, Economic, Operational, Legal, Schedule)", get_pg("1.6", "3")),
        ("CHAPTER 2", "REQUIREMENT ENGINEERING", get_pg("CH2", "5")),
        ("2.1", "Functional Requirements Specification", get_pg("2.1", "5")),
        ("2.2", "Non-Functional Requirements Specification", get_pg("2.2", "7")),
        ("2.3", "Use-Case Analysis & Actor Profiles", get_pg("2.3", "7")),
        ("2.4", "Requirement Prioritization (MoSCoW Matrix)", get_pg("2.4", "8")),
        ("2.5", "Constraints and Assumptions", get_pg("2.5", "9")),
        ("2.6", "Preliminary Product Description & Technology Stack Survey", get_pg("2.6", "9")),
        ("2.7", "Conceptual Models (Literature Review of Existing Urban Systems)", get_pg("2.7", "10")),
        ("CHAPTER 3", "SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC) PLANNING", get_pg("CH3", "12")),
        ("3.1", "Selection of SDLC Model (Agile Incremental Sprint Model)", get_pg("3.1", "12")),
        ("3.2", "Work Breakdown Structure (WBS)", get_pg("3.2", "12")),
        ("3.3", "Project Timeline & Scheduling (Gantt Chart & Sprint Roadmap)", get_pg("3.3", "13")),
        ("3.4", "Resource Planning (Hardware & Software Specifications)", get_pg("3.4", "14")),
        ("CHAPTER 4", "SYSTEM MODELING USING UML", get_pg("CH4", "15")),
        ("4.1", "Event Table (System Logic & Event Table)", get_pg("4.1", "15")),
        ("4.2", "Class Diagram", get_pg("4.2", "18")),
        ("4.3", "Use Case Diagram", get_pg("4.3", "19")),
        ("4.4", "Entity-Relationship (ER) & Data Flow Diagrams (DFD Level 0 & Level 1)", get_pg("4.4", "20")),
        ("4.5", "Object Diagram", get_pg("4.5", "23")),
        ("4.6", "Sequence Diagram", get_pg("4.6", "24")),
        ("4.7", "Activity Diagram", get_pg("4.7", "25")),
        ("4.8", "Component Model", get_pg("4.8", "27")),
        ("4.9", "Deployment Diagram", get_pg("4.9", "28")),
        ("CHAPTER 5", "SYSTEM ARCHITECTURE DESIGN", get_pg("CH5", "29")),
        ("5.1", "Frontend Architecture & Component Hierarchy", get_pg("5.1", "29")),
        ("5.2", "Backend Architecture & FastAPI REST API Telemetry Middleware", get_pg("5.2", "30")),
        ("5.3", "Database Schema Design & PostgreSQL/SQLite Data Dictionaries", get_pg("5.3", "30")),
        ("5.4", "API Structure, Endpoints & JSON Contracts", get_pg("5.4", "34")),
        ("5.5", "Security Considerations & Granular Access Control Policies", get_pg("5.5", "35")),
        ("5.6", "Procedural Design (A* Pathfinding & CSCI Formulations)", get_pg("5.6", "36")),
        ("MODULE 2", "IMPLEMENTATION, TESTING, DEPLOYMENT & EVALUATION PHASE", get_pg("MOD2", "37")),
        ("CHAPTER 6", "APPLICATION DEVELOPMENT", get_pg("CH6", "37")),
        ("6.1", "Frontend Implementation (Unity 6.3 LTS, 3D Canvas & Multi-Agent Loop)", get_pg("6.1", "37")),
        ("6.2", "Backend Implementation (FastAPI, Async Workers & Telemetry Proxy)", get_pg("6.2", "38")),
        ("6.3", "Database Integration (SQLAlchemy 2.0 Connection Pool & WAL Storage)", get_pg("6.3", "38")),
        ("6.4", "Authentication & Validation (Session Authorization & State Checksums)", get_pg("6.4", "39")),
        ("6.5", "Error Handling & Exception Management", get_pg("6.5", "39")),
        ("CHAPTER 7", "INTEGRATION & SYSTEM TESTING", get_pg("CH7", "40")),
        ("7.1", "Testing Approach & Quality Assurance Framework", get_pg("7.1", "40")),
        ("7.2", "Unit Testing", get_pg("7.2", "40")),
        ("7.3", "Black-Box Testing", get_pg("7.3", "40")),
        ("7.4", "Integration Testing", get_pg("7.4", "40")),
        ("7.5", "Beta Testing & Usability Evaluation (SUS Benchmark)", get_pg("7.5", "40")),
        ("7.6", "Comprehensive Test Case Matrix (Unit, Integration & System Tables)", get_pg("7.6", "41")),
        ("7.7", "Bug Tracking & Defect Management", get_pg("7.7", "52")),
        ("CHAPTER 8", "DEPLOYMENT & HOSTING", get_pg("CH8", "54")),
        ("8.1", "Cloud Deployment & Local Hosting Architecture", get_pg("8.1", "54")),
        ("8.2", "Standalone Executable & WebGL Build Packaging", get_pg("8.2", "55")),
        ("8.3", "Server Configuration & Secure Environment Variables (.env)", get_pg("8.3", "55")),
        ("8.4", "Version Control using GitHub & Project Directory Tree", get_pg("8.4", "55")),
        ("8.5", "GitHub Repository Structure", get_pg("8.5", "56")),
        ("8.6", "Render Cloud Web Service Deployment", get_pg("8.6", "56")),
        ("8.7", "Database Cloud Configuration (PostgreSQL / SQLite WAL)", get_pg("8.7", "56")),
        ("CHAPTER 9", "PERFORMANCE & SECURITY TESTING", get_pg("CH9", "57")),
        ("9.1", "Basic Load Testing & Latency Benchmarks (60 FPS & <50ms Target)", get_pg("9.1", "57")),
        ("9.2", "Input Validation Checks & Sanitization", get_pg("9.2", "57")),
        ("9.3", "Security Validation & Penetration Resistance", get_pg("9.3", "57")),
        ("CHAPTER 10", "FINAL DOCUMENTATION / RESULT AND DISCUSSION", get_pg("CH10", "59")),
        ("10.1", "Technical Report & Module Deliverables Summary", get_pg("10.1", "59")),
        ("10.2", "User Manual & Operational Walkthrough (Steps 1 to 7)", get_pg("10.2", "59")),
        ("10.3", "Application Screenshots & Visual Demonstrations", get_pg("10.3", "62")),
        ("10.4", "Source Code Documentation & Core Module Listings", get_pg("10.4", "69")),
        ("CHAPTER 11", "CONCLUSION", get_pg("CH11", "87")),
        ("11.1", "Significance of the System", get_pg("11.1", "87")),
        ("11.2", "Limitations of the System", get_pg("11.2", "87")),
        ("11.3", "Future Scope of the Project", get_pg("11.3", "88")),
        ("-", "REFERENCES", get_pg("REFS", "89")),
        ("-", "GLOSSARY", get_pg("GLOSS", "90")),
    ]

    toc_table_data = [
        [Paragraph("<b>Topic / No.</b>", styles['TableHead']),
         Paragraph("<b>Chapter / Section Description</b>", styles['TableHead']),
         Paragraph("<b>Page No.</b>", styles['TableHead'])]
    ]
    for top_no, desc, pg in toc_entries:
        is_mod = "MODULE" in top_no
        is_chap = "CHAPTER" in top_no
        style_t = styles['TableCellBold'] if (is_mod or is_chap) else styles['TableCell']
        style_d = styles['TableCellBold'] if (is_mod or is_chap) else styles['TableCell']
        toc_table_data.append([
            Paragraph(f"<b>{top_no}</b>" if (is_mod or is_chap) else top_no, style_t),
            Paragraph(f"<b>{desc}</b>" if (is_mod or is_chap) else desc, style_d),
            Paragraph(f"<b>{pg}</b>" if (is_mod or is_chap) else pg, styles['TableCellBold'])
        ])

    toc_table = Table(toc_table_data, colWidths=[80, 347, 60])
    toc_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.6),
    ]))
    elements.append(toc_table)
    elements.append(PageBreak())

    # =========================================================================
    # PAGE 7: TABLE OF TABLES
    # =========================================================================
    elements.append(Paragraph("<b>TABLE OF TABLES</b>", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=12, spaceBefore=4))

    tables_list = [
        ("Table 1.1", "Role and Responsibility Across Project Phases", get_pg("TBL_1_1", "1")),
        ("Table 2.1", "Functional Requirements Specification Table", get_pg("TBL_2_1", "6")),
        ("Table 2.2", "Non-Functional Requirements Specification Table", get_pg("TBL_2_2", "7")),
        ("Table 2.3", "Requirement Prioritization (MoSCoW Matrix)", get_pg("TBL_2_3", "8")),
        ("Table 2.4", "Comparative Analysis Matrix of Existing Simulation Systems", get_pg("TBL_2_4", "10")),
        ("Table 3.1", "Work Breakdown Structure (WBS) & Sprint Deliverables", get_pg("TBL_3_1", "12")),
        ("Table 4.1", "System Logic & Event Table", get_pg("TBL_4_1", "15")),
        ("Table 5.1", "SimulationSession (Municipal Jurisdictions) Data Dictionary", get_pg("TBL_5_1", "30")),
        ("Table 5.2", "CityMetrics (Subsystem Telemetry Logs) Data Dictionary", get_pg("TBL_5_2", "31")),
        ("Table 5.3", "ZoningGrid (50x50 Cell Matrix) Data Dictionary", get_pg("TBL_5_3", "32")),
        ("Table 5.4", "CitizenPetition (Civic Grievances) Data Dictionary", get_pg("TBL_5_4", "32")),
        ("Table 5.5", "DisasterIncident (Emergency Events) Data Dictionary", get_pg("TBL_5_5", "33")),
        ("Table 5.6", "TelemetryLog (Historical Telemetry Queue) Data Dictionary", get_pg("TBL_5_6", "33")),
        ("Table 5.7", "FastAPI REST Endpoints & JSON Contracts", get_pg("TBL_5_7", "34")),
        ("Table 7.1", "Unit Testing Test Cases Log (TC-01 to TC-11)", get_pg("TBL_7_1", "41")),
        ("Table 7.2", "Integration Testing Test Cases Log (TC-12 to TC-18)", get_pg("TBL_7_2", "47")),
        ("Table 7.3", "System & Black-Box Testing Test Cases Log (TC-19 to TC-25)", get_pg("TBL_7_3", "50")),
        ("Table 7.4", "Bug Tracking & Defect Management Log", get_pg("TBL_7_4", "52")),
    ]

    tbl_table_data = [
        [Paragraph("<b>Table No.</b>", styles['TableHead']),
         Paragraph("<b>Table Title / Description</b>", styles['TableHead']),
         Paragraph("<b>Page No.</b>", styles['TableHead'])]
    ]
    for tno, tdesc, tpg in tables_list:
        tbl_table_data.append([
            Paragraph(f"<b>{tno}</b>", styles['TableCellBold']),
            Paragraph(tdesc, styles['TableCell']),
            Paragraph(f"<b>{tpg}</b>", styles['TableCellBold'])
        ])
    tbl_table = Table(tbl_table_data, colWidths=[80, 347, 60])
    tbl_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.4),
    ]))
    elements.append(tbl_table)
    elements.append(PageBreak())

    # =========================================================================
    # PAGE 8: TABLE OF FIGURES (INCLUDES ALL 20 APPLICATION SCREENSHOTS)
    # =========================================================================
    elements.append(Paragraph("<b>TABLE OF FIGURES</b>", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=12, spaceBefore=4))

    figures_list = [
        ("Figure 3.1", "Project Schedule and Agile Development Gantt Chart", get_pg("FIG_3_1", "13")),
        ("Figure 4.1", "Class Diagram Mapping City Simulation Entities", get_pg("FIG_4_1", "18")),
        ("Figure 4.2", "Use Case Diagram for City Management System", get_pg("FIG_4_2", "19")),
        ("Figure 4.3", "Entity-Relationship (ER) Diagram for City Management Schema", get_pg("FIG_4_3", "20")),
        ("Figure 4.4", "DFD Level 0 – Context Diagram", get_pg("FIG_4_4", "21")),
        ("Figure 4.5", "DFD Level 1 – Process Breakdown", get_pg("FIG_4_5", "22")),
        ("Figure 4.6", "Object Diagram Illustrating Runtime Instances", get_pg("FIG_4_6", "23")),
        ("Figure 4.7", "Sequence Diagram for Simulation Tick & Telemetry Flow", get_pg("FIG_4_7", "24")),
        ("Figure 4.8", "Activity Diagram for Building Placement & Zoning Workflow", get_pg("FIG_4_8", "26")),
        ("Figure 4.9", "Component Diagram Showing Tier Interconnections", get_pg("FIG_4_9", "27")),
        ("Figure 4.10", "Deployment Diagram Across Unity Client, FastAPI and Database Cloud", get_pg("FIG_4_10", "28")),
        ("Figure 5.1", "Smart City High-Level 3-Tier Architecture Diagram", get_pg("FIG_5_1", "29")),
        ("Figure 8.1", "Deployment Architecture and Hosting Infrastructure", get_pg("FIG_8_1", "54")),
        ("Figure 10.1", "Main Menu & Simulation Founding Interface", get_pg("FIG_10_1", "63")),
        ("Figure 10.2", "Secure Mayor Authentication & Portal Login", get_pg("FIG_10_2", "63")),
        ("Figure 10.3", "Mayor Registration & Role Specialization", get_pg("FIG_10_3", "64")),
        ("Figure 10.4", "Municipal Founding & Climate Configuration", get_pg("FIG_10_4", "64")),
        ("Figure 10.5", "Real-Time 3D City Viewport & Master HUD", get_pg("FIG_10_5", "65")),
        ("Figure 10.6", "Mayor Quick-Action Dashboard & Live Telemetry", get_pg("FIG_10_6", "65")),
        ("Figure 10.7", "Industrial District Fire & Emergency Response Modal", get_pg("FIG_10_7", "66")),
        ("Figure 10.8", "City Decorations & Urban Beautification Panel", get_pg("FIG_10_8", "66")),
        ("Figure 10.9", "3D Spatial Map Overlays & District Filters", get_pg("FIG_10_9", "67")),
        ("Figure 10.10", "Taxes, Revenue & Municipal Bonds Ledger", get_pg("FIG_10_10", "67")),
        ("Figure 10.11", "Interactive Traffic Management & Signal Optimization", get_pg("FIG_10_11", "68")),
        ("Figure 10.12", "Multimodal Public Transit Dispatcher", get_pg("FIG_10_12", "68")),
        ("Figure 10.13", "Electricity Grid Capacity & Power Balance", get_pg("FIG_10_13", "69")),
        ("Figure 10.14", "Water Reservoir & Supply-Demand Network", get_pg("FIG_10_14", "69")),
        ("Figure 10.15", "Waste Management & Recycling Subsystem", get_pg("FIG_10_15", "70")),
        ("Figure 10.16", "Healthcare Infrastructure & Quality Monitoring", get_pg("FIG_10_16", "70")),
        ("Figure 10.17", "Education Quality Index & School Facilities", get_pg("FIG_10_17", "71")),
        ("Figure 10.18", "Public Safety, Police & Fire Protection", get_pg("FIG_10_18", "71")),
        ("Figure 10.19", "Environmental Sustainability & Green Cover Analytics", get_pg("FIG_10_19", "72")),
        ("Figure 10.20", "Citizen Petitions & Civic Grievance Inbox", get_pg("FIG_10_20", "72")),
    ]

    fig_table_data = [
        [Paragraph("<b>Figure No.</b>", styles['TableHead']),
         Paragraph("<b>Figure Title / Description</b>", styles['TableHead']),
         Paragraph("<b>Page No.</b>", styles['TableHead'])]
    ]
    for fno, fdesc, fpg in figures_list:
        fig_table_data.append([
            Paragraph(f"<b>{fno}</b>", styles['TableCellBold']),
            Paragraph(fdesc, styles['TableCell']),
            Paragraph(f"<b>{fpg}</b>", styles['TableCellBold'])
        ])
    fig_table = Table(fig_table_data, colWidths=[80, 347, 60])
    fig_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
    ]))
    elements.append(fig_table)
    elements.append(PageBreak())

    return elements
