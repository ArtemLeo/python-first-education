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

# list walk (forEach)
numbers = [20, 48, 91, 73, 37]
for i in numbers:
    print('Value in list numbers: ' + str(i))
print('--------------')

# list walk (by index)
for i in range(len(numbers)):
    print('Value in list numbers: ' + str(numbers[i]))
print('--------------')

# reverse variable/list walks (hard)
for i in range(8, 0, -1):
    print(i, ' ')
print('--------------')

list = [10, 20, 30, 40, 50, 60, 70]
for i in range(len(list) - 1, -1, -1):
    if list[i] == 4:
        break
    else:
        print(list[i])
print('--------------')

# nested loops
for i in range(len(numbers)):
    for j in range(i + 1):
        print(numbers[i])
