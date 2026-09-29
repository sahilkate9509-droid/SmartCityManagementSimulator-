import re

files = ['content_chapters_1_3.py','content_chapters_4_5.py','content_chapters_6_8.py','content_frontmatter.py']
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old = content
    
    # Fix: word + x + quote/smart-quote -> word + emdash
    # This handles cases where em dash became x" due to our previous fix
    content = re.sub(r'(?<=\w)x[\u201c\u201d\u2019\u2018"]\s*', '\u2014', content)
    
    if content != old:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed: {fname}')
    else:
        print(f'No changes: {fname}')
