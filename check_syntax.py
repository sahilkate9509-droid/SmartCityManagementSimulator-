"""Fix the 4 remaining syntax errors precisely by viewing and patching context."""
import ast

# Read each file and find context around the error
checks = [
    ('content_chapters_1_3.py', 59, 65),
    ('content_chapters_4_5.py', 48, 57),
    ('content_chapters_6_8.py', 383, 392),
    ('content_frontmatter.py', 323, 335),
]

for fname, s, e in checks:
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f'\n=== {fname} L{s}-{e} ===')
    for i in range(s-1, min(e, len(lines))):
        print(f'  L{i+1}: {repr(lines[i][:110])}')
