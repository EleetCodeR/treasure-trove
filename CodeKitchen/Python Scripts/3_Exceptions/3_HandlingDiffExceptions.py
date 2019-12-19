# try:
#     age = int(input("Age:"))
#     xfactor = 10/age
# except ValueError:
#     print("Please Enter a valid age.")
# except ZeroDivisionError:
#     print("Age can not be 0.")
# else:
#     print("No exception was thrown.")


# NOTE : defining mulitple exceptions:
try:
    age = int(input("Age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("Please Enter a valid age.")
else:
    print("No exception was thrown.")
