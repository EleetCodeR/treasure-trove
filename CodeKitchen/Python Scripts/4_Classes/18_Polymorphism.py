from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox.")


class DropDownList(UIControl):
    def draw(self):
        print("DrowpDownList.")

# To dynamically decide to draw control:
# def draw(control):
#     control.draw()

# Instead to pass a list of different controls, and draw each:


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
TextBox = TextBox()
# draw(ddl)  # This call will draw only a dropdownlist.
# draw(TextBox) # This call will draw only a Textbox

draw([ddl, TextBox])
# here Draw Method does not know which control it is dealing with as it is determined at runtime.
# each time for different control, draw method is called , hence POLYMORPHISM.(achieved in draw function.)
# Imagine if a webpage/form has a number of textboxes and DDLs,
# at that time instead of individually calling draw method on each instance we can pass a list of controls to a common method.
