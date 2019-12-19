from timeit import timeit
# NOTE : we can use timeit module to time the execution of python code.
# for this we need to enclose our code in """ (triple codes as multiline string)
# and assign it to a variable so that it can be passed to timeit function for execution.


code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass    
"""

code3 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
print("first code =", timeit(code1, number=10000))
print("second code =", timeit(code2, number=10000))
print("third code =", timeit(code3, number=10000))

# first code = 4.7499337
# second code = 0.0066123000000004595
# third code = 0.002125600000000283

# we can see huge difference in above values.
# This difference can be felt when performance and scalability is required by the application.
