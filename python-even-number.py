# Even number

import random

list = []
for i in range(10):
    list.append(random.randint(10, 100))

print('Random list: ' + str(list))


def even_numbers(list_value):
    even_list = []
    for j in list:
        if j % 2 == 0:
            even_list.append(j)
    return even_list


print('Even numbers list: ' + str(even_numbers(list)))
