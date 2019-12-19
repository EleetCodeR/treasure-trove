# Sometimes we need more control over atteributes.


class Product:
    def __init__(self, price):
        # self.set_price(price)
        self.price = price

    # def get_price(self):
    #     return self.__price

    @property
    def price(self):
        return self.price

    # def set_price(self, value):
    #     if value < 0:
    #         raise ValueError("Price can not be negative.")
    #     self.__price = value

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative.")
        self.__price = value

        # price = property(get_price, set_price)
        # Property is an object that can be used to get/set the value of an attribute.(i.e to manage an attribute.)


# Raising error like above is not "Pythonic"(doesn't use full potential of python.)
#product = Product(-50)


product = Product(10)
product.price = 2
print(product.price)

# also we can access geter/seter methods from object and at types we might want to keep our interface clear and concise.
# so instead of calling property function we can use decorators, and we change geter/seter method names.
# for above get'er method @property and above set'ter method @<name of attribute>.setter
# If we do not write set'er method , then it becomes a read only property.
# (in  trying to modify value will throw - AttributeError: can't set attribute)
