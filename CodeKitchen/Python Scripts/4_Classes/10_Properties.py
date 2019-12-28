# Sometimes we need more control over attributes.


class Product:
    def __init__(self, price):
        # self.set_price(price)
        self.price = price

    # def get_price(self):
    #     return self.__price

    # def set_price(self, value):
    #     if value < 0:
    #         raise ValueError("Price can not be negative.")
    #     self.__price = value

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative.")
        self.__price = value


# product = Product(-50)

# # Raising error like above (in set_price), and using getter/setter like above is not "Pythonic"(doesn't use full potential of python.)
# # Lets define a property instead as shown below:

# price = property(get_price, set_price) # see NOTE:1

# product = Product(10)
# print(product.price)
# product.price = 2
# print(product.price)

# NOTE: 1
# Property is an object of class Property ,that can be used to get/set the value of an attribute.(here 'price').
# Here we have also provided references as parameters to the methods that should be used for get/set of price,
# which are called internally.


product = Product(10)
product.price = 2
print(product.price)

# NOTE : 2
# Even after defining the property, we can still see getter/setter methods (get_price, set_price) in the object interface.(also in IDE intellisense)
# so to keep our object interface clean and simple we can use anotations (@property and @price.setter),
# Instead of calling property function.
# i.e, Above getter method write @property and above setter method write @<name of attribute>.setter (here @price.setter)
# If we do not write setter method , then it becomes a read only property.(in trying to modify value will throw - AttributeError: can't set attribute)
