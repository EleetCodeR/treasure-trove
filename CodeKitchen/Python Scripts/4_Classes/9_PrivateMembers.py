class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("PyThOn")
cloud.add("PYTHON")

print(cloud["PYTHON"])   # o/p :- 4

# print(cloud.__tags["PYTHON"])  # KeyError
# This error occured because we could directly access attribute "tags".
# To make this attribute private, use prefix __ (double underscore.) for attri."tag"

# NOTE : So to make attribute/method as private prefix them with __ (double underscore.)
# NOTE : however in python, making members private by this prefix is not a security feature, but a convention(to prevent accidental access);
# Because we can still access private members using __dict__ method, which is defined by default for every class/object;
# It consists of all the attributes of that particular class;
# The attributes in this dict. are automatically prefixed with classname by python interpreter.
print(cloud.__dict__)  # o/p :-  {'_TagCloud__tags': {'python': 4}}
print(cloud._TagCloud__tags)  # returns our dictionary 'tags'
