import random
import string

print(random.random())  # gives any random floating point number between 0 and 1
# enumerates between given range of integer numbers including endpoints.[a,b] cloed range.
print(random.randint(1, 10))
# randrange does not include endpoints
print(random.randrange(1, 10))

# Takes an array/sequence of elements and randomly picks an element from array.
print(random.choice([2, 4, 6, 8, 10]))
# Takes an array/sequence of elements and randomly picks an element from array.
print(random.choice(["An", "Arrray", "of", "Strings."]))

# picks one element ; randomly from sequence
print(random.choice("abcdefghijklmnopqrstuvwxyz0123456789"))
# to pick more than one element at random;
print(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=4))
# but this will return a list of size k,

# to join these element by a delimiter we can use join method from class string.
print("".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=4)))
# the string on which join is called is inserted between the iterable-string-object and result is given as a string.
# this can be used to generated random passwords from a given sequence.

print(",".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=4)))

# instead of typing all the characters like in above. we can use string class.
print(string.ascii_letters)  # all lowercase and uppercase letters.
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

# so a better way for generating random passwords is,
print("".join(random.choices(string.ascii_letters+string.digits, k=4)))

# RANDOM SHUFFLING AN ARRAY :
numbers = [1, 2, 3, 4, 5, 6]
random.shuffle(numbers)
print(numbers)
