import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

OUTPUT_DIR = r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\docs_figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['font.family'] = 'sans-serif'

def save_and_close(fig, filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    plt.tight_layout()
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Generated: {filepath}")

def add_header_footer(ax, title_num_name, page_num):
    # Header
    ax.text(50, 97.5, "SMART CITY MANAGEMENT SIMULATOR | UML DOCUMENTATION", 
            ha='center', va='center', fontsize=9.5, fontweight='normal', color='#64748b')
    ax.text(50, 94.2, title_num_name, 
            ha='center', va='center', fontsize=15, fontweight='bold', color='#1e1b4b')
    ax.plot([3, 97], [92.0, 92.0], color='#4f46e5', lw=2.0)
    
    # Footer
    ax.text(50, 2.0, f"SAHIL KATE | ROLL NO. 9041 | UML DIAGRAMS | PAGE {page_num} OF 8", 
            ha='center', va='center', fontsize=8.5, fontweight='normal', color='#64748b')

# =============================================================================
# 1. EVENT TABLE (PAGE 1)
# =============================================================================
def generate_event_table():
    fig, ax = plt.subplots(figsize=(18, 12), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')
    
    add_header_footer(ax, "1. EVENT TABLE", 1)
    
    events = [
        ("E01", "User logs in", "User submits email and password", "Player or administrator", "Authenticate user", "Login succeeds or an error message is displayed", "Player or administrator"),
        ("E02", "New city requested", "Player selects New City", "Player", "Create city", "A new city is initialized", "Player"),
        ("E03", "Saved city requested", "Player selects a saved city", "Player", "Load city", "The saved city is restored", "Player"),
        ("E04", "Zone created", "Player selects an area and zone type", "Player", "Manage zoning", "The zone is added to the city map", "Player"),
        ("E05", "Building requested", "Player selects a building and location", "Player", "Construct building", "The building is created or an error is displayed", "Player"),
        ("E06", "Building upgrade requested", "Player selects the upgrade option", "Player", "Upgrade building", "The building level is increased", "Player"),
        ("E07", "Road construction requested", "Player selects a road path", "Player", "Manage roads", "The road is added to the network", "Player"),
        ("E08", "Traffic level changes", "A simulation tick occurs", "Simulation clock", "Simulate traffic", "Traffic flow and congestion are updated", "Analytics dashboard"),
        ("E09", "Utility demand exceeds supply", "Demand becomes greater than capacity", "Utility network", "Manage utilities", "A utility-shortage warning is generated", "Player"),
        ("E10", "Tax or expense occurs", "A financial transaction is generated", "Budget system", "Manage budget", "The balance and transaction history are updated", "Player"),
        ("E11", "Citizen status changes", "A simulation tick occurs", "Simulation engine", "Update citizens", "Citizen health and happiness are updated", "Analytics dashboard"),
        ("E12", "Pollution level changes", "An environmental update occurs", "Environment system", "Monitor environment", "Environmental indicators are updated", "Player"),
        ("E13", "Disaster occurs", "A random disaster condition becomes true", "Disaster manager", "Handle disaster", "An emergency warning is generated", "Player"),
        ("E14", "Emergency response requested", "Player dispatches emergency units", "Player", "Manage emergency", "Units are dispatched and damage is controlled", "City"),
        ("E15", "Analytics requested", "User opens the analytics dashboard", "Player or analyst", "View analytics", "Charts and KPIs are displayed", "Player or analyst"),
        ("E16", "Simulation save requested", "Player selects Save or auto-save starts", "Player or system clock", "Save simulation", "A city snapshot is stored", "PostgreSQL database"),
        ("E17", "Report requested", "Analyst selects Export Report", "Analyst", "Generate report", "A report file is generated", "Analyst"),
        ("E18", "User management requested", "Administrator adds, updates, or removes a user", "Administrator", "Manage users", "User information is updated", "Administrator"),
    ]
    
    cols = ["ID", "Event", "Trigger", "Source", "Use case / process", "Response", "Destination"]
    col_x = [3, 8, 23, 40, 52, 65, 87]
    
    # Header row
    h_y = 88.0
    h_h = 4.0
    header_rect = patches.Rectangle((2.5, h_y - h_h/2), 95, h_h, facecolor='#0f2b5c', edgecolor='#0f2b5c')
    ax.add_patch(header_rect)
    for i, col_name in enumerate(cols):
        ax.text(col_x[i] + 0.5, h_y, col_name, ha='left', va='center', fontsize=9.2, fontweight='bold', color='#ffffff')
        
    # Data rows
    row_y = 83.2
    row_h = 4.2
    for idx, r in enumerate(events):
        bg = '#eef6fc' if idx % 2 == 1 else '#ffffff'
        r_rect = patches.Rectangle((2.5, row_y - row_h/2), 95, row_h, facecolor=bg, edgecolor='#cbd5e1', lw=0.6)
        ax.add_patch(r_rect)
        
        ax.text(col_x[0] + 0.5, row_y, r[0], ha='left', va='center', fontsize=8.5, fontweight='bold', color='#0284c7')
        ax.text(col_x[1] + 0.5, row_y, r[1], ha='left', va='center', fontsize=8.0, fontweight='bold', color='#0f172a')
        
        for c_idx in range(2, 7):
            ax.text(col_x[c_idx] + 0.5, row_y, r[c_idx], ha='left', va='center', fontsize=7.6, color='#334155')
            
        row_y -= 4.35
        
    save_and_close(fig, "fig_event_table.png")

# =============================================================================
# 2. CLASS DIAGRAM (PAGE 2) - 25 CLASSES, SPACIOUS & BEAUTIFUL
# =============================================================================
def generate_class_diagram():
    fig, ax = plt.subplots(figsize=(24, 16), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')
    
    add_header_footer(ax, "2. CLASS DIAGRAM", 2)
    
    def draw_uml_class(x, y, w, h, name, attrs=[], methods=[], bg='#ede9fe', border='#6366f1'):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3", facecolor=bg, edgecolor=border, lw=1.4)
        ax.add_patch(rect)
        
        # Header banner
        header_h = 2.4
        hdr_rect = patches.Rectangle((x, y + h - header_h), w, header_h, facecolor='#ddd6fe', edgecolor='none')
        ax.add_patch(hdr_rect)
        ax.text(x + w/2, y + h - 1.2, name, ha='center', va='center', fontsize=8.2, fontweight='bold', color='#1e1b4b')
        ax.plot([x, x + w], [y + h - header_h, y + h - header_h], color=border, lw=1.0)
        
        # Attributes
        curr_y = y + h - header_h - 0.9
        for a in attrs:
            ax.text(x + 0.6, curr_y, a, ha='left', va='center', fontsize=6.8, color='#1e293b')
            curr_y -= 1.05
            
        if methods:
            ax.plot([x, x + w], [curr_y + 0.3, curr_y + 0.3], color=border, lw=0.8, linestyle='--')
            curr_y -= 0.8
            for m in methods:
                ax.text(x + 0.6, curr_y, m, ha='left', va='center', fontsize=6.8, color='#1e293b')
                curr_y -= 1.05

    # Top: User
    draw_uml_class(43, 81, 14, 9.5, "User", [
        "-UUID userId", "-string username", "-string email", "-string role", "-string hashPassword"
    ], ["+login()", "+logout()"])

    # Upper Left: Player
    draw_uml_class(5, 71, 13, 8.5, "Player", [], [
        "+createCity()", "+loadCity()", "+saveCity()", "+constructBuilding()", "+manageBudget()"
    ])

    # Upper Center: UnityDashboard
    draw_uml_class(43, 68, 14, 7.5, "UnityDashboard", [], [
        "+displayMetrics()", "+displayCharts()", "+exportReport()"
    ])

    # Upper Right: Administrator
    draw_uml_class(82, 71, 13, 7.5, "Administrator", [], [
        "+manageUsers()", "+configureSystem()", "+viewSystemLogs()"
    ])

    # Middle Upper Left: UnityClient
    draw_uml_class(5, 56, 13, 7.5, "UnityClient", [], [
        "+renderCity()", "+dispatchAction()", "+receiveTelemetry()"
    ])

    # Middle Upper Right: BackendAPI
    draw_uml_class(77, 55, 18, 8.5, "BackendAPI", [], [
        "+saveState()", "+loadState()", "+processEmergency()", "+streamTelemetry()"
    ])

    # Mid Left: SimulationEngine
    draw_uml_class(3, 40, 16, 10, "SimulationEngine", [
        "-float simulationSpeed", "-DateTime simulationTime", "-bool isPaused"
    ], ["+start()", "+pause()", "+resume()", "+processTick()", "+triggerDisaster()"])

    # Service Row (Middle)
    draw_uml_class(32, 45, 11, 7.5, "AuthService", [], [
        "+authenticateUser()", "+generateToken()", "+validateToken()"
    ])
    draw_uml_class(44, 45, 11, 7.5, "CityService", [], [
        "+createCity()", "+getCity()", "+updateCity()", "+deleteCity()"
    ])
    draw_uml_class(76, 43, 11.5, 7.5, "AnalyticsService", [], [
        "+collectMetrics()", "+calculateKPI()", "+generateReport()"
    ])
    draw_uml_class(88.5, 43, 10.5, 7.5, "SaveLoadService", [], [
        "+saveSnapshot()", "+loadSnapshot()", "+listSaves()", "+deleteSave()"
    ])

    # Center Master Entity: City
    draw_uml_class(42.5, 31, 14, 11, "City", [
        "-UUID cityId", "-string cityName", "-int population", "-float happiness", "-float budget", "-DateTime createdAt"
    ], ["+updateCity()", "+getSnapshot()", "+triggerDisaster()"])

    # Center-Right: DisasterManager & Database
    draw_uml_class(66, 33, 13.5, 8.0, "DisasterManager", [
        "-UUID disasterId", "-string emergencyArea", "-float damageSpread"
    ], ["+handleDisaster()"])

    draw_uml_class(81, 31, 12, 8.5, "<<database>>\nDatabase", [], [
        "+insert()", "+update()", "+delete()", "+query()", "+openSession()"
    ])

    # Bottom Row of Domain Entities
    draw_uml_class(2, 19, 10.5, 8.5, "Zone", [
        "-UUID zoneId", "-enum zoneType", "-float area", "-int density"
    ], ["+changeZoneType()"])

    draw_uml_class(13.5, 19, 11, 8.5, "Citizen", [
        "-UUID citizenId", "-int age", "-string occupation", "-float health", "-float happiness"
    ], ["+consumeServices()", "+travel()"])

    draw_uml_class(25.5, 19, 11, 8.5, "Road", [
        "-UUID roadId", "-string roadType", "-int laneCount", "-float congestionLevel"
    ], ["+updateTrafficFlow()"])

    draw_uml_class(37.5, 19, 12, 8.5, "UtilityNetwork", [
        "-UUID networkId", "-string utilityType", "-float capacity", "-float currentDemand"
    ], ["+distributeResource()"])

    draw_uml_class(50.5, 19, 11.5, 8.5, "PublicService", [
        "-UUID serviceId", "-string serviceType", "-float coverage", "-int staffCount"
    ], ["+provideService()"])

    draw_uml_class(63, 19, 11.5, 8.5, "Budget", [
        "-decimal balance", "-decimal totalIncome", "-decimal totalExpense", "-float taxRate"
    ], ["+collectTax()", "+approveExpense()"])

    draw_uml_class(75.5, 19, 11.5, 8.5, "Environment", [
        "-float airQuality", "-float waterQuality", "-float greenCoverage"
    ], ["+calculatePollution()"])

    draw_uml_class(88, 19, 11, 8.5, "Disaster", [
        "-UUID disasterId", "-string disasterType", "-int severity", "-string status", "-DateTime startedAt"
    ], ["+trigger()", "+resolve()"])

    # Extra lower rows:
    draw_uml_class(2, 6, 12, 10, "Building", [
        "-UUID buildingId", "-string buildingType", "-int level", "-decimal constructionCost", "-float condition", "-string status"
    ], ["+construct()", "+upgrade()", "+demolish()"])

    draw_uml_class(15, 7, 10, 7.5, "Vehicle", [
        "-UUID vehicleId", "-string vehicleType", "-float speed", "-string route"
    ], ["+drive()"])

    draw_uml_class(26, 7, 10.5, 7.5, "TrafficSignal", [
        "-UUID signalId", "-string currentState", "-float cycleDuration"
    ], ["+changeSignal()"])

    draw_uml_class(63, 7, 11.5, 8.5, "Transaction", [
        "-UUID transactionId", "-string transactionType", "-string category", "-decimal amount", "-DateTime recordedAt"
    ], [])

    draw_uml_class(75.5, 7, 11.5, 8.5, "CityMetrics", [
        "-UUID metricId", "-int population", "-float happinessIndex", "-float pollutionIndex", "-float trafficIndex", "-DateTime capturedAt"
    ], [])

    draw_uml_class(88, 7, 11, 8.5, "SaveState", [
        "-UUID saveId", "-string saveName", "-string version", "-DateTime savedAt"
    ], ["+serializeCity()", "+deserializeCity()"])

    # Connecting arrows
    # User to Player and Admin
    ax.annotate('', xy=(12, 79.5), xytext=(43, 85), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    ax.annotate('', xy=(88, 78.5), xytext=(57, 85), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    
    # Player to UnityClient
    ax.annotate('', xy=(11.5, 63.5), xytext=(11.5, 71), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    ax.text(12.5, 67, "uses", fontsize=7.2, color='#475569')

    # Admin to BackendAPI
    ax.annotate('', xy=(86, 63.5), xytext=(88, 71), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    ax.text(88.5, 67, "administers", fontsize=7.2, color='#475569')

    # UnityClient to SimulationEngine
    ax.annotate('', xy=(11, 50), xytext=(11, 56), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    ax.text(12, 53, "controls", fontsize=7.2, color='#475569')

    # UnityClient to BackendAPI
    ax.plot([18, 77], [59, 59], color='#475569', lw=1.0, linestyle='--')
    ax.text(48, 60, "syncs", ha='center', fontsize=7.5, color='#475569')

    # UnityDashboard to BackendAPI
    ax.annotate('', xy=(77, 58), xytext=(57, 70), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.1))
    ax.text(67, 66, "requests", fontsize=7.2, color='#475569')

    # BackendAPI to Services
    for sx in [37.5, 49.5, 81.5, 93]:
        ax.plot([85, sx], [55, 52.5], color='#475569', lw=0.9, linestyle='--')

    # SimulationEngine to City
    ax.annotate('', xy=(42.5, 36), xytext=(19, 44), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.1))
    ax.text(30, 42, "simulates", fontsize=7.5, color='#475569')

    # City to Sub-entities
    for bx, lbl in [(7, "contains"), (19, "has"), (31, "has"), (43, "operates"), (56, "provides"), (68, "owns"), (81, "measures"), (93, "experiences")]:
        ax.plot([49.5, bx], [31, 27.5], color='#334155', lw=1.0)
        ax.text(bx, 28.5, lbl, ha='center', fontsize=6.8, color='#475569')

    # Zone to Building
    ax.annotate('', xy=(8, 16), xytext=(7, 19), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.1))
    ax.text(9, 17.5, "contains", fontsize=6.8, color='#475569')

    # Road to Vehicle / TrafficSignal
    ax.plot([31, 20], [19, 14.5], color='#334155', lw=0.9)
    ax.plot([31, 31], [19, 14.5], color='#334155', lw=0.9)
    ax.text(25, 16.5, "carries", fontsize=6.8, color='#475569')

    # Budget to Transaction
    ax.annotate('', xy=(68.5, 15.5), xytext=(68.5, 19), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.1))

    save_and_close(fig, "fig4_4_class.png")

# =============================================================================
# 3. OBJECT DIAGRAM (PAGE 3) - SPACIOUS, BALANCED, ZERO OVERFLOW
# =============================================================================
def generate_object_diagram():
    fig, ax = plt.subplots(figsize=(18, 11), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')
    
    add_header_footer(ax, "3. OBJECT DIAGRAM", 3)
    
    def draw_obj_box(x, y, w, h, title, props, bg='#ede9fe', border='#6366f1'):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4", facecolor=bg, edgecolor=border, lw=1.6)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h - 2.8, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1e1b4b')
        ax.plot([x + 0.8, x + w - 0.8], [y + h - 5.5, y + h - 5.5], color=border, lw=1.0)
        curr_y = y + h - 8.2
        for p in props:
            ax.text(x + w/2, curr_y, p, ha='center', va='center', fontsize=8.6, color='#1e293b')
            curr_y -= 2.8

    # Top: player1 : Player
    draw_obj_box(39, 76, 22, 14, "player1 : Player", ["name = Sahil", "role = City Manager"])

    # Middle: smartCity : City
    draw_obj_box(38, 44, 24, 17, "smartCity : City", [
        "name = Smart Pune", "population = 125000", "happiness = 78%"
    ])

    # Bottom Row: 5 objects spaced evenly within [3, 97]
    draw_obj_box(3, 17, 17, 14, "zoneA : Zone", ["type = Residential", "status = Active"])
    draw_obj_box(22.5, 17, 17, 14, "mainRoad : Road", ["lanes = 4", "congestion = 42%"])
    draw_obj_box(41.5, 17, 18, 14, "citizen101 : Citizen", ["occupation = Engineer", "happiness = 82%"])
    draw_obj_box(61.5, 17, 17, 14, "cityBudget : Budget", ["balance = 25000000", "taxRate = 8%"])
    draw_obj_box(80.5, 17, 17.5, 14, "powerGrid : UtilityNetwork", ["type = Electricity", "capacity = 500 MW"])

    # Sub-object: hospital01 : Building (below zoneA)
    draw_obj_box(3, 1.5, 17, 13, "hospital01 : Building", [
        "type = Hospital", "level = 2", "condition = 95%"
    ])

    # Connecting arrows & Labels
    # player1 to smartCity
    ax.annotate('', xy=(50, 61), xytext=(50, 76), arrowprops=dict(arrowstyle='->', color='#1e293b', lw=1.6))
    ax.text(50, 68.5, "manages", ha='center', va='center', fontsize=9.2, fontweight='bold', color='#1e293b')

    # smartCity to bottom objects
    conns = [
        (11.5, 31, "contains"),
        (31.0, 31, "has"),
        (50.5, 31, "has"),
        (70.0, 31, "owns"),
        (89.2, 31, "operates")
    ]
    for target_x, target_y, lbl in conns:
        ax.annotate('', xy=(target_x, target_y), xytext=(50, 44), arrowprops=dict(arrowstyle='->', color='#1e293b', lw=1.5))
        mx = (50 + target_x) / 2
        my = (44 + target_y) / 2
        ax.text(mx, my + 1.2, lbl, ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1e293b')

    # zoneA to hospital01
    ax.annotate('', xy=(11.5, 14.5), xytext=(11.5, 17), arrowprops=dict(arrowstyle='->', color='#1e293b', lw=1.5))
    ax.text(11.5, 15.8, "contains", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#1e293b')

    save_and_close(fig, "fig_object_diagram.png")

# =============================================================================
# 4. USE CASE DIAGRAM (PAGE 4) - BEAUTIFULLY SPACED, NO TEXT OVERFLOW
# =============================================================================
def generate_usecase():
    fig, ax = plt.subplots(figsize=(18, 11), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')
    
    add_header_footer(ax, "4. USE CASE DIAGRAM", 4)
    
    # System boundary box
    sys_box = patches.Rectangle((26, 7), 48, 81, edgecolor='#0f172a', facecolor='#ffffff', lw=2.0)
    ax.add_patch(sys_box)
    ax.text(50, 85.5, "Smart City Management Simulation System", ha='center', va='center', fontsize=12.5, fontweight='bold', color='#0f172a')
    
    # Draw Actor helper
    def draw_actor(x, y, label):
        c = plt.Circle((x, y + 4.5), 2.2, color='#0f172a', fill=False, lw=2.2)
        ax.add_patch(c)
        ax.plot([x, x], [y + 2.3, y - 2.8], color='#0f172a', lw=2.2)
        ax.plot([x - 3.8, x + 3.8], [y + 0.8, y + 0.8], color='#0f172a', lw=2.2)
        ax.plot([x, x - 3.0], [y - 2.8, y - 7.5], color='#0f172a', lw=2.2)
        ax.plot([x, x + 3.0], [y - 2.8, y - 7.5], color='#0f172a', lw=2.2)
        ax.text(x, y - 10.5, label, ha='center', va='top', fontsize=9.0, fontweight='bold', color='#0f172a', multialignment='center')

    # Left Actors
    draw_actor(16, 62, "City Manager /\nPlayer")
    draw_actor(16, 22, "Simulation\nEngine")

    # Right Actors
    draw_actor(84, 46, "City Analyst /\nAdministrator")
    draw_actor(84, 18, "Database &\nCloud Backend")

    # Draw Use Case helper
    def draw_uc(x, y, rx, ry, text):
        ellipse = patches.Ellipse((x, y), rx*2, ry*2, facecolor='#60a5fa', edgecolor='#1d4ed8', lw=1.8, zorder=3)
        ax.add_patch(ellipse)
        ax.text(x, y, text, ha='center', va='center', fontsize=8.2, fontweight='bold', color='#0f172a', zorder=4, multialignment='center')

    # Left Column Use Cases (wide ellipses so text is 100% inside)
    draw_uc(37.5, 70, 9.5, 5.2, "Plan City Zones\n& Infrastructure")
    draw_uc(37.5, 45, 9.5, 5.2, "Manage Municipal\nBudget & Taxes")
    draw_uc(37.5, 20, 9.5, 5.2, "Execute Simulation\nCycle")

    # Right Column Use Cases
    draw_uc(62.5, 79, 9.5, 5.2, "Construct Buildings\n& Roads")
    draw_uc(62.5, 65, 9.5, 5.2, "Deploy Utility Grids\n(Power & Water)")
    draw_uc(62.5, 51, 9.5, 5.2, "Inspect Citizen\nSatisfaction")
    draw_uc(62.5, 37, 9.5, 5.2, "Collect Revenue\n& Subsidies")
    draw_uc(62.5, 20, 9.5, 5.2, "Sync Telemetry\n& Save State")

    # Association lines
    ax.plot([16, 28], [62, 70], color='#1e293b', lw=1.6, zorder=1)
    ax.plot([16, 28], [62, 45], color='#1e293b', lw=1.6, zorder=1)
    ax.plot([16, 28], [22, 20], color='#1e293b', lw=1.6, zorder=1)

    ax.plot([84, 72], [46, 51], color='#1e293b', lw=1.6, zorder=1)
    ax.plot([84, 47], [46, 45], color='#1e293b', lw=1.6, zorder=1)
    ax.plot([84, 47], [46, 20], color='#1e293b', lw=1.6, zorder=1)
    ax.plot([84, 72], [18, 20], color='#1e293b', lw=1.6, zorder=1)

    # Dashed <<include>> and <<extend>> arrows
    def draw_rel(x1, y1, x2, y2, label):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', linestyle='dashed', color='#334155', lw=1.4), zorder=2)
        mx, my = (x1 + x2)/2, (y1 + y2)/2
        ax.text(mx, my + 1.2, label, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1e293b',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='none', alpha=0.9), zorder=5)

    draw_rel(47, 71.5, 53, 78, "<<include>>")
    draw_rel(47, 68.5, 53, 66, "<<include>>")
    draw_rel(53, 53, 47, 68, "<<extend>>")
    draw_rel(47, 43.5, 53, 39, "<<include>>")
    draw_rel(37.5, 25.2, 37.5, 39.8, "<<extend>>")
    draw_rel(53, 20, 47, 20, "<<extend>>")

    save_and_close(fig, "fig4_3_usecase.png")

# =============================================================================
# 5. SEQUENCE DIAGRAM (PAGE 5) - CLEAN LIFELINES & NO TEXT OVERLAP
# =============================================================================
def generate_sequence_diagram():
    fig, ax = plt.subplots(figsize=(20, 12), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')
    
    add_header_footer(ax, "5. SEQUENCE DIAGRAM", 5)
    
    lifelines = [
        ("Player", 7, True),
        ("Unity Client", 20, False),
        ("Simulation Engine", 33, False),
        ("Planning System", 46, False),
        ("Budget System", 59, False),
        ("FastAPI Backend", 72, False),
        ("PostgreSQL", 85, False),
        ("React Dashboard", 95, False)
    ]
    
    top_y = 88.0
    bot_y = 6.0
    for name, x, is_actor in lifelines:
        if is_actor:
            c = plt.Circle((x, top_y + 2.5), 1.5, color='#4f46e5', fill=False, lw=1.8)
            ax.add_patch(c)
            ax.plot([x, x], [top_y + 1.0, top_y - 2.0], color='#4f46e5', lw=1.8)
            ax.plot([x - 2.0, x + 2.0], [top_y + 0.0, top_y + 0.0], color='#4f46e5', lw=1.8)
            ax.plot([x, x - 1.8], [top_y - 2.0, top_y - 4.5], color='#4f46e5', lw=1.8)
            ax.plot([x, x + 1.8], [top_y - 2.0, top_y - 4.5], color='#4f46e5', lw=1.8)
            ax.text(x, top_y - 6.5, name, ha='center', va='center', fontsize=7.8, fontweight='bold', color='#1e1b4b')
        else:
            rect = patches.FancyBboxPatch((x - 5.5, top_y - 3.5), 11.0, 4.5, boxstyle="round,pad=0.2",
                                         facecolor='#ede9fe', edgecolor='#6366f1', lw=1.4)
            ax.add_patch(rect)
            ax.text(x, top_y - 1.25, name, ha='center', va='center', fontsize=7.8, fontweight='bold', color='#1e1b4b')
            
        ax.plot([x, x], [top_y - 7.0, bot_y + 5.0], color='#818cf8', lw=1.0, linestyle=':')
        
        # Bottom box
        if is_actor:
            c2 = plt.Circle((x, bot_y + 2.5), 1.5, color='#4f46e5', fill=False, lw=1.8)
            ax.add_patch(c2)
            ax.plot([x, x], [bot_y + 1.0, bot_y - 2.0], color='#4f46e5', lw=1.8)
            ax.plot([x - 2.0, x + 2.0], [bot_y + 0.0, bot_y + 0.0], color='#4f46e5', lw=1.8)
            ax.plot([x, x - 1.8], [bot_y - 2.0, bot_y - 4.5], color='#4f46e5', lw=1.8)
            ax.plot([x, x + 1.8], [bot_y - 2.0, bot_y - 4.5], color='#4f46e5', lw=1.8)
            ax.text(x, bot_y - 6.0, name, ha='center', va='center', fontsize=7.8, fontweight='bold', color='#1e1b4b')
        else:
            rect2 = patches.FancyBboxPatch((x - 5.5, bot_y), 11.0, 4.5, boxstyle="round,pad=0.2",
                                          facecolor='#ede9fe', edgecolor='#6366f1', lw=1.4)
            ax.add_patch(rect2)
            ax.text(x, bot_y + 2.25, name, ha='center', va='center', fontsize=7.8, fontweight='bold', color='#1e1b4b')

    # Draw messages helper with pill background
    def draw_msg(x1, x2, y, text, is_dashed=False):
        ls = 'dashed' if is_dashed else 'solid'
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle='->', linestyle=ls, color='#0f172a', lw=1.3), zorder=4)
        ax.text((x1 + x2)/2, y + 1.0, text, ha='center', va='center', fontsize=7.6, color='#0f172a', zorder=5,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='none', alpha=0.95))

    # Messages
    draw_msg(7, 20, 78, "Select building and location")
    draw_msg(20, 46, 74, "Validate placement")
    draw_msg(46, 33, 70, "Check zone and road access")
    draw_msg(33, 46, 66, "Location result", is_dashed=True)
    draw_msg(46, 59, 62, "Check available funds")
    draw_msg(59, 46, 58, "Budget result", is_dashed=True)

    # ALT BOX
    alt_box = patches.Rectangle((5, 17), 92, 38, facecolor='none', edgecolor='#6366f1', lw=1.4, linestyle='-')
    ax.add_patch(alt_box)
    
    ax.text(6.5, 53.5, "alt", fontsize=8.8, fontweight='bold', color='#1e1b4b')
    ax.plot([5, 10], [52, 52], color='#6366f1', lw=1.4)
    ax.plot([10, 12], [52, 55], color='#6366f1', lw=1.4)

    # Condition 1: Valid placement
    ax.text(50, 56.0, "[Valid placement and sufficient funds]", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#0f172a')
    
    draw_msg(46, 59, 50.5, "Deduct construction cost")
    draw_msg(46, 33, 46.5, "Create building")
    draw_msg(33, 20, 42.5, "Building created", is_dashed=True)
    draw_msg(46, 72, 38.5, "Save updated city")
    draw_msg(72, 85, 34.5, "Insert building and transaction")
    draw_msg(85, 72, 30.5, "Commit successful", is_dashed=True)
    draw_msg(72, 95, 26.5, "Send updated metrics", is_dashed=True)
    draw_msg(20, 7, 22.5, "Display completed building", is_dashed=True)

    # Divider in alt box
    ax.plot([5, 97], [20, 20], color='#6366f1', lw=1.0, linestyle='--')
    ax.text(50, 18.5, "[Invalid request]", ha='center', va='center', fontsize=8.2, fontweight='bold', color='#0f172a')

    # Condition 2: Invalid request
    draw_msg(46, 20, 14.5, "Return error", is_dashed=True)
    draw_msg(20, 7, 10.5, "Display error message", is_dashed=True)

    save_and_close(fig, "fig4_5_sequence.png")

# =============================================================================
# 6. ACTIVITY DIAGRAM (PAGE 6) - PERFECT MULTILINE TEXT, ZERO OVERFLOW
# =============================================================================
def generate_activity_diagram():
    fig, ax = plt.subplots(figsize=(16, 22), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')
    
    add_header_footer(ax, "6. ACTIVITY DIAGRAM", 6)
    
    def draw_action(x, y, w, h, text):
        rect = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.3",
                                     facecolor='#ede9fe', edgecolor='#6366f1', lw=1.3)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=7.2, color='#0f172a', multialignment='center')

    def draw_decision(x, y, w, h, text=""):
        poly = patches.Polygon([[x, y + h/2], [x + w/2, y], [x, y - h/2], [x - w/2, y]],
                               closed=True, facecolor='#ede9fe', edgecolor='#6366f1', lw=1.3)
        ax.add_patch(poly)
        if text:
            ax.text(x, y, text, ha='center', va='center', fontsize=6.8, color='#0f172a', multialignment='center')

    # Initial Node
    c_start = plt.Circle((50, 91.5), 1.0, facecolor='#4f46e5', edgecolor='#312e81', lw=1)
    ax.add_patch(c_start)
    ax.text(50, 93.0, "Start", ha='center', va='center', fontsize=7.2, color='#64748b')

    # Arrow to Main Menu
    ax.annotate('', xy=(50, 89.0), xytext=(50, 90.5), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    draw_action(50, 87.5, 12, 2.5, "Open Main Menu")

    # Arrow to Select Option Decision
    ax.annotate('', xy=(50, 84.5), xytext=(50, 86.2), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    draw_decision(50, 83.0, 11, 3.0, "Select Option")

    # Branch New City (Right)
    ax.annotate('', xy=(72, 79.5), xytext=(55.5, 83.0), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.1))
    ax.text(64, 82.5, "New City", fontsize=6.8, color='#475569')
    draw_action(72, 78.0, 19, 3.0, "Enter City Name\nand Select Map")
    
    ax.annotate('', xy=(72, 74.8), xytext=(72, 76.5), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.1))
    draw_action(72, 73.0, 20, 3.2, "Initialize Terrain, Budget\nand Population")

    # Branch Load City (Left)
    ax.annotate('', xy=(28, 75.0), xytext=(44.5, 83.0), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.1))
    ax.text(34, 80.5, "Load City", fontsize=6.8, color='#475569')
    draw_action(28, 73.0, 13, 2.8, "Load Saved City")

    # Both flow to Start Simulation
    ax.annotate('', xy=(48, 69.5), xytext=(28, 71.4), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.1))
    ax.annotate('', xy=(52, 69.5), xytext=(72, 71.4), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.1))
    draw_action(50, 68.5, 13, 2.4, "Start Simulation")

    # Arrow to Select Management Action Decision
    ax.annotate('', xy=(50, 65.5), xytext=(50, 67.3), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    draw_decision(50, 64.0, 16, 3.2, "Select Management Action")

    # 7 Branches from Management Action
    actions_row_y = 39.0
    
    # 1. Zoning
    ax.plot([42, 10], [64.0, 52.0], color='#334155', lw=1.0)
    ax.annotate('', xy=(10, actions_row_y + 1.5), xytext=(10, 52.0), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(11, 59.0, "Zoning", fontsize=6.5, color='#475569')
    draw_action(10, actions_row_y, 11, 2.8, "Create or\nModify Zone")

    # 2. Traffic
    ax.plot([43.5, 23], [63.5, 52.0], color='#334155', lw=1.0)
    ax.annotate('', xy=(23, actions_row_y + 1.5), xytext=(23, 52.0), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(24, 57.0, "Traffic", fontsize=6.5, color='#475569')
    draw_action(23, actions_row_y, 12, 2.8, "Manage Roads\nand Signals")

    # 3. Utilities
    ax.plot([46.5, 36], [62.8, 52.0], color='#334155', lw=1.0)
    ax.annotate('', xy=(36, actions_row_y + 1.5), xytext=(36, 52.0), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(33, 53.0, "Utilities", fontsize=6.5, color='#475569')
    draw_action(36, actions_row_y, 12, 2.8, "Manage Utility\nNetworks")

    # 4. Budget
    ax.annotate('', xy=(48, actions_row_y + 1.5), xytext=(49, 62.4), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(46, 50.0, "Budget", fontsize=6.5, color='#475569')
    draw_action(48, actions_row_y, 11, 2.8, "Manage Taxes\nand Expenses")

    # 5. Analytics
    ax.annotate('', xy=(60, actions_row_y + 1.5), xytext=(51, 62.4), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(57, 51.0, "Analytics", fontsize=6.5, color='#475569')
    draw_action(60, actions_row_y, 11, 2.8, "View\nDashboard")

    # 6. Emergency
    ax.plot([54.5, 72], [63.2, 52.0], color='#334155', lw=1.0)
    ax.annotate('', xy=(72, actions_row_y + 1.5), xytext=(72, 52.0), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(68, 54.0, "Emergency", fontsize=6.5, color='#475569')
    draw_action(72, actions_row_y, 12, 2.8, "Deploy Emergency\nServices")

    # 7. Construction Sub-flow (Right)
    ax.plot([58, 87], [64.0, 61.5], color='#334155', lw=1.0)
    ax.annotate('', xy=(87, 59.0), xytext=(87, 61.5), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(77, 62.5, "Construction", fontsize=6.5, color='#475569')
    draw_action(87, 57.5, 14, 2.8, "Validate Building\nPlacement")

    ax.annotate('', xy=(87, 54.5), xytext=(87, 56.1), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    draw_decision(87, 53.0, 10, 3.0, "Placement\nValid?")

    # Placement Invalid -> Display Error
    ax.plot([82, 82], [53.0, 42.0], color='#334155', lw=1.0)
    ax.annotate('', xy=(82, 40.5), xytext=(82, 42.0), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(80.0, 46.0, "No", fontsize=6.5, color='#475569')

    # Placement Valid -> Sufficient Budget?
    ax.annotate('', xy=(87, 48.0), xytext=(87, 51.5), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(88.5, 49.8, "Yes", fontsize=6.5, color='#475569')
    draw_decision(87, 46.5, 10, 3.0, "Sufficient\nBudget?")

    # Budget No -> Display Error
    ax.annotate('', xy=(84, 40.5), xytext=(84, 45.0), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    draw_action(83, 39.0, 9, 2.6, "Display\nError")

    # Budget Yes -> Construct Building
    ax.annotate('', xy=(93, 40.5), xytext=(91, 45.0), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(93.0, 43.0, "Yes", fontsize=6.5, color='#475569')
    draw_action(93.5, 39.0, 10, 2.6, "Construct\nBuilding")

    # Convergence bar / join into Process Simulation Tick
    tick_y = 33.5
    for ax_x in [10, 23, 36, 48, 60, 72, 83, 93.5]:
        ax.plot([ax_x, 50], [actions_row_y - 1.4, tick_y + 1.4], color='#334155', lw=0.9)
        
    ax.annotate('', xy=(50, tick_y + 1.3), xytext=(50, tick_y + 2.5), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    draw_action(50, tick_y, 16, 2.6, "Process Simulation Tick")

    # Update Population, Traffic...
    ax.annotate('', xy=(50, 29.2), xytext=(50, 32.2), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    draw_action(50, 27.5, 24, 3.4, "Update Population, Traffic,\nEconomy and Environment")

    # Decision: Disaster Occurred?
    ax.annotate('', xy=(50, 24.2), xytext=(50, 25.8), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    draw_decision(50, 22.8, 12, 2.8, "Disaster\nOccurred?")

    # Yes -> Trigger Disaster Event
    ax.plot([56, 80], [22.8, 22.8], color='#334155', lw=1.0)
    ax.annotate('', xy=(80, 19.0), xytext=(80, 22.8), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(67, 23.5, "Yes", fontsize=6.5, color='#475569')
    draw_action(80, 17.5, 14, 2.6, "Trigger Disaster Event")

    # No -> Continue Simulation Decision
    ax.annotate('', xy=(50, 15.6), xytext=(50, 21.4), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    ax.text(48, 18.5, "No", fontsize=6.5, color='#475569')
    draw_decision(50, 14.0, 13, 2.8, "Continue\nSimulation?")

    # Join from Trigger Disaster Event into Continue Simulation
    ax.plot([80, 80], [16.2, 14.0], color='#334155', lw=1.0)
    ax.annotate('', xy=(56.5, 14.0), xytext=(80, 14.0), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))

    # Continue Simulation -> Yes (loops all the way back to Start Simulation)
    ax.plot([56.5, 97, 97, 56.5], [14.0, 14.0, 68.5, 68.5], color='#334155', lw=1.0)
    ax.annotate('', xy=(56.5, 68.5), xytext=(58.5, 68.5), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.text(97.8, 42.0, "Yes", fontsize=6.5, color='#475569', rotation=90)

    # Continue Simulation -> Save and Exit -> End
    ax.annotate('', xy=(50, 9.6), xytext=(50, 12.6), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    ax.text(52, 11.2, "Save and Exit", fontsize=6.5, color='#475569')
    draw_action(50, 8.5, 11, 2.2, "Save City State")

    # End Node (bullseye)
    ax.annotate('', xy=(50, 5.8), xytext=(50, 7.4), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    c_out = plt.Circle((50, 4.8), 1.0, facecolor='#ffffff', edgecolor='#312e81', lw=1.2)
    c_in = plt.Circle((50, 4.8), 0.6, facecolor='#4f46e5', edgecolor='#4f46e5', lw=1)
    ax.add_patch(c_out)
    ax.add_patch(c_in)
    ax.text(50, 3.2, "End", ha='center', va='center', fontsize=7.2, color='#64748b')

    save_and_close(fig, "fig4_8_activity.png")

# =============================================================================
# 7. COMPONENT DIAGRAM (PAGE 7) - SPACIOUS & ZERO TEXT OVERFLOW
# =============================================================================
def generate_component_diagram():
    fig, ax = plt.subplots(figsize=(22, 12), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')
    
    add_header_footer(ax, "7. COMPONENT DIAGRAM", 7)
    
    def draw_comp_box(x, y, w, h, text, bg='#ede9fe', border='#6366f1'):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3", facecolor=bg, edgecolor=border, lw=1.3)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=8.0, color='#0f172a', multialignment='center')

    # Layer 1: Client Layer (Container)
    client_box = patches.Rectangle((18, 72), 68, 16, facecolor='none', edgecolor='#475569', lw=1.0)
    ax.add_patch(client_box)
    ax.text(50, 86.5, "Client Layer", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#475569')

    draw_comp_box(20, 75, 18, 8, "React TypeScript Dashboard")
    draw_comp_box(62, 75, 18, 8, "Unity 6 Simulation Client")

    # Layer 2: Application Interface (Container)
    api_box = patches.Rectangle((22, 56), 28, 13, facecolor='none', edgecolor='#475569', lw=1.0)
    ax.add_patch(api_box)
    ax.text(36, 67.5, "Application Interface", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#475569')

    draw_comp_box(24, 58, 11, 7, "REST API")
    draw_comp_box(37, 58, 11.5, 7, "WebSocket Service")

    # Layer 3: Simulation Components (Container, wide enough for 5 boxes)
    sim_box = patches.Rectangle((51, 56), 47, 13, facecolor='none', edgecolor='#475569', lw=1.0)
    ax.add_patch(sim_box)
    ax.text(74.5, 67.5, "Simulation Components", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#475569')

    draw_comp_box(52, 58, 8.8, 6.8, "Construction\nand Zoning")
    draw_comp_box(61.5, 58, 8.8, 6.8, "Traffic and\nCitizen AI")
    draw_comp_box(71, 58, 8.8, 6.8, "Utilities and\nServices")
    draw_comp_box(80.5, 58, 8.4, 6.8, "Economy\nand Budget")
    draw_comp_box(89.5, 58, 8.0, 6.8, "Environment\nSystem")

    # Layer 4: FastAPI Backend (Container)
    backend_box = patches.Rectangle((2, 38), 65, 13, facecolor='none', edgecolor='#475569', lw=1.0)
    ax.add_patch(backend_box)
    ax.text(32, 49.5, "FastAPI Backend", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#475569')

    draw_comp_box(3.5, 40, 11.5, 7, "Authentication\nComponent")
    draw_comp_box(16, 40, 11.5, 7, "City Management\nComponent")
    draw_comp_box(28.5, 40, 10.5, 7, "Analytics\nComponent")
    draw_comp_box(40, 40, 11.5, 7, "Save and Load\nComponent")
    draw_comp_box(52.5, 40, 13, 7, "Disaster and Event\nComponent")

    # Layer 5: Data Layer (Container)
    data_box = patches.Rectangle((18, 18), 38, 14, facecolor='none', edgecolor='#475569', lw=1.0)
    ax.add_patch(data_box)
    ax.text(37, 30.5, "Data Layer", ha='center', va='center', fontsize=9.0, fontweight='bold', color='#475569')

    draw_comp_box(20, 20, 12, 7.5, "PostgreSQL 17")
    draw_comp_box(35, 20, 18, 7.5, "Local Save and Asset Storage")

    # Connecting Lines
    ax.annotate('', xy=(29.5, 65), xytext=(29, 75), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.annotate('', xy=(42.5, 65), xytext=(29, 75), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))

    ax.annotate('', xy=(30, 65), xytext=(71, 75), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    ax.annotate('', xy=(43, 65), xytext=(71, 75), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.0))
    for sx in [56.4, 65.9, 75.4, 84.7, 93.5]:
        ax.plot([71, sx], [75, 64.8], color='#334155', lw=0.9)

    for bx in [9.2, 21.7, 33.7, 45.7, 59]:
        ax.annotate('', xy=(bx, 47), xytext=(29.5, 58), arrowprops=dict(arrowstyle='->', color='#334155', lw=0.9))

    ax.annotate('', xy=(21.7, 47), xytext=(42.7, 58), arrowprops=dict(arrowstyle='->', color='#334155', lw=0.9))
    ax.annotate('', xy=(33.7, 47), xytext=(42.7, 58), arrowprops=dict(arrowstyle='->', color='#334155', lw=0.9))

    for bx in [9.2, 21.7, 33.7, 45.7, 59]:
        ax.annotate('', xy=(26, 27.5), xytext=(bx, 40), arrowprops=dict(arrowstyle='->', color='#334155', lw=0.9))

    ax.annotate('', xy=(44, 27.5), xytext=(45.7, 40), arrowprops=dict(arrowstyle='->', color='#334155', lw=0.9))

    save_and_close(fig, "fig4_2_component_diagram.png")

# =============================================================================
# 8. DEPLOYMENT DIAGRAM (PAGE 8) - CLEAR 3-BOX & CYLINDER TOPOLOGY
# =============================================================================
def generate_deployment_diagram():
    fig, ax = plt.subplots(figsize=(18, 14), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')
    
    add_header_footer(ax, "8. DEPLOYMENT DIAGRAM", 8)
    
    def draw_node_box(x, y, w, h, title):
        rect = patches.Rectangle((x, y), w, h, facecolor='#ffffff', edgecolor='#0f172a', lw=1.6)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h - 2.5, title, ha='center', va='center', fontsize=9.2, fontweight='bold', color='#0f172a')

    def draw_inner_comp(x, y, w, h, title, bg='#ede9fe', border='#6366f1'):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2", facecolor=bg, edgecolor=border, lw=1.3)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, title, ha='center', va='center', fontsize=8.2, color='#0f172a', multialignment='center')

    # Top Row Nodes
    # 1. Development Platform (Left)
    draw_node_box(5, 72, 25, 17, "Development Platform")
    draw_inner_comp(7, 75, 21, 8.5, "Git Repository and CI/CD")

    # 2. Web Browser (Center)
    draw_node_box(35, 72, 28, 17, "Web Browser")
    draw_inner_comp(37, 75, 24, 8.5, "React Analytics Dashboard")

    # 3. Player Computer (Right)
    draw_node_box(67, 70, 30, 20, "Player Computer")
    draw_inner_comp(69, 80, 26, 6.5, "Unity 6 Game Application")
    draw_inner_comp(69, 72, 26, 6.5, "Local Cache and Settings")
    ax.annotate('', xy=(82, 78.5), xytext=(82, 80), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))

    # Middle Node: Application Server
    draw_node_box(25, 38, 38, 26, "Application Server")
    draw_inner_comp(34, 55, 20, 6.5, "HTTPS Reverse Proxy")
    draw_inner_comp(34, 46, 20, 6.5, "FastAPI Application")
    draw_inner_comp(27, 40, 16, 5.5, "Analytics Worker")

    ax.annotate('', xy=(44, 52.5), xytext=(44, 55), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))
    ax.annotate('', xy=(35, 45.5), xytext=(40, 46), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))

    # Bottom Node: Database Server
    draw_node_box(32, 11, 24, 21, "Database Server")
    
    # Cylinder for PostgreSQL
    cyl = patches.FancyBboxPatch((37, 21), 14, 6.5, boxstyle="round,pad=0.2", facecolor='#ede9fe', edgecolor='#6366f1', lw=1.3)
    ax.add_patch(cyl)
    ax.text(44, 24.2, "PostgreSQL 17", ha='center', va='center', fontsize=8.2, color='#0f172a')
    
    draw_inner_comp(36, 13, 16, 6.0, "Backup Storage")
    ax.annotate('', xy=(44, 19), xytext=(44, 21), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))

    # Communication Links
    # Dev Platform to App Server (Deployment)
    ax.annotate('', xy=(25, 59), xytext=(17.5, 72),
                arrowprops=dict(arrowstyle='->', linestyle='dotted', color='#334155', lw=1.4))
    ax.text(19, 64, "Deployment", ha='center', va='center', fontsize=7.8, color='#334155')

    # Web Browser to App Server (HTTPS)
    ax.annotate('', xy=(44, 61.5), xytext=(49, 72),
                arrowprops=dict(arrowstyle='->', color='#334155', lw=1.3))
    ax.text(49, 66.5, "HTTPS", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#1e1b4b')

    # Player Computer to App Server (HTTPS and WebSocket)
    ax.annotate('', xy=(63, 58), xytext=(69, 75),
                arrowprops=dict(arrowstyle='->', color='#334155', lw=1.3))
    ax.text(71, 64, "HTTPS and WebSocket", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#1e1b4b')

    # App Server to Database Server (SQL)
    ax.annotate('', xy=(44, 32), xytext=(44, 38),
                arrowprops=dict(arrowstyle='->', color='#334155', lw=1.3))
    ax.text(45.5, 35, "SQL", ha='left', va='center', fontsize=8.0, color='#334155')

    ax.annotate('', xy=(34, 28), xytext=(32, 40),
                arrowprops=dict(arrowstyle='->', color='#334155', lw=1.3))
    ax.text(31, 34, "SQL", ha='center', va='center', fontsize=8.0, color='#334155')

    save_and_close(fig, "fig_deployment_diagram.png")

if __name__ == '__main__':
    print("Generating all 8 diagrams from the user's PDF with zero overflow and maximum clarity...")
    generate_event_table()
    generate_class_diagram()
    generate_object_diagram()
    generate_usecase()
    generate_sequence_diagram()
    generate_activity_diagram()
    generate_component_diagram()
    generate_deployment_diagram()
    print("ALL 8 USER PDF DIAGRAMS GENERATED SUCCESSFULLY!")
