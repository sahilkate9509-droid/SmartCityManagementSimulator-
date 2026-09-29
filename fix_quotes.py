import re
import ast

def fix_file(fn):
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace pattern like word"word with word -- word or word - word or word: word
    # Specifically where a quote was placed instead of em-dash
    # e.g. tracks"such -> tracks -- such
    # concepts"such -> concepts -- such
    # sandbox"a true -> sandbox -- a true
    # dispersion"into -> dispersion -- into
    # degradation"to -> degradation -- to
    # simultaneously"such -> simultaneously -- such
    # peripheries"a -> peripheries -- a
    # design"maximized -> design -- maximized
    
    new_content = re.sub(r'([a-zA-Z0-9>])\"([a-zA-Z])', r'\1 -- \2', content)
    
    if new_content != content:
        with open(fn, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed broken quotes in {fn}")

for fn in ['content_chapters_1_3.py', 'content_chapters_4_5.py', 'content_chapters_6_8.py', 'content_frontmatter.py']:
    fix_file(fn)
