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


# def draw(control):
#     control.draw()

# Instead to pass a list of controls.
def draw(controls):
    for control in controls:
    control.draw()


ddl = DropDownList()
TextBox = TextBox()
# draw(ddl)
# draw(TextBox)

draw([ddl, TextBox])
# here Draw Method does not know which control it is dealing with as it is determined at runtime.
# each time for different control draw method is called , hence POLYMORPHISM.
