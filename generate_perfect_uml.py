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

# =============================================================================
# 1. CLASS DIAGRAM (Figure 4.1)
# =============================================================================
def generate_perfect_class_diagram():
    # 18 x 10.5 inches - landscape, high-resolution, perfectly spaced
    fig, ax = plt.subplots(figsize=(18, 10.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    def draw_class(x, y, w, h, name, stereotype="", attrs=[], methods=[], bg='#f0fdf4', border='#16a34a', header_bg='#dcfce7'):
        # Outer box
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2", facecolor=bg, edgecolor=border, lw=1.5)
        ax.add_patch(rect)
        
        # Header banner
        header_h = 3.2 if stereotype else 2.6
        header_rect = patches.Rectangle((x, y + h - header_h), w, header_h, facecolor=header_bg, edgecolor='none')
        ax.add_patch(header_rect)
        ax.plot([x, x + w], [y + h - header_h, y + h - header_h], color=border, lw=1.2)
        
        if stereotype:
            ax.text(x + w/2, y + h - 1.0, f"<<{stereotype}>>", ha='center', va='center', fontsize=7.2, fontstyle='italic', color='#334155')
            ax.text(x + w/2, y + h - 2.3, name, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#0f172a')
        else:
            ax.text(x + w/2, y + h - 1.3, name, ha='center', va='center', fontsize=8.8, fontweight='bold', color='#0f172a')
            
        curr_y = y + h - header_h - 1.0
        for a in attrs:
            ax.text(x + 0.8, curr_y, a, ha='left', va='center', fontsize=6.8, color='#1e293b')
            curr_y -= 1.05
            
        if methods:
            ax.plot([x, x + w], [curr_y + 0.3, curr_y + 0.3], color=border, lw=0.8, linestyle='--')
            curr_y -= 0.8
            for m in methods:
                ax.text(x + 0.8, curr_y, m, ha='left', va='center', fontsize=6.8, color='#0f172a')
                curr_y -= 1.05

    # Title Banner on top of diagram
    ax.text(50, 97.5, "SMART CITY MANAGEMENT SIMULATOR - DOMAIN CLASS DIAGRAM", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.plot([15, 85], [95.8, 95.8], color='#3b82f6', lw=1.5)

    # Row 1: Core Controller & Singleton (Top)
    draw_class(2, 77, 18, 17, "SimulationEngine", "Singleton", 
               ["-instance: SimulationEngine", "-currentTick: long", "-tickRate: float = 2.0", "-isPaused: bool", "-gameSpeed: float"],
               ["+StartSimulation(): void", "+PauseSimulation(): void", "+TickUpdate(): void", "+TriggerDisaster(type): void"],
               bg='#eff6ff', border='#2563eb', header_bg='#dbeafe')

    draw_class(24, 78, 17, 16, "CityGrid", "Spatial Matrix",
               ["-gridWidth: int = 50", "-gridHeight: int = 50", "-cellSize: float = 10.0", "-tiles: Tile[50,50]"],
               ["+GetTile(x, y): Tile", "+PlaceZone(x, y, zone): bool", "+CheckWaterCollision(x, y): bool"],
               bg='#eff6ff', border='#2563eb', header_bg='#dbeafe')

    draw_class(45, 78, 17, 16, "MayorPlayer", "Controller",
               ["-playerId: UUID", "-playerName: string", "-currentCityId: int", "-sessionTime: float"],
               ["+SelectTool(toolId): void", "+ExecuteZoning(plot): void", "+ApproveBudget(dept): void"],
               bg='#eff6ff', border='#2563eb', header_bg='#dbeafe')

    draw_class(66, 78, 16, 16, "FastAPIClient", "HTTP / Service",
               ["-baseUrl: string", "-authToken: string", "-timeoutSec: int = 5"],
               ["+PostTelemetry(metrics): Task", "+SaveCitySnapshot(json): Task", "+LoadCityState(id): CityDTO"],
               bg='#fdf4ff', border='#c026d3', header_bg='#fae8ff')

    draw_class(84, 78, 14, 16, "TelemetryLogger", "Persistence",
               ["-logBuffer: Queue", "-batchSize: int = 50"],
               ["+EnqueueMetric(m): void", "+FlushTelemetry(): void", "+ExportCSV(): string"],
               bg='#fdf4ff', border='#c026d3', header_bg='#fae8ff')

    # Row 2: Pure Domain Entities (Middle)
    draw_class(2, 49, 17, 21, "BuildingEntity", "Domain Entity",
               ["-buildingId: UUID", "-buildingType: BuildingType", "-level: int = 1", "-health: float = 100.0", "-powerDemand: float", "-waterDemand: float", "-workerCapacity: int", "-pollutionOutput: float"],
               ["+Upgrade(): bool", "+Demolish(): void", "+CalculateMaintenance(): float", "+ApplyWearAndTear(): void"],
               bg='#f0fdf4', border='#16a34a', header_bg='#dcfce7')

    draw_class(23, 49, 16, 21, "ZonePlot", "Spatial Partition",
               ["-plotId: int", "-zoneType: ZoneType", "-density: DensityLevel", "-landValue: float", "-desirabilityScore: float", "-taxYieldRate: float", "-buildingCount: int"],
               ["+AssignZoning(type): void", "+EvaluateDesirability(): float", "+ComputeTaxYield(): float"],
               bg='#f0fdf4', border='#16a34a', header_bg='#dcfce7')

    draw_class(43, 49, 17, 21, "CitizenAgent", "Multi-Agent AI",
               ["-agentId: UUID", "-homeLocation: Vector2Int", "-workLocation: Vector2Int", "-happiness: float", "-healthStatus: float", "-educationLevel: int", "-incomeBracket: float"],
               ["+PerformDailyCommute(): void", "+SeekHealthcare(): void", "+PayTaxes(rate): float", "+FileGrievance(): void"],
               bg='#f0fdf4', border='#16a34a', header_bg='#dcfce7')

    draw_class(64, 49, 17, 21, "RoadNetwork", "Graph / Flow",
               ["-roadNodes: List<Node>", "-roadSegments: List<Edge>", "-speedLimitKm: float", "-congestionIndex: float", "-accidentRisk: float"],
               ["+AddRoadSegment(p1, p2): void", "+ComputeAStarPath(src, dst): Path", "+RecalculateTrafficFlow(): void"],
               bg='#f0fdf4', border='#16a34a', header_bg='#dcfce7')

    draw_class(84, 49, 14, 21, "DisasterKernel", "Incident Engine",
               ["-disasterType: DisasterType", "-epicenter: Vector2Int", "-radiusKm: float", "-severity: int", "-activeDuration: float"],
               ["+SpawnDisaster(type, pos): void", "+PropagateDamage(): void", "+DispatchResponders(): void"],
               bg='#fff1f2', border='#e11d48', header_bg='#ffe4e6')

    # Row 3: Subsystem Managers & Calculations (Bottom)
    draw_class(2, 17, 18, 24, "BudgetManager", "Treasury Kernel",
               ["-treasuryBalance: decimal", "-residentialTaxRate: float", "-commercialTaxRate: float", "-industrialTaxRate: float", "-monthlyRevenue: decimal", "-monthlyExpenses: decimal"],
               ["+CollectTaxes(): decimal", "+DisburseSalaries(): void", "+FundInfrastructure(cost): bool", "+ComputeFiscalDeficit(): float", "+GenerateFinancialStatement(): Report"],
               bg='#fffbeb', border='#d97706', header_bg='#fef3c7')

    draw_class(24, 17, 17, 24, "UtilityNetwork", "BFS Grid Flow",
               ["-powerGridCapacityMw: float", "-waterReservoirMld: float", "-currentPowerDemand: float", "-currentWaterDemand: float", "-coveragePercentage: float", "-blackoutZones: List<int>"],
               ["+DistributePower(): void", "+DistributeWater(): void", "+DetectGridOverload(): bool", "+ConnectSubstation(node): void", "+OptimizeLoadShedding(): void"],
               bg='#fffbeb', border='#d97706', header_bg='#fef3c7')

    draw_class(45, 17, 18, 24, "EnvironmentEngine", "Air & Quality ODE",
               ["-aqiScore: float", "-pm25Concentration: float", "-industrialSmogLevel: float", "-trafficEmissions: float", "-greenSpaceBufferIndex: float", "-waterPurityIndex: float"],
               ["+SimulateGaussianPlume(): void", "+ComputeCompositeAQI(): float", "+ApplyVegetationFiltering(): void", "+EvaluateEnvironmentalScore(): int"],
               bg='#fffbeb', border='#d97706', header_bg='#fef3c7')

    draw_class(67, 17, 16, 24, "CSCIComputer", "Metric Normalizer",
               ["-compositeIndex: float", "-economicHealthW: float = 0.25", "-utilityReliabilityW: float = 0.25", "-citizenSatisfactionW: float = 0.25", "-environmentalW: float = 0.25"],
               ["+CalculateCompositeCSCI(): float", "+ComputeGradeLevel(): char", "+IdentifyBottlenecks(): List", "+ExportHistoricalKPI(): Dict"],
               bg='#fffbeb', border='#d97706', header_bg='#fef3c7')

    draw_class(86, 17, 12, 24, "PublicServices", "Civic Facilities",
               ["-hospitalBeds: int", "-policePatrols: int", "-schoolCapacity: int", "-crimeRate: float"],
               ["+DeployPatrol(): void", "+TreatCitizens(): void", "+EnrollStudents(): void", "+ComputeSafety(): float"],
               bg='#fffbeb', border='#d97706', header_bg='#fef3c7')

    # Associations & Navigation Arrows
    # SimulationEngine controls CityGrid, BudgetManager, UtilityNetwork, EnvironmentEngine
    ax.annotate('', xy=(24, 86), xytext=(20, 86), arrowprops=dict(arrowstyle='->', color='#2563eb', lw=1.6))
    ax.text(22, 87.5, "manages", ha='center', fontsize=6.8, fontweight='bold', color='#1e40af')

    ax.annotate('', xy=(11, 41), xytext=(11, 77), arrowprops=dict(arrowstyle='->', color='#2563eb', lw=1.6))
    ax.text(12, 45, "executes tick", ha='left', fontsize=6.8, fontweight='bold', color='#1e40af')

    # MayorPlayer uses CityGrid
    ax.annotate('', xy=(41, 86), xytext=(45, 86), arrowprops=dict(arrowstyle='->', color='#0f172a', lw=1.4))
    ax.text(43, 87.5, "edits", ha='center', fontsize=6.8, color='#334155')

    # CityGrid contains ZonePlot
    ax.annotate('', xy=(31, 70), xytext=(31, 78), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=1.5))
    ax.text(32, 74, "1 : 2500 cells", ha='left', fontsize=6.5, fontweight='bold', color='#15803d')

    # ZonePlot hosts BuildingEntity
    ax.annotate('', xy=(19, 59), xytext=(23, 59), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=1.5))
    ax.text(21, 60.5, "hosts", ha='center', fontsize=6.5, color='#15803d')

    # CitizenAgent resides in ZonePlot & BuildingEntity
    ax.annotate('', xy=(39, 59), xytext=(43, 59), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=1.5))
    ax.text(41, 60.5, "populates", ha='center', fontsize=6.5, color='#15803d')

    # RoadNetwork connects ZonePlot
    ax.annotate('', xy=(60, 59), xytext=(64, 59), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=1.5))
    ax.text(62, 60.5, "serves", ha='center', fontsize=6.5, color='#15803d')

    # DisasterKernel affects CityGrid
    ax.annotate('', xy=(84, 59), xytext=(81, 59), arrowprops=dict(arrowstyle='->', color='#e11d48', lw=1.5))

    # FastApiClient dispatches to TelemetryLogger
    ax.annotate('', xy=(84, 86), xytext=(82, 86), arrowprops=dict(arrowstyle='->', color='#c026d3', lw=1.5))
    ax.text(83, 87.5, "logs", ha='center', fontsize=6.5, color='#a21caf')

    # Bottom Managers feed CSCIComputer
    ax.annotate('', xy=(67, 28), xytext=(63, 28), arrowprops=dict(arrowstyle='->', color='#d97706', lw=1.5))
    ax.text(65, 29.5, "feeds KPI", ha='center', fontsize=6.5, color='#b45309')

    save_and_close(fig, "fig4_4_class.png")

# =============================================================================
# 2. OBJECT DIAGRAM (Figure 4.6)
# =============================================================================
def generate_perfect_object_diagram():
    # 16 x 9.5 inches - runtime snapshot at Tick #12,450
    fig, ax = plt.subplots(figsize=(16, 9.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    ax.text(50, 97.2, "OBJECT DIAGRAM: RUNTIME SNAPSHOT AT TICK #12,450", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.plot([18, 82], [95.2, 95.2], color='#3b82f6', lw=1.5)

    def draw_obj(x, y, w, h, name_class, props, bg='#eff6ff', border='#2563eb'):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3", facecolor=bg, edgecolor=border, lw=1.5)
        ax.add_patch(rect)
        # Header with underline
        ax.text(x + w/2, y + h - 1.8, name_class, ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1e293b')
        ax.plot([x + 1.0, x + w - 1.0], [y + h - 3.2, y + h - 3.2], color=border, lw=1.0)
        curr_y = y + h - 4.8
        for p in props:
            ax.text(x + 1.2, curr_y, p, ha='left', va='center', fontsize=7.6, color='#0f172a')
            curr_y -= 1.6

    # Top Object: activePlayer : MayorPlayer
    draw_obj(34, 76, 32, 17, "activePlayer : MayorPlayer", [
        "playerId = \"a9041-kate-2026\"",
        "playerName = \"Mayor Sahil Kate\"",
        "currentSessionId = \"MUM-SIM-2026-V5\"",
        "activeZoningTool = CommercialHighDensity",
        "sessionDuration = 3,745.2 seconds"
    ], bg='#f0fdf4', border='#16a34a')

    # Middle Object: metropolisSession : CityGrid
    draw_obj(31, 46, 38, 22, "metropolisSession : CityGrid", [
        "gridDimensions = 50 × 50 (2,500 total plots)",
        "activePopulatedZones = 1,420 zones",
        "currentCitizenPopulation = 48,650 citizens",
        "treasuryBalance = ₹14,820,500.00",
        "compositeCSCI = 84.6 / 100 [Rating: Grade A]",
        "currentDisasterStatus = None (Alert Code Green)"
    ], bg='#eff6ff', border='#2563eb')

    # Row 3: Subordinate Runtime Instances
    draw_obj(2, 12, 17, 26, "resSector4 : ZonePlot", [
        "plotCoordinates = (18, 24)",
        "zoneType = Residential",
        "density = MediumDensity",
        "landValue = ₹45,000 / plot",
        "taxYieldRate = 8.5%",
        "currentOccupants = 240",
        "waterConnected = True",
        "powerConnected = True",
        "satisfactionScore = 88.2%"
    ], bg='#fffbeb', border='#d97706')

    draw_obj(21, 12, 18, 26, "clinicHospital01 : Building", [
        "buildingId = \"BLD-HOSP-014\"",
        "buildingType = DistrictHospital",
        "level = 2 (Upgraded)",
        "healthEfficiency = 94.5%",
        "dailyPowerDemand = 45 kW",
        "dailyWaterDemand = 120 L",
        "bedCapacity = 150 beds",
        "currentPatients = 82",
        "condition = 98.2%"
    ], bg='#fffbeb', border='#d97706')

    draw_obj(41, 12, 18, 26, "marineDriveCorridor : Road", [
        "roadId = \"RD-EXPR-09\"",
        "roadType = 4LaneAvenue",
        "speedLimit = 60 km/h",
        "hourlyVehicleCount = 840",
        "congestionLevel = 32% (Fluid)",
        "pavementCondition = 95%",
        "connectedSubstations = 4",
        "transitFlowEfficiency = 91%"
    ], bg='#fffbeb', border='#d97706')

    draw_obj(61, 12, 18, 26, "solarSubstation : Utility", [
        "networkId = \"GRID-PWR-03\"",
        "sourceType = SolarHydroHybrid",
        "ratedCapacity = 650.0 MW",
        "currentPeakDemand = 480.2 MW",
        "gridReliability = 99.4%",
        "loadSheddingActive = False",
        "transmissionLoss = 2.1%",
        "operationalStatus = Nominal"
    ], bg='#fffbeb', border='#d97706')

    draw_obj(81, 12, 17, 26, "citizen1041 : CitizenAgent", [
        "agentId = \"CIT-9041-082\"",
        "age = 29 years",
        "profession = DataEngineer",
        "homePlot = Vector2Int(18, 24)",
        "workPlot = Vector2Int(35, 12)",
        "happinessIndex = 86.4%",
        "healthStatus = 94.0%",
        "monthlyTaxContribution = ₹4,200",
        "commuteDelayMinutes = 8.5 min"
    ], bg='#fffbeb', border='#d97706')

    # Instance Links & Labels
    # activePlayer to metropolisSession
    ax.annotate('', xy=(50, 68), xytext=(50, 76), arrowprops=dict(arrowstyle='->', color='#1e3a8a', lw=1.6))
    ax.text(52, 72, "supervises & commands", ha='left', va='center', fontsize=7.8, fontweight='bold', color='#1e3a8a')

    # metropolisSession to Subordinate Instances
    targets = [
        (10.5, 38, "allocates"),
        (30, 38, "constructs"),
        (50, 38, "routes traffic"),
        (70, 38, "powers & supplies"),
        (89.5, 38, "governs & taxes")
    ]
    for tx, ty, lbl in targets:
        ax.annotate('', xy=(tx, ty), xytext=(50, 46), arrowprops=dict(arrowstyle='->', color='#2563eb', lw=1.4))
        mx = (50 + tx) / 2
        my = (46 + ty) / 2
        ax.text(mx, my + 1.0, lbl, ha='center', va='center', fontsize=7.2, fontweight='bold', color='#1e40af',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#cbd5e1', lw=0.6))

    save_and_close(fig, "fig_object_diagram.png")

# =============================================================================
# 3. USE CASE DIAGRAM (Figure 4.2)
# =============================================================================
def generate_perfect_usecase_diagram():
    fig, ax = plt.subplots(figsize=(16, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    ax.text(50, 97.2, "USE CASE DIAGRAM: SMART CITY MANAGEMENT SIMULATOR", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.plot([16, 84], [95.2, 95.2], color='#3b82f6', lw=1.5)

    # System boundary box
    sys_box = patches.Rectangle((23, 6), 54, 86, edgecolor='#1e3a8a', facecolor='#f8fafc', lw=2.0, linestyle='-')
    ax.add_patch(sys_box)
    ax.text(50, 89.5, "Smart City Management Simulation System Boundary", ha='center', va='center', 
            fontsize=10.5, fontweight='bold', color='#1e3a8a')

    # Draw Actor
    def draw_actor(x, y, name, role=""):
        # Head
        c = plt.Circle((x, y + 4.5), 2.2, color='#1e3a8a', fill=False, lw=2.2)
        ax.add_patch(c)
        # Body
        ax.plot([x, x], [y + 2.3, y - 2.5], color='#1e3a8a', lw=2.2)
        # Arms
        ax.plot([x - 3.8, x + 3.8], [y + 0.8, y + 0.8], color='#1e3a8a', lw=2.2)
        # Legs
        ax.plot([x, x - 3.2], [y - 2.5, y - 7.5], color='#1e3a8a', lw=2.2)
        ax.plot([x, x + 3.2], [y - 2.5, y - 7.5], color='#1e3a8a', lw=2.2)
        # Labels
        ax.text(x, y - 10.0, name, ha='center', va='top', fontsize=8.5, fontweight='bold', color='#0f172a')
        if role:
            ax.text(x, y - 12.8, role, ha='center', va='top', fontsize=7.2, fontstyle='italic', color='#475569')

    # Left Primary Actors
    draw_actor(11, 68, "City Mayor", "<<Primary User>>")
    draw_actor(11, 26, "Simulation Clock", "<<System Timer (2 Hz)>>")

    # Right Secondary Actors
    draw_actor(89, 68, "Municipal Auditor", "<<Analyst / Admin>>")
    draw_actor(89, 26, "Cloud Backend", "<<FastAPI & Postgres>>")

    # Helper for Use Case Ellipse
    def draw_uc(x, y, rx, ry, text, code=""):
        ellipse = patches.Ellipse((x, y), rx*2, ry*2, facecolor='#dbeafe', edgecolor='#2563eb', lw=1.6, zorder=3)
        ax.add_patch(ellipse)
        if code:
            ax.text(x, y + 1.2, f"[{code}]", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#1e40af', zorder=4)
            ax.text(x, y - 0.8, text, ha='center', va='center', fontsize=7.6, fontweight='bold', color='#0f172a', zorder=4, multialignment='center')
        else:
            ax.text(x, y, text, ha='center', va='center', fontsize=7.8, fontweight='bold', color='#0f172a', zorder=4, multialignment='center')

    # Core Use Cases (Left Column inside Boundary)
    draw_uc(36, 78, 9.5, 4.2, "Zone Urban Plots\n(Res / Com / Ind)", "UC-01")
    draw_uc(36, 64, 9.5, 4.2, "Construct Civic Buildings\n& Road Infrastructure", "UC-02")
    draw_uc(36, 50, 9.5, 4.2, "Adjust Municipal Tax\n& Departmental Budgets", "UC-03")
    draw_uc(36, 36, 9.5, 4.2, "Execute Coupled ODE\nSimulation Cycle", "UC-04")
    draw_uc(36, 22, 9.5, 4.2, "Deploy Disaster Responders\n& Fire / Smog Units", "UC-05")

    # Extension / Inclusion Use Cases (Right Column inside Boundary)
    draw_uc(64, 78, 9.5, 4.2, "Validate Plot Elevation\n& Water Bounds", "UC-06")
    draw_uc(64, 64, 9.5, 4.2, "Route Utility Grids\n(Power & Water BFS)", "UC-07")
    draw_uc(64, 50, 9.5, 4.2, "Audit Financial Health\n& Revenue Projections", "UC-08")
    draw_uc(64, 36, 9.5, 4.2, "Calculate Composite\nCSCI Rating (0-100)", "UC-09")
    draw_uc(64, 22, 9.5, 4.2, "Dispatch Async Telemetry\n& Persist JSON State", "UC-10")

    # Actor Association Lines
    # Mayor associations
    for uy in [78, 64, 50, 22]:
        ax.plot([14.5, 26.5], [68, uy], color='#1e3a8a', lw=1.5, zorder=1)

    # Simulation Clock association
    ax.plot([14.5, 26.5], [26, 36], color='#1e3a8a', lw=1.5, zorder=1)

    # Auditor associations
    for uy in [50, 36]:
        ax.plot([85.5, 73.5], [68, uy], color='#1e3a8a', lw=1.5, zorder=1)

    # Cloud Backend associations
    for uy in [36, 22]:
        ax.plot([85.5, 73.5], [26, uy], color='#1e3a8a', lw=1.5, zorder=1)

    # Include & Extend Relationships
    def draw_rel(x1, y1, x2, y2, tag):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', linestyle='dashed', color='#475569', lw=1.4), zorder=2)
        mx, my = (x1 + x2)/2, (y1 + y2)/2
        ax.text(mx, my + 1.2, f"<<{tag}>>", ha='center', va='center', fontsize=6.8, fontweight='bold', color='#334155',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#cbd5e1', lw=0.6), zorder=5)

    draw_rel(45.5, 78, 54.5, 78, "include")
    draw_rel(45.5, 64, 54.5, 64, "include")
    draw_rel(45.5, 50, 54.5, 50, "extend")
    draw_rel(45.5, 36, 54.5, 36, "include")
    draw_rel(45.5, 36, 54.5, 22, "include")
    draw_rel(45.5, 22, 54.5, 22, "extend")

    save_and_close(fig, "fig4_3_usecase.png")

# =============================================================================
# 4. SEQUENCE DIAGRAM (Figure 4.7)
# =============================================================================
def generate_perfect_sequence_diagram():
    # 18 x 11 inches - clear lifelines, spacious messages, zero overlaps
    fig, ax = plt.subplots(figsize=(18, 11), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    ax.text(50, 97.2, "SEQUENCE DIAGRAM: SIMULATION TICK & TELEMETRY DISPATCH", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.plot([15, 85], [95.2, 95.2], color='#3b82f6', lw=1.5)

    lifelines = [
        ("Mayor (User)", 8, True),
        ("UI Controller", 23, False),
        ("Simulation Engine", 39, False),
        ("CityGrid Matrix", 55, False),
        ("Budget Treasury", 71, False),
        ("FastAPI Telemetry", 88, False)
    ]

    top_y = 90.0
    bot_y = 6.0

    for name, lx, is_actor in lifelines:
        if is_actor:
            c = plt.Circle((lx, top_y + 1.8), 1.6, color='#1e3a8a', fill=False, lw=1.8)
            ax.add_patch(c)
            ax.plot([lx, lx], [top_y + 0.2, top_y - 2.2], color='#1e3a8a', lw=1.8)
            ax.plot([lx - 2.2, lx + 2.2], [top_y - 0.8, top_y - 0.8], color='#1e3a8a', lw=1.8)
            ax.plot([lx, lx - 2.0], [top_y - 2.2, top_y - 4.5], color='#1e3a8a', lw=1.8)
            ax.plot([lx, lx + 2.0], [top_y - 2.2, top_y - 4.5], color='#1e3a8a', lw=1.8)
            ax.text(lx, top_y - 6.0, name, ha='center', va='center', fontsize=8.0, fontweight='bold', color='#1e3a8a')
        else:
            rect = patches.FancyBboxPatch((lx - 6.5, top_y - 3.5), 13.0, 4.8, boxstyle="round,pad=0.2",
                                         facecolor='#eff6ff', edgecolor='#2563eb', lw=1.4)
            ax.add_patch(rect)
            ax.text(lx, top_y - 1.1, name, ha='center', va='center', fontsize=7.8, fontweight='bold', color='#1e3a8a')

        # Lifeline dashed vertical line
        ax.plot([lx, lx], [top_y - 6.8, bot_y + 4.0], color='#94a3b8', lw=1.2, linestyle=':')

        # Bottom box
        rect2 = patches.FancyBboxPatch((lx - 6.5, bot_y), 13.0, 4.0, boxstyle="round,pad=0.2",
                                      facecolor='#eff6ff', edgecolor='#2563eb', lw=1.4)
        ax.add_patch(rect2)
        ax.text(lx, bot_y + 2.0, name, ha='center', va='center', fontsize=7.5, fontweight='bold', color='#1e3a8a')

    # Activation bars
    def draw_activation(lx, y_start, y_end):
        act = patches.Rectangle((lx - 0.8, y_end), 1.6, y_start - y_end, facecolor='#bfdbfe', edgecolor='#1d4ed8', lw=1.0, zorder=3)
        ax.add_patch(act)

    draw_activation(8, 82, 16)
    draw_activation(23, 80, 20)
    draw_activation(39, 76, 22)
    draw_activation(55, 72, 34)
    draw_activation(71, 64, 42)
    draw_activation(88, 52, 26)

    # Message Helper
    def draw_seq_msg(x1, x2, y, num, text, is_return=False):
        ls = 'dashed' if is_return else 'solid'
        col = '#475569' if is_return else '#0f172a'
        ax.annotate('', xy=(x2, y), xytext=(x1, y),
                    arrowprops=dict(arrowstyle='->', linestyle=ls, color=col, lw=1.4), zorder=4)
        msg_str = f"{num}. {text}" if num else text
        fontw = 'normal' if is_return else 'bold'
        ax.text((x1 + x2)/2, y + 1.2, msg_str, ha='center', va='center', fontsize=7.4, fontweight=fontw, color=col, zorder=5,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='none', alpha=0.9))

    # Chronological message exchange
    draw_seq_msg(8, 23, 80, "1", "ClickPlaceBuilding(Clinic, plotX=18, plotZ=24)")
    draw_seq_msg(23, 39, 76, "2", "DispatchPlacementRequest(buildingData)")
    draw_seq_msg(39, 55, 72, "3", "ValidateCellAvailability(18, 24)")
    draw_seq_msg(55, 39, 68, "", "Return: CellFreeAndBuildable (Status: OK)", is_return=True)
    draw_seq_msg(39, 71, 64, "4", "CheckTreasuryFunds(cost = ₹45,000)")
    draw_seq_msg(71, 39, 60, "", "Return: FundsApproved (Balance: ₹14.8M)", is_return=True)

    # Alternative Frame (alt: Valid Placement)
    alt_box = patches.Rectangle((6, 24), 85, 34, facecolor='none', edgecolor='#6366f1', lw=1.4, linestyle='-')
    ax.add_patch(alt_box)
    ax.text(8.5, 56.5, "alt [Sufficient Funds & Valid Zoning]", fontsize=7.8, fontweight='bold', color='#4338ca')
    ax.plot([6, 28], [55, 55], color='#6366f1', lw=1.2)
    ax.plot([28, 30], [55, 58], color='#6366f1', lw=1.2)

    draw_seq_msg(39, 71, 52, "5a", "DeductConstructionFee(₹45,000)")
    draw_seq_msg(39, 55, 46, "5b", "InstantiateBuildingMesh(Clinic, (18, 24))")
    draw_seq_msg(55, 39, 41, "", "MeshRegisteredInSpatialIndex()", is_return=True)
    draw_seq_msg(39, 88, 36, "5c", "PostAsyncTelemetry(/api/v1/telemetry/event)")
    draw_seq_msg(88, 39, 31, "", "HTTP 201 Created (Metric Logged)", is_return=True)
    draw_seq_msg(39, 23, 27, "5d", "UpdateHUDDisplay(NewBalance, Score=84.6)")

    # Divider in alt frame
    ax.plot([6, 91], [22, 22], color='#6366f1', lw=1.0, linestyle='--')
    ax.text(8.5, 20.2, "[else: Insufficient Funds / Invalid Collision]", fontsize=7.4, fontweight='bold', color='#b91c1c')
    draw_seq_msg(39, 23, 16, "5e", "ShowErrorBanner(\"Placement Rejected\")", is_return=True)
    draw_seq_msg(23, 8, 12, "", "PlayErrorSound & FlashRedOutline()", is_return=True)

    save_and_close(fig, "fig4_5_sequence.png")

# =============================================================================
# 5. ACTIVITY DIAGRAM (Figure 4.8)
# =============================================================================
def generate_perfect_activity_diagram():
    # 17 x 10 inches - spacious landscape layout with swimlanes, zero text overflow!
    fig, ax = plt.subplots(figsize=(17, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    ax.text(50, 97.2, "ACTIVITY DIAGRAM: BUILDING PLACEMENT & SIMULATION CYCLE WORKFLOW", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.plot([14, 86], [95.2, 95.2], color='#3b82f6', lw=1.5)

    # Three Swimlanes
    ax.plot([33.3, 33.3], [6, 93], color='#cbd5e1', lw=1.4, linestyle='--')
    ax.plot([66.6, 66.6], [6, 93], color='#cbd5e1', lw=1.4, linestyle='--')

    # Swimlane headers
    ax.text(16.6, 92.0, "SWIMLANE 1: MAYOR UI CONTROLLER", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1e40af')
    ax.text(50.0, 92.0, "SWIMLANE 2: SPATIAL VALIDATION ENGINE", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1e40af')
    ax.text(83.3, 92.0, "SWIMLANE 3: SIMULATION KERNEL & CLOUD", ha='center', va='center', fontsize=8.8, fontweight='bold', color='#1e40af')

    def draw_action(x, y, w, h, text, bg='#eff6ff', border='#2563eb'):
        rect = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.4", facecolor=bg, edgecolor=border, lw=1.4)
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=7.6, color='#0f172a', multialignment='center')

    def draw_decision(x, y, w, h, text=""):
        poly = patches.Polygon([[x, y + h/2], [x + w/2, y], [x, y - h/2], [x - w/2, y]],
                               closed=True, facecolor='#fef3c7', edgecolor='#d97706', lw=1.4)
        ax.add_patch(poly)
        if text:
            ax.text(x, y, text, ha='center', va='center', fontsize=7.0, fontweight='bold', color='#78350f', multialignment='center')

    # Initial Node (Swimlane 1)
    c_start = plt.Circle((16.6, 85), 1.5, facecolor='#1e3a8a', edgecolor='#1e3a8a')
    ax.add_patch(c_start)
    ax.text(16.6, 87.5, "Start", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#1e3a8a')

    # Action 1: Select Facility
    ax.annotate('', xy=(16.6, 78), xytext=(16.6, 83.5), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.3))
    draw_action(16.6, 75, 24, 5.0, "Select Facility / Infrastructure\nfrom Municipal Toolbar")

    # Action 2: Raycast Plot
    ax.annotate('', xy=(16.6, 68), xytext=(16.6, 72.5), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.3))
    draw_action(16.6, 65, 24, 5.0, "Raycast Mouse Pointer\nonto 50x50 Terrain Grid")

    # Flow from Lane 1 to Lane 2: Check Terrain & Water
    ax.annotate('', xy=(50.0, 65), xytext=(28.6, 65), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.3))
    draw_action(50.0, 65, 24, 5.0, "Check Slope, Water Body\n& Collision Mask")

    # Decision 1: Terrain Valid? (Lane 2)
    ax.annotate('', xy=(50.0, 56.5), xytext=(50.0, 62.5), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.3))
    draw_decision(50.0, 52.5, 18, 7.0, "Terrain\nValid?")

    # Terrain Invalid -> Lane 1 Error Banner
    ax.plot([41.0, 16.6], [52.5, 52.5], color='#b91c1c', lw=1.2)
    ax.annotate('', xy=(16.6, 47), xytext=(16.6, 52.5), arrowprops=dict(arrowstyle='->', color='#b91c1c', lw=1.2))
    ax.text(28.8, 54.0, "[No: Water/Steep]", fontsize=6.8, fontweight='bold', color='#b91c1c')
    draw_action(16.6, 44, 22, 5.0, "Display Visual Red Outline\n& Invalidation Banner", bg='#fff1f2', border='#e11d48')

    # Terrain Valid -> Check Budget (Lane 2)
    ax.annotate('', xy=(50.0, 43.5), xytext=(50.0, 49.0), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=1.3))
    ax.text(51.5, 46.5, "[Yes]", fontsize=6.8, fontweight='bold', color='#16a34a')
    draw_decision(50.0, 39.5, 18, 7.0, "Treasury\nSufficient?")

    # Budget Invalid -> Lane 1 Error Banner
    ax.plot([41.0, 27.6], [39.5, 39.5], color='#b91c1c', lw=1.2)
    ax.annotate('', xy=(16.6, 41.5), xytext=(27.6, 39.5), arrowprops=dict(arrowstyle='->', color='#b91c1c', lw=1.2))
    ax.text(32.0, 41.0, "[No: Deficit]", fontsize=6.8, fontweight='bold', color='#b91c1c')

    # Budget Valid -> Flow to Lane 3: Deduct Funds & Instantiate
    ax.annotate('', xy=(71.0, 39.5), xytext=(59.0, 39.5), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=1.3))
    ax.text(64.0, 41.0, "[Yes]", fontsize=6.8, fontweight='bold', color='#16a34a')
    draw_action(83.3, 39.5, 24, 5.5, "Deduct Construction Cost\n& Instantiate 3D Structure")

    # Flow to Subsystem Simulation (Lane 3)
    ax.annotate('', xy=(83.3, 30.5), xytext=(83.3, 36.5), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.3))
    draw_action(83.3, 27.5, 24, 5.5, "Update Coupled ODE Models\n(Power, Water, AQI, Traffic)")

    # Flow to Telemetry & Cloud (Lane 3)
    ax.annotate('', xy=(83.3, 18.5), xytext=(83.3, 24.5), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.3))
    draw_action(83.3, 15.5, 24, 5.5, "Post Telemetry Record to\nFastAPI Cloud & Update HUD")

    # Merge Error and Success to End Node (Lane 1 Bottom)
    ax.plot([83.3, 83.3, 16.6], [12.5, 8.0, 8.0], color='#334155', lw=1.2)
    ax.plot([16.6, 16.6], [41.5, 11.0], color='#334155', lw=1.2)
    ax.annotate('', xy=(16.6, 11.0), xytext=(16.6, 8.0), arrowprops=dict(arrowstyle='->', color='#334155', lw=1.2))

    # Terminal Node
    c_out = plt.Circle((16.6, 11.0), 1.8, facecolor='#ffffff', edgecolor='#1e3a8a', lw=1.5)
    c_in = plt.Circle((16.6, 11.0), 1.0, facecolor='#1e3a8a', edgecolor='#1e3a8a')
    ax.add_patch(c_out)
    ax.add_patch(c_in)
    ax.text(16.6, 6.5, "Activity Completed", ha='center', va='center', fontsize=7.2, fontweight='bold', color='#1e3a8a')

    save_and_close(fig, "fig4_8_activity.png")

# =============================================================================
# 6. COMPONENT DIAGRAM (Figure 4.9)
# =============================================================================
def generate_perfect_component_diagram():
    # 18 x 10 inches - spacious 3-tier component architecture, zero text clipping
    fig, ax = plt.subplots(figsize=(18, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    ax.text(50, 97.2, "COMPONENT DIAGRAM: 3-TIER ARCHITECTURAL CONTRACTS", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.plot([15, 85], [95.2, 95.2], color='#3b82f6', lw=1.5)

    def draw_component(x, y, w, h, name, interfaces=[], bg='#eff6ff', border='#2563eb'):
        # Main Component Box
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3", facecolor=bg, edgecolor=border, lw=1.5)
        ax.add_patch(rect)
        # UML Component Prong Tabs on top-right
        tab1 = patches.Rectangle((x + w - 3.2, y + h - 1.8), 2.2, 1.2, facecolor='#ffffff', edgecolor=border, lw=1.0)
        ax.add_patch(tab1)
        # Component Title
        ax.text(x + (w - 2)/2, y + h - 2.2, f"<<component>>\n{name}", ha='center', va='center', 
                fontsize=8.0, fontweight='bold', color='#0f172a', multialignment='center')
        
        # Interfaces listed inside
        if interfaces:
            ax.plot([x + 0.8, x + w - 0.8], [y + h - 4.2, y + h - 4.2], color=border, lw=0.8, linestyle='--')
            curr_y = y + h - 5.6
            for iface in interfaces:
                ax.text(x + 1.2, curr_y, f"+ {iface}", ha='left', va='center', fontsize=6.8, color='#334155')
                curr_y -= 1.3

    # Tier 1 Container: Presentation Tier (Client Workstation)
    tier1_box = patches.Rectangle((2, 62), 96, 30, facecolor='#f8fafc', edgecolor='#94a3b8', lw=1.2, linestyle='-')
    ax.add_patch(tier1_box)
    ax.text(6, 89.5, "TIER 1: PRESENTATION & CLIENT INTERFACE (UNITY 6.3 LTS / DIRECTX 12)", 
            fontsize=8.8, fontweight='bold', color='#1e3a8a')

    draw_component(4, 65, 21, 21, "UnityHUDController", ["IHeadsUpDisplay", "IMayorInputHandler", "INotificationBus"], bg='#eff6ff', border='#2563eb')
    draw_component(28, 65, 21, 21, "SceneViewportRenderer", ["ICameraNavigable", "ILightingShader", "IParticleEmitter"], bg='#eff6ff', border='#2563eb')
    draw_component(52, 65, 21, 21, "SimulationClockTimer", ["ITickTrigger (2 Hz)", "ITimeScaler (1x-3x)", "IPauseResume"], bg='#eff6ff', border='#2563eb')
    draw_component(76, 65, 20, 21, "LocalAudioDialogueManager", ["ISoundEffectBank", "IGrievanceVoiceover"], bg='#eff6ff', border='#2563eb')

    # Tier 2 Container: Simulation Engine Tier
    tier2_box = patches.Rectangle((2, 31), 96, 28, facecolor='#f0fdf4', edgecolor='#86efac', lw=1.2, linestyle='-')
    ax.add_patch(tier2_box)
    ax.text(6, 56.5, "TIER 2: SIMULATION ENGINE CORE (MULTI-THREADED C# / COMPUTATIONAL KERNEL)", 
            fontsize=8.8, fontweight='bold', color='#15803d')

    draw_component(4, 34, 21, 20, "SpatialGridManager", ["IZoningAllocator", "ICollisionMatrix", "ITerrainHeightmap"], bg='#ffffff', border='#16a34a')
    draw_component(28, 34, 21, 20, "CoupledODEDifferentialEngine", ["IEconomicTaxLoop", "IPowerWaterBFSFlow", "IAQIPlumeSimulator"], bg='#ffffff', border='#16a34a')
    draw_component(52, 34, 21, 20, "CitizenAIAgentEngine", ["IAgentDecisionTree", "IAStarPathfinder", "ICommuteScheduler"], bg='#ffffff', border='#16a34a')
    draw_component(76, 34, 20, 20, "DisasterKernelDispatcher", ["IIncidentTrigger", "IDamagePropagator", "IEmergencyUnitRoster"], bg='#ffffff', border='#16a34a')

    # Tier 3 Container: Cloud Backend & Data Tier
    tier3_box = patches.Rectangle((2, 3), 96, 25, facecolor='#fffbeb', edgecolor='#fde68a', lw=1.2, linestyle='-')
    ax.add_patch(tier3_box)
    ax.text(6, 25.5, "TIER 3: BACKEND TELEMETRY & PERSISTENCE (FASTAPI / POSTGRESQL 17 / SQLALCHEMY)", 
            fontsize=8.8, fontweight='bold', color='#b45309')

    draw_component(4, 6, 21, 17, "FastAPITelemetryRouter", ["POST /telemetry", "GET /metrics/csci", "GET /saves/{id}"], bg='#ffffff', border='#d97706')
    draw_component(28, 6, 21, 17, "SQLAlchemyORMDataLayer", ["ISessionRepository", "ITelemetryTimeSeries", "IUserCredentials"], bg='#ffffff', border='#d97706')
    draw_component(52, 6, 21, 17, "PostgreSQLDatabaseEngine", ["CitySessionsTable", "ZoningMatrixJson", "MetricsTimeSeries"], bg='#ffffff', border='#d97706')
    draw_component(76, 6, 20, 17, "ChartJSAnalyticsDashboard", ["ICSCIHistoricalTrend", "IBudgetBreakdownView"], bg='#ffffff', border='#d97706')

    # Inter-tier connectors
    # Tier 1 to Tier 2
    for x_pos in [14.5, 38.5, 62.5, 86]:
        ax.annotate('', xy=(x_pos, 54), xytext=(x_pos, 65), arrowprops=dict(arrowstyle='<->', color='#2563eb', lw=1.4))

    # Tier 2 to Tier 3
    ax.annotate('', xy=(14.5, 23), xytext=(14.5, 34), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=1.4))
    ax.annotate('', xy=(38.5, 23), xytext=(38.5, 34), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=1.4))
    ax.annotate('', xy=(52, 14.5), xytext=(49, 14.5), arrowprops=dict(arrowstyle='->', color='#d97706', lw=1.4))
    ax.annotate('', xy=(76, 14.5), xytext=(73, 14.5), arrowprops=dict(arrowstyle='<-', color='#d97706', lw=1.4))

    save_and_close(fig, "fig4_2_component_diagram.png")

# =============================================================================
# 7. DEPLOYMENT DIAGRAM (Figure 4.10)
# =============================================================================
def generate_perfect_deployment_diagram():
    # 17 x 10 inches - 3D isometric styled nodes, clear protocol labels
    fig, ax = plt.subplots(figsize=(17, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    ax.text(50, 97.2, "DEPLOYMENT DIAGRAM: PHYSICAL HARDWARE NODES & CLOUD TOPOLOGY", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.plot([15, 85], [95.2, 95.2], color='#3b82f6', lw=1.5)

    def draw_3d_node(x, y, w, h, depth, title, env, artifacts=[], bg='#ffffff', border='#1e3a8a'):
        # 3D Node Top Face
        top_poly = patches.Polygon([
            [x, y + h], [x + depth, y + h + depth], [x + w + depth, y + h + depth], [x + w, y + h]
        ], closed=True, facecolor='#e2e8f0', edgecolor=border, lw=1.2)
        ax.add_patch(top_poly)

        # 3D Node Right Face
        right_poly = patches.Polygon([
            [x + w, y], [x + w, y + h], [x + w + depth, y + h + depth], [x + w + depth, y + depth]
        ], closed=True, facecolor='#cbd5e1', edgecolor=border, lw=1.2)
        ax.add_patch(right_poly)

        # 3D Node Front Face
        front_rect = patches.Rectangle((x, y), w, h, facecolor=bg, edgecolor=border, lw=1.5)
        ax.add_patch(front_rect)

        # Titles
        ax.text(x + w/2, y + h - 2.6, f"<<device>>\n{title}", ha='center', va='center', 
                fontsize=8.5, fontweight='bold', color='#0f172a', multialignment='center')
        ax.text(x + w/2, y + h - 6.2, f"[{env}]", ha='center', va='center', 
                fontsize=7.2, fontstyle='italic', color='#475569')

        # Divider
        ax.plot([x + 1.0, x + w - 1.0], [y + h - 8.0, y + h - 8.0], color=border, lw=1.0)

        # Artifacts
        curr_y = y + h - 10.5
        for art in artifacts:
            art_rect = patches.FancyBboxPatch((x + 1.5, curr_y - 2.0), w - 3.0, 3.6, boxstyle="round,pad=0.2",
                                             facecolor='#eff6ff', edgecolor='#93c5fd', lw=0.8)
            ax.add_patch(art_rect)
            ax.text(x + w/2, curr_y - 0.2, f"«artifact» {art}", ha='center', va='center', fontsize=7.0, color='#1e40af')
            curr_y -= 4.6

    # Node 1: Client Workstation (Left)
    draw_3d_node(4, 20, 26, 64, 4, "Mayor Workstation Node", 
                 "OS: Windows 10/11 x64 | 16 GB RAM",
                 [
                     "SmartCitySimulator.exe",
                     "Unity 6.3 Runtime Engine",
                     "DirectX 12 / Vulkan API",
                     "Local SQLite Cache (Saves.db)",
                     "Postman Telemetry Client"
                 ], bg='#ffffff', border='#2563eb')

    # Node 2: FastAPI Cloud App Server (Center)
    draw_3d_node(38, 20, 26, 64, 4, "Cloud Application Server", 
                 "OS: Ubuntu 24.04 LTS (Docker Container)",
                 [
                     "Uvicorn ASGI Web Server",
                     "FastAPI Python 3.11 Runtime",
                     "SQLAlchemy 2.0 ORM Engine",
                     "Pydantic Validation Schemas",
                     "JWT Session Auth Handler"
                 ], bg='#ffffff', border='#16a34a')

    # Node 3: PostgreSQL Database Node (Right)
    draw_3d_node(72, 20, 24, 64, 4, "Enterprise Database Node", 
                 "PostgreSQL 17.2 | Port 5432",
                 [
                     "SmartCityDB (Relational)",
                     "TelemetryTimeSeries Store",
                     "WAL Logging Archive",
                     "Chart.js Analytics Portal",
                     "Automated Hourly Backup Service"
                 ], bg='#ffffff', border='#d97706')

    # Network Protocol Communication Links
    # Workstation to App Server (HTTP/2 REST + WebSockets)
    ax.annotate('', xy=(38, 56), xytext=(34, 56), arrowprops=dict(arrowstyle='<->', color='#2563eb', lw=2.0))
    ax.text(36, 60.5, "HTTP/2 REST & JSON\nAsync Telemetry\n[Port 8000 / HTTPS]", 
            ha='center', va='center', fontsize=7.2, fontweight='bold', color='#1e40af',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffff', edgecolor='#cbd5e1', lw=0.8))

    # App Server to Database Node (TCP/IP PostgreSQL)
    ax.annotate('', xy=(72, 56), xytext=(68, 56), arrowprops=dict(arrowstyle='<->', color='#16a34a', lw=2.0))
    ax.text(70, 60.5, "PostgreSQL Wire Protocol\nSQLAlchemy Pooling\n[TCP/IP Port 5432]", 
            ha='center', va='center', fontsize=7.2, fontweight='bold', color='#15803d',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffffff', edgecolor='#cbd5e1', lw=0.8))

    save_and_close(fig, "fig_deployment_diagram.png")

# =============================================================================
# 8. DFD LEVEL 0 (Figure 4.4)
# =============================================================================
def generate_perfect_dfd0():
    # 16 x 9.5 inches - high contrast, clear bubbles, spacious text
    fig, ax = plt.subplots(figsize=(16, 9.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    ax.text(50, 97.2, "DATA FLOW DIAGRAM (DFD): LEVEL 0 - CONTEXT DIAGRAM", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.plot([16, 84], [95.2, 95.2], color='#3b82f6', lw=1.5)

    def draw_entity(x, y, w, h, title, subtitle=""):
        rect = patches.Rectangle((x, y), w, h, facecolor='#ffffff', edgecolor='#0f172a', lw=1.8)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2 + (1.0 if subtitle else 0), title, ha='center', va='center', 
                fontsize=8.5, fontweight='bold', color='#0f172a')
        if subtitle:
            ax.text(x + w/2, y + h/2 - 2.0, f"({subtitle})", ha='center', va='center', 
                    fontsize=7.0, fontstyle='italic', color='#475569')

    # Central Process 0.0
    c_proc = plt.Circle((50, 50), 16, facecolor='#eff6ff', edgecolor='#2563eb', lw=2.4)
    ax.add_patch(c_proc)
    ax.plot([34, 66], [56, 56], color='#2563eb', lw=1.2)
    ax.text(50, 60.5, "0.0", ha='center', va='center', fontsize=11, fontweight='bold', color='#1e40af')
    ax.text(50, 48.0, "SMART CITY\nMANAGEMENT SIMULATOR\nSYSTEM", ha='center', va='center', 
            fontsize=9.0, fontweight='bold', color='#0f172a', multialignment='center')

    # External Entities
    draw_entity(3, 40, 18, 20, "City Mayor", "Primary User")
    draw_entity(40, 80, 20, 12, "Citizen Agents", "AI Population")
    draw_entity(79, 65, 18, 18, "FastAPI Cloud", "Telemetry API")
    draw_entity(79, 17, 18, 18, "PostgreSQL 17", "Enterprise DB")

    # Data flows with high-contrast text tags
    def draw_flow(x1, y1, x2, y2, tag, curve=0):
        style = f"arc3,rad={curve}" if curve else "arc3,rad=0"
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', connectionstyle=style, color='#1e3a8a', lw=1.6))
        mx = (x1 + x2)/2
        my = (y1 + y2)/2
        ax.text(mx, my + (2.5 if curve >= 0 else -2.5), tag, ha='center', va='center', 
                fontsize=7.2, fontweight='bold', color='#1e3a8a',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#cbd5e1', lw=0.6))

    # Mayor Flows
    draw_flow(21, 55, 34, 55, "Zoning & Budget Policies", curve=0.1)
    draw_flow(34, 45, 21, 45, "City Health, Alerts & CSCI", curve=0.1)

    # Citizen Flows
    draw_flow(46, 80, 46, 66, "Tax Payments & Grievances")
    draw_flow(54, 66, 54, 80, "Public Services & Healthcare")

    # FastAPI Flows
    draw_flow(64, 56, 79, 70, "Serialized Telemetry JSON", curve=-0.1)
    draw_flow(79, 75, 64, 61, "Aggregated Urban Benchmarks", curve=-0.1)

    # Database Flows
    draw_flow(64, 44, 79, 30, "City Snapshots & Saves", curve=0.1)
    draw_flow(79, 23, 64, 39, "Persisted City Recovery", curve=0.1)

    save_and_close(fig, "fig4_6_dfd0.png")

# =============================================================================
# 9. DFD LEVEL 1 (Figure 4.5)
# =============================================================================
def generate_perfect_dfd1():
    # 17 x 10 inches - 4 processes, 4 data stores, crystal-clear labels
    fig, ax = plt.subplots(figsize=(17, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    ax.text(50, 97.2, "DATA FLOW DIAGRAM (DFD): LEVEL 1 - PROCESS DECOMPOSITION", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.plot([15, 85], [95.2, 95.2], color='#3b82f6', lw=1.5)

    def draw_proc(x, y, r, num, title):
        c = plt.Circle((x, y), r, facecolor='#eff6ff', edgecolor='#2563eb', lw=1.8)
        ax.add_patch(c)
        ax.plot([x - r, x + r], [y + r*0.35, y + r*0.35], color='#2563eb', lw=1.0)
        ax.text(x, y + r*0.65, num, ha='center', va='center', fontsize=9.0, fontweight='bold', color='#1e40af')
        ax.text(x, y - r*0.2, title, ha='center', va='center', fontsize=7.4, fontweight='bold', color='#0f172a', multialignment='center')

    def draw_store(x, y, w, h, sid, sname):
        rect = patches.Rectangle((x, y), w, h, facecolor='#fffbeb', edgecolor='#d97706', lw=1.2)
        ax.add_patch(rect)
        ax.plot([x + 4.5, x + 4.5], [y, y + h], color='#d97706', lw=1.2)
        ax.text(x + 2.25, y + h/2, sid, ha='center', va='center', fontsize=7.8, fontweight='bold', color='#b45309')
        ax.text(x + 4.5 + (w - 4.5)/2, y + h/2, sname, ha='center', va='center', fontsize=7.4, fontweight='bold', color='#0f172a')

    # 4 Processes
    draw_proc(20, 72, 9.5, "1.0", "Spatial Matrix\n& Construction")
    draw_proc(20, 26, 9.5, "2.0", "Coupled ODE\nSimulation Loop")
    draw_proc(80, 72, 9.5, "3.0", "Civic Grievance\n& Disaster Kernel")
    draw_proc(80, 26, 9.5, "4.0", "FastAPI Cloud\nTelemetry Dispatch")

    # 4 Data Stores (Center)
    draw_store(40, 80, 20, 7.5, "D1", "CITY_SESSIONS")
    draw_store(40, 60, 20, 7.5, "D2", "ZONING_MATRIX_50x50")
    draw_store(40, 40, 20, 7.5, "D3", "METRICS_TIME_SERIES")
    draw_store(40, 20, 20, 7.5, "D4", "GRIEVANCES_INCIDENTS")

    # External Entity: Mayor (Top Left)
    rect_mayor = patches.Rectangle((2, 85), 14, 9, facecolor='#ffffff', edgecolor='#0f172a', lw=1.5)
    ax.add_patch(rect_mayor)
    ax.text(9, 89.5, "Mayor / Planner", ha='center', va='center', fontsize=8.0, fontweight='bold', color='#0f172a')

    # Flow from Mayor to Process 1.0
    ax.annotate('', xy=(16, 81), xytext=(9, 85), arrowprops=dict(arrowstyle='->', color='#1e3a8a', lw=1.4))
    ax.text(9, 82.5, "Zoning Commands", fontsize=6.8, color='#1e3a8a')

    # Process 1.0 <-> Stores
    ax.annotate('', xy=(40, 83), xytext=(29.5, 76), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=1.4))
    ax.annotate('', xy=(40, 64), xytext=(29.5, 70), arrowprops=dict(arrowstyle='->', color='#16a34a', lw=1.4))
    ax.text(34, 79.5, "Save Session", fontsize=6.5, color='#15803d')
    ax.text(34, 68.5, "Write Tiles", fontsize=6.5, color='#15803d')

    # Process 2.0 <-> Stores
    ax.annotate('', xy=(28, 32), xytext=(40, 62), arrowprops=dict(arrowstyle='->', color='#2563eb', lw=1.4))
    ax.text(33, 48, "Read Grid Matrix", fontsize=6.5, color='#1e40af')
    ax.annotate('', xy=(40, 44), xytext=(29.5, 28), arrowprops=dict(arrowstyle='->', color='#2563eb', lw=1.4))
    ax.text(33, 34, "Update Metrics", fontsize=6.5, color='#1e40af')

    # Process 3.0 <-> Stores
    ax.annotate('', xy=(72, 68), xytext=(60, 45), arrowprops=dict(arrowstyle='->', color='#e11d48', lw=1.4))
    ax.text(68, 55, "Deficit Triggers", fontsize=6.5, color='#be123c')
    ax.annotate('', xy=(60, 24), xytext=(72, 68), arrowprops=dict(arrowstyle='->', color='#e11d48', lw=1.4))
    ax.text(68, 38, "Record Incident", fontsize=6.5, color='#be123c')

    # Process 4.0 <-> Stores
    ax.annotate('', xy=(70.5, 26), xytext=(60, 42), arrowprops=dict(arrowstyle='->', color='#d97706', lw=1.4))
    ax.text(65, 33, "Fetch Metrics", fontsize=6.5, color='#b45309')

    # Process 4.0 -> FastAPI Cloud External Entity
    rect_cloud = patches.Rectangle((84, 5), 14, 9, facecolor='#ffffff', edgecolor='#0f172a', lw=1.5)
    ax.add_patch(rect_cloud)
    ax.text(91, 9.5, "FastAPI Cloud API", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#0f172a')
    ax.annotate('', xy=(91, 14), xytext=(85, 20), arrowprops=dict(arrowstyle='->', color='#d97706', lw=1.4))
    ax.text(90, 18, "Async JSON Post", fontsize=6.5, color='#b45309')

    save_and_close(fig, "fig4_7_dfd1.png")

# =============================================================================
# 10. ENTITY RELATIONSHIP DIAGRAM (Figure 4.3)
# =============================================================================
def generate_perfect_erd():
    # 17 x 10 inches - relational schema with clear PK/FK and cardinalities
    fig, ax = plt.subplots(figsize=(17, 10), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    fig.patch.set_facecolor('#ffffff')

    ax.text(50, 97.2, "ENTITY-RELATIONSHIP (ER) DIAGRAM: 3NF RELATIONAL SCHEMA", 
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1e3a8a')
    ax.plot([15, 85], [95.2, 95.2], color='#3b82f6', lw=1.5)

    def draw_entity_table(x, y, w, h, title, pk_fields=[], fk_fields=[], normal_fields=[]):
        rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2", facecolor='#ffffff', edgecolor='#0284c7', lw=1.5)
        ax.add_patch(rect)
        # Header banner
        hdr = patches.Rectangle((x, y + h - 4.5), w, 4.5, facecolor='#0284c7', edgecolor='none')
        ax.add_patch(hdr)
        ax.text(x + w/2, y + h - 2.25, title, ha='center', va='center', fontsize=8.2, fontweight='bold', color='#ffffff')

        curr_y = y + h - 6.2
        for pk in pk_fields:
            ax.text(x + 1.2, curr_y, f"[PK] {pk}", ha='left', va='center', fontsize=6.8, fontweight='bold', color='#b91c1c')
            curr_y -= 2.0
        for fk in fk_fields:
            ax.text(x + 1.2, curr_y, f"[FK] {fk}", ha='left', va='center', fontsize=6.8, fontweight='bold', color='#4338ca')
            curr_y -= 2.0
        for f in normal_fields:
            ax.text(x + 1.2, curr_y, f"-  {f}", ha='left', va='center', fontsize=6.8, color='#334155')
            curr_y -= 2.0

    # Table 1: CITIES (Master Entity) - Center Top
    draw_entity_table(36, 60, 28, 30, "CITIES (Master Session)", 
                      ["id : Integer (PK, AutoInc)"],
                      [],
                      [
                          "city_name : String[100]",
                          "mayor_name : String[100]",
                          "difficulty : String[20]",
                          "starting_budget : Float",
                          "created_at : DateTime",
                          "is_active : Boolean",
                          "seed : BigInteger"
                      ])

    # Table 2: CITY_SAVES (Left Middle)
    draw_entity_table(3, 56, 27, 30, "CITY_SAVES (Save Slots)",
                      ["id : Integer (PK, AutoInc)"],
                      ["city_id : Integer (FK -> CITIES.id)"],
                      [
                          "slot_index : Integer",
                          "save_name : String[100]",
                          "game_state_json : Text",
                          "saved_at : DateTime",
                          "file_size_bytes : Integer",
                          "checksum : String[64]"
                      ])

    # Table 3: CITY_TELEMETRY (Right Middle)
    draw_entity_table(70, 48, 27, 42, "CITY_TELEMETRY (Time-Series)",
                      ["id : Integer (PK, AutoInc)"],
                      ["city_id : Integer (FK -> CITIES.id)"],
                      [
                          "tick_number : BigInteger",
                          "population : Integer",
                          "budget : Float",
                          "happiness : Float",
                          "smart_city_score : Integer",
                          "electricity_used_mw : Float",
                          "water_used_mld : Float",
                          "pollution_index_aqi : Float",
                          "traffic_efficiency : Float",
                          "recorded_at : DateTime"
                      ])

    # Table 4: ZONING_GRID (Left Bottom)
    draw_entity_table(3, 8, 27, 38, "ZONING_GRID (50x50 Matrix)",
                      ["id : Integer (PK, AutoInc)"],
                      ["city_id : Integer (FK -> CITIES.id)"],
                      [
                          "plot_x : Integer",
                          "plot_z : Integer",
                          "zone_type : String[30]",
                          "density_level : Integer",
                          "building_type : String[50]",
                          "building_level : Integer",
                          "water_connected : Boolean",
                          "power_connected : Boolean"
                      ])

    # Table 5: CITIZEN_PETITIONS (Center Bottom)
    draw_entity_table(36, 8, 28, 38, "CITIZEN_PETITIONS (Civic)",
                      ["id : Integer (PK, AutoInc)"],
                      ["city_id : Integer (FK -> CITIES.id)"],
                      [
                          "category : String[40]",
                          "title : String[120]",
                          "grievance_description : Text",
                          "severity : Integer (1-5)",
                          "status : String[20]",
                          "affected_population : Integer",
                          "submitted_tick : BigInteger",
                          "resolved_tick : BigInteger"
                      ])

    # Table 6: DISASTER_INCIDENTS (Right Bottom)
    draw_entity_table(70, 8, 27, 34, "DISASTER_INCIDENTS (Events)",
                      ["id : Integer (PK, AutoInc)"],
                      ["city_id : Integer (FK -> CITIES.id)"],
                      [
                          "disaster_type : String[40]",
                          "epicenter_x : Integer",
                          "epicenter_z : Integer",
                          "damage_spread_radius : Float",
                          "financial_loss : Float",
                          "casualties : Integer",
                          "resolved : Boolean"
                      ])

    # Foreign Key Relationship Connectors with Cardinalities
    def draw_relation(x1, y1, x2, y2, card_from, card_to, lbl):
        ax.plot([x1, x2], [y1, y2], color='#0284c7', lw=1.6)
        ax.text(x1 + (2.0 if x1 < x2 else -2.0), y1 + 1.2, card_from, fontsize=7.2, fontweight='bold', color='#0369a1')
        ax.text(x2 + (-2.0 if x1 < x2 else 2.0), y2 + 1.2, card_to, fontsize=7.2, fontweight='bold', color='#0369a1')
        mx, my = (x1 + x2)/2, (y1 + y2)/2
        ax.text(mx, my + 1.5, lbl, ha='center', va='center', fontsize=6.8, fontweight='bold', color='#0369a1',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor='#bae6fd', lw=0.6))

    # CITIES (1) to CITY_SAVES (N)
    draw_relation(36, 75, 30, 75, "1", "N", "has saves")

    # CITIES (1) to CITY_TELEMETRY (N)
    draw_relation(64, 75, 70, 75, "1", "N", "logs telemetry")

    # CITIES (1) to ZONING_GRID (N)
    draw_relation(38, 60, 28, 46, "1", "2500", "allocates cells")

    # CITIES (1) to CITIZEN_PETITIONS (N)
    draw_relation(50, 60, 50, 46, "1", "N", "receives petitions")

    # CITIES (1) to DISASTER_INCIDENTS (N)
    draw_relation(62, 60, 72, 42, "1", "N", "experiences disasters")

    save_and_close(fig, "fig4_9_erd.png")

if __name__ == '__main__':
    print("Generating 10 crystal-clear, high-resolution UML & DFD figures...")
    generate_perfect_class_diagram()
    generate_perfect_object_diagram()
    generate_perfect_usecase_diagram()
    generate_perfect_sequence_diagram()
    generate_perfect_activity_diagram()
    generate_perfect_component_diagram()
    generate_perfect_deployment_diagram()
    generate_perfect_dfd0()
    generate_perfect_dfd1()
    generate_perfect_erd()
    print("ALL 10 FIGURES GENERATED SUCCESSFULLY!")
