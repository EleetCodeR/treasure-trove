# Compiled Python Files:

## Module-Loading :
### What is __pycache__ folder ? :
When we run the code a new folder is created by python-compiler called : "__pycache__".
This folder contains compiled files in the below format:

<filename> dot <implementation of python used for compilation> dot pyc
 for example:
<filename>.cpython-37.pyc

The python compiler stores compiled files in this folder, as they can be reused directly when "importing/loading" is needed and need not be re-compiled, hence due to this "module-loading" happens faster.
All these compiled files are in binary format.
Main module file/ entry-point file (default:'app.py') is always compiled , hence there is no-compiled file for it in pycache folder.

### But How does compiler understand that these compiled files are up-to-date or not?
for this, compiler compares the date-time of source code file/files and that of compiled file/files , 
if it matched then compiled files is up-to-date and used.


