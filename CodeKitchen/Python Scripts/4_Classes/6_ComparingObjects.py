class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
print(point == other)
# False; as by default == operator compares references/addresses of the two object in memory.
# hence implement __eq__ . (eq : equal)
print(point > other)
#  TypeError: '>' not supported between instances of 'Point'
# hence implement __gt__ . (gt : greater than)

print(point < other)
# NOTE : Python interpreter automatically translates above code even though we did not implement __lt__ .
# as we have implemented __gt__ .
