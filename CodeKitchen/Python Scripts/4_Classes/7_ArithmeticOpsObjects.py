class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point({self.x},{self.y})")


point = Point(10, 20)
other = Point(1, 2)
(point + other).draw()
# + is not supported by operands of type 'Point'.
# We need to implement magic method, which will be called automatically when + is used.
# so we implement __add__ method.
