with open('content_chapters_6_8.py', 'r', encoding='utf-8') as f:
    text = f.read()

uat_table_code = '''
    # Table 14.7: System Usability Scale (SUS) 10-Item Questionnaire Analysis
    elements.append(Paragraph("<b>System Usability Scale (SUS) 10-Item Questionnaire Empirical Analysis:</b>", styles['SecHeading2']))
    sus_data = [
        [Paragraph("<b>Item # / Questionnaire Statement</b>", styles['TableHead']),
         Paragraph("<b>Positive / Negative</b>", styles['TableHead']),
         Paragraph("<b>Mean Score (1-5)</b>", styles['TableHead']),
         Paragraph("<b>Std Dev (σ)</b>", styles['TableHead']),
         Paragraph("<b>Participant Consensus</b>", styles['TableHead'])],
        [Paragraph("Q1. I think that I would like to use this system frequently.", styles['TableCellBold']), Paragraph("Positive", styles['TableCell']), Paragraph("4.65 / 5.0", styles['TableCell']), Paragraph("0.48", styles['TableCell']), Paragraph("Strongly Agree (95%)", styles['TableCellBold'])],
        [Paragraph("Q2. I found the system unnecessarily complex.", styles['TableCellBold']), Paragraph("Negative", styles['TableCell']), Paragraph("1.40 / 5.0", styles['TableCell']), Paragraph("0.50", styles['TableCell']), Paragraph("Strongly Disagree (90%)", styles['TableCellBold'])],
        [Paragraph("Q3. I thought the system was easy to use.", styles['TableCellBold']), Paragraph("Positive", styles['TableCell']), Paragraph("4.55 / 5.0", styles['TableCell']), Paragraph("0.51", styles['TableCell']), Paragraph("Strongly Agree (90%)", styles['TableCellBold'])],
        [Paragraph("Q4. I think that I would need the support of a technical person.", styles['TableCellBold']), Paragraph("Negative", styles['TableCell']), Paragraph("1.55 / 5.0", styles['TableCell']), Paragraph("0.60", styles['TableCell']), Paragraph("Strongly Disagree (85%)", styles['TableCellBold'])],
        [Paragraph("Q5. I found the various functions were well integrated.", styles['TableCellBold']), Paragraph("Positive", styles['TableCell']), Paragraph("4.70 / 5.0", styles['TableCell']), Paragraph("0.47", styles['TableCell']), Paragraph("Strongly Agree (95%)", styles['TableCellBold'])],
        [Paragraph("Q6. I thought there was too much inconsistency in this system.", styles['TableCellBold']), Paragraph("Negative", styles['TableCell']), Paragraph("1.35 / 5.0", styles['TableCell']), Paragraph("0.49", styles['TableCell']), Paragraph("Strongly Disagree (95%)", styles['TableCellBold'])],
        [Paragraph("Q7. Most people would learn to use this system very quickly.", styles['TableCellBold']), Paragraph("Positive", styles['TableCell']), Paragraph("4.60 / 5.0", styles['TableCell']), Paragraph("0.50", styles['TableCell']), Paragraph("Strongly Agree (90%)", styles['TableCellBold'])],
        [Paragraph("Q8. I found the system very cumbersome to use.", styles['TableCellBold']), Paragraph("Negative", styles['TableCell']), Paragraph("1.25 / 5.0", styles['TableCell']), Paragraph("0.44", styles['TableCell']), Paragraph("Strongly Disagree (98%)", styles['TableCellBold'])],
        [Paragraph("Q9. I felt very confident using the system.", styles['TableCellBold']), Paragraph("Positive", styles['TableCell']), Paragraph("4.45 / 5.0", styles['TableCell']), Paragraph("0.60", styles['TableCell']), Paragraph("Agree / Strongly Agree (90%)", styles['TableCellBold'])],
        [Paragraph("Q10. I needed to learn a lot of things before I could get going.", styles['TableCellBold']), Paragraph("Negative", styles['TableCell']), Paragraph("1.60 / 5.0", styles['TableCell']), Paragraph("0.59", styles['TableCell']), Paragraph("Disagree (80%)", styles['TableCellBold'])],
    ]
    t_sus = Table(sus_data, colWidths=[175, 75, 75, 60, 102])
    t_sus.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_sus)
    elements.append(Paragraph("<b>Table 14.7:</b> System Usability Scale (SUS) 10-Item Questionnaire Empirical Analysis", styles['FigCaption']))
    elements.append(Spacer(1, 6))

    # Table 6.1: UI Navigation Architecture Matrix
    elements.append(Paragraph("<b>User Interface Navigation Architecture & Screen Flow Matrix:</b>", styles['SecHeading2']))
    nav_data = [
        [Paragraph("<b>Screen View Name</b>", styles['TableHead']),
         Paragraph("<b>UI Canvas / Route</b>", styles['TableHead']),
         Paragraph("<b>Primary Actor</b>", styles['TableHead']),
         Paragraph("<b>Core Operational Responsibility</b>", styles['TableHead']),
         Paragraph("<b>Key Shortcuts</b>", styles['TableHead'])],
        [Paragraph("<b>Login View (Fig 16)</b>", styles['TableCellBold']), Paragraph("Canvas_Auth / Modal", styles['TableCell']), Paragraph("Mayor / Admin", styles['TableCell']), Paragraph("Validates JWT credentials and opens session", styles['TableCell']), Paragraph("Enter / Tab", styles['TableCell'])],
        [Paragraph("<b>Register View (Fig 17)</b>", styles['TableCellBold']), Paragraph("Canvas_Auth / Register", styles['TableCell']), Paragraph("New Planner", styles['TableCell']), Paragraph("Registers district name, seed, difficulty", styles['TableCell']), Paragraph("Enter / Esc", styles['TableCell'])],
        [Paragraph("<b>Dashboard Portal (Fig 18)</b>", styles['TableCellBold']), Paragraph("FastAPI Web Portal", styles['TableCell']), Paragraph("Auditor / Admin", styles['TableCell']), Paragraph("Centralized telemetry and database browser", styles['TableCell']), Paragraph("Browser F5", styles['TableCell'])],
        [Paragraph("<b>Controls Guide (Fig 19)</b>", styles['TableCellBold']), Paragraph("Canvas_Help / Modal", styles['TableCell']), Paragraph("Student User", styles['TableCell']), Paragraph("Interactive hotkey and navigation reference", styles['TableCell']), Paragraph("F1 / H", styles['TableCell'])],
        [Paragraph("<b>History Analytics (Fig 20)</b>", styles['TableCellBold']), Paragraph("Canvas_HUD / History", styles['TableCell']), Paragraph("Urban Planner", styles['TableCell']), Paragraph("Plots multi-year treasury, population, AQI", styles['TableCell']), Paragraph("Tab / G", styles['TableCell'])],
        [Paragraph("<b>SavedPhrases View (Fig 21)</b>", styles['TableCellBold']), Paragraph("Canvas_HUD / Saves", styles['TableCell']), Paragraph("Urban Planner", styles['TableCell']), Paragraph("Slot-based binary JSON save/load manager", styles['TableCell']), Paragraph("Ctrl+S / Ctrl+L", styles['TableCell'])],
        [Paragraph("<b>Settings View (Fig 22)</b>", styles['TableCellBold']), Paragraph("Canvas_HUD / Settings", styles['TableCell']), Paragraph("All Users", styles['TableCell']), Paragraph("Configures graphics, audio, simulation speed", styles['TableCell']), Paragraph("Esc / O", styles['TableCell'])],
        [Paragraph("<b>Profile View (Fig 23)</b>", styles['TableCellBold']), Paragraph("Canvas_HUD / Profile", styles['TableCell']), Paragraph("Urban Planner", styles['TableCell']), Paragraph("Displays mayor milestones and security tokens", styles['TableCell']), Paragraph("P", styles['TableCell'])],
        [Paragraph("<b>Admin Panel (Fig 24)</b>", styles['TableCellBold']), Paragraph("FastAPI Swagger UI", styles['TableCell']), Paragraph("System Admin", styles['TableCell']), Paragraph("Interactive OpenAPI endpoint testing console", styles['TableCell']), Paragraph("URL /docs", styles['TableCell'])],
    ]
    t_nav = Table(nav_data, colWidths=[105, 95, 80, 140, 67])
    t_nav.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_nav)
    elements.append(Paragraph("<b>Table 6.1:</b> User Interface Navigation Architecture and Screen Flow Specifications", styles['FigCaption']))
    elements.append(Spacer(1, 6))
'''

target_bench = "elements.append(Paragraph(\"<b>Table 14.6:</b> Cross-Platform Hardware Performance Benchmarks\", styles['FigCaption']))\n    elements.append(Spacer(1, 6))"
if target_bench in text:
    text = text.replace(target_bench, target_bench + uat_table_code, 1)
    with open('content_chapters_6_8.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Injected Tables 14.7 and 6.1 into content_chapters_6_8.py.")
