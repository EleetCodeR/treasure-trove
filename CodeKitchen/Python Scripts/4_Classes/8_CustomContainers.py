class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


# Why Make custom containers ?
# Why not simple use a dictionary here?
# Bcause; we can add intelligence/customizations to basic in-built data structures using this approach.
# eg. here add method can tell all the tags are same by converting to lowercase and then comparing:
# normal dictionary would return 4 different tags.
cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("PyThOn")
cloud.add("PYTHON")
print(cloud.tags)


# To be able to read tags using subscript notation [ ], we need to implement respective magic method.
# To make our class Subscriptable; implment magic method called __getitem__(self,key) .
print(cloud["python"])

# return 0 as per our implementation; std.dictionary would throw error, as the key/tag is not present.
print(cloud["pithon"])

#  __getitem__  magic method only helps get the value using subscript , we can not set the value.
# to set the value using subscript , implement __setitem__(self,key,value) .
cloud["python"] = 10
print(cloud["python"])

len(cloud)  # implement __len__(self)
# to make our container iterable , we need to return iterator object using in-built function iter and implement __iter__
# iterator-object is an object that walks a container and gets one item at a time.
