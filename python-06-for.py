# For (loop/cycle)

# range
for i in range(11):
    if i % 2 == 0:
        print(i)
    else:
        continue
print('--------------')

for j in range(1, 11, 2):
    print(j)
print('--------------')

# list walk
numbers = [20, 48, 91, 73, 37]
for i in numbers:
    print('Value in list numbers: ' + str(i))
print('--------------')

# reverse list walks (hard)
list = [2, 3, 5, 9, 3, 6]
for i in range(len(list) - 1, -1, -1):
    if list[i] == 5:
        break
    else:
        print(list[i])
