#!/usr/bin/env python3
"""Fix all remaining garbled encoding across chapter files."""

files = [
    "content_chapters_1_3.py",
    "content_chapters_4_5.py", 
    "content_chapters_6_8.py",
    "content_frontmatter.py",
]

# These are the actual byte patterns we see in the file
# The bullet • appears as: ƒÆ'‚Â¢ƒÂ¢Å¡‚Â¬ƒš‚Â¢
# The 50×50 appears as: 50ƒÆ'†™ƒÂ¢x  

REPLACEMENTS = [
    # Bullet •  (multiple variants seen)
    ("ƒÆ'‚Â¢ƒÂ¢Å¡‚Â¬ƒš‚Â¢", "\u2022 "),  # full bullet sequence
    ("â€¢", "\u2022 "),  
    ("• ", "\u2022 "),
    # em-dash (—)
    ("ƒÆ'‚Â¢ƒÂ¢Å¡‚Â¬ƒÆ'†™ƒÆ'Å¡", "\u2014"),
    ("â€”", "\u2014"),
    ("â€“", "\u2013"),
    # Left double quote "
    ("ƒÆ'‚Â¢ƒÂ¢Å¡‚Â¬ƒÂ¢ÅÂ", "\u201c"),
    ("â€œ", "\u201c"),
    # Right double quote "
    ("â€", "\u201d"),
    # Apostrophe/right single '
    ("â€™", "\u2019"),
    # Left single '
    ("â€˜", "\u2018"),
    # Ellipsis …
    ("ƒÆ'‚Â¢ƒÂ¢Å¡‚Â¬Â¦", "..."),
    # Copyright ©
    ("Â©", "(c)"),
    # Registered ®
    ("Â®", ""),
    # Degree °
    ("Â°", "deg"),
    # Non-breaking space
    ("Â\u00a0", " "),
    ("Â ", " "),
    # 50x50 specific
    ("50ƒÆ'†™ƒÂ¢x", "50x"),
    ("ƒÆ'†™", "\u00d7"),
    # Remaining ƒ garbage
    ("ƒÆ'‚Â¢ƒÂ¢Å¡‚Â¬ƒš‚Â¢", "\u2022 "),
    ("ƒÂ¢Å¡‚Â¬", ""),
    ("ƒÆ'†™", ""),
    ("ƒš‚Â¢", ""),
    ("ƒÆ'‚Â¢", ""),
    ("ƒÂ¢Å¡", ""),
    ("‚Â¬", ""),
    ("‚Â¢", ""),
    ("ƒÆ'", ""),
    ("ƒÂ", ""),
    ("‚Â", ""),
    ("ƒš", ""),
    ("Å¡", ""),
    ("Å¡", ""),
    ("Å™", ""),
    # Clean up stray Â (from latin-1 non-breaking-space or other)
    ("Â", ""),
]

total_fixes = 0

for fname in files:
    with open(fname, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    original = content
    count = 0
    for bad, good in REPLACEMENTS:
        if bad in content:
            n = content.count(bad)
            content = content.replace(bad, good)
            count += n
    
    if content != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {count} replacements in: {fname}")
        total_fixes += count
    else:
        print(f"No changes: {fname}")

print(f"\nTotal replacements: {total_fixes}")
