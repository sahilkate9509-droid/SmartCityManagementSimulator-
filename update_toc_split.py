import re

file_path = r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\content_frontmatter.py"
with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# Replace the single page TOC section with the exact 2-page split
old_toc_start = "# PAGE 9: TABLE OF CONTENT"
old_toc_idx = code.find(old_toc_start)
if old_toc_idx == -1:
    print("Could not find old TOC start!")
    exit(1)

# Find return elements
ret_idx = code.find("return elements", old_toc_idx)

new_toc_code = """# PAGE 9 & 10: TABLE OF CONTENT (2-PAGE SYLLABUS FORMAT - MATCHING EXACT PDF)
    # =========================================================================
    elements.append(Paragraph("TABLE OF CONTENT", styles['ChapterHeading']))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=8, spaceBefore=2))
    
    toc_chap_style = styles['TableCellBold'].clone('TOCChap')
    toc_chap_style.fontSize = 7.5
    toc_chap_style.leading = 9.0
    toc_chap_style.textColor = colors.HexColor("#0f172a")

    toc_sec_style = styles['TableCell'].clone('TOCSec')
    toc_sec_style.fontSize = 7.2
    toc_sec_style.leading = 8.6
    toc_sec_style.textColor = colors.HexColor("#1e293b")
    
    toc_head_style = styles['TableHead'].clone('TOCHead')
    toc_head_style.fontSize = 8.2
    toc_head_style.leading = 10.0
    
    # PAGE 9: TOC PART 1 (Sections 1.1 to 4.3.1)
    toc_data_part1 = [
        [Paragraph("<b>Section No. / Title</b>", toc_head_style),
         Paragraph("<b>Page No.</b>", toc_head_style)],
        
        # Chapter 1
        [Paragraph("<b>CHAPTER 1: INTRODUCTION</b>", toc_chap_style), Paragraph("<b>1</b>", toc_chap_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;1.1 Background", toc_sec_style), Paragraph("1", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;1.2 Objectives", toc_sec_style), Paragraph("2", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;1.3 Purpose, Scope and Applicability", toc_sec_style), Paragraph("3", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.3.1 Purpose", toc_sec_style), Paragraph("3", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.3.2 Scope", toc_sec_style), Paragraph("3", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.3.3 Applicability", toc_sec_style), Paragraph("3", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;1.4 Achievements", toc_sec_style), Paragraph("4", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;1.5 Organization of Report", toc_sec_style), Paragraph("4", toc_sec_style)],
        
        # Chapter 2
        [Paragraph("<b>CHAPTER 2: SURVEY OF TECHNOLOGIES</b>", toc_chap_style), Paragraph("<b>5</b>", toc_chap_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;2.1 Front-End", toc_sec_style), Paragraph("5", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;2.2 Back-End", toc_sec_style), Paragraph("5", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;2.3 Languages", toc_sec_style), Paragraph("5", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;2.4 INTEGRATED DEVELOPMENT ENVIRONMENT", toc_sec_style), Paragraph("6", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;2.5 Justification for Technologies Used", toc_sec_style), Paragraph("6", toc_sec_style)],
        
        # Chapter 3
        [Paragraph("<b>CHAPTER 3: REQUIREMENTS AND ANALYSIS</b>", toc_chap_style), Paragraph("<b>8</b>", toc_chap_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;3.1 Problem Definition", toc_sec_style), Paragraph("8", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;3.2 Requirements Specification", toc_sec_style), Paragraph("9", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2.1 Functional Requirements", toc_sec_style), Paragraph("9", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.2.2 Non-Functional Requirements", toc_sec_style), Paragraph("11", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;3.3 Planning and Scheduling", toc_sec_style), Paragraph("12", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;3.4 Software and Hardware Requirements", toc_sec_style), Paragraph("13", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;3.5 Preliminary Product Description", toc_sec_style), Paragraph("14", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;3.6 Conceptual Models", toc_sec_style), Paragraph("14", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.6.1 Data Flow Diagram", toc_sec_style), Paragraph("14", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.6.2 Entity-Relationship (ER) Diagram", toc_sec_style), Paragraph("15", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.6.3 Event Table", toc_sec_style), Paragraph("16", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.6.4 UML Diagrams", toc_sec_style), Paragraph("16", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.6.4.1 Use Case Diagram", toc_sec_style), Paragraph("16", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.6.4.2 Activity Diagram", toc_sec_style), Paragraph("17", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.6.4.3 Sequence Diagram", toc_sec_style), Paragraph("18", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.6.4.4 Class Diagram", toc_sec_style), Paragraph("19", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.6.4.5 Object Diagram", toc_sec_style), Paragraph("20", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.6.4.6 Deployment Diagram", toc_sec_style), Paragraph("21", toc_sec_style)],
        
        # Chapter 4 (Part 1)
        [Paragraph("<b>CHAPTER 4: SYSTEM DESIGN</b>", toc_chap_style), Paragraph("<b>23</b>", toc_chap_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;4.1 Basic Modules:", toc_sec_style), Paragraph("23", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;4.2 Data Design:", toc_sec_style), Paragraph("23", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.1 schema Design", toc_sec_style), Paragraph("23", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.1.1 User Table", toc_sec_style), Paragraph("23", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.1.2 SignLanguageGestures Table", toc_sec_style), Paragraph("24", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.1.3 TranslationLogs Table", toc_sec_style), Paragraph("24", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.1.4 TranslationSessions Table", toc_sec_style), Paragraph("24", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.1.5 Saved_phrases Table", toc_sec_style), Paragraph("24", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.1.6 Tickets Table", toc_sec_style), Paragraph("25", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.1.7 History", toc_sec_style), Paragraph("25", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.2.1.8 SystemEvents Table", toc_sec_style), Paragraph("25", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;4.3 Procedural Design:", toc_sec_style), Paragraph("26", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3.1 Logic Diagram:", toc_sec_style), Paragraph("26", toc_sec_style)],
    ]
    
    toc_table_1 = Table(toc_data_part1, colWidths=[425, 62])
    toc_table_1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 1.6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.6),
    ]))
    elements.append(toc_table_1)
    elements.append(PageBreak())

    # PAGE 10: TOC PART 2 (Sections 4.3.2 to Glossary)
    toc_data_part2 = [
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3.2 Data Structure:", toc_sec_style), Paragraph("27", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4.3.3 Algorithms Design", toc_sec_style), Paragraph("27", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;4.4 User Interface Design", toc_sec_style), Paragraph("29", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;4.5 Security Issues", toc_sec_style), Paragraph("31", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;4.6 Test Case Design", toc_sec_style), Paragraph("32", toc_sec_style)],
        
        # Chapter 5
        [Paragraph("<b>CHAPTER 5: IMPLEMENTATION AND TESTING</b>", toc_chap_style), Paragraph("<b>34</b>", toc_chap_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;5.1 Implementation Approaches", toc_sec_style), Paragraph("34", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;5.2 Coding Details and Code Efficiency", toc_sec_style), Paragraph("34", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.2.1 Code Efficiency", toc_sec_style), Paragraph("34", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;5.3 Testing Approach", toc_sec_style), Paragraph("44", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.3.1 Unit Testing", toc_sec_style), Paragraph("44", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.3.2 Integrated Testing", toc_sec_style), Paragraph("44", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5.3.3 Beta Testing (User Acceptance Testing)", toc_sec_style), Paragraph("44", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;5.4 Modifications and Improvements", toc_sec_style), Paragraph("45", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;5.5 Test Cases", toc_sec_style), Paragraph("45", toc_sec_style)],
        
        # Chapter 6
        [Paragraph("<b>CHAPTER 6: RESULTS AND DISCUSSION</b>", toc_chap_style), Paragraph("<b>50</b>", toc_chap_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;6.1 Test Reports", toc_sec_style), Paragraph("50", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;6.2 User Documentation", toc_sec_style), Paragraph("53", toc_sec_style)],
        
        # Chapter 7
        [Paragraph("<b>CHAPTER 7: CONCLUSION</b>", toc_chap_style), Paragraph("<b>58</b>", toc_chap_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;7.1 Conclusion", toc_sec_style), Paragraph("58", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7.1.1 Significance of the System", toc_sec_style), Paragraph("58", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;7.2 Limitations of the System", toc_sec_style), Paragraph("59", toc_sec_style)],
        [Paragraph("&nbsp;&nbsp;&nbsp;&nbsp;7.3 Future Scope of the Project", toc_sec_style), Paragraph("59", toc_sec_style)],
        
        # End Matter
        [Paragraph("<b>REFERENCES</b>", toc_chap_style), Paragraph("<b>61</b>", toc_chap_style)],
        [Paragraph("<b>GLOSSARY</b>", toc_chap_style), Paragraph("<b>63</b>", toc_chap_style)],
    ]
    toc_table_2 = Table(toc_data_part2, colWidths=[425, 62])
    toc_table_2.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.2),
    ]))
    elements.append(toc_table_2)
    elements.append(PageBreak())
    
    """

updated_code = code[:old_toc_idx] + new_toc_code + code[ret_idx:]
with open(file_path, "w", encoding="utf-8") as f:
    f.write(updated_code)

print("Successfully applied 2-page TOC split to content_frontmatter.py!")
