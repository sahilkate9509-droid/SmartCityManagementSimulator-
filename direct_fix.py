# 1. content_chapters_1_3.py line 859
with open('content_chapters_1_3.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 859 (0-indexed 858):
for idx, line in enumerate(lines):
    if 'documentation""' in line:
        lines[idx] = line.replace('documentation""', 'documentation -- "')

with open('content_chapters_1_3.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# 2. content_chapters_4_5.py lines 49-60
with open('content_chapters_4_5.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'def build_schema_table(cols, rows):' in line:
        # Re-indent the entire build_schema_table function
        func_lines = [
            '    def build_schema_table(cols, rows):\n',
            '        tdata = [[Paragraph(f"<b>{c}</b>", styles[\'TableHead\']) for c in cols]]\n',
            '        for r in rows:\n',
            '            row_cells = []\n',
            '            for i, val in enumerate(r):\n',
            '                if i == 0:\n',
            '                    row_cells.append(Paragraph(f"<b>{val}</b>", styles[\'TableCellBold\']))\n',
            '                else:\n',
            '                    row_cells.append(Paragraph(val, styles[\'TableCell\']))\n',
            '            tdata.append(row_cells)\n',
            '        t = Table(tdata, colWidths=[100, 85, 60, 50, 195])\n'
        ]
        # Replace the 12 lines from idx to idx+11
        lines[idx:idx+11] = func_lines
        break

with open('content_chapters_4_5.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# 3. content_chapters_6_8.py lines 656-660
with open('content_chapters_6_8.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'for rf in refs:' in line:
        lines[idx] = '    for rf in refs:\n'
        lines[idx+1] = "        elements.append(Paragraph(rf, styles['AcademicBody']))\n"
        lines[idx+2] = '        elements.append(Spacer(1, 3))\n'
        break

with open('content_chapters_6_8.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# 4. content_frontmatter.py lines 326-331
with open('content_frontmatter.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if 'for ttitle, tpage in tables_list:' in line:
        loop_lines = [
            '    for ttitle, tpage in tables_list:\n',
            '        tbl_table_data.append([\n',
            '            Paragraph(f"<b>{ttitle.split(\':\')[0]}:</b> {ttitle.split(\':\', 1)[1].strip()}", styles[\'TableCell\']),\n',
            '            Paragraph(f"<b>{tpage}</b>", styles[\'TableCellBold\'])\n',
            '        ])\n'
        ]
        lines[idx:idx+5] = loop_lines
        break

with open('content_frontmatter.py', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Direct line replacements applied.")
