with open('content_chapters_1_3.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add historical urban theories in 1.1
history_addition = '''
    p_theories = (
        "<b>Theoretical Foundations of Spatial Urban Economics:</b> To construct an authentic digital twin, the simulator synthesizes "
        "five classic spatial economic paradigms: (1) <i>Von Thünen's Isolated State Model (1826)</i>, which established concentric rings of agricultural "
        "and industrial land use determined by transportation cost differentials; (2) <i>Walter Christaller's Central Place Theory (1933)</i>, "
        "explaining hexagonal hierarchies of market centers and retail service radii; (3) <i>Ernest Burgess's Concentric Zone Model (1925)</i>, "
        "characterizing radial outward expansion from a central business district through zones of transition and residential commuter belts; "
        "(4) <i>Homer Hoyt's Sector Model (1939)</i>, demonstrating directional transportation corridor growth; and (5) <i>Harris and Ullman's "
        "Multiple Nuclei Model (1945)</i>, modeling modern polycentric metropolises with dispersed specialized commercial and manufacturing nodes. "
        "The procedural placement algorithms and bid-rent equations in the simulator directly operationalize these theoretical principles, "
        "allowing users to observe emergent polycentric spatial structures as transportation networks expand."
    )
    elements.append(Paragraph(p_theories, styles['AcademicBody']))
    elements.append(Spacer(1, 4))
'''

target_hist = "elements.append(Paragraph(p2, styles['AcademicBody']))\n    elements.append(Spacer(1, 4))"
if target_hist in text:
    text = text.replace(target_hist, target_hist + history_addition, 1)

# 2. Add Table 3.0 in Problem Definition
table_30_code = '''
    # Table 3.0: Urban Planning Deficiencies & Digital Twin Countermeasures Matrix
    elements.append(Paragraph("<b>Table 3.0: Urban Planning Decision Paradigms & Digital Twin Countermeasures:</b>", styles['SecHeading3']))
    t30_data = [
        [Paragraph("<b>Planning Dimension</b>", styles['TableHead']),
         Paragraph("<b>Static Spreadsheet Models</b>", styles['TableHead']),
         Paragraph("<b>Commercial Entertainment Games</b>", styles['TableHead']),
         Paragraph("<b>SCMS Academic Digital Twin</b>", styles['TableHead'])],
        [Paragraph("<b>Spatial Representation</b>", styles['TableCellBold']), Paragraph("Non-spatial tabular rows and columns", styles['TableCell']), Paragraph("Proprietary 3D graphics (Closed engine)", styles['TableCell']), Paragraph("Interactive 50x50 procedural grid (Open URP)", styles['TableCell'])],
        [Paragraph("<b>Temporal Dynamics</b>", styles['TableCellBold']), Paragraph("Static annual or quarterly snapshots", styles['TableCell']), Paragraph("Game-loop tick (uncalibrated speed)", styles['TableCell']), Paragraph("Discrete-time 0.5s ticks = 1 virtual day", styles['TableCell'])],
        [Paragraph("<b>Mathematical Access</b>", styles['TableCellBold']), Paragraph("Formulas visible but spatially disconnected", styles['TableCell']), Paragraph("Hidden black-box proprietary code", styles['TableCell']), Paragraph("100% Transparent pure C# static equations", styles['TableCell'])],
        [Paragraph("<b>Subsystem Coupling</b>", styles['TableCellBold']), Paragraph("Isolated silos (budget only or tax only)", styles['TableCell']), Paragraph("Heuristic entertainment feedback", styles['TableCell']), Paragraph("Coupled differential equations across 6 sectors", styles['TableCell'])],
        [Paragraph("<b>Data Persistence</b>", styles['TableCellBold']), Paragraph("Manual file saving (XLSX / CSV)", styles['TableCell']), Paragraph("Proprietary binary game saves", styles['TableCell']), Paragraph("Relational PostgreSQL/SQLite + JSON Save Slots", styles['TableCell'])],
        [Paragraph("<b>Cloud Telemetry</b>", styles['TableCellBold']), Paragraph("None (Local desktop spreadsheets)", styles['TableCell']), Paragraph("None (Closed standalone binary)", styles['TableCell']), Paragraph("Asynchronous FastAPI REST telemetry ingest", styles['TableCell'])],
        [Paragraph("<b>Educational Cost</b>", styles['TableCellBold']), Paragraph("Low (Generic Office Suite)", styles['TableCell']), Paragraph("Retail software purchase ($30-$60/copy)", styles['TableCell']), Paragraph("100% Free and Open Source for Academia", styles['TableCell'])],
    ]
    t_30 = Table(t30_data, colWidths=[110, 120, 125, 132])
    t_30.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_30)
    elements.append(Paragraph("<b>Table 3.0:</b> Comparative Matrix of Urban Planning Paradigms vs SCMS Digital Twin", styles['FigCaption']))
    elements.append(Spacer(1, 6))
'''

target_prob = "elements.append(Paragraph(p_prob_def, styles['AcademicBody']))\n    elements.append(Spacer(1, 6))"
if target_prob in text:
    text = text.replace(target_prob, target_prob + table_30_code, 1)

with open('content_chapters_1_3.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated content_chapters_1_3.py with historical urban theories and Table 3.0.")
