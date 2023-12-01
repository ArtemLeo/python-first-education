# List methods: append, insert, count, reverse, remove
# List function: len, min, max

list_example = [1, 2, 3, [0, 0, 0], 4, 5]
print(list_example)

# index output
print(list_example[1])
print(list_example[3][0])
print('-------------------------')

# list + list
another_list = list_example + [6, 7, 8, 9]
print(another_list)

print(list_example + another_list)
print('-------------------------')

# string
text = 'Hello'
print('Show some index in string-list: ' + str(text[1]))
print('-------------------------')

# in (contain), not in
numbers = [9, 2, 5, 7, 1, 8, 0, 9, 3, 1]
if 9 in numbers:
    print('Yes')
else:
    print('No')

if 5 not in numbers:
    print('Not in')
else:
    print('In')
print('-------------------------')

# append
values = []
values.append('Hello')
values.append(5)
values.append([1, 2, 3])
print('Append elements in list: ' + str(values))
print('-------------------------')

# insert
values.insert(2, 100)
print('Insert 100 in list: ' + str(values))
print('-------------------------')

# count
print('Count of 9 in list = ' + str(numbers.count(9)))
print('-------------------------')

# reverse
print('Before reverse: ' + str(numbers))
numbers.reverse()
print('After reverse: ' + str(numbers))
print('-------------------------')

# remove
values.remove(5)
print('Remove some element: ' + str(values))
print('-------------------------')

# length
print('List length = ' + str(len(values)))
print('-------------------------')

# min, max
print('Min value: ' + str(min(numbers)))
print('Max value: ' + str(max(numbers)))
print('-------------------------')

