# Class Attributes vs Instance Attributes:


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point({self.x},{self.y})")

# the x,y defined above are used by instance of the class ; called instance attri.
# the default_color defined above is a class-level attribute; which is shared among all instances of the class.


point = Point(1, 2)
# Since Objects in Python are dynamic we can define attributes as below too:
# point.z = 10
another = Point(3, 4)
print(point.draw(), another.draw())
