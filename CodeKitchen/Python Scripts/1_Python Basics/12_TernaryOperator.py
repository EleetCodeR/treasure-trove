age = 22
# conventionally:
if age >= 18:
    message = "Eligible."
else:
    message = "Not eligible."

# Using Ternary operator, above code can be written in compact form.
# in other languages : message = age>= 18 ? "Eligible." : "Not eligible."
# in Python,
message = "Eligible." if age >= 18 else "Nor eligible."

print(message)
