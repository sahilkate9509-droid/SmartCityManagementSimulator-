import pypdf
import re

pdf_path = 'Smart_City_Management_Simulator_Black_Book.pdf'
reader = pypdf.PdfReader(pdf_path)
total_pages = len(reader.pages)
print(f"Total pages in PDF: {total_pages}")

# Map physical page to text content (starting from page 11 = displayed page 1)
pages_text = {}
for p in range(10, total_pages):
    displayed_p = p + 1 - 10
    pages_text[displayed_p] = reader.pages[p].extract_text()

def find_first_page(query):
    for dp in sorted(pages_text.keys()):
        txt = pages_text[dp]
        # normalize spaces
        norm_txt = re.sub(r'\s+', ' ', txt)
        norm_q = re.sub(r'\s+', ' ', query)
        if norm_q.lower() in norm_txt.lower():
            return dp
    return None

# Find all TOC sections
toc_queries = [
    ("CHAPTER 1: INTRODUCTION", "CHAPTER 1: INTRODUCTION"),
    ("1.1 Background", "1.1 Background"),
    ("1.2 Objectives", "1.2 Objectives"),
    ("1.3 Purpose, Scope and Applicability", "1.3 Purpose, Scope and Applicability"),
    ("1.3.1 Purpose", "1.3.1 Purpose"),
    ("1.3.2 Scope", "1.3.2 Scope"),
    ("1.3.3 Applicability", "1.3.3 Applicability"),
    ("1.4 Achievements", "1.4 Achievements"),
    ("1.5 Organization of Report", "1.5 Organization of Report"),
    ("CHAPTER 2: SURVEY OF TECHNOLOGIES", "CHAPTER 2: SURVEY OF TECHNOLOGIES"),
    ("2.1 Front-End", "2.1 Front-End"),
    ("2.2 Back-End", "2.2 Back-End"),
    ("2.3 Languages", "2.3 Languages"),
    ("2.4 INTEGRATED DEVELOPMENT ENVIRONMENT", "2.4 INTEGRATED DEVELOPMENT ENVIRONMENT"),
    ("2.5 Justification for Technologies Used", "2.5 Justification for Technologies Used"),
    ("CHAPTER 3: REQUIREMENTS AND ANALYSIS", "CHAPTER 3: REQUIREMENTS AND ANALYSIS"),
    ("3.1 Problem Definition", "3.1 Problem Definition"),
    ("3.2 Requirements Specification", "3.2 Requirements Specification"),
    ("3.2.1 Functional Requirements", "3.2.1 Functional Requirements"),
    ("3.2.2 Non-Functional Requirements", "3.2.2 Non-Functional Requirements"),
    ("3.3 Planning and Scheduling", "3.3 Planning and Scheduling"),
    ("3.4 Software and Hardware Requirements", "3.4 Software and Hardware Requirements"),
    ("3.5 Preliminary Product Description", "3.5 Preliminary Product Description"),
    ("3.6 Conceptual Models", "3.6 Conceptual Models"),
    ("3.6.1 Data Flow Diagram", "3.6.1 Data Flow Diagram"),
    ("3.6.2 Entity-Relationship (ER) Diagram", "3.6.2 Entity-Relationship (ER) Diagram"),
    ("3.6.3 Event Table", "3.6.3 Event Table"),
    ("3.6.4 UML Diagrams", "3.6.4 UML Diagrams"),
    ("3.6.4.1 Use Case Diagram", "3.6.4.1 Use Case Diagram"),
    ("3.6.4.2 Activity Diagram", "3.6.4.2 Activity Diagram"),
    ("3.6.4.3 Sequence Diagram", "3.6.4.3 Sequence Diagram"),
    ("3.6.4.4 Class Diagram", "3.6.4.4 Class Diagram"),
    ("3.6.4.5 Object Diagram", "3.6.4.5 Object Diagram"),
    ("3.6.4.6 Deployment Diagram", "3.6.4.6 Deployment Diagram"),
    ("CHAPTER 4: SYSTEM DESIGN", "CHAPTER 4: SYSTEM DESIGN"),
    ("4.1 Basic Modules:", "4.1 Basic Modules:"),
    ("4.2 Data Design:", "4.2 Data Design:"),
    ("4.2.1 schema Design", "4.2.1 schema Design"),
    ("4.2.1.1 User Table", "4.2.1.1 User Table"),
    ("4.2.1.2 SignLanguageGestures Table", "4.2.1.2 SignLanguageGestures Table"),
    ("4.2.1.3 TranslationLogs Table", "4.2.1.3 TranslationLogs Table"),
    ("4.2.1.4 TranslationSessions Table", "4.2.1.4 TranslationSessions Table"),
    ("4.2.1.5 Saved_phrases Table", "4.2.1.5 Saved_phrases Table"),
    ("4.2.1.6 Tickets Table", "4.2.1.6 Tickets Table"),
    ("4.2.1.7 History", "4.2.1.7 History"),
    ("4.2.1.8 SystemEvents Table", "4.2.1.8 SystemEvents Table"),
    ("4.3 Procedural Design:", "4.3 Procedural Design:"),
    ("4.3.1 Logic Diagram:", "4.3.1 Logic Diagram:"),
    ("4.3.2 Data Structure:", "4.3.2 Data Structure:"),
    ("4.3.3 Algorithms Design", "4.3.3 Algorithms Design"),
    ("4.4 User Interface Design", "4.4 User Interface Design"),
    ("4.5 Security Issues", "4.5 Security Issues"),
    ("4.6 Test Case Design", "4.6 Test Case Design"),
    ("CHAPTER 5: IMPLEMENTATION AND TESTING", "CHAPTER 5: IMPLEMENTATION AND TESTING"),
    ("5.1 Implementation Approaches", "5.1 Implementation Approaches"),
    ("5.2 Coding Details and Code Efficiency", "5.2 Coding Details and Code Efficiency"),
    ("5.2.1 Code Efficiency", "5.2.1 Code Efficiency"),
    ("5.3 Testing Approach", "5.3 Testing Approach"),
    ("5.3.1 Unit Testing", "5.3.1 Unit Testing"),
    ("5.3.2 Integrated Testing", "5.3.2 Integrated Testing"),
    ("5.3.3 Beta Testing (User Acceptance Testing)", "5.3.3 Beta Testing (User Acceptance Testing)"),
    ("5.4 Modifications and Improvements", "5.4 Modifications and Improvements"),
    ("5.5 Test Cases", "5.5 Test Cases"),
    ("CHAPTER 6: RESULTS AND DISCUSSION", "CHAPTER 6: RESULTS AND DISCUSSION"),
    ("6.1 Test Reports", "6.1 Test Reports"),
    ("6.2 User Documentation", "6.2 User Documentation"),
    ("CHAPTER 7: CONCLUSION", "CHAPTER 7: CONCLUSION"),
    ("7.1 Conclusion", "7.1 Conclusion"),
    ("7.1.1 Significance of the System", "7.1.1 Significance of the System"),
    ("7.2 Limitations of the System", "7.2 Limitations of the System"),
    ("7.3 Future Scope of the Project", "7.3 Future Scope of the Project"),
    ("REFERENCES", "REFERENCES"),
    ("GLOSSARY", "GLOSSARY"),
]

print("\n--- TOC SECTIONS ---")
toc_results = {}
for label, q in toc_queries:
    p = find_first_page(q)
    toc_results[label] = p
    print(f"{label} -> Page {p}")

print("\n--- FIGURES LIST ---")
fig_queries = [
    ("Figure 1: Gantt Chart", "Figure 1: Gantt Chart"),
    ("Figure 2: Agile Model", "Figure 2: Agile Model"),
    ("Figure 3: Data Flow Diagram", "Figure 3: Data Flow Diagram"),
    ("Figure 4: E-R Diagram", "Figure 4: E-R Diagram"),
    ("Figure 5: Event Table", "Figure 5: Event Table"),
    ("Figure 6: Use Case Diagram", "Figure 6: Use Case Diagram"),
    ("Figure 7: Activity Diagram", "Figure 7: Activity Diagram"),
    ("Figure 8: Sequence Diagram", "Figure 8: Sequence Diagram"),
    ("Figure 9: Class Diagram", "Figure 9: Class Diagram"),
    ("Figure 10: Object Diagram", "Figure 10: Object Diagram"),
    ("Figure 11: Deployment Diagram", "Figure 11: Deployment Diagram"),
    ("Figure 12: Logic Diagram", "Figure 12: Logic Diagram"),
    ("Figure 13: UI Page", "Figure 13: UI Page"),
    ("Figure 14: Profile Page", "Figure 14: Profile Page"),
    ("Figure 15: Translation Log/ History", "Figure 15: Translation Log/ History"),
    ("Figure 16: About us Page", "Figure 16: About us Page"),
    ("Figure 17: Login Page", "Figure 17: Login Page"),
    ("Figure 18: Register Page", "Figure 18: Register Page"),
    ("Figure 19: Dashboard Page", "Figure 19: Dashboard Page"),
    ("Figure 20: ASL Guide Page", "Figure 20: ASL Guide Page"),
    ("Figure 21: History Page", "Figure 21: History Page"),
    ("Figure 22: SavedPhrases Page", "Figure 22: SavedPhrases Page"),
    ("Figure 23: Setting Page", "Figure 23: Setting Page"),
    ("Figure 24: Profile Page", "Figure 24: Profile Page"),
    ("Figure 25: Admin Panel Page", "Figure 25: Admin Panel Page"),
]

fig_results = {}
for label, q in fig_queries:
    if label == "Figure 25: Profile Page":
        for dp in sorted(pages_text.keys()):
            if dp >= 35 and "figure 25: profile page" in pages_text[dp].lower():
                fig_results[label] = dp
                print(f"{label} -> Page {dp}")
                break
    else:
        p = find_first_page(q)
        fig_results[label] = p
        print(f"{label} -> Page {p}")

print("\n--- TABLES LIST ---")
tbl_queries = [
    ("Table 1: Pert Chart", "Table 1: Pert Chart"),
    ("Table 2: Event Table", "Table 2: Event Table"),
    ("Table 3: User schema", "Table 3: User schema"),
    ("Table 4: SignLanguageGestures Schema", "Table 4: SignLanguageGestures Schema"),
    ("Table 5: TranslationLogs Schema", "Table 5: TranslationLogs Schema"),
    ("Table 6: TranslationSessions Schema", "Table 6: TranslationSessions Schema"),
    ("Table 7: Saved_phrases", "Table 7: Saved_phrases"),
    ("Table 8: Tickets Schema", "Table 8: Tickets Schema"),
    ("Table 9: History Schema", "Table 9: History Schema"),
    ("Table 10: SystemEvents", "Table 10: SystemEvents"),
    ("Table 11: Data Integrity and Constraints", "Table 11: Data Integrity and Constraints"),
    ("Table 12: Test Case Table", "Table 12: Test Case Table"),
    ("Table 13: Test Cases", "Table 13: Test Cases"),
    ("Table 14: Test Reports", "Table 14: Test Reports"),
]

tbl_results = {}
for label, q in tbl_queries:
    p = find_first_page(q)
    tbl_results[label] = p
    print(f"{label} -> Page {p}")
