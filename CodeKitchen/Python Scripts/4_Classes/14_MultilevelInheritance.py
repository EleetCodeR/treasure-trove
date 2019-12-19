class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass

# Multilevel inheritance can increase complexities.
# Keep it to 2- levels
