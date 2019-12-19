# Using List.
def multiply(list):
    total = 1
    for number in list:
        total *= number
    return total


print(multiply([2, 3, 4, 5]))


# Using as Tuple.
def multiply2(*lis):
    total = 1
    for number in lis:
        total *= number
    return total


print(multiply2(2, 3, 4, 5))  # multiply2(2,3,4,5,....)

# NOTE : we sometimes need to pass arbitrary number of arguments to a function.
# We can use a list and iterate using for-loop, but there is even better way to do so.
# We can use Tuple(rather a function parameter acts as a tuple),
# just put asterisk (*) infront of parameter. (no need of square brackets like in list while call.)
