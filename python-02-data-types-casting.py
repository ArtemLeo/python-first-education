# Data types
# Names types can´t start with a some number
# Type conversion / Casting: str(), int(), float(), list()
# isinstance()

a = 5  # int (integer number)
b = 3.14  # float (double number)
c = 'name'  # str (string type) or " "
d = True  # bool (boolean type) or False

e = (5, 'hello', 10.5)  # tup (tuple) -> (ordered, immutable type)
f = [5, 'hey', 10.5]  # list (ordered, mutable type)
g = {'a', 'b', 'c'}  # set (unordered type, unique objects)
h = {'key1': 'value', "key2": "value"}  # dict (dictionary) -> (unordered type -> key : value)

i = None  # NoneType

print(type(a))
print("Is type 'a' an int type? ->", isinstance(a, int))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
