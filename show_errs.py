# Let's inspect the specific lines for each error file
def show_context(fname, line_no, context=10):
    print(f"=== {fname} around line {line_no} ===")
    with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    start = max(0, line_no - context - 1)
    end = min(len(lines), line_no + context)
    for idx in range(start, end):
        print(f"{idx+1:4d}: {repr(lines[idx])}")

show_context('content_chapters_1_3.py', 137)
show_context('content_chapters_4_5.py', 52)
show_context('content_chapters_6_8.py', 657)
show_context('content_frontmatter.py', 326)
