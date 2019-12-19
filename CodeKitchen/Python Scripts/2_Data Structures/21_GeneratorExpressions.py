# NOTE : GENERATOR OBJECT?
# Sometimes the scenario arises where the range of numbers/items we are dealing with,
# is too large to be stored into memory in the form of say List.(i.e, is Memory in-efficient)
# in such scenario instead of storing such a huge range, Generator obj. is used
# Generator object is iterable and generates a new value at every iteration.
# Irrespective of range the size of G-object remains same (120 Bytes); as shown below.
# NOTE : Hence when dealing with a really large dataset or potentially a really large stream of data,
# use a GENERATOR EXPRESSION to create a GENERATOR OBJECT.

from sys import getsizeof

values = (x*2 for x in range(1000))
print("Generator Obj (range:1000):", getsizeof(values))

values = (x*2 for x in range(1000000))
print("Generator Obj (range:1000000):", getsizeof(values))

values = [x*2 for x in range(1000000)]
print("List (range:1000000):", getsizeof(values))

# Generator Obj (range:1000): 120 B
# Generator Obj (range:1000000): 120 B
# List (range:1000000): 8697464 B

# NOTE : Because GEN.OBJ don't store all the objects in memory; and are dynamically generated over
# every iteration, we have no option of knowing total number of items we are working with beforehand.
values = (x*2 for x in range(1000000))
print(len(values))  # hence throws error.
# TypeError: object of type 'generator' has no len()
