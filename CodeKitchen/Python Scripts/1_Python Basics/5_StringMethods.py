course = "  Python Programming "
print(course.upper())  # all uppercase laters
print(course.lower())  # all lowercase laters
print(course.title())  # Starting later of each word is capitalized
#  strip - Removes trailing and leading white spaces and returnes the string.
print(course.strip())
print(course.lstrip())  # strip from left
print(course.rstrip())  # strip from right

print(course.find("Pro"))
print(course.find("o", 1, 13))

print(course.replace("P", "T"))
print(course)  # as string is immutable type. Original string is unchanged.

print("Progamming" in course)  # returns bool type
print("Programming" in course)
