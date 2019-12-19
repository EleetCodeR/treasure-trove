# Data Classes do not have any methods defined in them, they only contain data.
from collections import namedtuple


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(p1 == p2)
# # FALSE (when __eq__ is not implemented)
# # As python compares two objects and returns TRUE; only when are pointing to same memory location.
# # As in this case p1 and p2 are two separate variables they are stored at diffirent locations.
# print(id(p1), id(p2))
# # hence we impliment magic method __eq__
# print(p1 == p2)


# NOTE: but there is a better way to deal with Data Classes than implementing these magic methods;
# i.e, Using namedtuple method from Collections module to create a type/class.
Point = namedtuple("Point", ["x", 'y'])
p1 = Point(x=1, y=2)
p2 = Point(1, 2)
print(p1 == p2)
# NOTE : nametuple are better; because it has attributes just like a class; unlike a regular tuple.
print(p1.x)
# NOTE: namedtulpes are IMMUTABLE.
