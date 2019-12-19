from abc import ABC, abstractmethod


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


class TextBox:
    def draw(self):
        print("TextBox.")


class DropDownList:
    def draw(self):
        print("DrowpDownList.")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
TextBox = TextBox()

draw([ddl, TextBox])

# We do not need a Base Class like UIControl to achieve Polymorphism in draw function, as python is Dynamically typed laguage (Doesn't Check for type of language).
# but it is a good practice to have a common interface/contract.
# As long as, here, the object is iterable and has draw method it can implement polymorphism.
# This is called DUCK TYPING. (If it walks and quacks like a duck, it is a duck.)
