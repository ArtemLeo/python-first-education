# Create dict by list
list = ['first', 1, 2, 3, 'second', 10, 20, 'third', 15, 56, 70, 'fourth', -50]

dict = {}
count = None
for i in list:
    if type(i) == str:
        dict[i] = []
        count = i
    else:
        dict[count].append(i)
print(dict)

print(dict['first'])
print(dict['second'])
print(dict['third'])
print(dict['fourth'])
