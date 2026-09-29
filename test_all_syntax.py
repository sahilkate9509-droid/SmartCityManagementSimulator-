import ast
import glob

all_ok = True
for f in sorted(glob.glob("*.py")):
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            ast.parse(fp.read())
        print(f"[OK] {f}")
    except Exception as e:
        print(f"[ERROR] {f}: {type(e).__name__} - {e}")
        all_ok = False

if all_ok:
    print("\nALL PYTHON FILES PARSED SUCCESSFULLY!")
