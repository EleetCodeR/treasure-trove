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
m.walk()
m.eat()

print(m.age)

# Animal : Parent/Base class
# Mammal : Child/Subclass
# Fish : Child/Subclass
# we mention the name of baseclass/Parent class in round brackets after the class name.
# so the derived class then inherits the base class.
