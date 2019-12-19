# NOTE: In Python we can inherit from build in types.
# so we inherit all features of built in types and extend/add more as we require.

# Extend str :


class Text(str):
    def duplicate(self):
        return self+self

# Extend List :


class TrackableList(list):
    # overriding append method
    def append(self, object):
        print("Append Called")
        # now calling append method of the base class.
        super().append(object)


text = Text("Python")
print(text.lower())
print(text.duplicate())

list = TrackableList()
list.append("1")
print(list)
