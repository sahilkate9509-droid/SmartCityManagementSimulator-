import re
import ast

def normalize_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # We can parse the logical structure or re-indent properly.
    # Let's inspect the file and fix all indentations.
    # The files are simple:
    # Level 0: imports, def build_*(...)
    # Level 1 (4 spaces): elements of build_*
    # Level 2 (8 spaces): inside if os.path.exists(...) or for ...:
    # Level 3 (12 spaces): inside nested for/if
    # Level 4 (16 spaces): inside doubly nested
    
    # Let's write a dedicated fixer for each file based on its AST structure or line-by-line grammar.
    pass
