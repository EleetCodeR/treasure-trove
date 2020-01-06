from ecommerce.shopping import sales

# "dir" function : lists all the "attributes and methods" defined in an object.
# It returns an array of string objects.
# Mainly used for debugging.

print(dir(sales))

"""
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__'
, '__package__', '__spec__', 
'calc_shipping', 'calc_tax', 'contact']
"""

print(sales.__name__)
# we get name of the module (full qualified) : ecommerce.shopping.sales

print(sales.__package__)  # name of the package : ecommerce.shopping
print(sales.__file__)  # gives path to this file in the file sys.
