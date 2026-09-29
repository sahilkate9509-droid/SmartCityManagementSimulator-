import re

# 1. content_chapters_1_3.py
with open('content_chapters_1_3.py', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Replace any quote followed immediately by lowercase/uppercase letter within text strings
text = text.replace('concepts"such', 'concepts—such')
text = text.replace('dispersion"into', 'dispersion—into')
text = text.replace('sandbox"a true', 'sandbox—a true')
text = text.replace('degradation"to', 'degradation—to')
text = text.replace('simultaneously"such', 'simultaneously—such')
text = text.replace('', '—') # replace any leftover replacement chars with em-dash or bullet

with open('content_chapters_1_3.py', 'w', encoding='utf-8') as f:
    f.write(text)

# 2. content_chapters_4_5.py
with open('content_chapters_4_5.py', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

text = text.replace('', '—')
# Fix build_schema_table indentation
old_func = """def build_schema_table(cols, rows):
    tdata = [[Paragraph(f"<b>{c}</b>", styles['TableHead']) for c in cols]]
    for r in rows:
    row_cells = []
    for i, val in enumerate(r):
    if i == 0:
    row_cells.append(Paragraph(f"<b>{val}</b>", styles['TableCellBold']))
    else:
    row_cells.append(Paragraph(val, styles['TableCell']))
    tdata.append(row_cells)
    t = Table(tdata, colWidths=[100, 85, 60, 50, 195])"""

new_func = """def build_schema_table(cols, rows):
    tdata = [[Paragraph(f"<b>{c}</b>", styles['TableHead']) for c in cols]]
    for r in rows:
        row_cells = []
        for i, val in enumerate(r):
            if i == 0:
                row_cells.append(Paragraph(f"<b>{val}</b>", styles['TableCellBold']))
            else:
                row_cells.append(Paragraph(val, styles['TableCell']))
        tdata.append(row_cells)
    t = Table(tdata, colWidths=[100, 85, 60, 50, 195])"""

text = text.replace(old_func, new_func)

with open('content_chapters_4_5.py', 'w', encoding='utf-8') as f:
    f.write(text)

# 3. content_chapters_6_8.py
with open('content_chapters_6_8.py', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

text = text.replace('', '—')
text = text.replace('degradation"to', 'degradation—to')
text = text.replace('simultaneously"such', 'simultaneously—such')

old_refs_loop = """for rf in refs:
elements.append(Paragraph(rf, styles['AcademicBody']))
elements.append(Spacer(1, 3))"""

new_refs_loop = """for rf in refs:
    elements.append(Paragraph(rf, styles['AcademicBody']))
    elements.append(Spacer(1, 3))"""

text = text.replace(old_refs_loop, new_refs_loop)

# Also check any other loops
old_glossary_loop = """for term, defn in glossary:
elements.append(Paragraph(f"<b>{term}:</b> {defn}", styles['AcademicBody']))
elements.append(Spacer(1, 3))"""

new_glossary_loop = """for term, defn in glossary:
    elements.append(Paragraph(f"<b>{term}:</b> {defn}", styles['AcademicBody']))
    elements.append(Spacer(1, 3))"""

text = text.replace(old_glossary_loop, new_glossary_loop)

with open('content_chapters_6_8.py', 'w', encoding='utf-8') as f:
    f.write(text)

# 4. content_frontmatter.py
with open('content_frontmatter.py', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

text = text.replace('', '—')

old_front_loop = """    for ttitle, tpage in tables_list:
    tbl_table_data.append([
    Paragraph(f"<b>{ttitle.split(':')[0]}:</b> {ttitle.split(':', 1)[1].strip()}", styles['TableCell']),
    Paragraph(f"<b>{tpage}</b>", styles['TableCellBold'])
    ])"""

new_front_loop = """    for ttitle, tpage in tables_list:
        tbl_table_data.append([
            Paragraph(f"<b>{ttitle.split(':')[0]}:</b> {ttitle.split(':', 1)[1].strip()}", styles['TableCell']),
            Paragraph(f"<b>{tpage}</b>", styles['TableCellBold'])
        ])"""

text = text.replace(old_front_loop, new_front_loop)

with open('content_frontmatter.py', 'w', encoding='utf-8') as f:
    f.write(text)

# Fix BOM in files that have U+FEFF
for fn in ['apply_student_details.py', 'update_toc_split.py', 'verify_pages.py']:
    try:
        with open(fn, 'r', encoding='utf-8-sig') as f:
            c = f.read()
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(c)
    except Exception as e:
        print(f"BOM fix error on {fn}: {e}")

print("Repair all executed.")
