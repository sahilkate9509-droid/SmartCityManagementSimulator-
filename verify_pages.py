import pypdf

pdf_path = r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional\Smart_City_Management_Simulator_Black_Book.pdf"
reader = pypdf.PdfReader(pdf_path)
print(f"Total pages: {len(reader.pages)}")

check_pages = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 74]
for p in check_pages:
    txt = reader.pages[p-1].extract_text()
    first_lines = "\n".join([line.strip() for line in txt.split("\n") if line.strip()][:5])
    print(f"--- Page {p} ---")
    print(first_lines)
    print()
