import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen standard
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_slide_layout = prs.slide_layouts[6]
    
    # =========================================================================
    # THEME: OBSIDIAN GOLD & EMERALD CYBERNETIC PALETTE
    # =========================================================================
    C_BG_DARK       = RGBColor(10, 14, 23)      # #0A0E17 - Deep Onyx Obsidian Background
    C_BG_CARD       = RGBColor(18, 26, 38)      # #121A26 - Elevated Dark Charcoal Card
    C_BG_CARD_ALT   = RGBColor(24, 34, 50)      # #182232 - Secondary Card Accent
    C_BORDER_MUTED  = RGBColor(38, 52, 72)      # #263448 - Subtle Card Border
    
    # Vibrant Accent Colors
    C_EMERALD_NEON  = RGBColor(16, 185, 129)    # #10B981 - Cyber Emerald Primary
    C_MINT_GLOW     = RGBColor(52, 211, 153)    # #34D399 - Radiant Mint Accent
    C_GOLD_ACCENT   = RGBColor(245, 158, 11)    # #F59E0B - Warm Cyber Gold
    C_GOLD_LIGHT    = RGBColor(251, 191, 36)    # #FBBF24 - Bright Gold Text
    C_TEAL_CYAN     = RGBColor(45, 212, 191)    # #2DD4BF - Electric Teal
    C_ROSE_ALERT    = RGBColor(244, 63, 94)     # #F43F5E - Warning / Alert Rose
    
    # Typography Colors
    C_TEXT_LIGHT    = RGBColor(248, 250, 252)   # #F8FAFC - Pure Crisp White
    C_TEXT_MUTED    = RGBColor(160, 174, 192)   # #A0AEC0 - Light Steel Body Text
    C_TEXT_DIM      = RGBColor(113, 128, 150)   # #718096 - Dim Footer Text
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FIG_DIR = os.path.join(BASE_DIR, "docs_figures")
    
    def set_slide_background(slide, color=C_BG_DARK):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        
        # Dual-tone top cyber accent strip (Gold + Emerald)
        gold_strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(4.5), Inches(0.06))
        gold_strip.fill.solid()
        gold_strip.fill.fore_color.rgb = C_GOLD_ACCENT
        gold_strip.line.fill.background()

        emerald_strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(4.5), 0, prs.slide_width - Inches(4.5), Inches(0.06))
        emerald_strip.fill.solid()
        emerald_strip.fill.fore_color.rgb = C_EMERALD_NEON
        emerald_strip.line.fill.background()

        return bg

    def add_header(slide, title_text, category_badge="SMART CITY MANAGEMENT SIMULATOR", slide_num=None):
        # Badge Pill Background
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.38), Inches(4.0), Inches(0.28))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(20, 30, 44)
        pill.line.color.rgb = C_BORDER_MUTED
        pill.line.width = Pt(1)

        # Badge Text
        badge_box = slide.shapes.add_textbox(Inches(0.9), Inches(0.4), Inches(3.8), Inches(0.25))
        tf_b = badge_box.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
        p_b = tf_b.paragraphs[0]
        p_b.text = f"◆  {category_badge.upper()}"
        p_b.font.size = Pt(9.5)
        p_b.font.bold = True
        p_b.font.color.rgb = C_EMERALD_NEON
        
        # Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.0), Inches(0.65))
        tf_t = title_box.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(23)
        p_t.font.bold = True
        p_t.font.color.rgb = C_TEXT_LIGHT
        
        # Dual-Color Divider Line
        div = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.42), Inches(11.733), Inches(0.025))
        div.fill.solid()
        div.fill.fore_color.rgb = C_BORDER_MUTED
        div.line.fill.background()
        
        div_dot = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.40), Inches(1.8), Inches(0.05))
        div_dot.fill.solid()
        div_dot.fill.fore_color.rgb = C_GOLD_ACCENT
        div_dot.line.fill.background()
        
        # Slide Number Footer (out of 13)
        if slide_num:
            f_box = slide.shapes.add_textbox(Inches(11.5), Inches(7.05), Inches(1.0), Inches(0.3))
            tf_f = f_box.text_frame
            tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
            p_f = tf_f.paragraphs[0]
            p_f.alignment = PP_ALIGN.RIGHT
            p_f.text = f"{slide_num:02d} / 13"
            p_f.font.size = Pt(10)
            p_f.font.bold = True
            p_f.font.color.rgb = C_GOLD_LIGHT

            # Bottom Left Footer
            fl_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(8.0), Inches(0.3))
            tf_fl = fl_box.text_frame
            tf_fl.margin_left = tf_fl.margin_top = tf_fl.margin_right = tf_fl.margin_bottom = 0
            p_fl = tf_fl.paragraphs[0]
            p_fl.text = "B.Sc Computer Science Capstone | D.G. Ruparel College | University of Mumbai"
            p_fl.font.size = Pt(9)
            p_fl.font.color.rgb = C_TEXT_DIM

    def add_card(slide, left, top, width, height, title="", border_color=C_BORDER_MUTED, bg_color=C_BG_CARD, accent_bar=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)
        
        bar_color = accent_bar if accent_bar else border_color
        top_accent = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left + Inches(0.1), top + Inches(0.04), width - Inches(0.2), Inches(0.03))
        top_accent.fill.solid()
        top_accent.fill.fore_color.rgb = bar_color
        top_accent.line.fill.background()
        
        if title:
            t_box = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.18), width - Inches(0.4), Inches(0.4))
            tf = t_box.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = C_GOLD_LIGHT if accent_bar == C_GOLD_ACCENT else C_EMERALD_NEON
            
        return card

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s1)
    
    ruparel_logo = os.path.join(FIG_DIR, "ruparel_logo.png")
    mumbai_logo = os.path.join(FIG_DIR, "mumbai_university_logo.png")
    proj_logo = os.path.join(FIG_DIR, "project_logo.png")
    
    if os.path.exists(ruparel_logo):
        s1.shapes.add_picture(ruparel_logo, Inches(0.8), Inches(0.55), height=Inches(0.95))
    if os.path.exists(mumbai_logo):
        s1.shapes.add_picture(mumbai_logo, Inches(1.95), Inches(0.55), height=Inches(0.95))
    if os.path.exists(proj_logo):
        s1.shapes.add_picture(proj_logo, Inches(11.4), Inches(0.5), height=Inches(1.05))
        
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.85), Inches(11.7), Inches(2.2))
    tf = t_box.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = "SMART CITY MANAGEMENT SIMULATOR"
    p0.font.size = Pt(34)
    p0.font.bold = True
    p0.font.color.rgb = C_TEXT_LIGHT
    
    p1 = tf.add_paragraph()
    p1.text = "A Real-Time Multi-Agent Urban Simulation & Cloud Telemetry Platform"
    p1.font.size = Pt(17)
    p1.font.bold = True
    p1.font.color.rgb = C_EMERALD_NEON
    p1.space_before = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "Bachelor of Science in Computer Science (B.Sc CS) — Semester V (Academic Year 2026-2027)"
    p2.font.size = Pt(12.5)
    p2.font.color.rgb = C_TEXT_MUTED
    p2.space_before = Pt(8)

    # Candidate Card
    add_card(s1, Inches(0.8), Inches(4.3), Inches(5.6), Inches(2.4), "PROJECT RESEARCHER & CANDIDATE", border_color=C_GOLD_ACCENT, accent_bar=C_GOLD_ACCENT)
    cand_box = s1.shapes.add_textbox(Inches(1.05), Inches(4.9), Inches(5.1), Inches(1.6))
    tf_c = cand_box.text_frame
    tf_c.word_wrap = True
    
    pc1 = tf_c.paragraphs[0]
    pc1.text = "Sahil Vishal Kate"
    pc1.font.size = Pt(18)
    pc1.font.bold = True
    pc1.font.color.rgb = C_TEXT_LIGHT
    
    pc2 = tf_c.add_paragraph()
    pc2.text = "Roll No: 9041  |  Seat No: B.Sc CS Sem V"
    pc2.font.size = Pt(12)
    pc2.font.bold = True
    pc2.font.color.rgb = C_GOLD_LIGHT
    pc2.space_before = Pt(4)
    
    pc3 = tf_c.add_paragraph()
    pc3.text = "Department of Computer Science\nD.G. Ruparel College of Arts, Science & Commerce\nAffiliated to University of Mumbai"
    pc3.font.size = Pt(11)
    pc3.font.color.rgb = C_TEXT_MUTED
    pc3.space_before = Pt(6)

    # Supervisor Card
    add_card(s1, Inches(6.9), Inches(4.3), Inches(5.6), Inches(2.4), "ACADEMIC PROJECT SUPERVISOR", border_color=C_EMERALD_NEON, accent_bar=C_EMERALD_NEON)
    guid_box = s1.shapes.add_textbox(Inches(7.15), Inches(4.9), Inches(5.1), Inches(1.6))
    tf_g = guid_box.text_frame
    tf_g.word_wrap = True
    
    pg1 = tf_g.paragraphs[0]
    pg1.text = "Prof. Aarti Gawai"
    pg1.font.size = Pt(18)
    pg1.font.bold = True
    pg1.font.color.rgb = C_TEXT_LIGHT
    
    pg2 = tf_g.add_paragraph()
    pg2.text = "Assistant Professor & Project Guide"
    pg2.font.size = Pt(12)
    pg2.font.bold = True
    pg2.font.color.rgb = C_MINT_GLOW
    pg2.space_before = Pt(4)
    
    pg3 = tf_g.add_paragraph()
    pg3.text = "Department of Computer Science\nD.G. Ruparel College, Mumbai\nSpecialization: Distributed Systems & Software Engineering"
    pg3.font.size = Pt(11)
    pg3.font.color.rgb = C_TEXT_MUTED
    pg3.space_before = Pt(6)
    
    s1.notes_slide.notes_text_frame.text = (
        "Good morning respected examiners and faculty members. I am Sahil Vishal Kate, Roll No. 9041. "
        "Under the guidance of Prof. Aarti Gawai, I present my final year capstone project: 'Smart City Management Simulator'."
    )

    # =========================================================================
    # SLIDE 2: INTRODUCTION & PROBLEM STATEMENT
    # =========================================================================
    s2 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s2)
    add_header(s2, "Introduction & Problem Statement: The Urban Digital Twin", "PROBLEM FORMULATION", 2)
    
    add_card(s2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9), "THE URBAN CHALLENGE & TRADITIONAL LIMITS", C_ROSE_ALERT, accent_bar=C_ROSE_ALERT)
    pitfalls = [
        ("Demographic Surge & Complexity", "By 2050, 68% of humanity will reside in cities. Municipal systems are non-linear feedback loops where one policy impacts all subsystems."),
        ("Siloed Administrative Decisions", "Transport, healthcare, utilities, and tax policy operate in isolation with zero predictive cross-system feedback."),
        ("Prohibitive Commercial Digital Twins", "Enterprise solutions (Siemens, Bentley) cost millions and require high-performance supercomputing infrastructure."),
        ("Superficial Entertainment Games", "SimCity / Cities Skylines prioritize aesthetics over true mathematical rigor, API telemetry, and empirical audit data.")
    ]
    p_box = s2.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.1), Inches(4.1))
    ptf = p_box.text_frame
    ptf.word_wrap = True
    for i, (h, d) in enumerate(pitfalls):
        p = ptf.paragraphs[0] if i == 0 else ptf.add_paragraph()
        p.text = f"✕  {h}\n"
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = RGBColor(251, 113, 133)
        if i > 0:
            p.space_before = Pt(10)
        r = p.add_run()
        r.text = d
        r.font.size = Pt(10)
        r.font.bold = False
        r.font.color.rgb = C_TEXT_MUTED

    add_card(s2, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.9), "OUR SOLUTION: THE MULTI-AGENT SIMULATOR", C_EMERALD_NEON, accent_bar=C_EMERALD_NEON)
    solutions = [
        ("Deterministic Multi-Agent Engine", "Six coupled mathematical subsystems run synchronously every virtual day, mirroring authentic municipal dynamics."),
        ("Interactive 3D Sandbox in Unity", "Real-time procedural mesh generation, 24-hour day/night lighting, and responsive HUD on consumer hardware (60 FPS)."),
        ("Cloud Telemetry & Audit API", "Asynchronous REST client streaming high-frequency state metrics into PostgreSQL via FastAPI microservice."),
        ("Composite Smart City Index (CSCI)", "Standardized 0-100 municipal health score synthesizing budget, transit, public welfare, environment, and citizen sentiment.")
    ]
    s_box = s2.shapes.add_textbox(Inches(7.15), Inches(2.4), Inches(5.1), Inches(4.1))
    stf = s_box.text_frame
    stf.word_wrap = True
    for i, (h, d) in enumerate(solutions):
        p = stf.paragraphs[0] if i == 0 else stf.add_paragraph()
        p.text = f"✔  {h}\n"
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = C_EMERALD_NEON
        if i > 0:
            p.space_before = Pt(10)
        r = p.add_run()
        r.text = d
        r.font.size = Pt(10)
        r.font.bold = False
        r.font.color.rgb = C_TEXT_MUTED

    s2.notes_slide.notes_text_frame.text = (
        "Urban centers are facing unprecedented expansion. Traditional urban governance suffers from administrative silos and lack of simulation tools. "
        "Our project bridges the gap by delivering a low-cost, 60 FPS deterministic multi-agent digital twin with full cloud synchronization."
    )

    # =========================================================================
    # SLIDE 3: LITERATURE SURVEY & BENCHMARKING
    # =========================================================================
    s3 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s3)
    add_header(s3, "Literature Survey & Industry Benchmarking Matrix", "RESEARCH BACKGROUND", 3)
    
    add_card(s3, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.9), "STATE-OF-THE-ART COMPARATIVE EVALUATION MATRIX", border_color=C_GOLD_ACCENT, accent_bar=C_GOLD_ACCENT)
    
    rows, cols = 6, 6
    table_shape = s3.shapes.add_table(rows, cols, Inches(1.05), Inches(2.45), Inches(11.233), Inches(4.0))
    table = table_shape.table
    table.columns[0].width = Inches(2.4)
    table.columns[1].width = Inches(1.8)
    table.columns[2].width = Inches(1.8)
    table.columns[3].width = Inches(1.8)
    table.columns[4].width = Inches(1.8)
    table.columns[5].width = Inches(1.633)
    
    headers = ["Evaluation Metric", "Commercial GIS (Bentley)", "SimCity (EA)", "Cities: Skylines", "Academic AnyLogic", "Our Simulator"]
    for c_idx, h in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C_GOLD_ACCENT if c_idx == 5 else RGBColor(28, 38, 54)
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = C_BG_DARK if c_idx == 5 else C_TEXT_LIGHT
        p.alignment = PP_ALIGN.CENTER
        
    data = [
        ["Real-Time 3D Rendering", "Partial / Static", "Full 3D", "Full 3D", "2D / Minimal 3D", "Interactive 60 FPS 3D"],
        ["Mathematical Rigor", "High", "Low / Arcade", "Moderate", "High", "High (Deterministic)"],
        ["Cloud Telemetry & REST API", "Proprietary", "None", "None", "Add-on / Complex", "Native FastAPI + Postgres"],
        ["Hardware Requirements", "Enterprise Server", "Mid-Range PC", "High-End Gaming PC", "Mid-Range PC", "Consumer Laptop"],
        ["License / Accessibility", "Costly License", "Commercial Game", "Commercial Game", "Expensive Academic", "Open Source / Academic"]
    ]
    
    for r_idx, row in enumerate(data):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx + 1, c_idx)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C_BG_CARD if (r_idx % 2 == 0) else C_BG_CARD_ALT
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10)
            p.alignment = PP_ALIGN.LEFT if c_idx == 0 else PP_ALIGN.CENTER
            if c_idx == 5:
                p.font.bold = True
                p.font.color.rgb = C_EMERALD_NEON
            else:
                p.font.color.rgb = C_TEXT_MUTED

    s3.notes_slide.notes_text_frame.text = (
        "We systematically benchmarked existing commercial twins and simulation games. "
        "Our platform stands out by pairing real-time 3D rendering with deterministic equations and open REST telemetry on consumer hardware."
    )

    # =========================================================================
    # SLIDE 4: SYSTEM ARCHITECTURE (4-TIER DECOUPLED MODEL)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s4)
    add_header(s4, "High-Level System Architecture (4-Tier Decoupled Pattern)", "SYSTEM DESIGN", 4)
    
    arch_path = os.path.join(FIG_DIR, "fig4_1_architecture.png")
    if os.path.exists(arch_path):
        s4.shapes.add_picture(arch_path, Inches(0.8), Inches(1.8), width=Inches(6.4))
        
    add_card(s4, Inches(7.4), Inches(1.8), Inches(5.133), Inches(4.9), "DECOUPLED 4-TIER SPECIFICATION", border_color=C_GOLD_ACCENT, accent_bar=C_GOLD_ACCENT)
    layers = [
        ("1. Presentation & Immersion Layer", "Unity 6.3 LTS, Procedural 3D city mesh generation, day/night directional shadows, particle weather, responsive HUD canvas."),
        ("2. Simulation Core & Business Logic", "C# deterministic engine with discrete-time step advancement. Tightly isolates mathematical calculation from graphics rendering."),
        ("3. Networking & Integration Layer", "CityApiClient asynchronous HTTP middleware. Handles serialization, telemetry streaming, token headers, and offline caching."),
        ("4. Backend Telemetry & Storage", "FastAPI Python ASGI server, Pydantic schemas, SQLAlchemy ORM, and PostgreSQL 17 relational database persistence.")
    ]
    l_box = s4.shapes.add_textbox(Inches(7.6), Inches(2.4), Inches(4.7), Inches(4.1))
    ltf = l_box.text_frame
    ltf.word_wrap = True
    for i, (lh, ld) in enumerate(layers):
        p = ltf.paragraphs[0] if i == 0 else ltf.add_paragraph()
        p.text = f"◆ {lh}\n"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_GOLD_LIGHT
        if i > 0:
            p.space_before = Pt(8)
        r = p.add_run()
        r.text = ld
        r.font.size = Pt(9.5)
        r.font.bold = False
        r.font.color.rgb = C_TEXT_MUTED

    s4.notes_slide.notes_text_frame.text = (
        "The system follows a clean 4-tier decoupled architecture: Presentation, Simulation Core, Networking, and Backend Telemetry. "
        "This architectural isolation ensures the simulation logic can execute and be validated independently from rendering."
    )

    # =========================================================================
    # SLIDE 5: MULTI-AGENT SUBSYSTEM SIMULATION PIPELINE
    # =========================================================================
    s5 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s5)
    add_header(s5, "Subsystem Interaction & Discrete Simulation Pipeline", "ENGINE ARCHITECTURE", 5)
    
    comp_path = os.path.join(FIG_DIR, "fig4_2_component_diagram.png")
    if os.path.exists(comp_path):
        s5.shapes.add_picture(comp_path, Inches(0.8), Inches(1.8), width=Inches(6.4))
        
    add_card(s5, Inches(7.4), Inches(1.8), Inches(5.133), Inches(4.9), "DISCRETE DAILY SIMULATION STEP", border_color=C_EMERALD_NEON, accent_bar=C_EMERALD_NEON)
    steps = [
        ("Step 1: Utility Balancing", "UtilitySystem evaluates total power/water draw. Brownouts or droughts set deficit flags across the city."),
        ("Step 2: Fiscal Accounting", "EconomySystem calculates commercial, industrial, and residential tax receipts minus infrastructure upkeep."),
        ("Step 3: Attractiveness & Migration", "PopulationSystem synthesizes happiness, healthcare, schooling, and tax rates to drive citizen influx or flight."),
        ("Step 4: Traffic & Road Wear", "TrafficSystem calculates congestion on road corridors; applies smart traffic mitigation and increments pavement wear."),
        ("Step 5: Air Dispersion & Weather", "EnvironmentSystem models pollution plumes from industrial zones; parks act as carbon sinks."),
        ("Step 6: Smart City Index (CSCI)", "Aggregates all 6 dimensions into a normalized 0-100 score, triggering civic milestones.")
    ]
    st_box = s5.shapes.add_textbox(Inches(7.6), Inches(2.4), Inches(4.7), Inches(4.1))
    sttf = st_box.text_frame
    sttf.word_wrap = True
    for i, (sh, sd) in enumerate(steps):
        p = sttf.paragraphs[0] if i == 0 else sttf.add_paragraph()
        p.text = f"{sh}: "
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_EMERALD_NEON
        if i > 0:
            p.space_before = Pt(6)
        r = p.add_run()
        r.text = sd
        r.font.size = Pt(9.5)
        r.font.bold = False
        r.font.color.rgb = C_TEXT_MUTED

    s5.notes_slide.notes_text_frame.text = (
        "Every simulation day (1 real second), the central CityManager executes a 6-step discrete pipeline: "
        "Utility balance -> Fiscal calculation -> Migration attractiveness -> Traffic updates -> Pollution dispersion -> CSCI rating."
    )

    # =========================================================================
    # SLIDE 6: MATHEMATICAL SIMULATION FORMULATIONS
    # =========================================================================
    s6 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s6)
    add_header(s6, "Mathematical Modeling & Deterministic Algorithms", "MATHEMATICAL FORMULATIONS", 6)
    
    fw = Inches(5.6)
    fh = Inches(2.35)
    
    # Box 1: Economy
    add_card(s6, Inches(0.8), Inches(1.8), fw, fh, "1. MUNICIPAL FISCAL REVENUE FORMULATION", border_color=C_GOLD_ACCENT, accent_bar=C_GOLD_ACCENT)
    f1_box = s6.shapes.add_textbox(Inches(1.0), Inches(2.3), fw - Inches(0.4), fh - Inches(0.6))
    tf1 = f1_box.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "R_daily = (Pop * T_res) + (CommCount * T_comm) + (IndCount * T_ind) - C_maint\n"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_GOLD_LIGHT
    r = p.add_run()
    r.text = "• Balancing tax rates directly affects citizen happiness and business attraction.\n• Maintenance costs escalate quadratically with neglected infrastructure."
    r.font.size = Pt(9.5)
    r.font.bold = False
    r.font.color.rgb = C_TEXT_MUTED
    
    # Box 2: Attractiveness
    add_card(s6, Inches(6.9), Inches(1.8), fw, fh, "2. DEMOGRAPHIC MIGRATION ATTRACTIVENESS", border_color=C_EMERALD_NEON, accent_bar=C_EMERALD_NEON)
    f2_box = s6.shapes.add_textbox(Inches(7.1), Inches(2.3), fw - Inches(0.4), fh - Inches(0.6))
    tf2 = f2_box.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "A_city = 0.35*H + 0.20*Q_h + 0.20*Q_e - 0.15*T_rate - 0.10*AQI_penalty\n"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_MINT_GLOW
    r = p.add_run()
    r.text = "• H = Citizen Happiness (0-100), Q_h = Healthcare, Q_e = Education quality.\n• If A_city > 55, migration inflow occurs; if < 40, citizens leave the city."
    r.font.size = Pt(9.5)
    r.font.bold = False
    r.font.color.rgb = C_TEXT_MUTED

    # Box 3: Traffic
    add_card(s6, Inches(0.8), Inches(4.35), fw, fh, "3. TRAFFIC CONGESTION & MITIGATION", border_color=C_TEAL_CYAN, accent_bar=C_TEAL_CYAN)
    f3_box = s6.shapes.add_textbox(Inches(1.0), Inches(4.85), fw - Inches(0.4), fh - Inches(0.6))
    tf3 = f3_box.text_frame
    tf3.word_wrap = True
    p = tf3.paragraphs[0]
    p.text = "C_ratio = (VehicularDemand / NetworkCapacity) * (1 - B_transit) * (1 - B_smart)\n"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = C_TEAL_CYAN
    r = p.add_run()
    r.text = "• Public transit expansions reduce private vehicle load by up to 28%.\n• Smart traffic signalization unlocks reduce intersection delays by 15%."
    r.font.size = Pt(9.5)
    r.font.bold = False
    r.font.color.rgb = C_TEXT_MUTED

    # Box 4: CSCI
    add_card(s6, Inches(6.9), Inches(4.35), fw, fh, "4. COMPOSITE SMART CITY INDEX (CSCI)", border_color=RGBColor(168, 85, 247), accent_bar=RGBColor(168, 85, 247))
    f4_box = s6.shapes.add_textbox(Inches(7.1), Inches(4.85), fw - Inches(0.4), fh - Inches(0.6))
    tf4 = f4_box.text_frame
    tf4.word_wrap = True
    p = tf4.paragraphs[0]
    p.text = "CSCI = 0.25*S_econ + 0.20*S_env + 0.20*S_infra + 0.20*S_social + 0.15*S_gov\n"
    p.font.size = Pt(10.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(192, 132, 252)
    r = p.add_run()
    r.text = "• Normalizes 28 individual metrics into an ISO 37120-inspired 0-100 rating.\n• Governs city prestige levels from Frontier Settlement up to Metropolis."
    r.font.size = Pt(9.5)
    r.font.bold = False
    r.font.color.rgb = C_TEXT_MUTED

    s6.notes_slide.notes_text_frame.text = (
        "Unlike gamey titles, our simulator is driven by explicit mathematical equations. "
        "Treasury accounts for maintenance degradation; migration responds to welfare and taxes; and CSCI normalizes 28 metrics into an objective civic score."
    )

    # =========================================================================
    # SLIDE 7: UML CLASS ARCHITECTURE & DATABASE SCHEMA (ERD)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s7)
    add_header(s7, "Object-Oriented Design & Database Schema (UML & ERD)", "SOFTWARE ENGINEERING", 7)
    
    # Left: UML Class Picture
    class_img = os.path.join(FIG_DIR, "fig4_4_class.png")
    if os.path.exists(class_img):
        s7.shapes.add_picture(class_img, Inches(0.8), Inches(1.8), width=Inches(5.7))
        
    # Right: ERD Schema Picture
    erd_img = os.path.join(FIG_DIR, "fig4_9_erd.png")
    if os.path.exists(erd_img):
        s7.shapes.add_picture(erd_img, Inches(6.8), Inches(1.8), width=Inches(5.7))
        
    add_card(s7, Inches(0.8), Inches(5.1), Inches(11.733), Inches(1.7), "OOP DESIGN PATTERNS & RELATIONAL PERSISTENCE (POSTGRESQL 17)", border_color=C_GOLD_ACCENT, accent_bar=C_GOLD_ACCENT)
    des_box = s7.shapes.add_textbox(Inches(1.0), Inches(5.45), Inches(11.3), Inches(1.2))
    destf = des_box.text_frame
    destf.word_wrap = True
    desp = destf.paragraphs[0]
    desp.text = (
        "• UML Architecture: Singleton CityManager orchestrator, decoupled static mathematical calculation modules, and serializable DTOs.\n"
        "• PostgreSQL Relational Schema: 4 isolated entity domains (`users`, `cities`, `saves`, `telemetry`) for audit logs and historical metrics.\n"
        "• High-Frequency Telemetry: Streaming time-series snapshots enabling 30-day municipal performance tracking and analytics."
    )
    desp.font.size = Pt(11)
    desp.font.color.rgb = C_TEXT_LIGHT

    s7.notes_slide.notes_text_frame.text = (
        "Slide 7 showcases our software design models: The UML class diagram highlights singleton orchestration and DTO serialization, "
        "while the relational ERD in PostgreSQL ensures robust ACID storage of city save slots and time-series telemetry."
    )

    # =========================================================================
    # SLIDE 8: UNITY 3D PROCEDURAL WORLD & INTERACTIVE HUD
    # =========================================================================
    s8 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s8)
    add_header(s8, "Unity 3D Procedural Simulation & Interactive HUD", "3D VISUALS & HUD", 8)
    
    hud_img = os.path.join(FIG_DIR, "fig7_2_city_hud.png")
    if os.path.exists(hud_img):
        s8.shapes.add_picture(hud_img, Inches(0.8), Inches(1.8), width=Inches(6.4))
        
    add_card(s8, Inches(7.4), Inches(1.8), Inches(5.133), Inches(4.9), "VISUAL IMMERSION & MANAGEMENT CONTROLS", border_color=C_EMERALD_NEON, accent_bar=C_EMERALD_NEON)
    engine_features = [
        ("Procedural 3D World Generation", "Dynamic road grids, zoning boundaries (Residential, Commercial, Industrial), river carving, and bridges."),
        ("24-Hour Day/Night & Weather", "Orbital sunlight cycle, emissive night windows, and particle weather (rain, storms) affecting solar power and road friction."),
        ("Management HUD & Speed Controls", "Live telemetry banner showing population, treasury, citizen happiness, and speed toggles (0x, 1x, 2x, 4x)."),
        ("6-DOF Free Navigation Camera", "WASD panning, mouse-drag orbital rotation, and smooth mouse-wheel zooming for district inspections."),
        ("Incident Dispatch & Citizen Petitions", "Real-time alerts for structural fires, pipe bursts, and citizen petitions with immediate resolution levers.")
    ]
    ef_box = s8.shapes.add_textbox(Inches(7.6), Inches(2.4), Inches(4.7), Inches(4.1))
    eftf = ef_box.text_frame
    eftf.word_wrap = True
    for i, (efh, efd) in enumerate(engine_features):
        p = eftf.paragraphs[0] if i == 0 else eftf.add_paragraph()
        p.text = f"◆ {efh}: "
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_EMERALD_NEON
        if i > 0:
            p.space_before = Pt(8)
        r = p.add_run()
        r.text = efd
        r.font.size = Pt(9.2)
        r.font.bold = False
        r.font.color.rgb = C_TEXT_MUTED

    s8.notes_slide.notes_text_frame.text = (
        "The Unity 3D presentation layer provides dynamic procedural generation, orbital lighting, and responsive UI. "
        "Users interact via 6-DOF camera controls, tax policy sliders, speed toggles, and instant emergency incident dispatches."
    )

    # =========================================================================
    # SLIDE 9: FASTAPI BACKEND & CLOUD TELEMETRY MICROSERVICE
    # =========================================================================
    s9 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s9)
    add_header(s9, "FastAPI Backend & Cloud Telemetry Microservice", "BACKEND ARCHITECTURE", 9)
    
    db_img = os.path.join(FIG_DIR, "fig7_3_database_portal.png")
    if os.path.exists(db_img):
        s9.shapes.add_picture(db_img, Inches(0.8), Inches(1.8), width=Inches(6.4))
        
    add_card(s9, Inches(7.4), Inches(1.8), Inches(5.133), Inches(4.9), "REST API SPECIFICATIONS & METRICS", border_color=C_GOLD_ACCENT, accent_bar=C_GOLD_ACCENT)
    api_items = [
        ("High-Performance ASGI Engine", "Built with Python 3.12, FastAPI, and Uvicorn delivering sub-15ms response latency."),
        ("Strict Schema Validation", "Pydantic models validate all incoming client payloads, preventing malformed telemetry ingestion."),
        ("Full CRUD City Endpoints", "POST /cities (create), GET /cities (list), GET /cities/{id}, PUT /cities/{id}, DELETE /cities/{id}."),
        ("Automated OpenAPI Documentation", "Interactive Swagger UI (/docs) and ReDoc endpoints for developer testing."),
        ("Docker Containerization", "Docker Compose manages container orchestration for the FastAPI server and PostgreSQL 17 database.")
    ]
    a_box = s9.shapes.add_textbox(Inches(7.6), Inches(2.4), Inches(4.7), Inches(4.1))
    atf = a_box.text_frame
    atf.word_wrap = True
    for i, (ah, ad) in enumerate(api_items):
        p = atf.paragraphs[0] if i == 0 else atf.add_paragraph()
        p.text = f"◆ {ah}\n"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = C_GOLD_LIGHT
        if i > 0:
            p.space_before = Pt(8)
        r = p.add_run()
        r.text = ad
        r.font.size = Pt(9.5)
        r.font.bold = False
        r.font.color.rgb = C_TEXT_MUTED

    s9.notes_slide.notes_text_frame.text = (
        "The backend microservice utilizes FastAPI and PostgreSQL 17. It auto-generates Swagger UI documentation, "
        "enforces strict Pydantic payload validation, and is containerized with Docker Compose for seamless cloud deployment."
    )

    # =========================================================================
    # SLIDE 10: QUALITY ASSURANCE & HARDWARE BENCHMARKS
    # =========================================================================
    s10 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s10)
    add_header(s10, "Software Verification & Hardware Benchmarks", "TESTING & PERFORMANCE", 10)
    
    bench_img = os.path.join(FIG_DIR, "fig7_1_benchmarks.png")
    if os.path.exists(bench_img):
        s10.shapes.add_picture(bench_img, Inches(0.8), Inches(1.8), width=Inches(6.4))
        
    add_card(s10, Inches(7.4), Inches(1.8), Inches(5.133), Inches(4.9), "QA RESULTS & PROFILING METRICS", border_color=C_EMERALD_NEON, accent_bar=C_EMERALD_NEON)
    qa_perf_items = [
        ("50 Formal Test Cases (TC-01 to TC-50)", "Comprehensive unit, integration, boundary, and stress tests across all modules."),
        ("100% Pass Rate Achieved", "Zero critical defects, NaN calculations, or memory leaks across extended 5-hour runs."),
        ("Smooth 60+ FPS Rendering", "Tested on standard consumer laptops (GTX 1660 / RTX 3060) with 0 frame drops."),
        ("Sub-2ms Simulation CPU Overhead", "Discrete daily mathematical tick step requires only 1.8ms per virtual day."),
        ("Low Heap & Fast API Response", "Client heap under 320 MB; backend telemetry insertion completed in 8.4ms.")
    ]
    qp_box = s10.shapes.add_textbox(Inches(7.6), Inches(2.4), Inches(4.7), Inches(4.1))
    qptf = qp_box.text_frame
    qptf.word_wrap = True
    for i, (qph, qpd) in enumerate(qa_perf_items):
        p = qptf.paragraphs[0] if i == 0 else qptf.add_paragraph()
        p.text = f"◆ {qph}\n"
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = C_MINT_GLOW
        if i > 0:
            p.space_before = Pt(8)
        r = p.add_run()
        r.text = qpd
        r.font.size = Pt(9.5)
        r.font.bold = False
        r.font.color.rgb = C_TEXT_MUTED

    s10.notes_slide.notes_text_frame.text = (
        "Testing and hardware profiling proved 100% pass rate across 50 test cases. "
        "The application maintains smooth 60 FPS rendering on consumer hardware, with simulation math taking under 2ms per day."
    )

    # =========================================================================
    # SLIDE 11: KEY INNOVATIONS & PRACTICAL HIGHLIGHTS
    # =========================================================================
    s11 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s11)
    add_header(s11, "Key Innovations & Engineering Contributions", "PROJECT HIGHLIGHTS", 11)
    
    add_card(s11, Inches(0.8), Inches(1.8), Inches(11.733), Inches(4.9), "SUMMARY OF TECHNICAL INNOVATIONS", border_color=C_GOLD_ACCENT, accent_bar=C_GOLD_ACCENT)
    innovations = [
        ("Multi-Subsystem Deterministic Engine", "Tightly couples 6 distinct urban domains into synchronized discrete ticks, mirroring genuine socio-technical feedback."),
        ("Composite Smart City Index (CSCI)", "Transforms 28 isolated metrics into a standardized 0-100 index based on international smart city benchmarks."),
        ("Full-Stack Hybrid Cloud Architecture", "Bridges a real-time Unity 3D client with an enterprise Python/FastAPI microservice and PostgreSQL storage."),
        ("Disaster Management & Feedback Loops", "Non-scripted emergent behavior where brownouts impact health, traffic impairs emergency response, and taxes dictate migration."),
        ("Complete Academic & QA Documentation", "50 automated test cases, comprehensive UML diagrams, and complete black book report prepared to Mumbai University guidelines.")
    ]
    in_box = s11.shapes.add_textbox(Inches(1.1), Inches(2.4), Inches(11.1), Inches(4.0))
    intf = in_box.text_frame
    intf.word_wrap = True
    for i, (ih, idesc) in enumerate(innovations):
        p = intf.paragraphs[0] if i == 0 else intf.add_paragraph()
        p.text = f"{i+1}. {ih}: "
        p.font.size = Pt(11.5)
        p.font.bold = True
        p.font.color.rgb = C_GOLD_LIGHT
        if i > 0:
            p.space_before = Pt(12)
        r = p.add_run()
        r.text = idesc
        r.font.size = Pt(10.5)
        r.font.bold = False
        r.font.color.rgb = C_TEXT_MUTED

    s11.notes_slide.notes_text_frame.text = (
        "Key innovations center around deterministic multi-agent coupling, our standardized Composite Smart City Index, "
        "and our hybrid cloud architecture uniting Unity with FastAPI."
    )

    # =========================================================================
    # SLIDE 12: CHALLENGES, ROADMAP & CONCLUSION
    # =========================================================================
    s12 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s12)
    add_header(s12, "Challenges Overcome, Future Roadmap & Conclusion", "EVALUATION & ROADMAP", 12)
    
    add_card(s12, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.9), "CHALLENGES & FUTURE ROADMAP", C_GOLD_ACCENT, accent_bar=C_GOLD_ACCENT)
    ch_box = s12.shapes.add_textbox(Inches(1.05), Inches(2.4), Inches(5.1), Inches(4.1))
    chtf = ch_box.text_frame
    chtf.word_wrap = True
    
    ch_items = [
        ("Simulation Concurrency Solved:", "Decoupled discrete calculations from frame rendering to eliminate UI stuttering."),
        ("Floating-Point Drift Normalized:", "Fixed compound interest rounding errors in multi-year tax calculations."),
        ("Phase 1 Roadmap (AI & Navigation):", "NavMesh A* citizen pathfinding + Reinforcement Learning (PPO) policy advisor."),
        ("Phase 2 Roadmap (GIS & IoT):", "OpenStreetMap real-world network ingestion + live municipal sensor telemetry.")
    ]
    for i, (ch, cd) in enumerate(ch_items):
        p = chtf.paragraphs[0] if i == 0 else chtf.add_paragraph()
        p.text = f"⚡ {ch} "
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = C_GOLD_LIGHT
        if i > 0:
            p.space_before = Pt(10)
        r = p.add_run()
        r.text = cd
        r.font.size = Pt(9.5)
        r.font.bold = False
        r.font.color.rgb = C_TEXT_MUTED

    add_card(s12, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.9), "SUMMARY & ACADEMIC OUTCOMES", C_EMERALD_NEON, accent_bar=C_EMERALD_NEON)
    oc_box = s12.shapes.add_textbox(Inches(7.15), Inches(2.4), Inches(5.1), Inches(4.1))
    octf = oc_box.text_frame
    octf.word_wrap = True
    
    outcomes = [
        ("Successful System Delivery:", "Conceptualized, engineered, verified, and benchmarked an end-to-end 3D multi-agent urban simulator."),
        ("Full-Stack Academic Synthesis:", "Integrated Computer Graphics (Unity 6.3), Discrete Mathematics, Enterprise Backend (FastAPI), and Relational Databases (PostgreSQL 17)."),
        ("Validated Stability:", "100% pass across 50 test cases confirming zero memory leaks and deterministic state recovery."),
        ("Civic & Educational Utility:", "Delivered a risk-free computational laboratory enabling policymakers and students to stress-test urban strategies.")
    ]
    for i, (oh, od) in enumerate(outcomes):
        p = octf.paragraphs[0] if i == 0 else octf.add_paragraph()
        p.text = f"🎯 {oh} "
        p.font.size = Pt(10.5)
        p.font.bold = True
        p.font.color.rgb = C_EMERALD_NEON
        if i > 0:
            p.space_before = Pt(10)
        r = p.add_run()
        r.text = od
        r.font.size = Pt(9.5)
        r.font.bold = False
        r.font.color.rgb = C_TEXT_MUTED

    s12.notes_slide.notes_text_frame.text = (
        "In conclusion, the simulator successfully achieves all research and engineering objectives, synthesizing computer graphics, "
        "discrete mathematics, and enterprise backend engineering into an accessible urban planning platform."
    )

    # =========================================================================
    # SLIDE 13: ACKNOWLEDGEMENTS & CONCLUSION (NO QUESTION LINE)
    # =========================================================================
    s13 = prs.slides.add_slide(blank_slide_layout)
    set_slide_background(s13)
    
    # Big central Card with Gold & Emerald Cyber Borders
    add_card(s13, Inches(1.5), Inches(1.2), Inches(10.333), Inches(5.1), "", border_color=C_GOLD_ACCENT, accent_bar=C_EMERALD_NEON)
    
    t_box = s13.shapes.add_textbox(Inches(1.8), Inches(1.8), Inches(9.733), Inches(4.0))
    ttf = t_box.text_frame
    ttf.word_wrap = True
    
    # Grand Clean Title
    p1 = ttf.paragraphs[0]
    p1.alignment = PP_ALIGN.CENTER
    p1.text = "THANK YOU!"
    p1.font.size = Pt(44)
    p1.font.bold = True
    p1.font.color.rgb = C_TEXT_LIGHT
    
    # Project subtitle
    p2 = ttf.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    p2.text = "Smart City Management Simulator"
    p2.font.size = Pt(20)
    p2.font.bold = True
    p2.font.color.rgb = C_GOLD_LIGHT
    p2.space_before = Pt(10)

    # Student & Guide Details
    p3 = ttf.add_paragraph()
    p3.alignment = PP_ALIGN.CENTER
    p3.text = "Sahil Vishal Kate  |  Roll No: 9041  |  B.Sc Computer Science\nUnder Guidance of: Prof. Aarti Gawai\nDepartment of Computer Science\nD.G. Ruparel College, University of Mumbai"
    p3.font.size = Pt(13)
    p3.font.color.rgb = C_TEXT_MUTED
    p3.space_before = Pt(24)

    # Footer note
    p4 = ttf.add_paragraph()
    p4.alignment = PP_ALIGN.CENTER
    p4.text = "Project Codebase, Telemetry API & Documentation Available on Localhost & GitHub"
    p4.font.size = Pt(11)
    p4.font.bold = True
    p4.font.color.rgb = C_EMERALD_NEON
    p4.space_before = Pt(20)

    s13.notes_slide.notes_text_frame.text = (
        "I express my deepest gratitude to my guide Prof. Aarti Gawai, the Head of Department, and the faculty members "
        "of D.G. Ruparel College for their continuous guidance and support."
    )

    output_path = os.path.join(BASE_DIR, "Smart_City_Management_Simulator_Presentation.pptx")
    prs.save(output_path)
    print(f"Presentation successfully created with 13 slides at: {output_path}")
    return output_path

if __name__ == "__main__":
    create_deck()
