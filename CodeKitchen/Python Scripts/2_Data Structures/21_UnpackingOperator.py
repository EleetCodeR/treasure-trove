values = [0, 1, 2, 3, 4]
print(values)
print(*values)
# NOTE: Using unpacking Operator * ; we will be able to access/takeout individual values in any iterable.

# above code can be written as:
values = list(range(5))

# Defining list using Unpacking Operator:
values = [*range(5), *"Hello World"]
print(values)

# Using this operator we can combine different lists:
first = [1, 2]
second = [3]
values = [*values, *first, *second]
print(values)

# Unpacking Operator for Dictionaries (** Double Asterisk):
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
print(combined)
# o/p : {'x': 10, 'y': 2, 'z': 1}
# NOTE : Observe that when duplicate keys are present, only the most recent one is kept;
# As duplicate keys are not allowed in dictionary.
