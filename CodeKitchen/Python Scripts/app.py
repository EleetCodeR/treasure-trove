# do not delete this file
# This is the MAIN MODULE / FILE , as an "ENTRY POINT" to our program.


# "6th-Creating Modules" Topic: created a files 'sales.py'

# using this we import the modules itself as an object.    ##1
import ecommerce.shopping.sales
# Python compiler searches for "sales.py" in current directory.
# If it can not find this module in current directory it then searches in a "pre-defined directories".
# For this we need to use module "sys.path".
# importing objects from sales module.     ##2
from ecommerce.shopping.sales import calc_shipping, calc_tax
# however importing methods like above by listing can be noisy sometimes.in that case use ##1 method
import sys

#  ##1
# sales.calc_shipping()

# #  ##2
calc_shipping()
calc_tax()

# print(sys.path)  # we will get an array of different paths as strings.

# PACKAGE :
# If we move sales.py file in ecommerce folder compiler will throw error for import.
# If we create a file __init__.py in this sub-directory then it is treated as PACKAGE.
# now prefix the package name to that import and error is gone.i.e, ecommerce.sales
# In file System terms , PACAKAGE ~ Directory and MODULE ~ File

# Sub-Package:
# move sales.py file in a new folder shopping inside ecommerce package, and make it a package.
# so that - ecommerce.shopping.sales

# NOTE : Executing Module as Script:
# while loading modules, first Ecommerce package is initialized and then sales module.
# output:
# Ecommerce initialized.
# Sales initialized. ecommerce.shopping.sales
