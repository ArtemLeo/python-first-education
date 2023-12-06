# Create multi list
def create_multi_list(m, n):
    temp_list = []
    for i in range(m):
        inner_list = []
        for j in range(n):
            inner_list.append(0)
        temp_list.append(inner_list)
    return temp_list


result_list = create_multi_list(5, 10)
print(result_list)
print('-----------------------------')


def print_multi_list(some_list):
    for list in some_list:
        for element in list:
            print(element, end=' ')
        print()


print_multi_list(result_list)
