letters = ['a', 'd', 'c', 'd', 'd']
if "d" in letters:
    print(letters.index("d"))
# in-operator : whether the element is present in the list or not.(returns boolean type)
# index method : if given value to be searched is not present => throws ValueError: 'd' is not in list
# index method returns index of first occurance only,
print(letters.count("d"))
# Count returns 0 if not present.
