subject = "Data structures and Algorithms"
print(len(subject))  # len  (length) is common function not just for strings.
print(subject[0])   # returns first character of the string.
print(subject[-2])  # negative index starts from last character -1 and so on.
# substring:from default index 0 uptill the (mentioned_index)-1, i.e excluding last index; here 3
print(subject[0:3])
print(subject[:3])  # same as above.(deafult start index is 0)
print(subject[0:])  # prints from starting index 0 to last.
print(subject[:])  # prints whole string.
print(subject[3:])  # prints from 3rd index onwards.

# since string is immutable everytime new memory is assigned for string manipulation.
print(id(subject))
print(id(subject[0]))
