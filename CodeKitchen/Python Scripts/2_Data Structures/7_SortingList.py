###################### SORTING SIMPLE LISTS :NUMBERS ############################################
numbers = [3, 51, 8, 2, 6]

numbers.sort()
print(numbers)
numbers.sort(reverse=True)

# NOTE: sort method modifies original list.
print(sorted(numbers))
print(sorted(numbers, reverse=True))
# NOTE: sorted method takes an iterable and returns a new list with sorted items.

###################### SORTING COMPLEX LISTS :TUPLES ############################################

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
# NOTE : sort method can not sort list of tuple by default, we therefore define a function;
#  which will return an item on which we want to sort the list here.
# observe that we are not calling this function from sort method, instead only reference is given as key.
# This will call sort_item function for every item while iterating list return the key and sort the list.

#################################################################################################

# NOTE : the way above function is implemented is a bit ugly; for better way we use lambda function
# check Lambda Functions file.
