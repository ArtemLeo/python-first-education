# Split string

def split_string(string: str) -> list:
    list = []
    for i in range(0, len(string), 2):
        part = string[i:i + 2]
        if len(part) < 2:
            part += '_'
        list.append(part)
    return list


print(split_string("12345"))
