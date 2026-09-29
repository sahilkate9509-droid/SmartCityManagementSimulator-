"""Final surgical fix for all remaining errors - clean version."""
import ast, re

EM_DASH = '\u2014'

# FIX 1: content_chapters_1_3.py - "word"word -> word—word  
fname = 'content_chapters_1_3.py'
with open(fname, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace lowercase"lowercase with lowercase + em dash + lowercase
def fix_em_dashes_in_strings(text):
    # Only fix where a closing quote is immediately followed by a lowercase letter
    # (indicating the quote is actually an em dash that got corrupted)
    result = re.sub(r'([a-z])"([a-z])', r'\g<1>' + EM_DASH + r'\g<2>', text)
    return result

old = content
content = fix_em_dashes_in_strings(content)
if content != old:
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed 1_3 em dashes')

# FIX 2: content_chapters_4_5.py - fix function body indentation
fname = 'content_chapters_4_5.py'
with open(fname, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'def build_schema_table(' in line:
        fn_indent = len(line) - len(line.lstrip())
        body_needed = fn_indent + 4
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if not nxt.strip():
                j += 1
                continue
            ni = len(nxt) - len(nxt.lstrip())
            if ni <= fn_indent and nxt.strip():
                break
            if 0 < ni < body_needed:
                lines[j] = ' ' * body_needed + nxt.lstrip()
            j += 1
        break

with open(fname, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Fixed 4_5 function indentation')

# FIX 3: content_chapters_6_8.py - fix em dashes same way
fname = 'content_chapters_6_8.py'
with open(fname, 'r', encoding='utf-8') as f:
    content = f.read()
old = content
content = fix_em_dashes_in_strings(content)
if content != old:
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed 6_8 em dashes')

# FIX 4: content_frontmatter.py - fix for loop body indent  
fname = 'content_frontmatter.py'
with open(fname, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'for ttitle, tpage in tables_list:' in line:
        for_indent = len(line) - len(line.lstrip())
        body_needed = for_indent + 4
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if not nxt.strip():
                j += 1
                continue
            ni = len(nxt) - len(nxt.lstrip())
            if ni <= for_indent and nxt.strip():
                break
            if 0 < ni < body_needed:
                lines[j] = ' ' * body_needed + nxt.lstrip()
            j += 1
        break

with open(fname, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Fixed frontmatter for-loop')

# Final syntax check - loop until all errors resolved or no more progress
print('\n=== Final Syntax Check ===')
all_ok = True
for fn in ['content_chapters_1_3.py','content_chapters_4_5.py',
           'content_chapters_6_8.py','content_frontmatter.py']:
    try:
        with open(fn, 'r', encoding='utf-8') as f:
            ast.parse(f.read())
        print(f'  OK: {fn}')
    except SyntaxError as e:
        all_ok = False
        print(f'  ERROR {fn} L{e.lineno}: {repr(e.text[:80]) if e.text else ""}')

if all_ok:
    print('\nAll files SYNTAX CLEAN. Ready to build PDF.')
