# To Define constructor in Python, we use a magic method __init__ which is called a constructor.
# All the methods defined in a class should contain atleast one parameter (self);
# and then additionally we can add more parameters as we please


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Drawing Point({self.x},{self.y})")


point = Point(1, 2)
point.draw()
