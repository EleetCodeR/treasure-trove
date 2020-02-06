try:
    age = int(input("Age:"))
    print("this won't be printed if exception is thrown.")
except ValueError as ex:
    print("Please Enter a valid age.")
    print(ex, type(ex))
else:
    print("No exception was thrown.")

print("Execution continues.")
