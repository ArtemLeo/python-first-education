# Get plan
import math


def get_plan(current_production: int, months: int, percent: int) -> list:
    list = []
    for i in range(0, months):
        list.insert(i, math.floor((percent / 100) * current_production) + current_production)
        current_production = list[i]
    return list


print(get_plan(10, 4, 30))
