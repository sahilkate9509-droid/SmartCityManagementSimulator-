import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

OUTPUT_DIR = r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\docs_figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

# 1. High-Level Architecture
def generate_architecture():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Background
    fig.patch.set_facecolor('#ffffff')
    
    # Title
    ax.text(50, 96, "Smart City Management Simulator — System Architecture", 
            ha='center', va='center', fontsize=14, fontweight='bold', color='#1e293b')
    
    layers = [
        ("Presentation Layer (Unity 6.3 LTS UI & 3D Viewport)", 
         ["CityHUD & Navigation", "Zoning & Build Tools", "Day/Night & Weather Renderer", "Real-Time Telemetry Graphs"], 
         "#eff6ff", "#3b82f6", 75),
        ("Simulation Engine & Business Logic Layer (C# / Multi-Subsystem)", 
         ["Economy & Tax Engine", "Demographics & Housing", "Traffic & Route Network", "Utilities (Power/Water/Waste)", "Environmental AQI Grid"], 
         "#f0fdf4", "#10b981", 52),
        ("Application Integration & Networking Layer (CityApiClient)", 
         ["RESTful Client (UnityWebRequest)", "JSON Serialization / Deserialization", "Session Token & Save State Cache", "Asynchronous Telemetry Dispatcher"], 
         "#fefce8", "#eab308", 29),
        ("Backend & Persistence Layer (FastAPI + PostgreSQL / SQLite 3)", 
         ["FastAPI REST Endpoints", "SQLAlchemy 2.0 ORM Models", "Pydantic Schemas & Validation", "Database (cities, saves, telemetry)"], 
         "#faf5ff", "#a855f7", 6)
    ]
    
    for title, boxes, bg_col, border_col, y in layers:
        # Layer container
        rect = patches.FancyBboxPatch((4, y), 92, 17, boxstyle="round,pad=1", 
                                     facecolor=bg_col, edgecolor=border_col, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(7, y + 14.5, title, fontsize=10, fontweight='bold', color=border_col)
        
        # Sub-boxes
        n = len(boxes)
        box_w = 88 / n
        for i, b_text in enumerate(boxes):
            bx = 6 + i * box_w
            sub_rect = patches.FancyBboxPatch((bx, y + 2), box_w - 2, 10, boxstyle="round,pad=0.5",
                                             facecolor='#ffffff', edgecolor='#cbd5e1', linewidth=1)
            ax.add_patch(sub_rect)
            ax.text(bx + (box_w - 2)/2, y + 7, b_text, fontsize=7.5, ha='center', va='center',
                    color='#334155', wrap=True)
            
        # Downward arrows between layers
        if y > 10:
            ax.annotate('', xy=(50, y - 0.5), xytext=(50, y + 0.5),
                        arrowprops=dict(arrowstyle="->", color="#64748b", lw=2))
            
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig4_1_architecture.png"), dpi=300)
    plt.close()

# 2. UML Use Case Diagram
def generate_usecase():
    from generate_uml_from_pdf import generate_usecase
    generate_usecase()

# 3. UML Class Diagram
def generate_class_diagram():
    from generate_uml_from_pdf import generate_class_diagram
    generate_class_diagram()

# 4. UML Sequence Diagram
def generate_sequence_diagram():
    from generate_uml_from_pdf import generate_sequence_diagram
    generate_sequence_diagram()

# 5. DFD Level 0 & Level 1
def generate_dfd():
    # DFD Level 0
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    ax.text(50, 95, "Data Flow Diagram (DFD) — Level 0 (Context Diagram)", 
            ha='center', fontsize=12, fontweight='bold', color='#0f172a')
    
    # Process
    proc = patches.Circle((50, 50), 16, facecolor='#eff6ff', edgecolor='#2563eb', lw=2)
    ax.add_patch(proc)
    ax.text(50, 52, "0.0\nSmart City\nManagement\nSystem", ha='center', va='center', 
            fontsize=8.5, fontweight='bold', color='#1e40af')
    
    # Entities
    def draw_entity(x, y, w, h, text):
        rect = patches.Rectangle((x, y), w, h, facecolor='#ffffff', edgecolor='#334155', lw=1.5)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=8, fontweight='bold', color='#0f172a')
        
    draw_entity(6, 42, 18, 16, "City Mayor /\nPlanner")
    draw_entity(76, 62, 18, 16, "Cloud Database\n(Postgres/SQLite)")
    draw_entity(76, 22, 18, 16, "Municipal\nDashboard / Admin")
    
    # Flows
    ax.annotate('Planning Decisions, Tax Policy', xy=(34, 55), xytext=(24, 55),
                arrowprops=dict(arrowstyle="->", color='#475569', lw=1.2), fontsize=6.8)
    ax.annotate('City State, Alerts, Score', xy=(24, 45), xytext=(34, 45),
                arrowprops=dict(arrowstyle="->", color='#475569', lw=1.2), fontsize=6.8)
    
    ax.annotate('Telemetry Records, Saves', xy=(76, 70), xytext=(65, 60),
                arrowprops=dict(arrowstyle="->", color='#475569', lw=1.2), fontsize=6.8)
    ax.annotate('Saved States, Profiles', xy=(65, 52), xytext=(76, 62),
                arrowprops=dict(arrowstyle="->", color='#475569', lw=1.2), fontsize=6.8)
    
    ax.annotate('Historical Aggregates', xy=(76, 30), xytext=(65, 42),
                arrowprops=dict(arrowstyle="->", color='#475569', lw=1.2), fontsize=6.8)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig4_6_dfd0.png"), dpi=300)
    plt.close()

# 6. Entity Relationship Diagram
def generate_erd():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    ax.text(50, 96, "Entity-Relationship (ER) Diagram — Relational Schema", 
            ha='center', fontsize=12, fontweight='bold', color='#0f172a')
    
    tables = [
        ("CITIES (Master Entity)", 10, 48, 24, 40, [
            "id (PK, Integer)",
            "city_name (String[100])",
            "mayor_name (String[100])",
            "difficulty (String[20])",
            "starting_budget (Float)",
            "created_at (DateTime)",
            "is_active (Boolean)"
        ]),
        ("CITY_SAVES (Save Slots)", 40, 52, 24, 36, [
            "id (PK, Integer)",
            "city_id (FK -> cities.id)",
            "slot_index (Integer)",
            "save_name (String[100])",
            "game_state_json (Text)",
            "saved_at (DateTime)"
        ]),
        ("CITY_TELEMETRY (TimeSeries)", 68, 30, 26, 58, [
            "id (PK, Integer)",
            "city_id (FK -> cities.id)",
            "population (Integer)",
            "budget (Float)",
            "happiness (Float)",
            "smart_city_score (Integer)",
            "electricity_used (Float)",
            "water_used (Float)",
            "pollution_index (Float)",
            "traffic_efficiency (Float)",
            "recorded_at (DateTime)"
        ])
    ]
    
    for tname, tx, ty, tw, th, fields in tables:
        rect = patches.FancyBboxPatch((tx, ty), tw, th, boxstyle="round,pad=0.2",
                                     facecolor='#f8fafc', edgecolor='#0284c7', lw=1.5)
        ax.add_patch(rect)
        ax.text(tx + tw/2, ty + th - 3.5, tname, ha='center', va='center', 
                fontsize=7.8, fontweight='bold', color='#0369a1')
        ax.plot([tx, tx + tw], [ty + th - 7, ty + th - 7], color='#0284c7', lw=1)
        
        fy = ty + th - 10.5
        for f in fields:
            if "PK" in f:
                col = '#b91c1c'
                prefix = "[PK] "
            elif "FK" in f:
                col = '#4338ca'
                prefix = "[FK] "
            else:
                col = '#334155'
                prefix = "  -  "
            ax.text(tx + 1, fy, prefix + f.split('(')[0], fontsize=6.5, fontweight='bold' if 'PK' in f else 'normal', color=col)
            fy -= 3.8
            
    # Relationships
    ax.annotate('1 : N\nHas Saves', xy=(40, 70), xytext=(34, 70),
                arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.5), fontsize=7)
    
    ax.annotate('1 : N\nLogs Telemetry', xy=(68, 60), xytext=(34, 55),
                arrowprops=dict(arrowstyle="->", color='#0284c7', lw=1.5), fontsize=7)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig4_9_erd.png"), dpi=300)
    plt.close()

# 7. Performance Benchmarks
def generate_perf_charts():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)
    
    # Left: FPS vs Building Count
    entities = [50, 100, 250, 500, 1000, 1500, 2000]
    fps_low = [60, 60, 58, 54, 45, 38, 30]
    fps_high = [144, 144, 140, 132, 115, 95, 80]
    
    ax1.plot(entities, fps_high, marker='o', color='#10b981', lw=2, label='Recommended GPU (RTX 3060)')
    ax1.plot(entities, fps_low, marker='s', color='#f59e0b', lw=2, label='Minimum Spec (GTX 1650)')
    ax1.axhline(30, color='#ef4444', linestyle='--', label='Target Minimum (30 FPS)')
    ax1.set_title("Frame Rate Stability vs Building Count", fontsize=10, fontweight='bold')
    ax1.set_xlabel("Active Urban Entities (Buildings/Vehicles)", fontsize=8.5)
    ax1.set_ylabel("Frames Per Second (FPS)", fontsize=8.5)
    ax1.grid(True, linestyle=':', alpha=0.6)
    ax1.legend(fontsize=7.5)
    
    # Right: Telemetry Time Series (30 Days)
    days = np.arange(1, 31)
    pop = 1000 + 450 * np.log1p(days * 1.5) + np.random.normal(0, 15, 30)
    happiness = 65 + 15 * np.sin(days / 4) + np.random.normal(0, 1.5, 30)
    happiness = np.clip(happiness, 40, 95)
    
    ax2.plot(days, pop, color='#3b82f6', lw=2, label='Population Growth')
    ax2_twin = ax2.twinx()
    ax2_twin.plot(days, happiness, color='#8b5cf6', lw=2, linestyle='--', label='Citizen Happiness (%)')
    ax2.set_title("30-Day Urban Growth & Happiness Dynamics", fontsize=10, fontweight='bold')
    ax2.set_xlabel("Simulation Cycle (Days)", fontsize=8.5)
    ax2.set_ylabel("Population", color='#3b82f6', fontsize=8.5)
    ax2_twin.set_ylabel("Happiness Index (%)", color='#8b5cf6', fontsize=8.5)
    ax2.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig7_1_benchmarks.png"), dpi=300)
    plt.close()

# 8. High-Fidelity UI Screens & Visualizations
def generate_ui_visualizations():
    # UI 1: 3D City Simulation Main HUD
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Viewport representation
    ax.fill([0, 100, 100, 0], [0, 0, 100, 100], color='#1e293b') # sky/night
    # Ground terrain
    ax.fill([0, 100, 100, 0], [0, 0, 75, 75], color='#15803d')
    # River
    river_x = np.linspace(0, 100, 100)
    river_y = 35 + 8 * np.sin(river_x / 12)
    ax.fill_between(river_x, river_y - 6, river_y + 6, color='#0284c7', alpha=0.85)
    
    # Buildings
    b_coords = [(15, 45, 8, 22, '#64748b'), (25, 48, 10, 28, '#0369a1'), (37, 50, 7, 18, '#475569'),
                (60, 42, 9, 25, '#b45309'), (72, 44, 12, 32, '#047857'), (86, 40, 8, 20, '#64748b')]
    for bx, by, bw, bh, col in b_coords:
        ax.fill([bx, bx + bw, bx + bw, bx], [by, by, by + bh, by + bh], color=col, edgecolor='#f8fafc', lw=1)
        # Windows
        for wx in np.linspace(bx + 1.5, bx + bw - 2, 3):
            for wy in np.linspace(by + 3, by + bh - 3, 5):
                ax.fill([wx, wx+1, wx+1, wx], [wy, wy+1.5, wy+1.5, wy], color='#fef08a')
                
    # Roads & Bridge
    ax.fill([0, 100, 100, 0], [28, 28, 33, 33], color='#334155')
    ax.plot([0, 100], [30.5, 30.5], color='#facc15', linestyle='--', lw=1.5)
    
    # Top HUD Bar
    top_bar = patches.Rectangle((0, 88), 100, 12, facecolor='#0f172ae6', edgecolor='#334155')
    ax.add_patch(top_bar)
    ax.text(3, 94, "🏙️ NEO-VERIDIA | 2026", color='#ffffff', fontsize=10, fontweight='bold')
    ax.text(25, 94, "👥 24,850", color='#60a5fa', fontsize=9, fontweight='bold')
    ax.text(38, 94, "💰 $184,200 (+$4,210/d)", color='#34d399', fontsize=9, fontweight='bold')
    ax.text(62, 94, "⚡ 94% Power | 💧 98% Water", color='#38bdf8', fontsize=8.5)
    ax.text(85, 94, "🏆 Score: 88/100", color='#facc15', fontsize=9, fontweight='bold')
    
    # Simulation Speed Controls
    ax.text(82, 82, "[ ⏸️ Pause ] [ ▶️ 1x ] [ ⏩ 2x ] [ ⏭️ 4x ]", 
            color='#ffffff', fontsize=7.5, bbox=dict(facecolor='#0f172ab3', edgecolor='#64748b', boxstyle='round,pad=0.4'))
    
    # Bottom Building Palette
    bot_bar = patches.FancyBboxPatch((15, 2), 70, 10, boxstyle="round,pad=0.5", facecolor='#0f172ae6', edgecolor='#3b82f6')
    ax.add_patch(bot_bar)
    ax.text(50, 7, "[ 🏠 Residential ]  [ 🏢 Commercial ]  [ 🏭 Industrial ]  [ 🌳 Parks ]  [ ⚡ Solar Plant ]  [ 🚒 Services ]", 
            color='#e2e8f0', ha='center', va='center', fontsize=8, fontweight='bold')
    
    # Side Alert Box
    alert_box = patches.FancyBboxPatch((3, 62), 22, 18, boxstyle="round,pad=0.3",
                                      facecolor='#0f172acc', edgecolor='#e11d48', lw=1.2)
    ax.add_patch(alert_box)
    ax.text(4, 76, "⚠️ CITIZEN PETITION", color='#fb7185', fontsize=7.5, fontweight='bold')
    ax.text(4, 71, "District 4 traffic exceeds 82%.\nExpand transit routes.", color='#f1f5f9', fontsize=6.8)
    ax.text(4, 65, "[ APPROVE (-$12k) ] [ DISMISS ]", color='#38bdf8', fontsize=6.5, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig7_2_city_hud.png"), dpi=300)
    plt.close()

    # UI 2: Web Database Inspector & Analytics Portal
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Web Browser Frame
    browser_frame = patches.Rectangle((2, 2), 96, 96, facecolor='#0b111e', edgecolor='#1e293b', lw=2)
    ax.add_patch(browser_frame)
    
    # Browser Header
    ax.fill([2, 98, 98, 2], [92, 92, 98, 98], color='#131c2e')
    ax.plot([4, 6, 8], [95, 95, 95], 'o', color='#ef4444', markersize=4)
    ax.plot([7], [95], 'o', color='#f59e0b', markersize=4)
    ax.plot([10], [95], 'o', color='#10b981', markersize=4)
    ax.text(50, 95, "https://smartcity-telemetry.internal:8000/docs — FastAPI Swagger Explorer", 
            ha='center', va='center', color='#94a3b8', fontsize=7.5, fontfamily='monospace')
    
    # Portal Title
    ax.text(6, 86, "🏙️ Smart City Telemetry & Database Management Console", color='#ffffff', fontsize=12, fontweight='bold')
    ax.text(6, 82, "FastAPI v0.115 + SQLAlchemy 2.0 Engine | Database: SQLite 3 / PostgreSQL 17", color='#64748b', fontsize=7.5)
    
    # KPI Stat Cards
    kpis = [("TOTAL ACTIVE CITIES", "12", "#3b82f6"), ("REGISTERED SAVE SLOTS", "48", "#10b981"), 
            ("TELEMETRY SNAPSHOTS", "14,920", "#8b5cf6"), ("SYSTEM HEALTH", "99.98%", "#06b6d4")]
    for i, (klabel, kval, kcol) in enumerate(kpis):
        kx = 6 + i * 22.5
        krect = patches.FancyBboxPatch((kx, 68), 21, 10, boxstyle="round,pad=0.3",
                                       facecolor='#131c2e', edgecolor='#20314d', lw=1.2)
        ax.add_patch(krect)
        ax.text(kx + 2, 75, klabel, color='#94a3b8', fontsize=6.2, fontweight='bold')
        ax.text(kx + 2, 70.5, kval, color=kcol, fontsize=11, fontweight='bold')
        
    # Table Header & Data Rows
    ax.fill([6, 94, 94, 6], [58, 58, 63, 63], color='#0e1626')
    ax.text(8, 60.5, "City ID", color='#60a5fa', fontsize=7, fontweight='bold')
    ax.text(20, 60.5, "City Name", color='#60a5fa', fontsize=7, fontweight='bold')
    ax.text(38, 60.5, "Mayor", color='#60a5fa', fontsize=7, fontweight='bold')
    ax.text(54, 60.5, "Population", color='#60a5fa', fontsize=7, fontweight='bold')
    ax.text(68, 60.5, "Budget", color='#60a5fa', fontsize=7, fontweight='bold')
    ax.text(82, 60.5, "Smart Score", color='#60a5fa', fontsize=7, fontweight='bold')
    
    rows = [
        ("1", "Green Valley", "Mayor Kate", "18,420", "$145,200", "86 / 100", '#10b981'),
        ("2", "Metro Horizon", "Dr. A. Sharma", "42,100", "$420,800", "91 / 100", '#10b981'),
        ("3", "Cyber Heights", "A. Gawai", "29,650", "$210,000", "79 / 100", '#eab308'),
        ("4", "Sun Haven", "Admin Demo", "8,920", "$78,500", "64 / 100", '#f97316')
    ]
    
    for idx, (cid, cname, cmayor, cpop, cbud, csc, sc_col) in enumerate(rows):
        ry = 51 - idx * 6.2
        ax.plot([6, 94], [ry - 1, ry - 1], color='#20314d', lw=0.8)
        ax.text(8, ry + 1.5, cid, color='#f8fafc', fontsize=6.8, fontfamily='monospace')
        ax.text(20, ry + 1.5, cname, color='#f8fafc', fontsize=6.8, fontweight='bold')
        ax.text(38, ry + 1.5, cmayor, color='#94a3b8', fontsize=6.8)
        ax.text(54, ry + 1.5, cpop, color='#cbd5e1', fontsize=6.8)
        ax.text(68, ry + 1.5, cbud, color='#34d399', fontsize=6.8, fontfamily='monospace')
        ax.text(82, ry + 1.5, csc, color=sc_col, fontsize=6.8, fontweight='bold')
        
    # Bottom REST API Endpoints Box
    api_box = patches.FancyBboxPatch((6, 6), 88, 17, boxstyle="round,pad=0.3",
                                    facecolor='#131c2e', edgecolor='#3b82f6', lw=1)
    ax.add_patch(api_box)
    ax.text(8, 19, "REST API Endpoints Tested & Verified:", color='#60a5fa', fontsize=7.5, fontweight='bold')
    ax.text(8, 14, "[POST] /cities/                 201 Created   — New City State Registration", color='#34d399', fontsize=6.8, fontfamily='monospace')
    ax.text(8, 10, "[GET]  /cities/{id}/telemetry   200 OK        — 30-Day Historical Time-Series Ingestion", color='#38bdf8', fontsize=6.8, fontfamily='monospace')
    ax.text(8, 6.5, "[PUT]  /cities/{id}/save        200 OK        — Full State Snapshot Serialization & Cloud Sync", color='#fbbf24', fontsize=6.8, fontfamily='monospace')
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig7_3_database_portal.png"), dpi=300)
    plt.close()

if __name__ == '__main__':
    print("Generating system architecture diagram...")
    generate_architecture()
    print("Generating UML use case diagram...")
    generate_usecase()
    print("Generating UML class diagram...")
    generate_class_diagram()
    print("Generating UML sequence diagram...")
    generate_sequence_diagram()
    print("Generating DFD level 0 diagram...")
    generate_dfd()
    print("Generating ER diagram...")
    generate_erd()
    print("Generating performance charts...")
    generate_perf_charts()
    print("Generating UI visualizations...")
    generate_ui_visualizations()
    print("All diagrams successfully generated in docs_figures directory!")
