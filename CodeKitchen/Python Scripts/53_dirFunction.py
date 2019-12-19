from ecommerce.shopping import sales

print(dir(sales))

"""
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__'
, '__package__', '__spec__', 
'calc_shipping', 'calc_tax', 'contact']
"""
# dir function lists all the attributes and methods defined in an object.
# returns an array of string objects.

print(sales.__name__)  # we get name of the module
print(sales.__package__)  # name of the package
print(sales.__file__)  # gives path to this file and the file sys.
