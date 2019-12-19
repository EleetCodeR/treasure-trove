class Animal:
    def __init__(self):
        self.age = 1
        print("Animal C'tor")

    def eat(self):
        print("eat")

# Animal : Parent/Base class
# Mammal : Child/Subclass
# Fish : Child/Subclass


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal C'tor")
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()

print(m.weight)
print(m.age)  # AttributeError: 'Mammal' object has no attribute 'age'
# Why this error??
# Constructor in Animal class was not executed (hence no age defined); because it was overriden by constructor in Subclass - Mammal.
# This is called Method Overriding.It can be used to Extend the methods defined in base class.
# If we want to execute cons'tor of Base class first , we can use super() method to call methods of base class from anywhere in subclass.
