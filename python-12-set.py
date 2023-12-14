# Set (unordered type, unique objects)
# create set
a = set()
print(type(a))

b = {1, 10, 5, 'hello'}
print(str(type(b)) + ' b = ' + str(b))
print('---------------------')

# add
a.add(1)
a.add(10)
a.add(5)
a.add('hello')
print(str(type(a)) + ' a = ' + str(a))
print('---------------------')

# from list to set (long method)
my_list = [1, 3, 6, 9, 1, 5, 2, 8, 4, 0, 4]
my_set = set()
for i in my_list:
    my_set.add(i)
print('from list to set: ' + str(my_set))

# from list to set (short method)
my_set = set(my_list)
print('from list to set: ' + str(my_set))

# from set to list
my_list = list(my_set)
print('from set to list: ' + str(my_list))
print('---------------------')

# operator 'in/not in' (contain: True/False)
print(5 in my_set)
print(7 not in my_set)
