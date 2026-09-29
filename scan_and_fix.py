import ast
import glob
import re

# 1. Fix content_chapters_1_3.py
fname = 'content_chapters_1_3.py'
with open(fname, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('sandbox"a true', 'sandbox—a true')
text = text.replace('peripheriesa', 'peripheries—a')
text = text.replace('peripheries"a', 'peripheries—a')

with open(fname, 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Fix content_chapters_4_5.py
fname = 'content_chapters_4_5.py'
with open(fname, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_helper = False
for i, line in enumerate(lines):
    if 'def build_schema_table(cols, rows):' in line:
        in_helper = True
        new_lines.append(line)
        continue
    if in_helper and 'def ' in line and not 'build_schema_table' in line:
        in_helper = False
    
    if in_helper:
        # Check indentation of lines inside build_schema_table
        if line.startswith('    for r in rows:'):
            new_lines.append(line)
        elif line.startswith('    row_cells = []'):
            new_lines.append('        row_cells = []\n')
        elif line.startswith('    for i, val in enumerate(r):'):
            new_lines.append('        for i, val in enumerate(r):\n')
        elif line.startswith('    if i == 0:'):
            new_lines.append('            if i == 0:\n')
        elif line.startswith('    row_cells.append(Paragraph(f"<b>{val}</b>", styles[\'TableCellBold\']))'):
            new_lines.append('                row_cells.append(Paragraph(f"<b>{val}</b>", styles[\'TableCellBold\']))\n')
        elif line.startswith('    else:'):
            new_lines.append('            else:\n')
        elif line.startswith('    row_cells.append(Paragraph(val, styles[\'TableCell\']))'):
            new_lines.append('                row_cells.append(Paragraph(val, styles[\'TableCell\']))\n')
        elif line.startswith('    tdata.append(row_cells)'):
            new_lines.append('        tdata.append(row_cells)\n')
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

with open(fname, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

# 3. Fix content_chapters_6_8.py
fname = 'content_chapters_6_8.py'
with open(fname, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('degradation"to', 'degradation—to')
text = text.replace('simultaneouslysuch', 'simultaneously—such')
text = text.replace('degradationto', 'degradation—to')

with open(fname, 'w', encoding='utf-8') as f:
    f.write(text)

# 4. Fix content_frontmatter.py
fname = 'content_frontmatter.py'
with open(fname, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if line.startswith('    for ttitle, tpage in tables_list:'):
        new_lines.append(line)
    elif line.startswith('    tbl_table_data.append(['):
        new_lines.append('        tbl_table_data.append([\n')
    elif line.startswith('    Paragraph(f"<b>{ttitle.split(\':\')[0]}:</b>'):
        new_lines.append('            ' + line.strip() + '\n')
    elif line.startswith('    Paragraph(f"<b>{tpage}</b>"'):
        new_lines.append('            ' + line.strip() + '\n')
    elif line.startswith('    ])') and len(lines) > i-3 and 'tables_list' in lines[i-4]:
        new_lines.append('        ])\n')
    else:
        new_lines.append(line)

with open(fname, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Scan and fix applied.")
