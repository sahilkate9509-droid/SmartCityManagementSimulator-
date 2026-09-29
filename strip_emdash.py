import ast

files = ['content_chapters_1_3.py', 'content_chapters_4_5.py', 'content_chapters_6_8.py', 'content_frontmatter.py']

for fn in files:
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    # Remove the inserted em-dash
    text = text.replace('—', '')
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(text)

print("Em-dash characters stripped.")
