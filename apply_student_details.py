import os
import re

base_dir = r"c:\Users\sahilabc\OneDrive\Desktop\sahil\SmartCityManagementSimulator_Professional"

# 1. Update content_frontmatter.py
frontmatter_path = os.path.join(base_dir, "content_frontmatter.py")
with open(frontmatter_path, "r", encoding="utf-8") as f:
    txt = f.read()

txt = txt.replace("Mr. SAHIL VISHAL KATE", "Ms. SHARAVNI LAXMAN GHODE")
txt = txt.replace("Mr. Sahil Vishal Kate.", "Ms. Sharavni Laxman Ghode.")
txt = txt.replace("SAHIL VISHAL KATE", "SHARAVNI LAXMAN GHODE")
txt = txt.replace("Sahil Vishal Kate", "Sharavni Laxman Ghode")
txt = txt.replace("PROF. AARTI GAWAI", "PROF. PRANALI CHOUDARI")
txt = txt.replace("Prof. Aarti Gawai", "Prof. Pranali Choudari")
txt = txt.replace("9041", "9022")

with open(frontmatter_path, "w", encoding="utf-8") as f:
    f.write(txt)
print("Updated content_frontmatter.py successfully!")

# 2. Update content_chapters_4_5.py
ch45_path = os.path.join(base_dir, "content_chapters_4_5.py")
with open(ch45_path, "r", encoding="utf-8") as f:
    txt = f.read()

txt = txt.replace("Sahil Vishal Kate, Roll No. 9041", "Sharavni Laxman Ghode, Roll No. 9022")
txt = txt.replace("Prof. Aarti Gawai", "Prof. Pranali Choudari")

with open(ch45_path, "w", encoding="utf-8") as f:
    f.write(txt)
print("Updated content_chapters_4_5.py successfully!")

# 3. Update content_chapters_6_8.py
ch68_path = os.path.join(base_dir, "content_chapters_6_8.py")
with open(ch68_path, "r", encoding="utf-8") as f:
    txt = f.read()

txt = txt.replace("S. V. Kate and A. Gawai", "S. L. Ghode and P. Choudari")

with open(ch68_path, "w", encoding="utf-8") as f:
    f.write(txt)
print("Updated content_chapters_6_8.py successfully!")

# 4. Update Smart_City_Management_Simulator_Test_Cases.csv
csv_path = os.path.join(base_dir, "Smart_City_Management_Simulator_Test_Cases.csv")
if os.path.exists(csv_path):
    with open(csv_path, "r", encoding="utf-8") as f:
        txt = f.read()
    txt = txt.replace("Mayor: 'Sahil Kate'", "Mayor: 'Sharavni Ghode'")
    with open(csv_path, "w", encoding="utf-8") as f:
        f.write(txt)
    print("Updated Smart_City_Management_Simulator_Test_Cases.csv successfully!")

# 5. Update generate_all_figures.py
gen_all_fig_path = os.path.join(base_dir, "generate_all_figures.py")
if os.path.exists(gen_all_fig_path):
    with open(gen_all_fig_path, "r", encoding="utf-8") as f:
        txt = f.read()
    txt = txt.replace("Mayor: Sahil Kate", "Mayor: Sharavni Ghode")
    with open(gen_all_fig_path, "w", encoding="utf-8") as f:
        f.write(txt)
    print("Updated generate_all_figures.py successfully!")

# 6. Update generate_syllabus_figures.py
gen_syl_path = os.path.join(base_dir, "generate_syllabus_figures.py")
if os.path.exists(gen_syl_path):
    with open(gen_syl_path, "r", encoding="utf-8") as f:
        txt = f.read()
    txt = txt.replace('"SK"', '"SG"')
    txt = txt.replace("SAHIL VISHAL KATE", "SHARAVNI LAXMAN GHODE")
    txt = txt.replace("Sahil Vishal Kate", "Sharavni Laxman Ghode")
    txt = txt.replace("sahil_kate_9041", "sharavni_ghode_9022")
    txt = txt.replace("sahil.kate@ruparel.edu", "sharavni.ghode@ruparel.edu")
    txt = txt.replace("Prof. Aarti Gawai", "Prof. Pranali Choudari")
    txt = txt.replace("9041", "9022")
    with open(gen_syl_path, "w", encoding="utf-8") as f:
        f.write(txt)
    print("Updated generate_syllabus_figures.py successfully!")

