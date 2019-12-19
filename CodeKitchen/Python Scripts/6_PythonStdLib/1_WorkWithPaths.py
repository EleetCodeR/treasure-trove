from pathlib import Path

# ============ / Creating a PATH-OBJECT / ============
# # Absolute Path:
# Path("C:\\Program Files\\Microsoft")

# # using RAW STRINGS:
# Path(r"C:\Program Files\Common Files")
# # In raw strings backslash is not an escape character, it is taken as is.

# # Current Directory/Folder:
# Path()

# # Combining path objects together:
# Path() / Path("ecommerce\ __init.py")
# # or combining Path object with strings:
# Path() / "ecommerce" / "__init__.py"

# # Get the home directory of the current user:
# Path.home()

# Relative Path:
path = Path(r"ecommerce\ __init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)  # name of file.
print(path.stem)  # name without extension.
print(path.suffix)  # extension
print(path.parent)  # name of parent

# using the same path-object but replacing the filename
path = path.with_name("file.txt")
print(path)
print(path.absolute())  # for Absolute Path.

# TO replace the extension of file in existing path.
path = path.with_suffix(".py")
print(path)

# NOTE : Creating a Path object doesn't create a File or directory, modify
# We are only representing path in above code.
