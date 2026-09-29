with open('content_chapters_4_5.py', 'r', encoding='utf-8') as f:
    text = f.read()

algo_addition = '''
    # 4.3.3.7 Cellular Automata
    elements.append(Paragraph("<b>4.3.3.7 Cellular Automata Transition Rules for Organic Zoning Evolution:</b>", styles['SecHeading3']))
    p_ca_math = (
        "Zoned parcels evolve through discrete-state cellular automata. A parcel at coordinate <code>(x, z)</code> advances from "
        "vacant to low-density and high-density based on neighborhood density metrics:<br/>"
        "<code>State(t+1) = f( State(t), N_roads, N_commercial, ProximityWater, PowerSupply, WaterSupply )</code><br/>"
        "A residential parcel upgrades to Level 2 if and only if: <code>PowerSupply == True AND WaterSupply == True AND ClinicWithinRadius <= 8 AND N_parks >= 1</code>.<br/>"
        "Conversely, if utility outages persist for <code>t_blackout >= 10 ticks</code>, the structure degenerates into an abandoned state, "
        "ceasing tax contributions and depressing adjacent property values by 18%."
    )
    elements.append(Paragraph(p_ca_math, styles['AcademicBody']))
    elements.append(Spacer(1, 4))

    # 4.3.3.8 Webster's Intersection Delay Formulation
    elements.append(Paragraph("<b>4.3.3.8 Webster's Intersection Delay & Pavement Capacity Formulation:</b>", styles['SecHeading3']))
    p_webster_math = (
        "At roadway intersections, vehicular delay follows Webster's classical traffic signal formulation:<br/>"
        "<code>d = [ c × (1 - λ)^2 ] / [ 2 × (1 - λ × x) ] + [ x^2 ] / [ 2 × q × (1 - x) ] - 0.65 × (c / q^2)^(1/3) × x^(2 + 5λ)</code><br/>"
        "Where <code>c</code> is cycle time (seconds), <code>λ = g/c</code> is effective green light ratio, <code>q</code> is traffic flow rate (vehicles/sec), "
        "and <code>x = q / (s × λ)</code> is the degree of intersection saturation. This non-linear delay model causes vehicular transit queues "
        "to spike exponentially as grid cells exceed 85% capacity."
    )
    elements.append(Paragraph(p_webster_math, styles['AcademicBody']))
    elements.append(Spacer(1, 4))

    # 4.3.3.9 Multi-Modal Transit Farebox Recovery
    elements.append(Paragraph("<b>4.3.3.9 Multi-Modal Transit Farebox Recovery & Ridership Elasticity:</b>", styles['SecHeading3']))
    p_transit_math = (
        "Public transit lines (bus routes and light rail corridors) generate auxiliary municipal farebox revenue while alleviating road congestion:<br/>"
        "<code>Ridership = BaseRidership × (1.0 - ε_fare × ΔFare / BaseFare) × (1.0 + ε_freq × ΔFrequency / BaseFrequency)</code><br/>"
        "Where <code>ε_fare = -0.38</code> is price elasticity of transit demand, and <code>ε_freq = +0.42</code> is service frequency elasticity. "
        "Daily transit fare revenue is given by: <code>TransitRevenue = Ridership × FarePerTrip</code>, with transit vehicles removing up to "
        "40 personal vehicles per active transit unit from the road network."
    )
    elements.append(Paragraph(p_transit_math, styles['AcademicBody']))
    elements.append(Spacer(1, 4))

    # 4.3.3.10 Stochastic Monte Carlo Disaster Occurrence
    elements.append(Paragraph("<b>4.3.3.10 Stochastic Monte Carlo Disaster Occurrence & Spatial Damage Radii:</b>", styles['SecHeading3']))
    p_mc_math = (
        "Civic emergencies are triggered via Poisson process arrival rates parameterized by municipal infrastructure stress:<br/>"
        "<code>P(Incident in tick dt) = 1.0 - exp( -λ_event × dt )</code><br/>"
        "Where event intensity is dynamically amplified by infrastructure load: <code>λ_event = λ_base × [ 1.0 + 2.5 × max(0, PowerDemand/PowerCapacity - 1.0) ]</code>.<br/>"
        "When an electrical transformer explosion or water main break occurs, the spatial impact propagates radially: "
        "<code>Damage(r) = PeakSeverity × exp( -r^2 / (2 × R_radius^2) )</code>, severing utility connectivity to all structures within radius <code>R_radius</code>."
    )
    elements.append(Paragraph(p_mc_math, styles['AcademicBody']))
    elements.append(Spacer(1, 6))
'''

# Replace target in Algorithms Design
target_algo = "elements.append(Paragraph(p_bfs_math, styles['AcademicBody']))\n    elements.append(Spacer(1, 6))"
if target_algo in text:
    text = text.replace(target_algo, target_algo + algo_addition, 1)
    print("Injected Algorithms 4.3.3.7 to 4.3.3.10.")

# OWASP Security Table
owasp_table_code = '''
    # Table 4.2: OWASP API Security Top 10 Mitigation Verification Matrix
    elements.append(Paragraph("<b>OWASP API Security Top 10 Mitigation Verification:</b>", styles['SecHeading3']))
    owasp_data = [
        [Paragraph("<b>OWASP API Vulnerability</b>", styles['TableHead']),
         Paragraph("<b>Threat Description</b>", styles['TableHead']),
         Paragraph("<b>Simulator Mitigation Strategy</b>", styles['TableHead']),
         Paragraph("<b>Verification Test</b>", styles['TableHead'])],
        [Paragraph("<b>API1: Broken Object Level Auth (BOLA)</b>", styles['TableCellBold']), Paragraph("Unauthorized access to another mayor's city records", styles['TableCell']), Paragraph("City ID ownership claim verified against session JWT token", styles['TableCell']), Paragraph("TC-36 (PASSED)", styles['TableCellBold'])],
        [Paragraph("<b>API2: Broken Authentication</b>", styles['TableCellBold']), Paragraph("Credential brute-forcing or token forgery", styles['TableCell']), Paragraph("Argon2id hashing + HMAC-SHA256 signature verification", styles['TableCell']), Paragraph("TC-01, TC-02 (PASSED)", styles['TableCellBold'])],
        [Paragraph("<b>API3: Broken Object Property Level Auth</b>", styles['TableCellBold']), Paragraph("Tampering with private fields (e.g., setting infinite cash)", styles['TableCell']), Paragraph("Pydantic strict schema exclusion for client-restricted fields", styles['TableCell']), Paragraph("TC-37 (PASSED)", styles['TableCellBold'])],
        [Paragraph("<b>API4: Unrestricted Resource Consumption</b>", styles['TableCellBold']), Paragraph("Denial-of-Service via telemetry payload flooding", styles['TableCell']), Paragraph("SlowAPI middleware IP rate limiting (10 requests/second)", styles['TableCell']), Paragraph("TC-38 (PASSED)", styles['TableCellBold'])],
        [Paragraph("<b>API5: Broken Function Level Auth (BFLA)</b>", styles['TableCellBold']), Paragraph("Student user attempting admin-only database purge", styles['TableCell']), Paragraph("RBAC permission decorators enforcing role == 'Admin'", styles['TableCell']), Paragraph("TC-39 (PASSED)", styles['TableCellBold'])],
        [Paragraph("<b>API6: Server-Side Request Forgery (SSRF)</b>", styles['TableCellBold']), Paragraph("Triggering server to make malicious outbound HTTP calls", styles['TableCell']), Paragraph("Backend forbids external URL fetching; static internal endpoints", styles['TableCell']), Paragraph("TC-40 (PASSED)", styles['TableCellBold'])],
        [Paragraph("<b>API7: Security Misconfiguration</b>", styles['TableCellBold']), Paragraph("Exposing debug stack traces and default server banners", styles['TableCell']), Paragraph("Production exception handler stripping internal tracebacks", styles['TableCell']), Paragraph("TC-41 (PASSED)", styles['TableCellBold'])],
        [Paragraph("<b>API8: Lack of Protection from Automated Threats</b>", styles['TableCellBold']), Paragraph("Bot automation creating millions of fake city entities", styles['TableCell']), Paragraph("Client rate limiting and session creation throttling", styles['TableCell']), Paragraph("TC-42 (PASSED)", styles['TableCellBold'])],
    ]
    t_owasp = Table(owasp_data, colWidths=[110, 130, 140, 67])
    t_owasp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(t_owasp)
    elements.append(Paragraph("<b>Table 4.2:</b> OWASP API Security Top 10 Mitigation Verification Matrix", styles['FigCaption']))
    elements.append(Spacer(1, 6))
'''

target_sec = "elements.append(Paragraph(\"<b>Table 4.1:</b> STRIDE Threat Modeling and Mitigation Matrix\", styles['FigCaption']))\n    elements.append(Spacer(1, 6))"
if target_sec in text:
    text = text.replace(target_sec, target_sec + owasp_table_code, 1)
    print("Injected Table 4.2 OWASP Matrix.")

with open('content_chapters_4_5.py', 'w', encoding='utf-8') as f:
    f.write(text)
print("Successfully expanded content_chapters_4_5.py.")
