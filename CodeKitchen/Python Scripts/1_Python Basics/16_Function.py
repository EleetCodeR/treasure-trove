def increment(number, by):
    # we can return multiple values at a time in Python, eg.a tuple.
    return (number, number+by)


# 2 line separation is needed after a function definition by convention. (pep8)

print(increment(2, 3))
# o/p : (2,5)
# NOTE: a tuple is like a list, which is read-only / immutable.
# for LIST [] brackets are used ; while  for tuple () brackets.
# eg. number = (1,2,3)

# NOTE: Keyword Argument. = binding arguments by mentioning parameters.
print(increment(2, by=3))

# NOTE: default Value of parameters can be set , while defining function itself.
# rg. def increment(number, by=1):
# function call : increment(2)

# NOTE: TYPE ANNOTATION AND PARAMETER ANNOTATION.
# we know we can annotate a variable , val:int = 2.
# similarly, (below example: para.annotn + default val.)


def increment2(number: int, by: int = 2):
    return (number, number+by)


print(increment2(2))

# NOTE: function Return type.


def increment3(number: int, by: int = 2) -> tuple:
    return (number, number+by)


print(increment3(2))
