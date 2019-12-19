letters = ["a", "b", "c", "d", 'e', 'f', 'g', 'h', 'i', 'j']

# similar to strings
print(letters[0])
print(letters[-1])

# List is mutable.
letters[0] = "A"
print(letters)

# NOTE: slicing the list. # Rules of indexing are same as that of strings.
print(letters[0:3])
print(letters[:])

numbers = list(range(20))
# step count. (here every 2nd element is selected,all even numbers)
print(numbers[::2])
print(numbers[::-1])  # -1 as a step reverses the list.
