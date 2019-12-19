from array import array

# NOTE: most of times we will use list , but when performance issues;say due to very large "list of numbers"; we will use array.

numbers = array("i", [1, 2, 3])

# "i" is a typecode (a single character string), that specifies type of items (here signed int) in an array.
# (refer typecodes in python3 documents).
# every object in this array should be of same type, else TYPE ERROR.
# eg. numbers = array("i", [1, 2, 3, 4.0])  will throw type-error.same as below.
numbers[0] = 4.0
