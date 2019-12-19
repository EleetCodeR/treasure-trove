firstname = "Vishal"
lastname = "Ramane"
# String concatenation
print(firstname+" "+lastname)

# But formatted string is better approach than concatenation.
# formatted string is an expression; is evaluated at runtime.
fullname = f"{firstname} {lastname}"
print(fullname)

# Any valid expression can be put in curly  braces
formatted_str = f"{len(firstname)} { 2 + 2}"
print(formatted_str)
