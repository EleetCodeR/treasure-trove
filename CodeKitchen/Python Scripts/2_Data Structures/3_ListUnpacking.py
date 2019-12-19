# NOTE: we often need to access/assign individual item of a list to different variables.
numbers = [1, 2, 3]

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
# above code is similar to below.

# THIS IS LIST UNPACKING:-
first, second, third = numbers

# NOTE: Number of variables on LHS of assignment operator should be same as #elements in List to be unpacked.
# Otherwise , "ValueError : too many values to unpack."

# NOTE : PACKING & UNPACKING
# Often we are interested in few of the elements and not all;
# We can unpack the elements we want as usual, but at the same time;
# remaining elements can be re-packed in a different list by using asterisk *, as shown below.
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first, second, *other = List
print(first)  # 1
print(second)  # 2
print(other)  # [3,4,5,6,7,8,9,10] a new list.

# NOTE: When interested in first and last,
first, *other, last = List
print(first, last)  # 1 10
print(other)  # [2, 3, 4, 5, 6, 7, 8, 9]

# NOTE: Similar rules apply for a tuple.
