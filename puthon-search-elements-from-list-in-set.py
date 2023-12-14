# Search elements from a list in a set

def search_elements(input_set, input_list):
    if len(input_list) > len(input_set):
        return False
    for i in input_list:
        if i in input_set:
            continue
        else:
            return False
    return True


print(search_elements({1, 2, 10, 4, 5, 'hello'}, [5, 2]))
