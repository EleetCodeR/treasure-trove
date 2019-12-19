def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age

# calculate_xfactor(-1)
# here; not handling exception will result in crash.


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


# NOTE : It is not recommended to raise exception as it is costly.
