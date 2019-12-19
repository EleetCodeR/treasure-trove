try:
    age = int(input("Age:"))
    print("this wont be printed if exception is thrown.")
except ValueError as ex:
    print("Please Enter a valid age.")
    print(ex, type(ex))
else:
    print("No exception was thrown.")
print("Execution continues.")
