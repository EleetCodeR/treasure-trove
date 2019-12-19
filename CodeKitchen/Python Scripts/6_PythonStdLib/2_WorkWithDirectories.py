from pathlib import Path

path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# path.iterdir() returns generator object.
for i in path.iterdir():
    print(i)

# Convert generator object to list using list comprehension.
paths = [p for p in path.iterdir()]
print(paths, end='\n')

# to print only the directories and not files.
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths, end='\n')

# LIMITATIONS:
# No pattern matching/searching.
# No recursive search.
# hence use glob.

# NOTE: PATTERN SEARCHING + RECURSIVE SEARCH
# Pattern for all files *.*
py_files = [p for p in path.glob("*.py")]
print(py_files, end='\n')

py_files = [p for p in path.rglob("*.py")]
print(py_files, end='\n')
