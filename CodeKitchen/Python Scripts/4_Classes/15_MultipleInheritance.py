# NOTE: Multiple Inheritance and Diamond Problem:
# superclass             A
#                      /   \
#                     /     \
# subclasses         B       C
#                     \     /
#                      \   /
# sub-subclass           D

# if B,C derived from A and D is derived from B and C both.
# and a method of A is overriden in B and C both but not in D,
# then D doesnt understand which parent class should it inherit it from.


class Employee:
    def greet(self):
        print("Employee Greets")


class Person:
    def greet(self):
        print("Person Greets")


class Manager(Person, Employee):
    pass


m = Manager()
m.greet()
# Employee Greets  ; when Manager(Employee, Person):
# Person Greets ; when Manager(Person, Employee):
# NOTE: This is because we mentioned Employee as Base Class first.eg.Manager(Employee, Person):
# NOTE: This Problem does not arise if there is no-common method between the classes ;
# and Multiple Inheritance can be useful.


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class Flyingfish(Flyer, Swimmer):
    pass
