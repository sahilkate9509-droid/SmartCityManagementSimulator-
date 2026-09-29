import ast

# 1. content_chapters_1_3.py
with open('content_chapters_1_3.py', 'r', encoding='utf-8') as f:
    raw = f.read()

# Let's fix content_chapters_1_3.py:
# We know the specific loops and ifs in content_chapters_1_3.py:
# L118: for ob in p_spec_objs:
# L478: def make_fr_table(...)
# L515, L529, L543, L557, L571, L585: for el in make_fr_table(...)
# L646: if os.path.exists(gantt_path):
# L709: if os.path.exists(agile_path):
# L874: if os.path.exists(cls_path):
# L930: if os.path.exists(obj_path):
# L985: if os.path.exists(uc_path):
# L1041: if os.path.exists(seq_path):
# L1101: if os.path.exists(act_path):
# L1157: if os.path.exists(dep_path):

lines = raw.splitlines(keepends=True)
fixed_1_3 = []
in_spec_objs = False
in_fr_table = False
in_fr_subloop = False
in_img_if = 0

for i, line in enumerate(lines):
    stripped = line.strip()
    if line.startswith('import ') or line.startswith('from ') or line.startswith('def build_chapters_1_3'):
        fixed_1_3.append(line)
        continue
    
    # Handle make_fr_table
    if stripped.startswith('def make_fr_table'):
        in_fr_table = True
        fixed_1_3.append('    ' + stripped + '\n')
        continue
    if in_fr_table:
        if stripped.startswith('for rid, rdesc, rpri in fr_rows:'):
            in_fr_subloop = True
            fixed_1_3.append('        ' + stripped + '\n')
            continue
        if in_fr_subloop:
            if stripped.startswith('t_fr_data.append(') or stripped.startswith('Paragraph(') or stripped == '])':
                fixed_1_3.append('            ' + stripped + '\n')
                if stripped == '])':
                    in_fr_subloop = False
                continue
            else:
                in_fr_subloop = False
        if stripped.startswith('return '):
            fixed_1_3.append('        ' + stripped + '\n')
            in_fr_table = False
            continue
        fixed_1_3.append('        ' + stripped + '\n')
        continue
    
    # Handle for ob in p_spec_objs:
    if stripped.startswith('for ob in p_spec_objs:'):
        in_spec_objs = True
        fixed_1_3.append('    ' + stripped + '\n')
        continue
    if in_spec_objs:
        if stripped.startswith('elements.append('):
            fixed_1_3.append('        ' + stripped + '\n')
            continue
        else:
            in_spec_objs = False
            
    # Handle for el in make_fr_table(...):
    if stripped.startswith('for el in make_fr_table('):
        fixed_1_3.append('    ' + stripped + '\n')
        fixed_1_3.append('        elements.append(el)\n')
        continue
    if stripped == 'elements.append(el)' and i > 0 and 'make_fr_table' in lines[i-1]:
        continue # handled above
        
    # Handle if os.path.exists(...):
    if stripped.startswith('if os.path.exists('):
        in_img_if = 3 # next 3 lines are in if block
        fixed_1_3.append('    ' + stripped + '\n')
        continue
    if in_img_if > 0:
        if stripped.startswith('elements.append('):
            fixed_1_3.append('        ' + stripped + '\n')
            in_img_if -= 1
            continue
        else:
            in_img_if = 0

    if stripped:
        fixed_1_3.append('    ' + stripped + '\n')
    else:
        fixed_1_3.append('\n')

with open('content_chapters_1_3.py', 'w', encoding='utf-8') as f:
    f.writelines(fixed_1_3)

print("content_chapters_1_3.py normalized.")

# 2. content_chapters_4_5.py
with open('content_chapters_4_5.py', 'r', encoding='utf-8') as f:
    raw = f.read()

lines = raw.splitlines(keepends=True)
fixed_4_5 = []
in_schema = False
in_schema_r = False
in_schema_i = False
in_if = 0
in_dic = False

for i, line in enumerate(lines):
    stripped = line.strip()
    if line.startswith('import ') or line.startswith('from ') or line.startswith('def build_chapters_4_5'):
        fixed_4_5.append(line)
        continue
    
    if stripped.startswith('def build_schema_table'):
        in_schema = True
        fixed_4_5.append('    ' + stripped + '\n')
        continue
    if in_schema:
        if stripped.startswith('for r in rows:'):
            in_schema_r = True
            fixed_4_5.append('        ' + stripped + '\n')
            continue
        if in_schema_r:
            if stripped.startswith('row_cells = []'):
                fixed_4_5.append('            ' + stripped + '\n')
                continue
            if stripped.startswith('for i, val in enumerate(r):'):
                in_schema_i = True
                fixed_4_5.append('            ' + stripped + '\n')
                continue
            if in_schema_i:
                if stripped.startswith('if i == 0:'):
                    fixed_4_5.append('                ' + stripped + '\n')
                    continue
                if stripped.startswith('row_cells.append(Paragraph(f"<b>{val}</b>"'):
                    fixed_4_5.append('                    ' + stripped + '\n')
                    continue
                if stripped.startswith('else:'):
                    fixed_4_5.append('                ' + stripped + '\n')
                    continue
                if stripped.startswith('row_cells.append(Paragraph(val'):
                    fixed_4_5.append('                    ' + stripped + '\n')
                    in_schema_i = False
                    continue
            if stripped.startswith('tdata.append(row_cells)'):
                in_schema_r = False
                fixed_4_5.append('            ' + stripped + '\n')
                continue
        if stripped.startswith('return t'):
            fixed_4_5.append('        ' + stripped + '\n')
            in_schema = False
            continue
        fixed_4_5.append('        ' + stripped + '\n')
        continue
    
    if stripped.startswith('for cname, ctype, ctarget, crule in dic_rows:'):
        in_dic = True
        fixed_4_5.append('    ' + stripped + '\n')
        continue
    if in_dic:
        if stripped.startswith('t_dic_data.append(') or stripped.startswith('Paragraph(') or stripped == '])':
            fixed_4_5.append('        ' + stripped + '\n')
            if stripped == '])':
                in_dic = False
            continue
        else:
            in_dic = False

    if stripped.startswith('if os.path.exists('):
        in_if = 3
        fixed_4_5.append('    ' + stripped + '\n')
        continue
    if in_if > 0:
        if stripped.startswith('elements.append('):
            fixed_4_5.append('        ' + stripped + '\n')
            in_if -= 1
            continue
        else:
            in_if = 0

    if stripped:
        fixed_4_5.append('    ' + stripped + '\n')
    else:
        fixed_4_5.append('\n')

with open('content_chapters_4_5.py', 'w', encoding='utf-8') as f:
    f.writelines(fixed_4_5)

print("content_chapters_4_5.py normalized.")

# 3. content_chapters_6_8.py
with open('content_chapters_6_8.py', 'r', encoding='utf-8') as f:
    raw = f.read()

lines = raw.splitlines(keepends=True)
fixed_6_8 = []
in_if = 0
in_refs = False

for i, line in enumerate(lines):
    stripped = line.strip()
    if line.startswith('import ') or line.startswith('from ') or line.startswith('def build_chapters_6_8'):
        fixed_6_8.append(line)
        continue
    
    if stripped.startswith('if os.path.exists('):
        in_if = 3
        fixed_6_8.append('    ' + stripped + '\n')
        continue
    if in_if > 0:
        if stripped.startswith('elements.append('):
            fixed_6_8.append('        ' + stripped + '\n')
            in_if -= 1
            continue
        else:
            in_if = 0

    if stripped.startswith('for rf in refs:'):
        in_refs = True
        fixed_6_8.append('    ' + stripped + '\n')
        continue
    if in_refs:
        if stripped.startswith('elements.append('):
            fixed_6_8.append('        ' + stripped + '\n')
            continue
        else:
            in_refs = False

    if stripped:
        fixed_6_8.append('    ' + stripped + '\n')
    else:
        fixed_6_8.append('\n')

with open('content_chapters_6_8.py', 'w', encoding='utf-8') as f:
    f.writelines(fixed_6_8)

print("content_chapters_6_8.py normalized.")

# 4. content_frontmatter.py
with open('content_frontmatter.py', 'r', encoding='utf-8') as f:
    raw = f.read()

lines = raw.splitlines(keepends=True)
fixed_fm = []
in_if = 0
in_loop = False

for i, line in enumerate(lines):
    stripped = line.strip()
    if line.startswith('import ') or line.startswith('from ') or line.startswith('def build_frontmatter'):
        fixed_fm.append(line)
        continue
    
    if stripped.startswith('if os.path.exists('):
        in_if = 2
        fixed_fm.append('    ' + stripped + '\n')
        continue
    if in_if > 0:
        if stripped.startswith('elements.append('):
            fixed_fm.append('        ' + stripped + '\n')
            in_if -= 1
            continue
        else:
            in_if = 0

    if stripped.startswith('for ftitle, fpage in figures_list:') or stripped.startswith('for ttitle, tpage in tables_list:') or stripped.startswith('for ab, desc in abbrs:'):
        in_loop = True
        fixed_fm.append('    ' + stripped + '\n')
        continue
    if in_loop:
        if stripped.startswith('tbl_') or stripped.startswith('abbr_') or stripped.startswith('Paragraph(') or stripped.startswith('elements.append(') or stripped == '])':
            fixed_fm.append('        ' + stripped + '\n')
            if stripped == '])':
                in_loop = False
            continue
        else:
            in_loop = False

    if stripped:
        fixed_fm.append('    ' + stripped + '\n')
    else:
        fixed_fm.append('\n')

with open('content_frontmatter.py', 'w', encoding='utf-8') as f:
    f.writelines(fixed_fm)

print("content_frontmatter.py normalized.")
