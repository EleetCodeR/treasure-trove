def increment(number, by):
    # we can return multiple values at a time in Python, eg.a tuple.
    return (number, number+by)


# 2 line separation is needed after a function definition by convention. (pep8)

print(increment(2, 3))
# o/p : (2,5)
# NOTE: a tuple is like a list, which is read-only / immutable.
# for LIST [] brackets are used ; while  for tuple () brackets.
# eg. number = (1,2,3)

# NOTE: Keyword Argument:
# use argument = parameters in function call,i.e,binding arguments by mentioning parameters.
# if keyword arguments are used while functin call , the order of parameters need not match function prototype.
print(increment(by=3, number=2))

# NOTE: default Value of parameters can be set using keyword arguments while defining function itself.
# eg. def increment(number, by=1):
# function call : increment(2)

# NOTE: TYPE ANNOTATION AND PARAMETER ANNOTATION.
# we know we can annotate a variable , val:int = 2.
# similarly, (below example: para.annotn + default val.)
# These annotations do not impose typechecking .


def increment2(number: int, by: int = 2):
    return (number, number+by)


print(increment2(2))

# NOTE: function Return type.


def increment3(number: int, by: int = 2) -> tuple:
    return (number, number+by)


print(increment3(2))
