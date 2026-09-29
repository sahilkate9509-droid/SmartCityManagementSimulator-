# 1. content_chapters_1_3.py
with open('content_chapters_1_3.py', 'r', encoding='utf-8') as f:
    text = f.read()

target1 = """        for rid, rdesc, rpri in fr_rows:
        t_data.append([
        Paragraph(f"<b>{rid}</b>", styles['TableCellBold']),
        Paragraph(rdesc, styles['TableCell']),
        Paragraph(f"<b>{rpri}</b>", styles['TableCell'])
        ])"""

replace1 = """        for rid, rdesc, rpri in fr_rows:
            t_data.append([
                Paragraph(f"<b>{rid}</b>", styles['TableCellBold']),
                Paragraph(rdesc, styles['TableCell']),
                Paragraph(f"<b>{rpri}</b>", styles['TableCell'])
            ])"""

text = text.replace(target1, replace1)
with open('content_chapters_1_3.py', 'w', encoding='utf-8') as f:
    f.write(text)

# 2. content_chapters_4_5.py
with open('content_chapters_4_5.py', 'r', encoding='utf-8') as f:
    text = f.read()

target2 = """    for cname, ctype, ctarget, crule in dic_rows:
    tdata_dic.append([
    Paragraph(f"<b>{cname}</b>", styles['TableCellBold']),
    Paragraph(ctype, styles['TableCell']),
    Paragraph(ctarget, styles['TableCell']),
    Paragraph(crule, styles['TableCell'])
    ])"""

replace2 = """    for cname, ctype, ctarget, crule in dic_rows:
        tdata_dic.append([
            Paragraph(f"<b>{cname}</b>", styles['TableCellBold']),
            Paragraph(ctype, styles['TableCell']),
            Paragraph(ctarget, styles['TableCell']),
            Paragraph(crule, styles['TableCell'])
        ])"""

text = text.replace(target2, replace2)
with open('content_chapters_4_5.py', 'w', encoding='utf-8') as f:
    f.write(text)

# 3. content_frontmatter.py
with open('content_frontmatter.py', 'r', encoding='utf-8') as f:
    text = f.read()

target3 = """    for ftitle, fpage in figures_list:
    fig_table_data.append([
    Paragraph(f"<b>{ftitle.split(':')[0]}:</b> {ftitle.split(':', 1)[1].strip()}", styles['TableCell']),
    Paragraph(f"<b>{fpage}</b>", styles['TableCellBold'])
    ])"""

replace3 = """    for ftitle, fpage in figures_list:
        fig_table_data.append([
            Paragraph(f"<b>{ftitle.split(':')[0]}:</b> {ftitle.split(':', 1)[1].strip()}", styles['TableCell']),
            Paragraph(f"<b>{fpage}</b>", styles['TableCellBold'])
        ])"""

text = text.replace(target3, replace3)
with open('content_frontmatter.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied 3 final fixes.")
