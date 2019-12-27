letters = ['a', 'b', 'c']

# ADD
letters.append("d")  # adds new item at the last-position.
print(letters)
# add at an index.(rest of the list is kept same and shifted.)
letters.insert(2, "_")
print(letters)

# REMOVE
# Removes only one item from the given index.(by default last index.)
letters.pop(1)
print(letters)
# when you don't know the index of item to be removed, just mentioned the item to be removed.
letters.remove("_")
print(letters)

del letters[0]  # can remove items at an index.like pop.
del letters[0:2]  # to remove range of items del is used.
