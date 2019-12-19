# Definition : LAMBDA FUNCTION
# In computer programming, an 'anonymous function' is a function definition that is not bound to an identifier.
# Anonymous functions are often arguments being passed to higher-order functions,
# or used for constructing the result of a higher-order function that needs to return a function.

# Syntax : lambda <parameters..>: <expression>

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


# def sort_item(item):
#     return item[1]

# items.sort(key=sort_item)
items.sort(key=lambda item: item[1])
print(items)
