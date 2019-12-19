list1 = [1, 2, 3]
list2 = [10, 20, 30]
# we need a new list =[(1,10),(2,20),(3,30)] likewise.
# we can not use map function as it uses one list.
# WE CAN DIRECTLY USE ZIP FUNCTION IN PYTHON TO COMBINE LIST INTO LIST OF TUPLES.

combined = list(zip(list1, list2))
str_combined = list(zip("abc", list1, list2))
print(combined)
print(str_combined)
