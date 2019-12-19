#  NOTE:
# "With-Statement" can be used with only those object which supports "context management protocol".
# i.e, Which has __enter__ and __exit__ these magic methods.
# USE : if we open any external resource (say file) using with statement. Python interpreter automatically closes them.
# so finally clause is not required.

try:
    # For multiple resources:- with open("app.py") as file, open("another.py") as target:
    with open("app.py") as file:
        print("File Opened.")

    age = int(input("Age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("Please Enter a valid age.")
else:
    print("No exception was thrown.")
