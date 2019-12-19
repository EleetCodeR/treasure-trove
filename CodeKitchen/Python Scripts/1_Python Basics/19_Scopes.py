# NOTE 1>: In Python we have function scope and File/Global scope.
#  we do not have block scope like in Java-like languages;
# meaning a variable defined in an IF-block will be still accessible outside of IF-block.

message = "a"  # Global
print(message)


def greet():
    # global message  # will access global variable instead, see NOTE 3.
    message = "b"  # local WHY?? See NOTE 2.
    print(message)
    if True:
        message = "c"  # local
        print(message)
    print(message)  # local


greet()
print(message)  # Global

# NOTE 2>: By default Python enforces good programming practices,
# it doesn't let you erroneously modify Global variable inside a function.
# (can cause problems in other functions using the same variable.)
# So, it defines a new variable in local scope instead.
# NOTE 3>:However to modify global variable in a function we can use keyword "global" to specify it's global scope.
