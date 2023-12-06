# Mirror multi list
current_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


def mirror_multi_list(some_list):
    for list in some_list:
        for element in range(len(list) // 2):
            temp = list[element]
            list[element] = list[len(list) - 1 - element]
            list[len(list) - 1 - element] = temp
    return some_list


print(mirror_multi_list(current_list))
