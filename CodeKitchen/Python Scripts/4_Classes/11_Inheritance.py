class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

# Animal : Parent/Base class
# Mammal : Child/Subclass
# Fish : Child/Subclass


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
