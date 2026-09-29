import os
import sys
import json
import re
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from report_styles import get_academic_styles, PRINTABLE_WIDTH, PAGE_WIDTH, PAGE_HEIGHT
from blackbook_core import AcademicNumberedCanvas
from content_frontmatter import build_frontmatter
from content_chapters_1_3 import build_chapters_1_3
from content_chapters_4_5 import build_chapters_4_5
from content_chapters_6_8 import build_chapters_6_8
from pypdf import PdfReader

OUTPUT_PDF = r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\Smart_City_Management_Simulator_Black_Book.pdf"
FIG_DIR = r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\docs_figures"

def render_doc(toc_dict=None):
    styles = get_academic_styles()
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    story = []
    story.extend(build_frontmatter(styles, PRINTABLE_WIDTH, FIG_DIR, toc_dict))
    story.extend(build_chapters_1_3(styles, PRINTABLE_WIDTH, FIG_DIR))
    story.extend(build_chapters_4_5(styles, PRINTABLE_WIDTH, FIG_DIR))
    story.extend(build_chapters_6_8(styles, PRINTABLE_WIDTH, FIG_DIR))
    
    doc.build(story, canvasmaker=AcademicNumberedCanvas)
    return doc

def sync_and_build():
    print("Pass 1: Compiling initial PDF layout...")
    render_doc(None)
    
    reader = PdfReader(OUTPUT_PDF)
    total_pages = len(reader.pages)
    print(f"Pass 1 Total Pages: {total_pages}")
    
    # Find Chapter 1 physical start page dynamically
    FRONTMATTER_OFFSET = 9
    for p_idx in range(8, min(16, total_pages)):
        txt = (reader.pages[p_idx].extract_text() or "").lower()
        if "role and responsibility" in txt or "problem identification & feasibility study" in txt:
            FRONTMATTER_OFFSET = p_idx
            break
    print(f"Detected FRONTMATTER_OFFSET: {FRONTMATTER_OFFSET} (Chapter 1 on physical page {FRONTMATTER_OFFSET + 1})")
    AcademicNumberedCanvas.frontmatter_offset = FRONTMATTER_OFFSET
    
    pages_text = {}
    for p_idx in range(FRONTMATTER_OFFSET, total_pages):
        disp_p = p_idx + 1 - FRONTMATTER_OFFSET
        pages_text[disp_p] = reader.pages[p_idx].extract_text() or ""
        
    def find_page(query):
        norm_q = re.sub(r'\s+', ' ', query).strip().lower()
        for dp in sorted(pages_text.keys()):
            txt = pages_text[dp]
            norm_txt = re.sub(r'\s+', ' ', txt).lower()
            if norm_q in norm_txt:
                return dp
        return None

    # Query mapping for TOC, Tables, Figures
    queries = {
        # Modules & Chapters
        "CH1": "PROBLEM IDENTIFICATION & FEASIBILITY STUDY",
        "1.1": "1.1 Background and Motivation",
        "1.2": "1.2 Objectives",
        "1.3": "1.3 Identification of a Real-World Problem",
        "1.4": "1.4 Problem Justification and Scope Definition",
        "1.5": "1.5 Stakeholder Identification & Beneficiary Analysis",
        "1.6": "1.6 Feasibility Analysis (Technical, Economic",
        "CH2": "CHAPTER 2",
        "2.1": "2.1 Functional Requirements Specification",
        "2.2": "2.2 Non-Functional Requirements Specification",
        "2.3": "2.3 Use-Case Analysis & Actor Profiles",
        "2.4": "2.4 Requirement Prioritization (MoSCoW Matrix)",
        "2.5": "2.5 Constraints and Assumptions",
        "2.6": "2.6 Preliminary Product Description & Technology Stack Survey",
        "2.7": "2.7 Conceptual Models (Literature Review",
        "CH3": "SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC) PLANNING",
        "3.1": "3.1 Selection of SDLC Model",
        "3.2": "3.2 Work Breakdown Structure (WBS)",
        "3.3": "3.3 Project Timeline & Scheduling",
        "3.4": "3.4 Resource Planning (Hardware & Software",
        "CH4": "SYSTEM MODELING USING UML",
        "4.1": "4.1 Event Table (System Logic & Event Table)",
        "4.2": "4.2 Class Diagram",
        "4.3": "4.3 Use Case Diagram",
        "4.4": "4.4 Entity-Relationship (ER) & Data Flow Diagrams",
        "4.5": "4.5 Object Diagram",
        "4.6": "4.6 Sequence Diagram",
        "4.7": "4.7 Activity Diagram",
        "4.8": "4.8 Component Model",
        "4.9": "4.9 Deployment Diagram",
        "CH5": "SYSTEM ARCHITECTURE DESIGN",
        "5.1": "5.1 Frontend Architecture & Component Hierarchy",
        "5.2": "5.2 Backend Architecture & FastAPI REST API",
        "5.3": "5.3 Database Schema Design & PostgreSQL/SQLite",
        "5.4": "5.4 API Structure, Endpoints & JSON Contracts",
        "5.5": "5.5 Security Considerations & Granular Access Control",
        "5.6": "5.6 Procedural Design (A* Pathfinding",
        "MOD2": "MODULE 2",
        "CH6": "APPLICATION DEVELOPMENT",
        "6.1": "6.1 Frontend Implementation (Unity 6.3 LTS",
        "6.2": "6.2 Backend Implementation (FastAPI",
        "6.3": "6.3 Database Integration (SQLAlchemy",
        "6.4": "6.4 Authentication & Validation (Session",
        "6.5": "6.5 Error Handling & Exception Management",
        "CH7": "INTEGRATION & SYSTEM TESTING",
        "7.1": "7.1 Testing Approach & Quality Assurance Framework",
        "7.2": "7.2 Unit Testing",
        "7.3": "7.3 Black-Box Testing",
        "7.4": "7.4 Integration Testing",
        "7.5": "7.5 Beta Testing & Usability Evaluation",
        "7.6": "7.6 Comprehensive Test Case Matrix",
        "7.7": "7.7 Bug Tracking & Defect Management",
        "CH8": "DEPLOYMENT & HOSTING",
        "8.1": "8.1 Cloud Deployment & Local Hosting Architecture",
        "8.2": "8.2 Standalone Executable & WebGL Build",
        "8.3": "8.3 Server Configuration & Secure Environment Variables",
        "8.4": "8.4 Version Control using GitHub",
        "8.5": "8.5 GitHub Repository Structure",
        "8.6": "8.6 Render Cloud Web Service Deployment",
        "8.7": "8.7 Database Cloud Configuration",
        "CH9": "PERFORMANCE & SECURITY TESTING",
        "9.1": "9.1 Basic Load Testing & Latency Benchmarks",
        "9.2": "9.2 Input Validation Checks & Sanitization",
        "9.3": "9.3 Security Validation & Penetration Resistance",
        "CH10": "FINAL DOCUMENTATION / RESULT AND DISCUSSION",
        "10.1": "10.1 Technical Report & Module Deliverables Summary",
        "10.2": "10.2 User Manual & Operational Walkthrough",
        "10.3": "10.3 Application Screenshots & Visual Demonstrations",
        "10.4": "10.4 Source Code Documentation & Core Module Listings",
        "CH11": "CHAPTER 11",
        "11.1": "11.1 Significance of the System",
        "11.2": "11.2 Limitations of the System",
        "11.3": "11.3 Future Scope of the Project",
        "REFS": "REFERENCES",
        "GLOSS": "GLOSSARY",

        # Tables
        "TBL_1_1": "Table 1.1: Role and Responsibility",
        "TBL_2_1": "Table 2.1: Functional Requirements",
        "TBL_2_2": "Table 2.2: Non-Functional Requirements",
        "TBL_2_3": "Table 2.3: MoSCoW",
        "TBL_2_4": "Table 2.4: Comparative Analysis",
        "TBL_3_1": "Table 3.1: Work Breakdown Structure",
        "TBL_4_1": "Table 4.1: System Logic & Event Table",
        "TBL_5_1": "Table 5.1: SimulationSession",
        "TBL_5_2": "Table 5.2: CityMetrics",
        "TBL_5_3": "Table 5.3: ZoningGrid",
        "TBL_5_4": "Table 5.4: CitizenPetition",
        "TBL_5_5": "Table 5.5: DisasterIncident",
        "TBL_5_6": "Table 5.6: TelemetryLog",
        "TBL_5_7": "Table 5.7: REST API Endpoints",
        "TBL_7_1": "Table 7.1: Unit Testing Test Cases Log",
        "TBL_7_2": "Table 7.2: Integration Testing Test Cases Log",
        "TBL_7_3": "Table 7.3: System & Black-Box Testing Test Cases Log",
        "TBL_7_4": "Table 7.4: Bug Tracking & Defect Management Log",

        # Figures
        "FIG_3_1": "Figure 3.1: Project Schedule",
        "FIG_4_1": "Figure 4.1: Class Diagram",
        "FIG_4_2": "Figure 4.2: Use Case Diagram",
        "FIG_4_3": "Figure 4.3: Entity-Relationship",
        "FIG_4_4": "Figure 4.4: DFD Level 0",
        "FIG_4_5": "Figure 4.5: DFD Level 1",
        "FIG_4_6": "Figure 4.6: Object Diagram",
        "FIG_4_7": "Figure 4.7: Sequence Diagram",
        "FIG_4_8": "Figure 4.8: Activity Diagram",
        "FIG_4_9": "Figure 4.9: Component Diagram",
        "FIG_4_10": "Figure 4.10: Deployment Diagram",
        "FIG_5_1": "Figure 5.1: Smart City High-Level 3-Tier",
        "FIG_8_1": "Figure 8.1: Deployment Architecture",
        "FIG_10_1": "Figure 10.1: Main Menu",
        "FIG_10_2": "Figure 10.2: Secure Mayor Authentication",
        "FIG_10_3": "Figure 10.3: Mayor Registration",
        "FIG_10_4": "Figure 10.4: Municipal Founding",
        "FIG_10_5": "Figure 10.5: Real-Time 3D City Viewport",
        "FIG_10_6": "Figure 10.6: Mayor Quick-Action Dashboard",
        "FIG_10_7": "Figure 10.7: Industrial District Fire",
        "FIG_10_8": "Figure 10.8: City Decorations",
        "FIG_10_9": "Figure 10.9: 3D Spatial Map Overlays",
        "FIG_10_10": "Figure 10.10: Taxes, Revenue",
        "FIG_10_11": "Figure 10.11: Interactive Traffic Management",
        "FIG_10_12": "Figure 10.12: Multimodal Public Transit",
        "FIG_10_13": "Figure 10.13: Electricity Grid Capacity",
        "FIG_10_14": "Figure 10.14: Water Reservoir",
        "FIG_10_15": "Figure 10.15: Waste Management",
        "FIG_10_16": "Figure 10.16: Healthcare Infrastructure",
        "FIG_10_17": "Figure 10.17: Education Quality Index",
        "FIG_10_18": "Figure 10.18: Public Safety",
        "FIG_10_19": "Figure 10.19: Environmental Sustainability",
        "FIG_10_20": "Figure 10.20: Citizen Petitions",
    }
    
    synced_dict = {}
    for k, q in queries.items():
        found = find_page(q)
        if found:
            synced_dict[k] = found
        else:
            print(f"Notice: Could not locate page for query: '{q}' (key: {k})")

    print("\nPass 2: Rebuilding final PDF with synchronized Table of Contents & Indexes...")
    render_doc(synced_dict)
    
    final_reader = PdfReader(OUTPUT_PDF)
    final_count = len(final_reader.pages)
    print(f"\n=======================================================")
    print(f"SUCCESS! SMART CITY MANAGEMENT SIMULATOR BLACK BOOK GENERATED!")
    print(f"File Location: {OUTPUT_PDF}")
    print(f"Total Page Count: {final_count} pages")
    print(f"=======================================================")
    return final_count

if __name__ == '__main__':
    sync_and_build()
