# Magic Methods : which have 2 underscores at the beginning and end of there name.
# called automatically by Python interpreter depending on how we use it.
#


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(1, 2)
print(str(point))
print(point.__str__())
# __str__ method is used to convert object to string.
