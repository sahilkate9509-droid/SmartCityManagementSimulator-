with open('content_chapters_6_8.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = "elements.append(Paragraph(p_future, styles['AcademicBody']))\n    elements.append(Spacer(1, 4))"

expanded_future_code = '''elements.append(Paragraph(p_future, styles['AcademicBody']))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>7.3.1 Real-World OpenStreetMap (OSM) Vector GIS Ingestion:</b>", styles['SecHeading2']))
    p_fs_1 = (
        "While the current release procedurally generates synthetic 50×50 coordinate grids, real-world urban planning requires analyzing "
        "existing municipal morphology. A primary future enhancement is developing an OpenStreetMap (OSM) and GeoJSON vector ingestion pipeline. "
        "By parsing OSM XML nodes, ways, and relations, the simulator will automatically reconstruct authentic street centerlines, building footprints, "
        "and natural waterways for real metropolitan territories such as Mumbai, London, or Tokyo. This will allow city municipal corporations to load "
        "their actual ward boundaries and stress-test zoning proposals on top of authentic cadastral data."
    )
    elements.append(Paragraph(p_fs_1, styles['AcademicBody']))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>7.3.2 Deep Reinforcement Learning (DRL) Multi-Agent Policy Optimization:</b>", styles['SecHeading2']))
    p_fs_2 = (
        "To advance beyond human heuristic decision-making, the platform will integrate Unity ML-Agents and PyTorch to train autonomous policy agents. "
        "Using Proximal Policy Optimization (PPO), deep reinforcement learning agents can be tasked with maximizing the Composite Smart City Index (CSCI) "
        "over multi-decade horizons under stochastic weather and economic shocks. By comparing human municipal decisions against AI-discovered Pareto-optimal "
        "tax and infrastructure policies, researchers can identify novel counter-intuitive strategies for sustainable urban development."
    )
    elements.append(Paragraph(p_fs_2, styles['AcademicBody']))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>7.3.3 Multiplayer Collaborative Urban Governance:</b>", styles['SecHeading2']))
    p_fs_3 = (
        "Urban planning is inherently a collaborative, multi-stakeholder endeavor involving conflicting interests between housing developers, transit "
        "authorities, and environmental protection agencies. Future releases will extend the FastAPI backend with WebSocket duplex communication and "
        "distributed lock management. This will enable multi-user simulation sessions where multiple human participants govern adjacent municipal wards, "
        "negotiating cross-border transit connections, energy sharing agreements, and joint pollution abatement pacts in real time."
    )
    elements.append(Paragraph(p_fs_3, styles['AcademicBody']))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>7.3.4 Virtual Reality (VR) Immersive Digital Twin Experience:</b>", styles['SecHeading2']))
    p_fs_4 = (
        "Translating macroscopic urban plans into visceral human experiences is crucial for public participatory democracy. By porting the Unity 6.3 "
        "client engine to OpenXR headsets (e.g., Meta Quest 3, HTC Vive), planners and citizens can step directly into the simulated streets at 1:1 scale. "
        "Users will be able to experience pedestrian walkability, visual building scale, shading from high-rise structures, and ambient traffic noise, "
        "fostering empathetic civic engagement prior to physical construction."
    )
    elements.append(Paragraph(p_fs_4, styles['AcademicBody']))
    elements.append(Spacer(1, 4))

    elements.append(Paragraph("<b>7.3.5 Physical IoT Hardware-in-the-Loop Integration:</b>", styles['SecHeading2']))
    p_fs_5 = (
        "The software architecture is engineered to interface seamlessly with physical sensor hardware. A future extension will connect the FastAPI "
        "backend to physical Arduino, Raspberry Pi, and ESP32 microcontroller nodes deployed in environmental monitoring stations. Real-time physical "
        "readings of ambient classroom temperature, humidity, and carbon dioxide concentrations will directly feed into the simulator's environmental "
        "subsystem, transforming the digital twin into an authentic hardware-in-the-loop laboratory testbed."
    )
    elements.append(Paragraph(p_fs_5, styles['AcademicBody']))
    elements.append(Spacer(1, 6))'''

if target in text:
    # Replace the existing bullet loop as well
    old_loop_target = '''    for fp in future_points:
        elements.append(Paragraph(f"• {fp}", styles['AcademicBullet']))
        elements.append(Spacer(1, 3))'''
    
    # Find start of target to end of old loop
    idx_target = text.find(target)
    idx_loop = text.find(old_loop_target)
    if idx_target != -1 and idx_loop != -1:
        end_loop = idx_loop + len(old_loop_target)
        text = text[:idx_target] + expanded_future_code + text[end_loop:]
        with open('content_chapters_6_8.py', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Updated Future Scope in content_chapters_6_8.py.")
