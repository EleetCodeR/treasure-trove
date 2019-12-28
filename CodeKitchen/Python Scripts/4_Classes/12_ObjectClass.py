class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()

print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))

# Animal : Parent/Base class
# Mammal : Child/Subclass
# Fish : Child/Subclass
o = object()

print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))

# Every class in python is derived from Object class.i.e Object class is Base class of all classes in Python.(Superclass)
# all the magic methods are inherited from Object class.
