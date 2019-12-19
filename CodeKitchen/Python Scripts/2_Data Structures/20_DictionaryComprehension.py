values = []
for x in range(5):
    values.append(x*2)

# for above code we can use list-comprehension\as:
values = [x*2 for x in range(5)]
# so above 3-lines of code is compressed to one line.
print("List:", values)

# NOTE: Such Comprehensions are not limited to only LISTS, but can be used with SETS & DICTIONARIES.
# (by replacing square braces by curly.)

# NOTE : SET COMPREHENSION:
values = {x*2 for x in range(5)}
print("Set:", values)

# NOTE : DICTIONARY COMPREHENSION:
# What is the difference in set and dictionary comp?
# in Dict. we have key-value entries.so expression changes to:
values = {x: x*2 for x in range(5)}
print("Dictionary:", values)


# Can we use Comprehension expressions for Tuple also ?
values = (x*2 for x in range(5))
print(values)
# o/p : <generator object <genexpr> at 0x00000220B7AB4930>
# What is this Generator Object? Next topic.
