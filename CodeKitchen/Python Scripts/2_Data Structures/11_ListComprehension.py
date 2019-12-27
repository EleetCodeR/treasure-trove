items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

#prices = list(map(lambda item: item[1], items))

# # LIST COMPREHENSION : Above code can written cleanly and simply as,
# [<expression> for <variable/iterator> in <iterable>]

prices = [item[1] for item in items]
print(prices)

#Filtered = list(filter(lambda item: item[1] >= 10, items))
# [<expression> for <variable/iterator> in <iterable> if <condition>]

Filtered = [item for item in items if item[1] >= 10]
print(Filtered)

# NOTE : LIST COMPREHENSION is a Python concept and is recommended for above scenarios.
