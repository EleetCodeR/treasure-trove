letters = ['a', 'b', 'c', 'd']
for letter in letters:
    print(letter)

for letter in enumerate(letters):
    print(letter)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')

for letter in enumerate(letters, 2):
    print(letter)
# indexing starts from 2 here.
# (2, 'a')
# (3, 'b')
# (4, 'c')
# (5, 'd')

# NOTE:
# enumerate function returns an iterable object which consist of index and a value from original iterable object passed as parameter.
# It is useful when an indexed list is needed. returned object by enumerate is of the form of a tuple or a pair.
# indexing by default starts from 0, if not mentioned otherwise.

# Accessing individual elements from a tuple,
for letter in enumerate(letters):
    print(letter[0], letter[1])
# 0 a
# 1 b
# 2 c
# 3 d

# NOTE: a better way to unpack tuples in above code is as shown;
# the iterable object returned by enumerate function is unpacked while looping itself.
for index, letter in enumerate(letters):
    print(index, letter)
# 0 a
# 1 b
# 2 c
# 3 d
