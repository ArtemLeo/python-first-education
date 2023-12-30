from math import floor


def get_speed_statistic(test_results: list) -> list:
    list = []
    if len(test_results) == 0:
        return [0, 0, 0]

    list.append(test_results[0])
    for i in test_results:
        if i < list[0]:
            list[0] = i
    list.append(test_results[0])
    for i in test_results:
        if i > list[1]:
            list[1] = i
    total = 0
    for i in test_results:
        total += i
    average = floor(total / len(test_results))
    list.append(average)
    return list


print(get_speed_statistic([8, 9, 3, 12]))


# or
def get_speed_statistic2(test_results: list) -> list:
    list = []
    if len(test_results) == 0:
        return [0, 0, 0]
    list.insert(0, min(test_results))
    list.insert(1, max(test_results))
    sum_speed = sum(test_results)
    middle_speed = floor(sum_speed / len(test_results))
    list.insert(2, middle_speed)
    return list


print(get_speed_statistic2([8, 9, 3, 12]))
