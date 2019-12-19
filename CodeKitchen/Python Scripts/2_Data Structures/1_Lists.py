letters = ["a", "b", "c", "d"]
matrix = [[0, 1], [2, 3]]  # 2D array.
List = ["a", "b", "c", 0, 1, 2, 3, [0, 1], [2, 3]]  # NOTE-2
zeros = [0]*5  # NOTE-3

# NOTE-4 # numbers from 0 to 19 will be elements of the list.
numbers = list(range(20))

combined = zeros + letters  # NOTE-5
chars = list("Hello World")  # Each letter will appear as an element in list.

print(List)
print(combined)
print(len(combined))  # NOTE-6
print(chars)

# NOTE LISTS in Python.
# NOTE 1>: We can define List in python by using square brackets.
# NOTE 2>: Objects in List in Python can be of different types.(mix)
# NOTE 3>: we can repeat an item in a list by multiplying it with a number. eg. if we want 100 zeros in a list = [0]*100
# NOTE 4>: We can fill a list by enumerating numbers using RANGE function. As List function takes an Iterable parameter.
# NOTE 5>: We can concatenate List using + operator.
# NOTE 6>: We can find number of items in a list by using len function.
