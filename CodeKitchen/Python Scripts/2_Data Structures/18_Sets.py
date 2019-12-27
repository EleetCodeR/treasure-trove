# SET : unordered collection of uniquely defined items.
# hence,
# NOTE : Sets can not be indexed.=> throws TYPE ERROR.

numbers = [2, 3, 4, 5, 7, 7]

first = set(numbers)
# automatically removes duplicates and converts to set, no error thrown.
print("First:", first)

if 7 in first:
    print("Is 7 present in first set? Yes.")

# NOTE : we use curly braces to define Sets.
second = {1, 4, 4, 6}
second.add(5)
second.remove(5)
print("Second:", second)

# NOTE : What makes sets really useful,
# is the mathematical-operations/Set-operations that can be performed with them.
# Union:
print("Union:", first | second)

# Intersection:
print("Intersection:", first & second)

# Set-Difference:
print("Set-Difference:", first - second)

# NOTE : Symmetric Difference:
print("Symmetric Difference:", first ^ second)
