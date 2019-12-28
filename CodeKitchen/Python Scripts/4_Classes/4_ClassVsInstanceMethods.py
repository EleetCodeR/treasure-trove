# Class Level method :
# Many times we need to initialize an object of a class with multiple attributes,
# Which can be a complex task at times; we can use Class-Level methods (often called Factory Methods) to simplify this.
# To declare a method as a class method it must be annotated/decorated;
# using "@classmethod" decorator.
# 'cls' is used as parameter to class methods as a convention (can be any parameter);


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        # there can be complex code here.
        return cls(0, 0)

    def draw(self):
        print(f"Point({self.x},{self.y})")


#point = Point(0, 0)
point = Point.zero()
# Observe that in above code "zero" method is called on class ref and it's not an object instance.
point.draw()
