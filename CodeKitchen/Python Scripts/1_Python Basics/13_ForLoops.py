# # In python,  String is an ITERABLE type.
# for x in "Python":
#     print(x)

# # List is ITERABLE.
# for x in ['a', 'b', 'c']:
#     print(x)

# # we can iterate over numbers using inbuilt function "range".
print("Type 1")
for x in range(5):  # range function by default starts from 0 , till 'stop'-1
    print(x)

print("Type 2")
for x in range(2, 5):  # will start from 2, instead of 0.
    print(x)

print("Type 3")
for x in range(0, 10, 2):  # 0 to 10 , increments by 2 steps (default 1 )
    print(x)

# NOTE:  1 St Arg : Start, 2nd Arg : Stop., 3rd Arg : Step.
# RANGE function does not take large values as argument.eg. range(5000000) is not supported.
# As memory it can address is limited.
# RANGE function  returns object of 'range' type only. which is iterable type. eg.
print(type(range(5)))
print([1, 2, 3, 4, 5])
