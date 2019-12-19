letters = ['a', 'b', 'c']

# ADD
letters.append("d")  # add at last position.
print(letters)
letters.insert(2, "_")  # add at an index.
print(letters)

# REMOVE
letters.pop(1)  # removes only one item from the given index.
print(letters)
letters.remove("_")  # when you don't know the index of item to be removed.
print(letters)

del letters[0]  # can remove items at an index.like pop.
del letters[0:2]  # to remove range of items del is used.
