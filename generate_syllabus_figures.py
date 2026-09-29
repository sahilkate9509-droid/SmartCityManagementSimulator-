import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\docs_figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

def save_fig(fig, filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300)
    plt.close(fig)
    print(f"Generated: {filepath}")

# 1. Figure 2: Agile Model
def gen_agile_model():
    fig, ax = plt.subplots(figsize=(10, 5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 50)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    ax.text(50, 47, "AGILE SCRUM METHODOLOGY LIFECYCLE", ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.text(50, 44, "Iterative 2-Week Sprint Architecture for Smart City Management Simulator", ha='center', va='center', fontsize=8.5, color='#475569')

    # Boxes
    boxes = [
        (4, 15, 16, 20, "Product Backlog", ["• User Stories", "• Simulation Modules", "• 3D Assets", "• REST APIs"], "#f1f5f9", "#3b82f6"),
        (24, 15, 16, 20, "Sprint Planning", ["• Scope Definition", "• Story Estimation", "• Task Breakdown", "• Sprint Backlog"], "#eff6ff", "#2563eb"),
        (44, 15, 20, 20, "Sprint Execution\n(2 Weeks)", ["• Daily Standups", "• Unity C# Scripts", "• FastAPI Endpoints", "• Regression Tests"], "#f0fdf4", "#16a34a"),
        (68, 15, 14, 20, "Sprint Review\n& Demo", ["• Live Simulator Run", "• UI Validation", "• Telemetry Checks", "• Guide Feedback"], "#fefce8", "#ca8a04"),
        (85, 15, 13, 20, "Shippable\nIncrement", ["• Stable Build", "• Zero Crashes", "• CI Artifacts", "• Doc Updates"], "#faf5ff", "#9333ea")
    ]

    for x, y, w, h, title, items, bg, border in boxes:
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=1.2", facecolor=bg, edgecolor=border, lw=1.8)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h - 3, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0f172a')
        item_y = y + h - 7
        for itm in items:
            ax.text(x + 1.5, item_y, itm, ha='left', va='center', fontsize=6.8, color='#334155')
            item_y -= 3.2

    # Arrows between boxes
    arrow_props = dict(facecolor='#1e3a8a', edgecolor='#1e3a8a', width=1.5, headwidth=6, shrink=0.08)
    ax.annotate('', xy=(24, 25), xytext=(20, 25), arrowprops=arrow_props)
    ax.annotate('', xy=(44, 25), xytext=(40, 25), arrowprops=arrow_props)
    ax.annotate('', xy=(68, 25), xytext=(64, 25), arrowprops=arrow_props)
    ax.annotate('', xy=(85, 25), xytext=(82, 25), arrowprops=arrow_props)

    # Sprint Retrospective Feedback loop
    ax.annotate('Sprint Retrospective & Continuous Improvement',
                xy=(32, 13), xytext=(75, 7),
                arrowprops=dict(facecolor='#dc2626', edgecolor='#dc2626', width=1.2, headwidth=5, connectionstyle="arc3,rad=0.25"),
                ha='center', va='center', fontsize=7.5, fontweight='bold', color='#b91c1c')

    save_fig(fig, "fig_agile_model.png")

# 2. Figure 9: Object Diagram
def gen_object_diagram():
    from generate_uml_from_pdf import generate_object_diagram
    generate_object_diagram()

# 3. Figure 10: Deployment Diagram
def gen_deployment_diagram():
    from generate_uml_from_pdf import generate_deployment_diagram
    generate_deployment_diagram()

# 4. Figure 11: Logic Diagram
def gen_logic_diagram():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 60)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    ax.text(50, 57, "PROCEDURAL LOGIC DIAGRAM: SIMULATION TICK EXECUTION", ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.text(50, 54, "Synchronous Subsystem Update, Analytical Aggregation, and Telemetry Broadcast", ha='center', va='center', fontsize=8.5, color='#475569')

    # Flowchart shapes
    # Start
    start = patches.FancyBboxPatch((40, 45), 20, 6, boxstyle="round,pad=1", facecolor='#22c55e', edgecolor='#15803d', lw=1.5)
    ax.add_patch(start)
    ax.text(50, 48, "Simulation Tick Trigger\n(FixedUpdate dt=0.5s)", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#ffffff')

    # Subsystem parallel step
    proc1 = patches.FancyBboxPatch((10, 32), 80, 8, boxstyle="round,pad=0.8", facecolor='#eff6ff', edgecolor='#3b82f6', lw=1.5)
    ax.add_patch(proc1)
    ax.text(50, 36, "Execute Coupled Subsystem Differential Updates", ha='center', va='center', fontsize=8, fontweight='bold', color='#1d4ed8')
    ax.text(50, 33.5, "Economy Tax / Demographics Migration / Utility Propagation / Traffic & AQI Dispersion", ha='center', va='center', fontsize=6.8, color='#334155')

    # Decision: Citizen Event?
    dec1 = patches.Polygon([[50, 28], [65, 23], [50, 18], [35, 23]], closed=True, facecolor='#fef9c3', edgecolor='#ca8a04', lw=1.5)
    ax.add_patch(dec1)
    ax.text(50, 23, "Citizen Event / Disaster\nTrigger Check?", ha='center', va='center', fontsize=7, fontweight='bold', color='#854d0e')

    # Branch Event modal
    evt_box = patches.FancyBboxPatch((75, 20), 22, 6, boxstyle="round,pad=0.8", facecolor='#fee2e2', edgecolor='#ef4444', lw=1.5)
    ax.add_patch(evt_box)
    ax.text(86, 23, "Pause Simulation &\nDisplay Event Modal", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#991b1b')

    # Aggregation step
    agg_box = patches.FancyBboxPatch((30, 8), 40, 6, boxstyle="round,pad=0.8", facecolor='#f3e8ff', edgecolor='#a855f7', lw=1.5)
    ax.add_patch(agg_box)
    ax.text(50, 11, "Aggregate CSCI Metric, Refresh HUD &\nBroadcast JSON Telemetry Packet", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#6b21a8')

    # Arrows
    arrow_props = dict(facecolor='#1e3a8a', edgecolor='#1e3a8a', width=1.2, headwidth=5)
    ax.annotate('', xy=(50, 40), xytext=(50, 45), arrowprops=arrow_props)
    ax.annotate('', xy=(50, 28), xytext=(50, 32), arrowprops=arrow_props)
    ax.annotate('Yes', xy=(75, 23), xytext=(65, 23), arrowprops=arrow_props)
    ax.annotate('No', xy=(50, 14), xytext=(50, 18), arrowprops=arrow_props)
    ax.annotate('', xy=(70, 11), xytext=(86, 20), arrowprops=arrow_props)

    save_fig(fig, "fig_logic_diagram.png")

# 5. UI Figures: Profile, About Us, Login, Register, History, SavedPhrases, Setting, Admin Panel
def gen_ui_mockups():
    # Helper to build clean UI mockup frames
    def make_ui_frame(title, subtitle):
        fig, ax = plt.subplots(figsize=(8, 4.8), dpi=300)
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 60)
        ax.axis('off')
        fig.patch.set_facecolor('#0f172a') # Dark modern UI background

        # Window header bar
        header = patches.FancyBboxPatch((2, 53), 96, 5, boxstyle="round,pad=0.5", facecolor='#1e293b', edgecolor='#334155', lw=1)
        ax.add_patch(header)
        ax.text(5, 55.5, "● ● ●", fontsize=8, color='#ef4444')
        ax.text(50, 55.5, title, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#f8fafc')
        ax.text(50, 50, subtitle, ha='center', va='center', fontsize=7.5, color='#94a3b8')
        return fig, ax

    # Figure 13: Profile Page
    fig, ax = make_ui_frame("MAYOR & ADMINISTRATOR PROFILE", "Smart City Management Simulator - User Profile View")
    card = patches.FancyBboxPatch((15, 8), 70, 38, boxstyle="round,pad=1", facecolor='#1e293b', edgecolor='#3b82f6', lw=1.5)
    ax.add_patch(card)
    # Avatar circle
    avatar = plt.Circle((28, 30), 10, facecolor='#2563eb', edgecolor='#60a5fa', lw=2)
    ax.add_patch(avatar)
    ax.text(28, 30, "SK", ha='center', va='center', fontsize=12, fontweight='bold', color='#ffffff')
    ax.text(28, 16, "SAHIL VISHAL KATE\nMayor / Lead Planner", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#f8fafc')

    # Profile stats
    stats = [
        ("Roll Number:", "9041 (TYBSc CS)"),
        ("Institution:", "D.G. Ruparel College / Univ. of Mumbai"),
        ("Supervisor:", "Prof. Aarti Gawai"),
        ("Mayoral Level:", "Level 14 - Metropolitan Visionary"),
        ("Simulation Hours:", "48.5 Hours"),
        ("Overall CSCI Rating:", "88.2 / 100 (Excellence Tier)")
    ]
    py = 39
    for k, v in stats:
        ax.text(45, py, k, fontsize=7.5, color='#94a3b8')
        ax.text(62, py, v, fontsize=7.5, fontweight='bold', color='#38bdf8')
        py -= 5
    save_fig(fig, "fig_profile_page.png")
    # Also save profile_page2
    save_fig(fig, "fig_profile_page2.png")

    # Figure 15: About Us Page
    fig, ax = make_ui_frame("ABOUT THE PROJECT", "Smart City Management Simulator - System Information")
    about_card = patches.FancyBboxPatch((10, 8), 80, 38, boxstyle="round,pad=1", facecolor='#10b981', lw=1.5)
    ax.add_patch(about_card)
    ax.text(50, 41, "SMART CITY MANAGEMENT SIMULATOR (PROFESSIONAL)", ha='center', va='center', fontsize=9.5, fontweight='bold', color='#34d399')
    ax.text(50, 36, "An Interactive Multi-Agent Urban Digital Twin for Real-Time Decision Support", ha='center', va='center', fontsize=7.5, color='#cbd5e1')
    ax.plot([15, 85], [33, 33], color='#334155', lw=1)

    details = [
        "• Developed by: Sahil Vishal Kate (Roll No. 9041)",
        "• Project Supervisor: Prof. Aarti Gawai",
        "• Academic Department: Department of Computer Science, D.G. Ruparel College",
        "• University Affiliation: University of Mumbai (Academic Year 2026-2027)",
        "• Client Graphics: Unity 6.3 LTS / C# Multi-Threaded Engine",
        "• Cloud Telemetry: FastAPI REST Backend / PostgreSQL 17 / SQLite 3 Database"
    ]
    py = 28
    for d in details:
        ax.text(18, py, d, fontsize=7.2, color='#f1f5f9')
        py -= 4
    save_fig(fig, "fig_about_us_page.png")

    # Figure 16: Login Page
    fig, ax = make_ui_frame("MAYOR PORTAL LOGIN", "Secure Authentication & District Access")
    login_box = patches.FancyBboxPatch((25, 10), 50, 36, boxstyle="round,pad=1", facecolor='#1e293b', edgecolor='#6366f1', lw=1.5)
    ax.add_patch(login_box)
    ax.text(50, 40, "Municipal Administrator Sign In", ha='center', va='center', fontsize=9, fontweight='bold', color='#e0e7ff')
    
    # Input fields
    f1 = patches.FancyBboxPatch((30, 28), 40, 6, boxstyle="round,pad=0.5", facecolor='#0f172a', edgecolor='#475569', lw=1)
    ax.add_patch(f1)
    ax.text(33, 31, "User: sahil_kate_9041", fontsize=7.5, color='#94a3b8')

    f2 = patches.FancyBboxPatch((30, 19), 40, 6, boxstyle="round,pad=0.5", facecolor='#0f172a', edgecolor='#475569', lw=1)
    ax.add_patch(f2)
    ax.text(33, 22, "Pass: **************", fontsize=7.5, color='#94a3b8')

    # Button
    btn = patches.FancyBboxPatch((30, 12), 40, 5, boxstyle="round,pad=0.5", facecolor='#4f46e5', edgecolor='#6366f1', lw=1)
    ax.add_patch(btn)
    ax.text(50, 14.5, "AUTHENTICATE & ENTER SIMULATOR", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#ffffff')
    save_fig(fig, "fig_login_page.png")

    # Figure 17: Register Page
    fig, ax = make_ui_frame("MAYOR REGISTRATION", "Create New Municipal Planning Authority Account")
    reg_box = patches.FancyBboxPatch((22, 7), 56, 40, boxstyle="round,pad=1", facecolor='#1e293b', edgecolor='#8b5cf6', lw=1.5)
    ax.add_patch(reg_box)
    ax.text(50, 42, "New Administrator Registration", ha='center', va='center', fontsize=9, fontweight='bold', color='#ddd6fe')

    fields = [
        ("Full Name:", "Sahil Vishal Kate"),
        ("Academic Roll No:", "9041"),
        ("Official Email:", "sahil.kate@ruparel.edu"),
        ("Department:", "Computer Science (Sem V)")
    ]
    py = 33
    for lbl, val in fields:
        f = patches.FancyBboxPatch((36, py), 38, 4.5, boxstyle="round,pad=0.4", facecolor='#0f172a', edgecolor='#475569', lw=0.8)
        ax.add_patch(f)
        ax.text(25, py + 2.2, lbl, fontsize=7, color='#94a3b8')
        ax.text(38, py + 2.2, val, fontsize=7, color='#e2e8f0')
        py -= 6

    reg_btn = patches.FancyBboxPatch((30, 9), 40, 5, boxstyle="round,pad=0.5", facecolor='#7c3aed', edgecolor='#8b5cf6', lw=1)
    ax.add_patch(reg_btn)
    ax.text(50, 11.5, "REGISTER MUNICIPAL JURISDICTION", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#ffffff')
    save_fig(fig, "fig_register_page.png")

    # Figure 20: History Page
    fig, ax = make_ui_frame("SIMULATION AUDIT & TELEMETRY HISTORY", "Historical Multi-Year Subsystem Telemetry Graphing")
    h_box = patches.FancyBboxPatch((8, 8), 84, 38, boxstyle="round,pad=1", facecolor='#1e293b', edgecolor='#0284c7', lw=1.5)
    ax.add_patch(h_box)
    ax.text(12, 41, "Historical Metric Analytics: Treasury ($), Population, and CSCI Index", fontsize=8.2, fontweight='bold', color='#38bdf8')
    
    # Simple simulated chart curve inside card
    cx = np.linspace(15, 85, 30)
    cy1 = 20 + 8 * np.sin(cx / 10) + (cx - 15) * 0.15 # Treasury
    cy2 = 18 + 5 * np.cos(cx / 12) + (cx - 15) * 0.1 # CSCI
    ax.plot(cx, cy1, color='#10b981', lw=2, label="Treasury Growth ($)")
    ax.plot(cx, cy2, color='#38bdf8', lw=2, label="CSCI Index Rating")
    ax.plot([15, 85], [15, 15], color='#475569', lw=1)
    ax.plot([15, 15], [15, 36], color='#475569', lw=1)
    ax.text(86, cy1[-1], "Treasury ($42.5k)", fontsize=6.8, color='#10b981', va='center')
    ax.text(86, cy2[-1], "CSCI (88.2)", fontsize=6.8, color='#38bdf8', va='center')
    save_fig(fig, "fig_history_page.png")

    # Figure 21: SavedPhrases / Saved Cities Page
    fig, ax = make_ui_frame("SAVED CITIES & STATE SNAPSHOTS", "Slot-Based Cloud Persistence and Save Games (Saved_phrases Slot System)")
    s_box = patches.FancyBboxPatch((8, 8), 84, 38, boxstyle="round,pad=1", facecolor='#1e293b', edgecolor='#f59e0b', lw=1.5)
    ax.add_patch(s_box)
    ax.text(12, 41, "Persistent Save Slots (Local Disk + Cloud Database Sync)", fontsize=8.2, fontweight='bold', color='#fbbf24')

    slots = [
        ("Slot 1: Metropolis_Industrial_Corridor", "Tick: 14,200 | Population: 24,180 | CSCI: 84.6 | Status: Cloud Synced", "#10b981"),
        ("Slot 2: Green_Eco_Valley_Sanctuary", "Tick: 8,450 | Population: 12,400 | CSCI: 91.2 | Status: Cloud Synced", "#10b981"),
        ("Slot 3: Coastal_Harbor_Port_Logistics", "Tick: 19,800 | Population: 41,200 | CSCI: 78.4 | Status: Local Storage", "#38bdf8"),
        ("Slot 4: Disaster_Resilience_Benchmark", "Tick: 3,200 | Population: 5,600 | CSCI: 65.0 | Status: Local Storage", "#f59e0b")
    ]
    py = 34
    for title, sub, col in slots:
        sb = patches.FancyBboxPatch((12, py - 1), 76, 5.2, boxstyle="round,pad=0.3", facecolor='#0f172a', edgecolor='#334155', lw=1)
        ax.add_patch(sb)
        ax.text(15, py + 2.2, title, fontsize=7.2, fontweight='bold', color='#f8fafc')
        ax.text(15, py, sub, fontsize=6.2, color='#94a3b8')
        btn = patches.FancyBboxPatch((78, py), 9, 3.5, boxstyle="round,pad=0.2", facecolor=col, edgecolor=col)
        ax.add_patch(btn)
        ax.text(82.5, py + 1.7, "LOAD", ha='center', va='center', fontsize=6.2, fontweight='bold', color='#ffffff')
        py -= 6.8
    save_fig(fig, "fig_saved_phrases_page.png")

    # Figure 22: Setting Page
    fig, ax = make_ui_frame("SIMULATOR SETTINGS & CONFIGURATION", "Engine Parameters, Rendering Fidelity, and Network Options")
    set_box = patches.FancyBboxPatch((10, 8), 80, 38, boxstyle="round,pad=1", facecolor='#1e293b', edgecolor='#64748b', lw=1.5)
    ax.add_patch(set_box)
    ax.text(14, 41, "Runtime Simulation Configuration Parameters", fontsize=8.2, fontweight='bold', color='#94a3b8')

    configs = [
        ("Simulation Fixed Tick Interval:", "[ 0.50 Seconds (Standard) ]"),
        ("Graphics Rendering Tier:", "[ Ultra High (Shadow Cascades 4096) ]"),
        ("Procedural River & Water Mesh:", "[ Enabled (Dynamic Sinusoidal Shader) ]"),
        ("Atmospheric Weather Particle Density:", "[ High (Rain / Smog Particle Systems) ]"),
        ("FastAPI Cloud Ingestion URL:", "[ http://127.0.0.1:8000/api/v1/telemetry ]"),
        ("Automatic Disaster Frequency:", "[ Normal (15 Minute Mean Interval) ]")
    ]
    py = 34
    for k, v in configs:
        ax.text(14, py, k, fontsize=7.2, color='#cbd5e1')
        ax.text(60, py, v, fontsize=7.2, fontweight='bold', color='#38bdf8')
        py -= 4.8
    save_fig(fig, "fig_setting_page.png")

    # Figure 24: Admin Panel Page
    fig, ax = make_ui_frame("FASTAPI SWAGGER ADMIN CONSOLE", "REST Telemetry API Documentation & Server Management Portal")
    adm_box = patches.FancyBboxPatch((8, 8), 84, 38, boxstyle="round,pad=1", facecolor='#1e293b', edgecolor='#ec4899', lw=1.5)
    ax.add_patch(adm_box)
    ax.text(12, 41, "FastAPI Interactive OpenAPI / Swagger UI Management Console", fontsize=8.2, fontweight='bold', color='#f472b6')

    endpoints = [
        ("POST", "/api/v1/telemetry", "Ingest multi-subsystem simulation snapshot packet", "#10b981"),
        ("GET", "/api/v1/cities/{id}", "Retrieve municipal state, budget, and zoning grid data", "#3b82f6"),
        ("POST", "/api/v1/cities/save", "Commit city snapshot to cloud PostgreSQL / SQLite slot", "#10b981"),
        ("GET", "/api/v1/analytics/csci", "Generate historical CSCI trend and KPI compliance report", "#3b82f6"),
        ("POST", "/api/v1/admin/reset", "Purge test telemetry records and reseed baseline schemas", "#ef4444")
    ]
    py = 34
    for m, ep, desc, col in endpoints:
        eb = patches.FancyBboxPatch((12, py - 1), 76, 5, boxstyle="round,pad=0.2", facecolor='#0f172a', edgecolor='#334155', lw=1)
        ax.add_patch(eb)
        mb = patches.FancyBboxPatch((14, py), 9, 3.2, boxstyle="round,pad=0.2", facecolor=col, edgecolor=col)
        ax.add_patch(mb)
        ax.text(18.5, py + 1.6, m, ha='center', va='center', fontsize=6, fontweight='bold', color='#ffffff')
        ax.text(25, py + 1.6, ep, fontsize=6.8, fontweight='bold', color='#f8fafc', fontfamily='monospace')
        ax.text(52, py + 1.6, desc, fontsize=6.2, color='#94a3b8')
        py -= 5.8
    save_fig(fig, "fig_admin_panel_page.png")

if __name__ == '__main__':
    print("Generating Agile Model...")
    gen_agile_model()
    print("Generating Object Diagram...")
    gen_object_diagram()
    print("Generating Deployment Diagram...")
    gen_deployment_diagram()
    print("Generating Logic Diagram...")
    gen_logic_diagram()
    print("Generating UI Mockups...")
    gen_ui_mockups()
    print("All syllabus figures successfully generated!")
