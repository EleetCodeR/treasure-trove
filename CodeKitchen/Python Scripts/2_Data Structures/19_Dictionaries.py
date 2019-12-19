# NOTE : In Python we can only use immutable types as keys in dictionary.
point = {"x": 1, "y": 2}
# but a better way is,
point = dict(x=1, y=2)


# in Dictionary we can not access elements using numeric-key/index , we use string.
point["x"] = 10  # changing the value
point["z"] = 20  # defines a new key-val, when on LHS side.
point["100"] = 100
print(point)


# NOTE: While trying to access the element if key does not exist in dictionary => "Key Error"
# to avoid exception while access, we can check first;
if "a" in point:
    print(point["a"])
# OR we can use get-method.(and can also set default value)
print(point.get("a", 10))
# None.(if default value is not set)
# returns default value when key is not found. (here-10)

# An Entry can be removed using del method
del point["x"]
print(point)


# NOTE : looping in dictionary:
for x in point:
    print(x)

# so in each iteration loop variable holds key of each item of dict.
# so we can write as shown:
for key in point:
    print(key, "=", point[key])

# another way is unpacking at loop variable itself;
for key, value in point.items():
    print(key, "=", value)
