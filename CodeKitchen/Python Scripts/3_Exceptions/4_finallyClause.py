try:
    file = open("app.py")
    age = int(input("Age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("Please Enter a valid age.")
else:
    print("No exception was thrown.")
finally:
    file.close()

# NOTE: Finally clause ensures that code in this clause is executed irrespective of exception
#  all the external resources are released in this clause.
