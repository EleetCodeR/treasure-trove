# Class: Blueprint for creating Objects. eg. Humans
# Object: Instance of a Class. eg. John, Mosh,Ted.
# All the methods defined in a class should contain atleast one parameter (self);
# and then additionally we can add more parameters as we please


class Point:
    def draw(self):
        print("Draw.")


# to create an object of the class just call class name as a function.
point = Point()
print(type(point))  # <class '__main__.Point'>
print(isinstance(point, Point))  # True.

# To construct an object of the class and initialize with parameters,
# we need to define a special method called as Constructor.
