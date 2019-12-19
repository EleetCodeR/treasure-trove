names = ["AJohn", "Mary"]
for name in names:
    if name.startswith("J"):
        print('Found.')
        break
else:
    print("Not Found.")
# NOTE:
# In FOR-ELSE block , else block is executed, if
# FOR loop completes by iterating all iterable items.
# i.e execution happens without a break statement.
