items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# Suppose we need to filter out the products with price >= 10 from the list.
# we can use filter function for this rather than conventional approach.
# filter function returns filter object which is iterable.
Filtered = list(filter(lambda item: item[1] >= 10, items))
print(Filtered)