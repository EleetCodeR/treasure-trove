from zipfile import ZipFile
from pathlib import Path

# ========================== CREATING ZIP FILES =======================================
# # To create and open a zip file in write mode:

# zip = ZipFile("ecommerce.zip", "w")
# # now writing to this zip file,
# for path in Path(
#         r"C:\Users\Vishal Ramane\Documents\GitHub\treasure-trove\CodeKitchen\Python Scripts\ecommerce\__init__.py").rglob("*.*"):
#     zip.write(path)
# zip.close()

# NOTE:
# But if there is some error in above for loop code it will throw error, and close statement might be skipped.
# For this we use try-finally block or With statement...so,

# # To create and open a zip file in write mode.
# with ZipFile("ecommerce.zip", "w") as zip:
#     # now writing to this zip file,
#     for path in Path(r"C:\Users\Vishal Ramane\Documents\GitHub\treasure-trove\CodeKitchen\Python Scripts\ecommerce").rglob("*.*"):
#         zip.write(path)


# ========================== READING ZIP FILES =======================================
with ZipFile("ecommerce.zip") as zip:
    print(zip.namelist())
    # returns list of file names in the archive.
    # we can also get information about archived files,
    info_Obj = zip.getinfo(
        "Users/Vishal Ramane/Documents/GitHub/treasure-trove/CodeKitchen/Python Scripts/ecommerce/customer/contact.py")
    print(info_Obj.file_size)
    print(info_Obj.compress_size)  # No compression since small file.

    # zip.extractall(" ") is used to extract current archive file into a specific location.
