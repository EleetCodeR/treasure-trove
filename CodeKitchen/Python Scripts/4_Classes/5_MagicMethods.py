# Magic Methods : which have 2 underscores at the beginning and end of their name.
# Are called automatically by Python interpreter depending on how we use them.
# eg. __init__ and __str__ below.


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x},,,{self.y})"

    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(1, 2)
print(str(point))
print(point.__str__())
# __str__ method is used to convert an object to string.
# Observe that both are giving the same output, meaning both are calling the same method.
# since we have modified the __str__ , the call to (built-in) str() gives preference to our implementation.
