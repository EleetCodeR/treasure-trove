# Find the most repeated character in given text.

from pprint import pprint
sentence = "This is a common interview question"

# sentence = sentence.lower()
# uniques = {*sentence}
# max = 0
# for x in uniques:
#     if x != ' ':
#         count = 0
#         for y in sentence:
#             if x == y:
#                 count = count + 1

#         if max < count:
#             max = count
#             char = x
# print("Most repeated char:", char, "Count:", max)


# Mosh's Solution:
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

# pprint is used for pretty print.(to control how to display o/p in terminal)
# pprint(char_frequency)
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
# pprint(char_frequency_sorted)
pprint(char_frequency_sorted[0])
