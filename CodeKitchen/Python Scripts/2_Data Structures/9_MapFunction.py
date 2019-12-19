items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# #<1>  To separate prices from above list into a new list; Conventional way-
# prices = []
# for item in items:
#     prices.append(item[1])

# #<2>
# x = map(lambda item: item[1], items)
# print(x)  # <map object at 0x000001B4F64DFE48>
# # NOTE : map returns an iterable object. which can be looped or converted to a list.

# #<3>
# x = map(lambda item: item[1], items)
# for item in x:
#     print(item)
# # Above code will print all the items of the list returned by map.

# #<4> Converting map object to list using list method.
prices = list(map(lambda item: item[1], items))
for item in prices:
    print(prices)
