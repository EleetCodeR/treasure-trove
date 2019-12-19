browsing_session = []

browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

# Pop to get item at Top of stack(tos)
last = browsing_session.pop()
print(last)
print("redirect", browsing_session)

# Empty stack
if browsing_session:
    print("Stack empty")
# as [] empty list is boolean False.

# to get item at tos.
if not browsing_session:
    browsing_session[-1]
