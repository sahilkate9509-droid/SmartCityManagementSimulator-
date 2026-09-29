with open('content_chapters_1_3.py', 'r', encoding='utf-8') as f:
    content = f.read()

old = 'procedural 50x\\"50 terrain generation'
new = 'procedural 50x50 terrain generation'
if old in content:
    content = content.replace(old, new)
    print("Fixed 50x50 (escaped quote variant)")
else:
    # Try another variant
    old2 = '50x\u201d50'
    if old2 in content:
        content = content.replace(old2, '50x50')
        print("Fixed 50x50 (smart quote variant)")
    else:
        import re
        content = re.sub(r'50x["\u201c\u201d\u2019\u2018]50', '50x50', content)
        print("Fixed 50x50 (regex variant)")

with open('content_chapters_1_3.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
