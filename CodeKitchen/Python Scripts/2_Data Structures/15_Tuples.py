point = (1, 2)
print(point)

# or we can even declare without round brackets, but must write trailing comma; otherwise could be construed as integer.
point = 1,
print(point)
point = 1, 2
print(point)

# Similar to lists , we can concatenate the tuples too.
point = (1, 2) + (3, 4)
print(point)

# replicating a tuple.
point = (1, 2) * 3
print(point)

# Converting to an iterable to a tuple.
point = tuple([1, 2, 3, 4])
print(point)
point = tuple("Hello World")
print(point)

# similar to list we can acces items in tuple using indices.
print(point[1])
print(point[0:4])
print(point[::2])
print(point[::-1])
