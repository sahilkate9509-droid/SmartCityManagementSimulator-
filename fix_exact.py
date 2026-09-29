# 1. Fix content_chapters_1_3.py line 859
with open('content_chapters_1_3.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    'Language (UML) diagrams (Figures 3 through 8). These diagrams -- derived from the formal system engineering documentation""\n"delineate',
    'Language (UML) diagrams (Figures 3 through 8). These diagrams -- derived from the formal system engineering documentation -- "\n"delineate'
)
# Also remove duplicate header # 3.6.2.1 Use Case Diagram right before 3.6.2.4 Class Diagram
text = text.replace(
    '    # 3.6.2.1 Use Case Diagram\n    elements.append(Paragraph("3.6.2.1 Use Case Diagram", styles[\'SecHeading3\']))\n    # 3.6.2.4 Class Diagram',
    '    # 3.6.2.4 Class Diagram'
)

with open('content_chapters_1_3.py', 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Fix content_chapters_4_5.py lines 52-59
with open('content_chapters_4_5.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line == '    row_cells = []\n':
        new_lines.append('        row_cells = []\n')
    elif line == '    for i, val in enumerate(r):\n':
        new_lines.append('        for i, val in enumerate(r):\n')
    elif line == '    if i == 0:\n':
        new_lines.append('            if i == 0:\n')
    elif line == '    row_cells.append(Paragraph(f"<b>{val}</b>", styles[\'TableCellBold\']))\n':
        new_lines.append('                row_cells.append(Paragraph(f"<b>{val}</b>", styles[\'TableCellBold\']))\n')
    elif line == '    else:\n':
        new_lines.append('            else:\n')
    elif line == "    row_cells.append(Paragraph(val, styles['TableCell']))\n":
        new_lines.append("                row_cells.append(Paragraph(val, styles['TableCell']))\n")
    elif line == '    tdata.append(row_cells)\n':
        new_lines.append('        tdata.append(row_cells)\n')
    else:
        new_lines.append(line)

with open('content_chapters_4_5.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# 3. Fix content_chapters_6_8.py refs loop
with open('content_chapters_6_8.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if line == "elements.append(Paragraph(rf, styles['AcademicBody']))\n":
        new_lines.append("    elements.append(Paragraph(rf, styles['AcademicBody']))\n")
    elif line == "elements.append(Spacer(1, 3))\n":
        new_lines.append("    elements.append(Spacer(1, 3))\n")
    else:
        new_lines.append(line)

with open('content_chapters_6_8.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# 4. Fix content_frontmatter.py tables loop
with open('content_frontmatter.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_tables_loop = False
for i, line in enumerate(lines):
    if 'for ttitle, tpage in tables_list:' in line:
        in_tables_loop = True
        new_lines.append(line)
        continue
    if in_tables_loop:
        if line.startswith('    tbl_table_data.append(['):
            new_lines.append('        tbl_table_data.append([\n')
        elif line.startswith('    Paragraph(f"<b>{ttitle.split'):
            new_lines.append('            ' + line.strip() + '\n')
        elif line.startswith('    Paragraph(f"<b>{tpage}</b>"'):
            new_lines.append('            ' + line.strip() + '\n')
        elif line.startswith('    ])'):
            new_lines.append('        ])\n')
            in_tables_loop = False
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open('content_frontmatter.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Exact fixes applied.")
