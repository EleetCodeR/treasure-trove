# Lets look at different useful methods often used with files.

from pathlib import Path
# to import human readable time,
from time import ctime

import shutil

path = Path(r"C:\Users\Vishal Ramane\Documents\GitHub\treasure-trove\CodeKitchen\Python Scripts\ecommerce\__init__.py")
# path.exists()
# path.rename("init.txt") # to rename the file.
# path.unlink() # will delete the file.

print(path.stat())  # returns statresult object as shown below.
# os.stat_result(st_mode=33206, st_ino=12384898975432650, st_dev=2518230490, st_nlink=1, st_uid=0,
# st_gid=0, st_size=33, st_atime=1578236324, st_mtime=1566729781, st_ctime=1576780490)

# where ; st_size = size of file in bytes,
# st_atime = last access time,
# st_mtime = last modified time,
# st_ctime = creation time.
# All above times are shown in seconds after 'epoch', which is the start of computer and is platform depended.
# (In computing, an epoch is a date and time from which a computer measures system time.)

# To print Human readble time, import ctime function from time module, and pass time to it in seconds.
print(ctime(path.stat().st_ctime))

# ===================================== READ/WRITING FILES =======================================
# path.read_bytes() # returns file content in binary.
print(path.read_text())  # returns file content in string.
# read_text is easier to use than Open() function, as automatically closes file.etc

# # Similarly,
# path.write_text("Writing to file")
# path.write_bytes()

# ===================================== COPYING FILES =======================================
source = Path(
    r"C:\Users\Vishal Ramane\Documents\GitHub\treasure-trove\CodeKitchen\Python Scripts\ecommerce\__init__.py")
target = Path() / "__init__.py"

# target.write_text(source.read_text())

# NOTE:
# when using Path objects for copy , we need to read content of file from source and then feed it to target for writing.
# so copying using path is tedious and not a recommended method.
# There is a better way,
# Using "shutil" (shell utilities) module, which provides number of high level operations.

shutil.copy(source, target)
