import re

with open('content_chapters_1_3.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add Tables 2.3 and 2.4 in Chapter 2 (after Table 2.2)
t23_t24_code = '''
    # Table 2.3: Database Engine Comparison
    db_data = [
        [Paragraph("<b>Evaluation Metric</b>", styles['TableHead']),
         Paragraph("<b>SQLite 3 (WAL Mode)</b>", styles['TableHead']),
         Paragraph("<b>PostgreSQL 17.0</b>", styles['TableHead']),
         Paragraph("<b>MySQL 8.4 LTS</b>", styles['TableHead']),
         Paragraph("<b>MongoDB 7.0</b>", styles['TableHead'])],
        [Paragraph("<b>Storage Architecture</b>", styles['TableCellBold']), Paragraph("Embedded Serverless B-Tree", styles['TableCell']), Paragraph("Client-Server Object-Relational", styles['TableCell']), Paragraph("Client-Server Relational", styles['TableCell']), Paragraph("Document JSON / BSON Store", styles['TableCell'])],
        [Paragraph("<b>Concurrency Model</b>", styles['TableCellBold']), Paragraph("WAL Mode (Multi-Reader, 1-Writer)", styles['TableCell']), Paragraph("MVCC (Multi-Version Concurrency)", styles['TableCell']), Paragraph("Row-Level Locking (InnoDB)", styles['TableCell']), Paragraph("WiredTiger Document Locks", styles['TableCell'])],
        [Paragraph("<b>ACID Compliance</b>", styles['TableCellBold']), Paragraph("Full ACID Guaranteed", styles['TableCell']), Paragraph("Full ACID with Strict Serializability", styles['TableCell']), Paragraph("Full ACID (InnoDB)", styles['TableCell']), Paragraph("Tunable Eventual Consistency", styles['TableCell'])],
        [Paragraph("<b>Setup / Ops Footprint</b>", styles['TableCellBold']), Paragraph("Zero Configuration (Single File)", styles['TableCell']), Paragraph("Enterprise Daemon Service", styles['TableCell']), Paragraph("Enterprise Daemon Service", styles['TableCell']), Paragraph("Clustered Daemon Service", styles['TableCell'])],
        [Paragraph("<b>Write Latency (ms)</b>", styles['TableCellBold']), Paragraph("0.12 ms (Local Disk NVMe)", styles['TableCell']), Paragraph("1.45 ms (Network TCP Socket)", styles['TableCell']), Paragraph("1.82 ms (Network TCP Socket)", styles['TableCell']), Paragraph("2.10 ms (Document Serialization)", styles['TableCell'])],
        [Paragraph("<b>Simulator Suitability</b>", styles['TableCellBold']), Paragraph("Ideal for Standalone Lab Clients", styles['TableCell']), Paragraph("Ideal for Cloud Telemetry Clusters", styles['TableCell']), Paragraph("Moderate / High Maintenance", styles['TableCell']), Paragraph("Unsuitable for Relational Saves", styles['TableCell'])],
    ]
    t_db = Table(db_data, colWidths=[105, 100, 100, 95, 87])
    t_db.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_db)
    elements.append(Paragraph("<b>Table 2.3:</b> Comparative Database Engine Evaluation Matrix", styles['FigCaption']))
    elements.append(Spacer(1, 6))

    # Table 2.4: Programming Language Evaluation Matrix
    lang_data = [
        [Paragraph("<b>Language Metric</b>", styles['TableHead']),
         Paragraph("<b>C# (.NET 8.0) (Selected)</b>", styles['TableHead']),
         Paragraph("<b>Python 3.12 (Selected)</b>", styles['TableHead']),
         Paragraph("<b>C++20</b>", styles['TableHead']),
         Paragraph("<b>Java 21 LTS</b>", styles['TableHead'])],
        [Paragraph("<b>Execution Environment</b>", styles['TableCellBold']), Paragraph("CoreCLR JIT / Unity Native C++", styles['TableCell']), Paragraph("CPython 3.12 Bytecode / Asyncio", styles['TableCell']), Paragraph("Direct Machine Assembly", styles['TableCell']), Paragraph("HotSpot JVM Runtime", styles['TableCell'])],
        [Paragraph("<b>Memory Model</b>", styles['TableCellBold']), Paragraph("Generational GC + Unmanaged Structs", styles['TableCell']), Paragraph("Reference Counting + Cycle GC", styles['TableCell']), Paragraph("Manual RAII / Smart Pointers", styles['TableCell']), Paragraph("Generational ZGC / G1 GC", styles['TableCell'])],
        [Paragraph("<b>Type System</b>", styles['TableCellBold']), Paragraph("Static Strong Type Safety", styles['TableCell']), Paragraph("Dynamic with Strict Type Hints", styles['TableCell']), Paragraph("Static Compile-Time Types", styles['TableCell']), Paragraph("Static Strong Type Safety", styles['TableCell'])],
        [Paragraph("<b>Graphics Engine API</b>", styles['TableCellBold']), Paragraph("Unity Scripting Core Native API", styles['TableCell']), Paragraph("Pygame / Panda3D (Limited 3D)", styles['TableCell']), Paragraph("Unreal / DirectX / Vulkan APIs", styles['TableCell']), Paragraph("jMonkeyEngine / LWJGL", styles['TableCell'])],
        [Paragraph("<b>Development Speed</b>", styles['TableCellBold']), Paragraph("Very Rapid (Rich Frameworks)", styles['TableCell']), Paragraph("Extremely Rapid Prototyping", styles['TableCell']), Paragraph("Slow / Verbose Compilation", styles['TableCell']), Paragraph("Moderate / Enterprise Verbose", styles['TableCell'])],
    ]
    t_lang = Table(lang_data, colWidths=[105, 100, 100, 95, 87])
    t_lang.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_lang)
    elements.append(Paragraph("<b>Table 2.4:</b> Comparative Programming Language Evaluation Matrix", styles['FigCaption']))
    elements.append(Spacer(1, 6))
'''

# Replace target in Chapter 2
target_2 = "elements.append(Paragraph(\"<b>Table 2.2:</b> Comparative Backend Framework Evaluation Matrix\", styles['FigCaption']))\n    elements.append(Spacer(1, 6))"
if target_2 in text:
    text = text.replace(target_2, target_2 + t23_t24_code)
    print("Injected Tables 2.3 and 2.4 into Chapter 2.")

# 2. Add Tables 3.10 to 3.14 in Section 3.6.4
uml_tables_code = '''
    # Table 3.10: Activity Decision & State Transition Table
    elements.append(Paragraph("<b>Activity Decision & State Transition Table:</b>", styles['SecHeading3']))
    act_table_data = [
        [Paragraph("<b>Step ID</b>", styles['TableHead']),
         Paragraph("<b>Current State</b>", styles['TableHead']),
         Paragraph("<b>Condition Evaluated</b>", styles['TableHead']),
         Paragraph("<b>Success Action / Next State</b>", styles['TableHead']),
         Paragraph("<b>Failure Action / Abort State</b>", styles['TableHead'])],
        [Paragraph("ACT-01", styles['TableCellBold']), Paragraph("Structure Selected", styles['TableCell']), Paragraph("Mouse Click Detected on Viewport", styles['TableCell']), Paragraph("Raycast against Terrain -> ACT-02", styles['TableCell']), Paragraph("Maintain Ghost Cursor -> ACT-01", styles['TableCell'])],
        [Paragraph("ACT-02", styles['TableCellBold']), Paragraph("Raycast Validated", styles['TableCell']), Paragraph("Target Coordinates (X,Z) <= 50", styles['TableCell']), Paragraph("Check Cell Occupancy -> ACT-03", styles['TableCell']), Paragraph("Emit Out-of-Bounds Error -> Abort", styles['TableCell'])],
        [Paragraph("ACT-03", styles['TableCellBold']), Paragraph("Occupancy Check", styles['TableCell']), Paragraph("Cell.structure == Vacant", styles['TableCell']), Paragraph("Check Water Obstacle -> ACT-04", styles['TableCell']), Paragraph("Show Cell Occupied Alert -> Abort", styles['TableCell'])],
        [Paragraph("ACT-04", styles['TableCellBold']), Paragraph("Water Obstacle Check", styles['TableCell']), Paragraph("Cell.isWater == False OR Type == Bridge", styles['TableCell']), Paragraph("Check Treasury Funds -> ACT-05", styles['TableCell']), Paragraph("Emit Water Collision Audio -> Abort", styles['TableCell'])],
        [Paragraph("ACT-05", styles['TableCellBold']), Paragraph("Treasury Funds Check", styles['TableCell']), Paragraph("TreasuryBalance >= StructureCost", styles['TableCell']), Paragraph("Instantiate 3D Mesh -> ACT-06", styles['TableCell']), Paragraph("Display Insufficient Funds Alert -> Abort", styles['TableCell'])],
        [Paragraph("ACT-06", styles['TableCellBold']), Paragraph("Placement Committed", styles['TableCell']), Paragraph("Deduct Funds & Update Grid Bitmask", styles['TableCell']), Paragraph("Refresh HUD & Recalculate Flow", styles['TableCell']), Paragraph("Rollback Grid State -> Abort", styles['TableCell'])],
    ]
    t_act_spec = Table(act_table_data, colWidths=[55, 100, 125, 110, 97])
    t_act_spec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_act_spec)
    elements.append(Paragraph("<b>Table 3.10:</b> Activity Decision Logic & State Transition Specifications", styles['FigCaption']))
    elements.append(Spacer(1, 6))
'''

# Replace target after Activity Diagram
target_act = "elements.append(Paragraph(p_act_analysis, styles['AcademicBody']))\n    elements.append(Spacer(1, 6))"
if target_act in text:
    text = text.replace(target_act, target_act + uml_tables_code, 1)
    print("Injected Table 3.10 after Activity Diagram.")

# Table 3.11 after Sequence Diagram
seq_table_code = '''
    # Table 3.11: Object Message Exchange & Latency Budget Table
    elements.append(Paragraph("<b>Sequence Messaging & Latency Budget Specifications:</b>", styles['SecHeading3']))
    seq_table_data = [
        [Paragraph("<b>Message ID</b>", styles['TableHead']),
         Paragraph("<b>Origin Object</b>", styles['TableHead']),
         Paragraph("<b>Recipient Object</b>", styles['TableHead']),
         Paragraph("<b>Method Signature / Synchronicity</b>", styles['TableHead']),
         Paragraph("<b>Latency Budget</b>", styles['TableHead'])],
        [Paragraph("MSG-01", styles['TableCellBold']), Paragraph("Unity Engine Timer", styles['TableCell']), Paragraph("CityManager", styles['TableCell']), Paragraph("UpdateTick() [Synchronous]", styles['TableCell']), Paragraph("< 0.10 ms", styles['TableCellBold'])],
        [Paragraph("MSG-02", styles['TableCellBold']), Paragraph("CityManager", styles['TableCell']), Paragraph("EconomySystem", styles['TableCell']), Paragraph("ComputeTaxRevenue(CityState) [Sync]", styles['TableCell']), Paragraph("< 0.35 ms", styles['TableCellBold'])],
        [Paragraph("MSG-03", styles['TableCellBold']), Paragraph("CityManager", styles['TableCell']), Paragraph("UtilitySystem", styles['TableCell']), Paragraph("ComputeGridBalance(CityState) [Sync]", styles['TableCell']), Paragraph("< 0.60 ms", styles['TableCellBold'])],
        [Paragraph("MSG-04", styles['TableCellBold']), Paragraph("CityManager", styles['TableCell']), Paragraph("DemographicSystem", styles['TableCell']), Paragraph("UpdateMigration(CityState) [Sync]", styles['TableCell']), Paragraph("< 0.45 ms", styles['TableCellBold'])],
        [Paragraph("MSG-05", styles['TableCellBold']), Paragraph("CityManager", styles['TableCell']), Paragraph("CityHUD", styles['TableCell']), Paragraph("RefreshGauges(CityState) [Sync]", styles['TableCell']), Paragraph("< 1.10 ms", styles['TableCellBold'])],
        [Paragraph("MSG-06", styles['TableCellBold']), Paragraph("CityManager", styles['TableCell']), Paragraph("TelemetryAgent", styles['TableCell']), Paragraph("QueueSnapshot(CityState) [Sync]", styles['TableCell']), Paragraph("< 0.25 ms", styles['TableCellBold'])],
        [Paragraph("MSG-07", styles['TableCellBold']), Paragraph("TelemetryAgent", styles['TableCell']), Paragraph("FastAPI Ingest API", styles['TableCell']), Paragraph("POST /api/v1/telemetry [Async HTTP]", styles['TableCell']), Paragraph("< 50.0 ms", styles['TableCellBold'])],
    ]
    t_seq_spec = Table(seq_table_data, colWidths=[60, 95, 95, 160, 77])
    t_seq_spec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_seq_spec)
    elements.append(Paragraph("<b>Table 3.11:</b> Sequence Messaging Protocol & Latency Budget Table", styles['FigCaption']))
    elements.append(Spacer(1, 6))
'''

target_seq = "elements.append(Paragraph(p_seq_analysis, styles['AcademicBody']))\n    elements.append(Spacer(1, 6))"
if target_seq in text:
    text = text.replace(target_seq, target_seq + seq_table_code, 1)
    print("Injected Table 3.11 after Sequence Diagram.")

with open('content_chapters_1_3.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Successfully expanded content_chapters_1_3.py.")
