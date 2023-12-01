# Even number

import random

list = []
for i in range(10):
    list.append(random.randint(10, 100))

print('Random list: ' + str(list))


def even_num(list_values):
    result = []
    for j in list:
        if j % 2 == 0:
            result.append(j)
    return result


print('Evens list: ' + str(even_num(list)))
