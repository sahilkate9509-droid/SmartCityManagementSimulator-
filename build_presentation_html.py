import os

def generate_html_presentation():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "Smart_City_Presentation.html")

    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart City Management Simulator — Project Presentation & Viva Defense</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-base: #0a0e17;
            --bg-surface: #121a26;
            --bg-card: rgba(18, 26, 38, 0.88);
            --bg-card-hover: rgba(24, 34, 50, 0.98);
            --border-card: rgba(245, 158, 11, 0.25);
            --border-glow: rgba(16, 185, 129, 0.45);
            --text-primary: #f8fafc;
            --text-secondary: #a0aec0;
            --text-muted: #718096;
            --accent-blue: #f59e0b;
            --accent-cyan: #10b981;
            --accent-emerald: #10b981;
            --accent-amber: #fbbf24;
            --accent-rose: #f43f5e;
            --accent-purple: #a855f7;
            --gradient-accent: linear-gradient(135deg, #10b981 0%, #f59e0b 50%, #10b981 100%);
            --shadow-glow: 0 0 35px rgba(16, 185, 129, 0.15);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-base);
            color: var(--text-primary);
            overflow: hidden;
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
            user-select: none;
        }

        /* Top control bar */
        header.top-bar {
            height: 52px;
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 24px;
            z-index: 100;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            font-weight: 700;
            font-size: 15px;
            letter-spacing: 0.5px;
            color: #fff;
        }

        .brand-badge {
            background: rgba(6, 182, 212, 0.15);
            color: var(--accent-cyan);
            border: 1px solid rgba(6, 182, 212, 0.3);
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
            text-transform: uppercase;
        }

        .controls-cluster {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.12);
            color: var(--text-primary);
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .btn:hover {
            background: rgba(6, 182, 212, 0.15);
            border-color: var(--accent-cyan);
            color: var(--accent-cyan);
            transform: translateY(-1px);
        }

        .btn-primary {
            background: var(--accent-blue);
            border-color: var(--accent-blue);
            color: #fff;
        }
        .btn-primary:hover {
            background: #1d4ed8;
            border-color: #1d4ed8;
            color: #fff;
        }

        /* Slide viewport */
        .slide-viewport {
            flex: 1;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            background: radial-gradient(circle at 50% 30%, rgba(37, 99, 235, 0.08) 0%, transparent 70%);
        }

        .slide-container {
            width: 100%;
            height: 100%;
            position: relative;
        }

        .slide {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            padding: 40px 60px 70px 60px;
            display: flex;
            flex-direction: column;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.35s cubic-bezier(0.4, 0, 0.2, 1), transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            transform: scale(0.98);
        }

        .slide.active {
            opacity: 1;
            pointer-events: auto;
            transform: scale(1);
        }

        /* Slide Header */
        .slide-header {
            margin-bottom: 24px;
        }

        .slide-tag {
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            color: var(--accent-cyan);
            margin-bottom: 4px;
        }

        .slide-title {
            font-size: 32px;
            font-weight: 800;
            color: #fff;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .slide-divider {
            height: 2px;
            width: 100%;
            background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue), transparent);
            margin-top: 12px;
            border-radius: 2px;
        }

        /* Slide Content Area */
        .slide-content {
            flex: 1;
            display: flex;
            gap: 28px;
            align-items: stretch;
            min-height: 0;
        }

        /* Card Styles */
        .card {
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            border-radius: 14px;
            padding: 24px;
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: var(--gradient-accent);
            opacity: 0.6;
        }

        .card-title {
            font-size: 16px;
            font-weight: 700;
            color: var(--accent-cyan);
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            gap: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .card-body {
            flex: 1;
            overflow-y: auto;
            color: var(--text-secondary);
            font-size: 14.5px;
            line-height: 1.6;
        }

        .card-body p {
            margin-bottom: 12px;
        }

        .card-body ul {
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .card-body li {
            position: relative;
            padding-left: 20px;
        }

        .card-body li::before {
            content: '▹';
            position: absolute;
            left: 0;
            color: var(--accent-cyan);
            font-weight: bold;
        }

        .highlight-text {
            color: #fff;
            font-weight: 600;
        }

        /* Image Display Box */
        .figure-box {
            flex: 1.2;
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 12px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
        }

        .figure-box img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            border-radius: 8px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
            cursor: zoom-in;
            transition: transform 0.2s;
        }

        .figure-box img:hover {
            transform: scale(1.01);
        }

        .fig-caption {
            font-size: 12px;
            color: var(--text-muted);
            margin-top: 8px;
            text-align: center;
            font-family: 'JetBrains Mono', monospace;
        }

        /* Table Design */
        .slide-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13.5px;
        }

        .slide-table th {
            background: rgba(37, 99, 235, 0.25);
            color: #fff;
            padding: 12px 14px;
            text-align: left;
            border-bottom: 2px solid var(--accent-blue);
            font-weight: 700;
        }

        .slide-table td {
            padding: 10px 14px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.06);
            color: var(--text-secondary);
        }

        .slide-table tr:hover td {
            background: rgba(255, 255, 255, 0.03);
            color: #fff;
        }

        .badge-pill {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 700;
        }

        .badge-success { background: rgba(16, 185, 129, 0.2); color: var(--accent-emerald); border: 1px solid rgba(16, 185, 129, 0.4); }
        .badge-danger { background: rgba(244, 63, 94, 0.2); color: var(--accent-rose); border: 1px solid rgba(244, 63, 94, 0.4); }
        .badge-warning { background: rgba(245, 158, 11, 0.2); color: var(--accent-amber); border: 1px solid rgba(245, 158, 11, 0.4); }
        .badge-info { background: rgba(6, 182, 212, 0.2); color: var(--accent-cyan); border: 1px solid rgba(6, 182, 212, 0.4); }

        /* Formula Box */
        .formula-card {
            background: rgba(15, 23, 42, 0.9);
            border: 1px solid rgba(6, 182, 212, 0.3);
            border-radius: 10px;
            padding: 16px;
            margin-bottom: 16px;
        }

        .formula-code {
            font-family: 'JetBrains Mono', monospace;
            color: #38bdf8;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 6px;
            background: rgba(0, 0, 0, 0.4);
            padding: 8px 12px;
            border-radius: 6px;
            border-left: 3px solid var(--accent-cyan);
        }

        /* Interactive Simulator Demo Widget */
        .interactive-calculator {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 16px;
            margin-top: 10px;
        }

        .calc-control {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .calc-label {
            font-size: 12px;
            font-weight: 600;
            color: var(--text-secondary);
            display: flex;
            justify-content: space-between;
        }

        .calc-slider {
            -webkit-appearance: none;
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #334155;
            outline: none;
        }

        .calc-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 16px;
            height: 16px;
            border-radius: 50%;
            background: var(--accent-cyan);
            cursor: pointer;
            box-shadow: 0 0 8px var(--accent-cyan);
        }

        .csci-score-display {
            grid-column: span 2;
            background: rgba(6, 182, 212, 0.1);
            border: 1px solid rgba(6, 182, 212, 0.3);
            border-radius: 10px;
            padding: 16px;
            text-align: center;
            display: flex;
            justify-content: space-around;
            align-items: center;
        }

        .csci-big-val {
            font-size: 38px;
            font-weight: 800;
            color: var(--accent-cyan);
            font-family: 'JetBrains Mono', monospace;
        }

        /* Bottom Status bar */
        footer.bottom-bar {
            height: 48px;
            background: rgba(15, 23, 42, 0.95);
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 24px;
            font-size: 12.5px;
            color: var(--text-muted);
            z-index: 100;
        }

        .nav-buttons {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .slide-progress-bar {
            position: absolute;
            top: 0;
            left: 0;
            height: 3px;
            background: var(--gradient-accent);
            width: 5%;
            transition: width 0.3s ease;
        }

        /* Slide Sorter / Overview Modal */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(8px);
            z-index: 1000;
            display: none;
            flex-direction: column;
            padding: 40px;
        }

        .modal-overlay.active {
            display: flex;
        }

        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
        }

        .sorter-grid {
            flex: 1;
            overflow-y: auto;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 16px;
            padding-right: 12px;
        }

        .sorter-thumb {
            background: var(--bg-surface);
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 8px;
            padding: 14px;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .sorter-thumb:hover, .sorter-thumb.active {
            border-color: var(--accent-cyan);
            box-shadow: 0 0 15px rgba(6, 182, 212, 0.3);
            transform: translateY(-2px);
        }

        .sorter-num {
            font-size: 11px;
            font-weight: 700;
            color: var(--accent-cyan);
        }

        .sorter-name {
            font-size: 13px;
            font-weight: 600;
            color: #fff;
        }

        /* Speaker notes drawer */
        .notes-drawer {
            position: fixed;
            bottom: 48px;
            left: 0;
            width: 100%;
            height: 180px;
            background: rgba(15, 23, 42, 0.96);
            backdrop-filter: blur(16px);
            border-top: 2px solid var(--accent-blue);
            padding: 20px 40px;
            display: none;
            flex-direction: column;
            z-index: 90;
            box-shadow: 0 -10px 40px rgba(0, 0, 0, 0.5);
        }

        .notes-drawer.open {
            display: flex;
        }

        .notes-header {
            font-size: 12px;
            font-weight: 700;
            color: var(--accent-cyan);
            text-transform: uppercase;
            margin-bottom: 8px;
            display: flex;
            justify-content: space-between;
        }

        .notes-content {
            font-size: 15px;
            color: #e2e8f0;
            line-height: 1.6;
            overflow-y: auto;
        }

        /* Print styles */
        @media print {
            header.top-bar, footer.bottom-bar, .modal-overlay, .notes-drawer {
                display: none !important;
            }
            body {
                overflow: visible !important;
                background: #0f172a !important;
                -webkit-print-color-adjust: exact !important;
                print-color-adjust: exact !important;
            }
            .slide-viewport {
                height: auto !important;
                display: block !important;
            }
            .slide-container {
                position: static !important;
            }
            .slide {
                position: relative !important;
                opacity: 1 !important;
                pointer-events: auto !important;
                transform: none !important;
                page-break-after: always !important;
                height: 100vh !important;
                padding: 30px !important;
            }
        }
    </style>
</head>
<body>

    <!-- Header Navigation -->
    <header class="top-bar">
        <div class="brand">
            <span style="font-size: 20px;">🏙️</span>
            <span>SMART CITY MANAGEMENT SIMULATOR</span>
            <span class="brand-badge">B.Sc CS Final Viva</span>
        </div>

        <div class="controls-cluster">
            <button class="btn" onclick="toggleOverview()" title="View All Slides (O / Esc)">
                <span>🗂️</span> Slides
            </button>
            <button class="btn" onclick="toggleNotes()" title="Speaker Notes (N)">
                <span>🎙️</span> Notes
            </button>
            <button class="btn" onclick="toggleFullscreen()" title="Fullscreen (F)">
                <span>⛶</span> Fullscreen
            </button>
            <button class="btn btn-primary" onclick="window.print()" title="Print Slide Deck to PDF">
                <span>🖨️</span> Export PDF
            </button>
        </div>
    </header>

    <!-- Main Viewport -->
    <main class="slide-viewport">
        <div class="slide-container" id="slideDeck">

            <!-- ================= SLIDE 1: TITLE ================= -->
            <section class="slide active" data-title="Title & Identification" data-notes="Good morning respected examiners, internal faculty members, and my project guide Prof. Aarti Gawai. I am Sahil Vishal Kate, Roll No. 9041, from D.G. Ruparel College. Today, I am proud to defend my capstone project: Smart City Management Simulator.">
                <div class="slide-header">
                    <div class="slide-tag">PROJECT DEFENSE & VIVA VOCE — 2026-2027</div>
                    <h1 class="slide-title">SMART CITY MANAGEMENT SIMULATOR</h1>
                    <div style="font-size: 19px; color: var(--accent-cyan); font-weight: 600; margin-top: 4px;">
                        A Real-Time Multi-Agent Urban Simulation & Cloud Telemetry Platform
                    </div>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="card" style="flex: 1.1;">
                        <div class="card-title">👨‍💻 Candidate & Academic Affiliation</div>
                        <div class="card-body">
                            <p><span class="highlight-text" style="font-size: 20px;">Sahil Vishal Kate</span></p>
                            <p style="color: var(--accent-amber); font-weight: 600; font-family: 'JetBrains Mono', monospace;">
                                Roll No.: 9041 | Seat No.: Sem V
                            </p>
                            <p>Degree: <b>Bachelor of Science in Computer Science (B.Sc CS)</b></p>
                            <p>College: <b>D.G. Ruparel College of Arts, Science and Commerce</b></p>
                            <p>Affiliated to: <b>University of Mumbai, Maharashtra, India</b></p>
                            <div style="display: flex; gap: 20px; margin-top: 24px;">
                                <img src="docs_figures/ruparel_logo.png" style="height: 65px;" alt="Ruparel Logo">
                                <img src="docs_figures/mumbai_university_logo.png" style="height: 65px;" alt="Mumbai University Logo">
                                <img src="docs_figures/project_logo.png" style="height: 65px;" alt="Project Logo">
                            </div>
                        </div>
                    </div>

                    <div class="card" style="flex: 0.9;">
                        <div class="card-title">🎓 Project Supervision & Technology Core</div>
                        <div class="card-body">
                            <p>Under the Guidance of:</p>
                            <p><span class="highlight-text" style="font-size: 18px;">Prof. Aarti Gawai</span></p>
                            <p style="color: var(--accent-emerald);">Assistant Professor & Project Supervisor</p>
                            <p>Department of Computer Science, D.G. Ruparel College</p>
                            <hr style="border-color: rgba(255,255,255,0.1); margin: 16px 0;">
                            <div class="card-title" style="margin-bottom: 8px;">⚙️ Technology Stack</div>
                            <ul>
                                <li><b>Client Engine:</b> Unity 6.3 LTS (C# 12, Procedural 3D)</li>
                                <li><b>Cloud Telemetry:</b> Python 3.12, FastAPI (ASGI)</li>
                                <li><b>Persistence:</b> PostgreSQL 17 / SQLite 3, SQLAlchemy</li>
                                <li><b>DevOps:</b> Docker, Docker Compose, Swagger OpenAPI</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 2: EXECUTIVE SUMMARY ================= -->
            <section class="slide" data-title="Executive Summary" data-notes="By 2050, over 68% of the world's population will live in cities. Urban centers are non-linear socio-technical systems where single policy changes have cascading ripple effects. Our project delivers an urban digital twin to model these trade-offs safely.">
                <div class="slide-header">
                    <div class="slide-tag">EXECUTIVE SUMMARY</div>
                    <h2 class="slide-title">The Urban Digital Twin & Problem Space</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="card" style="flex: 1;">
                        <div class="card-title">🌐 Global Urban Transition</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Demographic Explosion:</b> 68% of human population in urban agglomerations by 2050 (+2.5 Billion people).</li>
                                <li><b>Non-Linear Dynamics:</b> Heavy industrial zoning raises taxes but spikes particulate pollution (PM2.5), driving public health collapse and demographic flight.</li>
                                <li><b>The High Cost of Failure:</b> Municipal infrastructure mistakes take decades to fix and cost billions of public funds.</li>
                            </ul>
                        </div>
                    </div>

                    <div class="card" style="flex: 1;">
                        <div class="card-title">💡 The Computational Twin Solution</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Real-Time 3D Sandbox:</b> An interactive computational sandbox rendering dynamic cities with day/night illumination and procedural terrain.</li>
                                <li><b>Deterministic Multi-Agent Engine:</b> Six synchronized simulation layers governing Economy, Demographics, Utilities, Traffic, Healthcare, and AQI.</li>
                                <li><b>Standardized Rating:</b> The <i>Composite Smart City Index (CSCI)</i> provides an objective 0-100 score inspired by ISO 37120.</li>
                            </ul>
                        </div>
                    </div>

                    <div class="card" style="flex: 1;">
                        <div class="card-title">🚀 Core Project Contributions</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Decoupled Architecture:</b> Pure C# mathematical model isolated from rendering graphics, enabling independent unit testing.</li>
                                <li><b>Cloud Telemetry Pipeline:</b> Async REST streaming from Unity into PostgreSQL with automated audit reporting.</li>
                                <li><b>Consumer Hardware Accessibility:</b> Solid 60+ FPS on regular student laptops without requiring expensive GPU clusters.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 3: PROBLEM STATEMENT ================= -->
            <section class="slide" data-title="Problem Statement" data-notes="Traditional municipal planning suffers from two extremes: bureaucratic spreadsheets with no dynamic feedback, or commercial software that costs millions. Meanwhile, video games prioritize entertainment over real telemetry. We bridge this critical gap.">
                <div class="slide-header">
                    <div class="slide-tag">PROBLEM FORMULATION</div>
                    <h2 class="slide-title">Traditional Governance Gaps vs. Digital Twin</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="card" style="flex: 1; border-color: rgba(244, 63, 94, 0.4);">
                        <div class="card-title" style="color: var(--accent-rose);">❌ Traditional Municipal Limitations</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Siloed Decision-Making:</b> Transportation, energy grids, and health departments operate without synchronized cross-department feedback loops.</li>
                                <li><b>Static & Post-Facto Data:</b> Reliance on annual census forms and static maps means crises are analyzed months after damage occurs.</li>
                                <li><b>Cost-Prohibitive Enterprise Software:</b> Siemens or Bentley Digital Twins cost $100k+ and demand supercomputer clusters.</li>
                                <li><b>Lack of Rigor in Entertainment Games:</b> SimCity & Cities: Skylines prioritize casual gameplay, lacking deterministic formulas and REST audit pipelines.</li>
                            </ul>
                        </div>
                    </div>

                    <div class="card" style="flex: 1; border-color: rgba(16, 185, 129, 0.4);">
                        <div class="card-title" style="color: var(--accent-emerald);">✅ Our Engineering Innovations</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Synchronous Discrete Pipeline:</b> 6 subsystems tick harmoniously every virtual day (1 real sec = 1 virtual day).</li>
                                <li><b>Dynamic Cause-and-Effect Feedback:</b> Power deficits cascade into factory shutdowns, unemployment, and citizen migration.</li>
                                <li><b>Enterprise Cloud Integration:</b> Complete OpenAPI/Swagger REST endpoints with PostgreSQL telemetry history.</li>
                                <li><b>Accessible & Open:</b> Runs smoothly on standard educational PCs with full source code transparency.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 4: LITERATURE SURVEY ================= -->
            <section class="slide" data-title="Literature Survey" data-notes="We conducted a comprehensive literature survey across commercial platforms, gaming engines, and academic tools like AnyLogic. Our solution uniquely delivers 3D real-time rendering, deterministic math, and cloud telemetry on consumer hardware.">
                <div class="slide-header">
                    <div class="slide-tag">STATE OF THE ART</div>
                    <h2 class="slide-title">Comparative Analysis & Literature Survey</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="card" style="flex: 1;">
                        <div class="card-title">📊 Architectural Benchmark Matrix</div>
                        <div class="card-body">
                            <table class="slide-table">
                                <thead>
                                    <tr>
                                        <th>Platform / Solution</th>
                                        <th>Visual Fidelity</th>
                                        <th>Mathematical Rigor</th>
                                        <th>Cloud Telemetry</th>
                                        <th>Hardware Target</th>
                                        <th>Licensing</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td><b>Bentley / Siemens</b></td>
                                        <td>High (Static BIM)</td>
                                        <td>High</td>
                                        <td>Proprietary Cloud</td>
                                        <td>Enterprise Server</td>
                                        <td><span class="badge-pill badge-danger">Costly ($$$$)</span></td>
                                    </tr>
                                    <tr>
                                        <td><b>SimCity (EA)</b></td>
                                        <td>3D Interactive</td>
                                        <td>Arcade / Heuristic</td>
                                        <td>None</td>
                                        <td>Mid Gaming PC</td>
                                        <td><span class="badge-pill badge-warning">Proprietary Game</span></td>
                                    </tr>
                                    <tr>
                                        <td><b>Cities: Skylines</b></td>
                                        <td>High 3D</td>
                                        <td>Moderate</td>
                                        <td>None</td>
                                        <td>High-End Gaming PC</td>
                                        <td><span class="badge-pill badge-warning">Commercial Game</span></td>
                                    </tr>
                                    <tr>
                                        <td><b>Academic AnyLogic</b></td>
                                        <td>2D / Discrete Grid</td>
                                        <td>High (Pure Math)</td>
                                        <td>Add-on Database</td>
                                        <td>Standard PC</td>
                                        <td><span class="badge-pill badge-warning">Expensive Academic</span></td>
                                    </tr>
                                    <tr style="background: rgba(6, 182, 212, 0.1);">
                                        <td><b>Our Platform</b></td>
                                        <td><b>Interactive 3D (60 FPS)</b></td>
                                        <td><b>High (Deterministic)</b></td>
                                        <td><b>FastAPI + PostgreSQL</b></td>
                                        <td><b>Consumer Laptop</b></td>
                                        <td><span class="badge-pill badge-success">Open Academic</span></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 5: SYSTEM ARCHITECTURE ================= -->
            <section class="slide" data-title="System Architecture" data-notes="Fig 4.1 shows our 4-tier decoupled architecture: Unity 3D presentation, C# deterministic simulation engine, CityApiClient async networking, and FastAPI with PostgreSQL. This enables unit-testing simulation logic without launching graphics.">
                <div class="slide-header">
                    <div class="slide-tag">SYSTEM ARCHITECTURE</div>
                    <h2 class="slide-title">High-Level 4-Tier Decoupled Architecture</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="figure-box">
                        <img src="docs_figures/fig4_1_architecture.png" alt="Architecture Diagram">
                        <div class="fig-caption">Fig. 4.1: Decoupled 4-Tier Software Architecture</div>
                    </div>

                    <div class="card" style="flex: 0.9;">
                        <div class="card-title">🏗️ Architectural Layer Breakdown</div>
                        <div class="card-body">
                            <ul>
                                <li><b>1. Presentation Layer (Unity 6.3 LTS):</b> Procedural mesh rendering, 24h orbital daylighting, weather particles, and dynamic HUD canvas.</li>
                                <li><b>2. Simulation Logic Layer (C# Engine):</b> Stateless mathematical routines executing synchronized daily discrete steps (Economy, Population, Utilities).</li>
                                <li><b>3. Networking Layer (CityApiClient):</b> Asynchronous non-blocking HTTP REST client with token authorization and offline failover caching.</li>
                                <li><b>4. Persistence Layer (FastAPI + PostgreSQL):</b> High-throughput ASGI microservice, Pydantic validation schemas, and SQLAlchemy ORM storage.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 6: COMPONENT PIPELINE ================= -->
            <section class="slide" data-title="Component Pipeline" data-notes="The runtime pipeline is orchestrated by CityManager. Every frame advances delta time. At fixed daily intervals (1 sec = 1 day), CityManager steps UtilitySystem, EconomySystem, PopulationSystem, TrafficSystem, EnvironmentSystem, and CSCI aggregation.">
                <div class="slide-header">
                    <div class="slide-tag">RUNTIME LIFECYCLE</div>
                    <h2 class="slide-title">Subsystem Execution & Synchronous Pipeline</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="figure-box">
                        <img src="docs_figures/fig4_2_component_diagram.png" alt="Component Diagram">
                        <div class="fig-caption">Fig. 4.2: Subsystem Interaction & Data Flow Pipeline</div>
                    </div>

                    <div class="card" style="flex: 0.9;">
                        <div class="card-title">⏱️ The Daily Discrete Simulation Step</div>
                        <div class="card-body">
                            <ul>
                                <li><b style="color:var(--accent-cyan);">1. Utility Balancing:</b> Power and water demands are balanced. Brownout or drought flags propagate downstream.</li>
                                <li><b style="color:var(--accent-emerald);">2. Fiscal Settlement:</b> Collects residential, commercial, and industrial taxes; deducts facility maintenance costs.</li>
                                <li><b style="color:var(--accent-amber);">3. Demographics & Migration:</b> Evaluates citizen happiness and attractiveness to compute immigration or demographic flight.</li>
                                <li><b style="color:var(--accent-rose);">4. Traffic & Road Pavement:</b> Calculates corridor congestion ratios and decrements road quality under heavy vehicle wear.</li>
                                <li><b style="color:var(--accent-purple);">5. Environmental Dispersion:</b> Models industrial pollution spread; park canopies act as carbon sinks.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 7: MATHEMATICAL FORMULATIONS ================= -->
            <section class="slide" data-title="Mathematical Models" data-notes="Our simulator is governed by explicit mathematical formulas. The municipal treasury balances tax receipts and infrastructure costs. Attractiveness determines migration. The Composite Smart City Index aggregates 28 metrics into an objective 0-100 score.">
                <div class="slide-header">
                    <div class="slide-tag">MATHEMATICAL RIGOR</div>
                    <h2 class="slide-title">Deterministic Simulation Algorithms & Formulas</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="card" style="flex: 1;">
                        <div class="card-title">📐 Core Mathematical Formulations</div>
                        <div class="card-body">
                            <div class="formula-card">
                                <div style="font-weight:700; color:#fff; margin-bottom:4px;">1. Municipal Fiscal Revenue:</div>
                                <div class="formula-code">R_daily = (Pop * T_res) + (Comm * T_comm) + (Ind * T_ind) - Maint_total</div>
                                <div style="font-size:12px; color:var(--text-muted);">Taxes generate income; facility maintenance costs increase with age and neglect.</div>
                            </div>

                            <div class="formula-card">
                                <div style="font-weight:700; color:#fff; margin-bottom:4px;">2. Demographic Attractiveness:</div>
                                <div class="formula-code">A_city = 0.35*H + 0.20*Q_h + 0.20*Q_e - 0.15*T_rate - 0.10*AQI_penalty</div>
                                <div style="font-size:12px; color:var(--text-muted);">Attractiveness > 55 triggers population influx; Attractiveness < 40 triggers citizen exodus.</div>
                            </div>

                            <div class="formula-card">
                                <div style="font-weight:700; color:#fff; margin-bottom:4px;">3. Composite Smart City Index (CSCI):</div>
                                <div class="formula-code">CSCI = 0.25*S_econ + 0.20*S_env + 0.20*S_infra + 0.20*S_social + 0.15*S_gov</div>
                                <div style="font-size:12px; color:var(--text-muted);">Synthesizes 28 indicators across 5 pillars into a standardized 0-100 score.</div>
                            </div>
                        </div>
                    </div>

                    <div class="card" style="flex: 1;">
                        <div class="card-title">🧪 Live Mathematical Model Demonstrator</div>
                        <div class="card-body">
                            <p style="font-size:13px; margin-bottom:12px;">
                                Adjust parameters below to observe real-time recalculation of the <b>Composite Smart City Index (CSCI)</b>:
                            </p>
                            
                            <div class="interactive-calculator">
                                <div class="calc-control">
                                    <div class="calc-label"><span>Economy / Treasury:</span> <span id="val_econ">75</span></div>
                                    <input type="range" class="calc-slider" id="sl_econ" min="0" max="100" value="75" oninput="updateDemoCSCI()">
                                </div>
                                <div class="calc-control">
                                    <div class="calc-label"><span>Environmental Quality:</span> <span id="val_env">60</span></div>
                                    <input type="range" class="calc-slider" id="sl_env" min="0" max="100" value="60" oninput="updateDemoCSCI()">
                                </div>
                                <div class="calc-control">
                                    <div class="calc-label"><span>Infrastructure & Transit:</span> <span id="val_infra">80</span></div>
                                    <input type="range" class="calc-slider" id="sl_infra" min="0" max="100" value="80" oninput="updateDemoCSCI()">
                                </div>
                                <div class="calc-control">
                                    <div class="calc-label"><span>Healthcare & Social:</span> <span id="val_soc">70</span></div>
                                    <input type="range" class="calc-slider" id="sl_soc" min="0" max="100" value="70" oninput="updateDemoCSCI()">
                                </div>
                                <div class="calc-control" style="grid-column: span 2;">
                                    <div class="calc-label"><span>Governance & Happiness:</span> <span id="val_gov">65</span></div>
                                    <input type="range" class="calc-slider" id="sl_gov" min="0" max="100" value="65" oninput="updateDemoCSCI()">
                                </div>

                                <div class="csci-score-display">
                                    <div>
                                        <div style="font-size: 11px; text-transform:uppercase; color:var(--text-muted);">Calculated CSCI</div>
                                        <div class="csci-big-val" id="res_csci">70.5</div>
                                    </div>
                                    <div>
                                        <div style="font-size: 11px; text-transform:uppercase; color:var(--text-muted);">Civic Tier Rating</div>
                                        <div id="res_tier" style="font-size:18px; font-weight:700; color:var(--accent-emerald);">Metropolis</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 8: UML OBJECT MODEL ================= -->
            <section class="slide" data-title="UML Object Model" data-notes="Fig 4.4 displays our Object-Oriented Class Hierarchy. We utilized the Singleton pattern for CityManager, stateless pure methods for simulation subsystems, Observer event delegates for UI alerts, and DTOs for JSON persistence.">
                <div class="slide-header">
                    <div class="slide-tag">OBJECT-ORIENTED DESIGN</div>
                    <h2 class="slide-title">UML Class Structure & Design Patterns</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="figure-box">
                        <img src="docs_figures/fig4_4_class.png" alt="Class Diagram">
                        <div class="fig-caption">Fig. 4.4: Complete UML Class Diagram & Subsystem Relationships</div>
                    </div>

                    <div class="card" style="flex: 0.9;">
                        <div class="card-title">🧩 Applied Design Patterns</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Singleton Orchestration:</b> <code>CityManager</code> acts as the single central hub, coordinating simulation clocks and cross-module events.</li>
                                <li><b>Stateless Mathematical Modules:</b> <code>EconomySystem</code>, <code>PopulationSystem</code>, and <code>TrafficSystem</code> use pure static methods, ensuring high unit-testability.</li>
                                <li><b>Observer & Event Handlers:</b> Citizen requests, structural fires, and blackouts notify the UI via decoupled C# event delegates.</li>
                                <li><b>Data Transfer Objects (DTO):</b> <code>CitySaveData</code> and <code>TelemetryRecord</code> encapsulate clean JSON serializable representations.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 9: DATABASE PERSISTENCE ================= -->
            <section class="slide" data-title="Database Architecture" data-notes="Fig 4.9 outlines our Entity Relationship Diagram. We use PostgreSQL 17 managed through SQLAlchemy ORM. The relational model stores user accounts, city master records, binary save blobs, and high-frequency time-series telemetry.">
                <div class="slide-header">
                    <div class="slide-tag">PERSISTENCE ARCHITECTURE</div>
                    <h2 class="slide-title">Relational Database Design & Schema (ERD)</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="figure-box">
                        <img src="docs_figures/fig4_9_erd.png" alt="ERD Diagram">
                        <div class="fig-caption">Fig. 4.9: Relational Entity-Relationship Diagram (PostgreSQL 17)</div>
                    </div>

                    <div class="card" style="flex: 0.9;">
                        <div class="card-title">🗄️ Relational Table Entities</div>
                        <div class="card-body">
                            <ul>
                                <li><b><code>users</code> Table:</b> Stores administrator credentials with hashed passwords and role authorizations.</li>
                                <li><b><code>cities</code> Table:</b> Master city entity containing city name, difficulty level, starting treasury, and creation timestamps.</li>
                                <li><b><code>saves</code> Table:</b> Houses full JSON snapshots of the city state, infrastructure upgrades, and active citizen petitions.</li>
                                <li><b><code>telemetry</code> Table:</b> High-frequency time-series logging population, happiness, treasury, AQI, and CSCI for 30-day analytics.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 10: PROCEDURAL 3D WORLD ================= -->
            <section class="slide" data-title="3D World Generation" data-notes="Unity 6.3 LTS renders our dynamic world. Features include procedural road networks, dynamic river carving, 24-hour orbital sunlight cycles, and particle-based weather states that directly influence road friction and solar generation.">
                <div class="slide-header">
                    <div class="slide-tag">GRAPHICS & IMMERSION</div>
                    <h2 class="slide-title">Procedural 3D World & Dynamic Environment</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="figure-box" style="flex:1;">
                        <img src="docs_figures/fig5_2_daynight.png" alt="Day Night Cycle">
                        <div class="fig-caption">Fig. 5.2: 24-Hour Orbital Day/Night Lighting Transition</div>
                    </div>
                    <div class="figure-box" style="flex:1;">
                        <img src="docs_figures/fig5_1_terrain_river.png" alt="Terrain and River Generation">
                        <div class="fig-caption">Fig. 5.1: Procedural Terrain, River Carving & Bridge Placement</div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 11: HUD TELEMETRY CONTROLS ================= -->
            <section class="slide" data-title="HUD & User Controls" data-notes="Fig 7.2 displays the City HUD interface. It provides comprehensive real-time feedback: population, treasury, citizen satisfaction, and zoning palettes. Navigation includes 6-DOF camera panning, orbiting, zooming, and warp speeds.">
                <div class="slide-header">
                    <div class="slide-tag">USER EXPERIENCE</div>
                    <h2 class="slide-title">Interactive Heads-Up Display (HUD) & Controls</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="figure-box">
                        <img src="docs_figures/fig7_2_city_hud.png" alt="City HUD">
                        <div class="fig-caption">Fig. 7.2: In-Game Interactive Telemetry HUD & Policy Controls</div>
                    </div>

                    <div class="card" style="flex: 0.9;">
                        <div class="card-title">🕹️ Navigation & Civic Tools</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Free 6-DOF Camera:</b> WASD smooth translation, Right-Mouse orbital pitch/yaw, and scroll-wheel elevation zoom.</li>
                                <li><b>Simulation Speed Multiplier:</b> Toggle seamlessly between Pause (0x), Normal (1x), Fast (2x), and Warp (4x) speeds.</li>
                                <li><b>Zoning & Infrastructure Palette:</b> Single-click placement of Residential, Commercial, and Industrial zones with auto-road connection.</li>
                                <li><b>Citizen Petition Feed:</b> Real-time citizen grievances requiring policy resolutions or financial interventions.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 12: FASTAPI BACKEND ================= -->
            <section class="slide" data-title="FastAPI Cloud Backend" data-notes="Fig 7.3 shows our FastAPI Swagger UI. Built with Python 3.12, FastAPI, and PostgreSQL 17, it delivers sub-15ms response latency for telemetry snapshots and automated OpenAPI documentation. Containerized with Docker Compose.">
                <div class="slide-header">
                    <div class="slide-tag">CLOUD SERVICES</div>
                    <h2 class="slide-title">FastAPI Backend & Telemetry Microservice</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="figure-box">
                        <img src="docs_figures/fig7_3_database_portal.png" alt="Database Portal">
                        <div class="fig-caption">Fig. 7.3: Interactive Swagger API Documentation & Database Portal</div>
                    </div>

                    <div class="card" style="flex: 0.9;">
                        <div class="card-title">⚡ Microservice Architecture</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Asynchronous ASGI Engine:</b> Powered by Uvicorn and FastAPI, achieving high throughput and sub-15ms response latency.</li>
                                <li><b>Type-Safe Validation:</b> Pydantic schemas validate all simulation telemetry, rejecting malformed client payloads.</li>
                                <li><b>Full CRUD Endpoints:</b> Dedicated routes for city creation (<code>POST /cities</code>), querying, updates, and telemetry history.</li>
                                <li><b>Docker Orchestration:</b> Multi-container deployment with PostgreSQL and pgAdmin preconfigured in <code>docker-compose.yml</code>.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 13: QUALITY ASSURANCE ================= -->
            <section class="slide" data-title="Quality Assurance" data-notes="Fig 6.1 illustrates our Testing Pyramid. We formulated 50 formal test cases across Unit, Integration, System, and Security domains. All 50 test cases achieved a 100% PASS rate upon final release.">
                <div class="slide-header">
                    <div class="slide-tag">VERIFICATION & QA</div>
                    <h2 class="slide-title">Testing Pyramid & 50 Exhaustive Test Cases</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="figure-box">
                        <img src="docs_figures/fig6_1_test_pyramid.png" alt="Testing Pyramid">
                        <div class="fig-caption">Fig. 6.1: Quality Assurance Testing Pyramid & Distribution</div>
                    </div>

                    <div class="card" style="flex: 0.9;">
                        <div class="card-title">🛡️ QA Verification Metrics</div>
                        <div class="card-body">
                            <ul>
                                <li><b>50 Test Cases (TC-01 to TC-50):</b> 100% PASS rate achieved across all simulation, graphical, and cloud persistence modules.</li>
                                <li><b>Mathematical Boundary Tests:</b> Validated zero population, extreme debt states, brownout resilience, and compound tax caps.</li>
                                <li><b>Network Resilience:</b> Verified graceful offline fallback when backend server is temporarily unreachable.</li>
                                <li><b>Determinism Validation:</b> Repeated execution across identical seed initializations produced identical numerical trajectories.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 14: PERFORMANCE BENCHMARKS ================= -->
            <section class="slide" data-title="Performance Benchmarks" data-notes="Hardware benchmarks in Fig 7.1 show consistent 60+ FPS performance. Simulation ticks consume just 1.8ms per virtual day, client heap stays under 320 MB, and API latency averages 8.4ms.">
                <div class="slide-header">
                    <div class="slide-tag">PROFILING & STRESS TESTING</div>
                    <h2 class="slide-title">Hardware Performance & Stress Profiling</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="figure-box">
                        <img src="docs_figures/fig7_1_benchmarks.png" alt="Benchmarks">
                        <div class="fig-caption">Fig. 7.1: Performance Profiling: FPS, CPU Time, and Memory Footprint</div>
                    </div>

                    <div class="card" style="flex: 0.9;">
                        <div class="card-title">📈 System Performance Benchmarks</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Solid 60+ FPS Rendering:</b> Stable framerate on mid-range hardware with zero stuttering during camera rotations.</li>
                                <li><b>1.8ms Simulation Tick:</b> Low CPU calculation overhead leaves >14ms of each 16.6ms frame budget for GPU rendering.</li>
                                <li><b>Memory Optimization:</b> Client managed heap remains under 320 MB during extended 5-hour continuous simulation runs.</li>
                                <li><b>Telemetry Latency:</b> Average PostgreSQL record insertion latency measured at 8.4ms over local network.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 15: DISASTER & INCIDENTS ================= -->
            <section class="slide" data-title="Disasters & Emergency" data-notes="Emergent municipal incidents challenge the player. Random building fires, water bursts, and traffic gridlocks test fiscal resilience and emergency department dispatch efficiency.">
                <div class="slide-header">
                    <div class="slide-tag">EMERGENCY MANAGEMENT</div>
                    <h2 class="slide-title">Random Incidents, Citizen Petitions & Disasters</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="figure-box" style="flex:1;">
                        <img src="docs_figures/fig7_5_disaster_emergency.png" alt="Disaster Response">
                        <div class="fig-caption">Fig. 7.5: Structural Fire Incident & Emergency Dispatch</div>
                    </div>
                    <div class="figure-box" style="flex:1;">
                        <img src="docs_figures/fig7_6_citizen_petition.png" alt="Citizen Petition">
                        <div class="fig-caption">Fig. 7.6: Interactive Citizen Petition & Policy Choice Interface</div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 16: KEY INNOVATIONS ================= -->
            <section class="slide" data-title="Key Innovations" data-notes="Our core technical contributions include the multi-agent coupling, standardized CSCI metric, full-stack hybrid cloud architecture, and end-to-end documentation compliant with Mumbai University guidelines.">
                <div class="slide-header">
                    <div class="slide-tag">CONTRIBUTIONS</div>
                    <h2 class="slide-title">Key Innovations & Engineering Contributions</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="card" style="flex: 1;">
                        <div class="card-title">🌟 Architectural & Scientific Highlights</div>
                        <div class="card-body">
                            <ul>
                                <li><b style="color:var(--accent-cyan);">Multi-Subsystem Determinism:</b> Tightly couples 6 municipal sectors into synchronized ticks, mirroring genuine socio-technical feedback loops.</li>
                                <li><b style="color:var(--accent-emerald);">Standardized CSCI Index:</b> Converts 28 raw data metrics into an objective 0-100 rating based on international ISO 37120 standards.</li>
                                <li><b style="color:var(--accent-amber);">Full-Stack Hybrid Cloud:</b> Combines high-fidelity 3D Unity graphics with modern Python FastAPI cloud telemetry and PostgreSQL.</li>
                                <li><b style="color:var(--accent-purple);">Emergent Cause-and-Effect:</b> Unscripted interactions where budget deficits directly degrade road quality, impair emergency response, and trigger demographic exodus.</li>
                                <li><b style="color:var(--accent-rose);">Complete Academic Rigor:</b> 50 verified test cases, 30+ architectural diagrams, and exhaustive black book documentation.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 17: LIMITATIONS & CHALLENGES ================= -->
            <section class="slide" data-title="Limitations & Challenges" data-notes="We overcame concurrency hurdles and floating-point compounding. Current boundaries include procedural primitive visuals and single-player focus, creating clear avenues for future research.">
                <div class="slide-header">
                    <div class="slide-tag">CRITICAL EVALUATION</div>
                    <h2 class="slide-title">Engineering Challenges Overcome & Boundaries</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="card" style="flex: 1; border-color: rgba(245, 158, 11, 0.4);">
                        <div class="card-title" style="color: var(--accent-amber);">⚡ Engineering Hurdles Overcome</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Simulation Concurrency in Unity:</b> Executed complex multi-subsystem equations on background ticks without causing frame-time stutter on the main render thread.</li>
                                <li><b>Compound Floating-Point Drift:</b> Implemented deterministic epsilon thresholds to prevent long-term tax and population rounding anomalies.</li>
                                <li><b>Cross-Platform JSON Serialization:</b> Reconciled Unity C# data structures with Python Pydantic models through strict schema contracts.</li>
                            </ul>
                        </div>
                    </div>

                    <div class="card" style="flex: 1; border-color: rgba(6, 182, 212, 0.4);">
                        <div class="card-title" style="color: var(--accent-cyan);">⚠️ Current System Scope Boundaries</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Procedural Primitive Visuals:</b> Buildings and vehicles utilize procedural geometric primitives rather than custom photorealistic assets.</li>
                                <li><b>Single-Operator Focus:</b> Currently tailored for single-user administrative sandboxing rather than multiplayer cooperative planning.</li>
                                <li><b>Simulated Weather States:</b> Transitions follow Markov probability chains rather than ingestion of live satellite meteorological feeds.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 18: FUTURE ROADMAP ================= -->
            <section class="slide" data-title="Future Roadmap" data-notes="Our future roadmap is divided into three phases: Phase 1 adds A* NavMesh pathfinding and RL policy optimization. Phase 2 introduces real OpenStreetMap GIS ingestion and live IoT feeds. Phase 3 enables collaborative multiplayer and VR immersion.">
                <div class="slide-header">
                    <div class="slide-tag">FUTURE SCOPE</div>
                    <h2 class="slide-title">Technology Roadmap & Strategic Vision</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="card" style="flex: 1;">
                        <div class="card-title">🤖 Phase 1: AI & Navigation</div>
                        <div class="card-body">
                            <ul>
                                <li><b>NavMesh Agent Pathfinding:</b> Dynamic A* vehicular rerouting around traffic accidents and road construction zones.</li>
                                <li><b>Reinforcement Learning (PPO):</b> Autonomous policy advisors suggesting optimal tax rates and green buffer zones.</li>
                            </ul>
                        </div>
                    </div>

                    <div class="card" style="flex: 1;">
                        <div class="card-title">🗺️ Phase 2: GIS & IoT Ingestion</div>
                        <div class="card-body">
                            <ul>
                                <li><b>OpenStreetMap (OSM) Integration:</b> Ingest real-world metropolitan road networks and elevation contour maps.</li>
                                <li><b>Live IoT Telemetry Feeds:</b> Connect to municipal smart sensor APIs for true real-time digital twin monitoring.</li>
                            </ul>
                        </div>
                    </div>

                    <div class="card" style="flex: 1;">
                        <div class="card-title">👓 Phase 3: Multiplayer & VR</div>
                        <div class="card-body">
                            <ul>
                                <li><b>Collaborative Multi-Tenancy:</b> Allow multiple planning students to concurrently co-govern adjacent municipal wards.</li>
                                <li><b>VR Street Immersion:</b> OpenXR virtual reality tours enabling first-person street-level walkability audits.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 19: CONCLUSION ================= -->
            <section class="slide" data-title="Conclusion & Outcomes" data-notes="The Smart City Management Simulator achieves all proposed aims. It proves that real-time 3D immersion, deterministic multi-agent math, and cloud telemetry can be unified into an accessible platform on consumer hardware.">
                <div class="slide-header">
                    <div class="slide-tag">PROJECT SUMMARY</div>
                    <h2 class="slide-title">Conclusion & Academic Learning Outcomes</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="card" style="flex: 1;">
                        <div class="card-title">🎯 Summary of Deliverables & Takeaways</div>
                        <div class="card-body">
                            <ul>
                                <li><b style="color:var(--accent-cyan);">Successful Project Delivery:</b> Conceptualized, architected, and validated a complete 3D multi-agent urban digital twin.</li>
                                <li><b style="color:var(--accent-emerald);">Full-Stack Synthesis:</b> United Unity 3D game engine technology, discrete mathematics, FastAPI ASGI REST services, and PostgreSQL relational persistence.</li>
                                <li><b style="color:var(--accent-amber);">Demonstrated Determinism:</b> 50 test cases confirm numerical stability, deterministic repeatability, and zero memory leaks.</li>
                                <li><b style="color:var(--accent-purple);">Educational & Civic Value:</b> Provides an accessible, risk-free computational laboratory where urban planners can prototype policy interventions before deploying public capital.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>

            <!-- ================= SLIDE 20: ACKNOWLEDGEMENTS & QA ================= -->
            <section class="slide" data-title="Q&A and Defense" data-notes="I express my sincere thanks to my guide Prof. Aarti Gawai, our HOD, and the faculty members of D.G. Ruparel College. I am now pleased to invite questions from the honorable examiners.">
                <div class="slide-header">
                    <div class="slide-tag">ACKNOWLEDGEMENTS & DEFENSE</div>
                    <h2 class="slide-title">Thank You — Viva Defense Discussion</h2>
                    <div class="slide-divider"></div>
                </div>
                <div class="slide-content">
                    <div class="card" style="flex: 1; align-items: center; justify-content: center; text-align: center; padding: 40px;">
                        <div style="font-size: 52px; margin-bottom: 12px;">🏙️</div>
                        <h2 style="font-size: 34px; font-weight: 800; color: #fff; margin-bottom: 8px;">THANK YOU!</h2>
                        <div style="font-size: 18px; color: var(--accent-cyan); font-weight: 600; margin-bottom: 24px;">
                            Questions, Feedback & Viva Voce Discussion
                        </div>
                        <p style="color: var(--text-secondary); max-width: 650px; font-size: 15px; margin-bottom: 20px;">
                            <b>Sahil Vishal Kate</b> (Roll No.: 9041)<br>
                            Under the Esteemed Guidance of: <b>Prof. Aarti Gawai</b><br>
                            Department of Computer Science<br>
                            <b>D.G. Ruparel College of Arts, Science and Commerce</b><br>
                            Affiliated to the University of Mumbai
                        </p>
                        <div class="badge-pill badge-info" style="font-size: 13px; padding: 6px 16px;">
                            🚀 Complete Unity Build, FastAPI Telemetry & Black Book Ready
                        </div>
                    </div>
                </div>
            </section>

        </div>
    </main>

    <!-- Slide Sorter Modal -->
    <div class="modal-overlay" id="overviewModal" onclick="toggleOverview()">
        <div class="modal-header" onclick="event.stopPropagation()">
            <h2 style="font-size: 20px; color: #fff;">🗂️ Slide Navigation Overview (Press O or Esc)</h2>
            <button class="btn" onclick="toggleOverview()">✕ Close</button>
        </div>
        <div class="sorter-grid" id="sorterGrid" onclick="event.stopPropagation()">
            <!-- Dynamic thumbnails generated via JS -->
        </div>
    </div>

    <!-- Live Speaker Notes Drawer -->
    <div class="notes-drawer" id="notesDrawer">
        <div class="notes-header">
            <span>🎙️ SPEAKER NOTES & VIVA TALKING POINTS (PRESS N TO TOGGLE)</span>
            <span id="notesSlideTag">SLIDE 1 / 20</span>
        </div>
        <div class="notes-content" id="notesText">
            Speaker notes loading...
        </div>
    </div>

    <!-- Bottom Status Bar -->
    <footer class="bottom-bar">
        <div class="slide-progress-bar" id="progressBar"></div>
        <div>
            <span id="slideIndicator" style="font-weight: 700; color: #fff;">Slide 1 / 20</span> — 
            <span id="slideTitleDisplay" style="color: var(--accent-cyan);">Title & Identification</span>
        </div>
        <div class="nav-buttons">
            <button class="btn" onclick="prevSlide()" title="Previous Slide (Left Arrow / PageUp)">◀ Prev</button>
            <button class="btn" onclick="nextSlide()" title="Next Slide (Right Arrow / Space / PageDown)">Next ▶</button>
        </div>
    </footer>

    <script>
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;
        let currentSlide = 0;

        function updateSlide() {
            slides.forEach((slide, index) => {
                slide.classList.toggle('active', index === currentSlide);
            });

            const activeSlide = slides[currentSlide];
            const title = activeSlide.getAttribute('data-title') || '';
            const notes = activeSlide.getAttribute('data-notes') || 'No notes for this slide.';

            // Update UI elements
            document.getElementById('slideIndicator').textContent = `Slide ${currentSlide + 1} / ${totalSlides}`;
            document.getElementById('slideTitleDisplay').textContent = title;
            document.getElementById('progressBar').style.width = `${((currentSlide + 1) / totalSlides) * 100}%`;
            
            document.getElementById('notesSlideTag').textContent = `SLIDE ${currentSlide + 1} / ${totalSlides} — ${title.toUpperCase()}`;
            document.getElementById('notesText').textContent = notes;

            // Update modal active thumb
            const thumbs = document.querySelectorAll('.sorter-thumb');
            thumbs.forEach((th, idx) => {
                th.classList.toggle('active', idx === currentSlide);
            });
        }

        function nextSlide() {
            if (currentSlide < totalSlides - 1) {
                currentSlide++;
                updateSlide();
            }
        }

        function prevSlide() {
            if (currentSlide > 0) {
                currentSlide--;
                updateSlide();
            }
        }

        function goToSlide(index) {
            if (index >= 0 && index < totalSlides) {
                currentSlide = index;
                updateSlide();
                const modal = document.getElementById('overviewModal');
                if (modal.classList.contains('active')) {
                    toggleOverview();
                }
            }
        }

        function toggleFullscreen() {
            if (!document.fullscreenElement) {
                document.documentElement.requestFullscreen().catch(err => {
                    alert(`Error attempting to enable fullscreen: ${err.message}`);
                });
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                }
            }
        }

        function toggleOverview() {
            const modal = document.getElementById('overviewModal');
            modal.classList.toggle('active');
        }

        function toggleNotes() {
            const drawer = document.getElementById('notesDrawer');
            drawer.classList.toggle('open');
        }

        // Populate Slide Sorter
        function initSorter() {
            const grid = document.getElementById('sorterGrid');
            grid.innerHTML = '';
            slides.forEach((slide, idx) => {
                const title = slide.getAttribute('data-title') || `Slide ${idx + 1}`;
                const thumb = document.createElement('div');
                thumb.className = `sorter-thumb ${idx === currentSlide ? 'active' : ''}`;
                thumb.onclick = () => goToSlide(idx);
                thumb.innerHTML = `
                    <div class="sorter-num">SLIDE ${idx + 1}</div>
                    <div class="sorter-name">${title}</div>
                `;
                grid.appendChild(thumb);
            });
        }

        // Keyboard Controls
        window.addEventListener('keydown', (e) => {
            if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
                nextSlide();
            } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
                prevSlide();
            } else if (e.key.toLowerCase() === 'f') {
                toggleFullscreen();
            } else if (e.key.toLowerCase() === 'o' || e.key === 'Escape') {
                toggleOverview();
            } else if (e.key.toLowerCase() === 'n') {
                toggleNotes();
            } else if (e.key === 'Home') {
                goToSlide(0);
            } else if (e.key === 'End') {
                goToSlide(totalSlides - 1);
            }
        });

        // Interactive Demonstrator Function
        function updateDemoCSCI() {
            const econ = parseFloat(document.getElementById('sl_econ').value);
            const env = parseFloat(document.getElementById('sl_env').value);
            const infra = parseFloat(document.getElementById('sl_infra').value);
            const soc = parseFloat(document.getElementById('sl_soc').value);
            const gov = parseFloat(document.getElementById('sl_gov').value);

            document.getElementById('val_econ').textContent = econ;
            document.getElementById('val_env').textContent = env;
            document.getElementById('val_infra').textContent = infra;
            document.getElementById('val_soc').textContent = soc;
            document.getElementById('val_gov').textContent = gov;

            // CSCI = 0.25*econ + 0.20*env + 0.20*infra + 0.20*soc + 0.15*gov
            const csci = (0.25 * econ) + (0.20 * env) + (0.20 * infra) + (0.20 * soc) + (0.15 * gov);
            document.getElementById('res_csci').textContent = csci.toFixed(1);

            let tier = "Settlement";
            let color = "#94a3b8";
            if (csci >= 85) { tier = "Metropolis"; color = "#10b981"; }
            else if (csci >= 70) { tier = "Smart City"; color = "#06b6d4"; }
            else if (csci >= 55) { tier = "Developing Township"; color = "#3b82f6"; }
            else if (csci >= 40) { tier = "Basic Municipality"; color = "#f59e0b"; }
            else { tier = "Distressed Settlement"; color = "#f43f5e"; }

            const tierEl = document.getElementById('res_tier');
            tierEl.textContent = tier;
            tierEl.style.color = color;
        }

        // Initialize
        initSorter();
        updateSlide();
        updateDemoCSCI();
    </script>
</body>
</html>
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Interactive HTML presentation successfully created at: {output_path}")

if __name__ == "__main__":
    generate_html_presentation()
