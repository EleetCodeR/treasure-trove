x = 1
# Primitive types (int,bool,string etc.) are 'immutable'.(can not be modified once initialized.)
print(f"X :{id(x)}")
x = x+1
# when its value is modified, a new memory address is assigned instead.
print(f"X :{id(x)}")

# List is mutable.
array = [1, 2, 3]
# observe how List/Array is denoted differently in python.
print(f"Array:{id(array)}")
array.append(4)
# hence it can be modified and memory address remains same.
print(f"Array:{id(array)}")
