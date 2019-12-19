# Arbitrary Arguments : Parameter as Dictionary.
def save_user(**user):
    print(user)   # {'id': 1, 'name': 'admin'}


save_user(id=1, name="admin")
# by adding double asterisk to function parameter ,
# we can use "keyword-arguments" while calling function.
# as you can see in o/p , f'parameter acts as a 'Dictionary'.(key-value pairs.)
