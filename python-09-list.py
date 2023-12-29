# List methods: append, insert, count, reverse, remove, pop, sort, index, extend
# List function: len, min, max
import math

list_example = [1, 2, 3, [77, 88, 99], 4, 5]
print(list_example)

# output by index
print(list_example[1])
print(list_example[3][0])
print('-------------------------')

# list + list / extend([0, 0, 0, 0])
another_list = list_example + [6, 7, 8, 9]
print(another_list)  # list.extend([6, 7, 8, 9, 0])
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

# find index of element
print(f'Index of value 5 in list = {numbers.index(5)}')
print('-------------------------')

# append (add the value to the end of the list)
values = []
values.append('Hello')
values.append(5)
values.append([1, 2, 3])
print('Append elements in list: ' + str(values))
print('-------------------------')

# insert (add a value to the list by index)
values.insert(2, 100)
print('Insert 100 in list: ' + str(values))
print('-------------------------')

# sort
num = [3, 7, 2, 9, 4, 6, 1]
num.sort()  # sorting: min -> max
print(f'sort(): {num}')
num.sort(reverse=True)  # sorting: max -> min
print(f'sort(reverse=True): {num}')
print('-------------------------')

# count (quantity of this value in the list)
print('Count of 9 in list = ' + str(numbers.count(9)))
print('-------------------------')

# reverse
print('Before reverse: ' + str(numbers))
numbers.reverse()
print('After reverse: ' + str(numbers))
print('-------------------------')

# remove (delete by value, not by index)
values.remove(5)
print('Remove some element: ' + str(values))
print('-------------------------')

# pop (delete last list value pop() or by index pop(2))
values.pop()
print('pop = delete last list value ' + str(values))
print('-------------------------')

# slices
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(arr[2:5])  # it a new list
print(arr[:])  # create copy of list
print(arr[1:7:2])  # step in list
print(arr[::-1])  # reverse list
print('-------------------------')

# length
print('List length = ' + str(len(values)))
print('-------------------------')

# min, max
print('Min value: ' + str(min(numbers)))
print('Max value: ' + str(max(numbers)))
print('-------------------------')

# import math
round(12.1)  # 12 -> rounds to the nearest integer (up or down)
math.floor(12.1)  # 12 -> rounds down (to the nearest smaller integer)
math.ceil(12.1)  # 13 -> rounds up (to the nearest higher integer)
math.trunc(12.1)  # 12 -> "cuts off" the fractional part

# multidimensional lists
multi_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(multi_list)
print('Get element in multi-list: ' + str(multi_list[1][1]))
print('-------------------------')

# display multidimensional lists
for list in multi_list:
    print(list)
print('-------------------------')

for list in multi_list:
    for element in list:
        print(element, end=' ')
    print()
print('-------------------------')


def display_multi_list(some_list):
    for i in range(len(some_list)):
        for j in range(len(some_list[i])):
            print(some_list[i][j], end=' ')
        print()


display_multi_list(multi_list)
