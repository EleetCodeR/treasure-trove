# do not delete this file.
# This is the MAIN MODULE / FILE , as an "ENTRY POINT" to our program.

# 1 to 4 , 50,51,52,53,54,55 and then 6th.
# ================ 50.Creating Modules =================================================
# we created file 'sales.py'
# there are two ways to import modules see methods ##1 and ##2 below.


# using this we import the modules itself as an object.as shown below......##1
import ecommerce.shopping.sales

# NOTE(1):  MODULE SEARCH PATH :
# Python compiler searches for "sales.py" in current directory.
# If it can not find this module in current directory it then searches in a "pre-defined directories".
# For this we need to use module "sys" and its method "path"...eg."sys.path".


# importing objects from sales module instead of whole module as above.....##2
from ecommerce.shopping.sales import calc_shipping, calc_tax
# however importing methods like above by listing can be noisy sometimes. in that case use ##1 method
import sys  # code for NOTE1

# # call by ##1 method
# sales.calc_shipping()

# # call by ##2 method
calc_shipping()
calc_tax()

# print(sys.path)  # code for NOTE1, we will get an array of different paths as strings.

# ================ 52.PACKAGE ==========================================================
# As our project/application grows, number of files/modules also grow, hence we need to organize them into subdirectories.
# Lets create a directory "ecommerce", and move sale.py file in it.
# If we move sales.py file in "ecommerce" folder compiler will throw error for import in app.py file.
# to fix this if we create a file __init__.py in this sub-directory (ecommerce) then it is treated as PACKAGE.
# A PACKAGE is a container for one or more modules (files).
# now prefix the package name to that import and error is gone.i.e, ecommerce.sales
# In file System terms ; analogy= PACAKAGE ~ Directory and MODULE ~ File

# ======= Sub-Packages ==========:
# when package size get too large we can organize it using subpackages.
# move sales.py file in a new folder "shopping" inside "ecommerce" package, and make it a package as it gives error in app.py.
# so that importing modules is now done as - "ecommerce.shopping.sales" in app.py.
# ======================================================================================

# NOTE : Executing Module as Script:
# while loading modules, first Ecommerce package is initialized and then sales module.
# output:
# Ecommerce initialized.
# Sales initialized. ecommerce.shopping.sales
