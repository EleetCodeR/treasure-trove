from pathlib import Path

# ============ / Creating a PATH-OBJECT / ============
# # Absolute Path:
# Path("C:\\Program Files\\Microsoft")

# # using RAW STRINGS instead, where backslash is not an escape character:
# Path(r"C:\Program Files\Common Files")

# # To represent Current Directory/Folder:
# Path()

# # Combining path objects together using /:
# Path() / Path("ecommerce\ __init.py")
# # or combining Path object with strings directly:
# Path() / "ecommerce" / "__init__.py"

# # To get the home directory of the current user:
# Path.home()

# Relative Path:
path = Path(r"C:\Users\Vishal Ramane\Documents\GitHub\treasure-trove\CodeKitchen\Python Scripts\ecommerce\__init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.name)  # filename.
print(path.stem)  # filename without extension.
print(path.suffix)  # returns extension
print(path.parent)  # name of parent

# creating new path using existing path-object, but replacing the filename
path = path.with_name("file.txt")
print(path)
print(path.absolute())  # for Absolute Path.

# To replace the extension of file in existing path.
path = path.with_suffix(".py")
print(path)

# NOTE : IMPORTANT:
# Creating a Path object doesn't create a File or directory, or modify it.
# We are only representing a path in above code.
