# Scrolling text
def scrolling_text(string: str) -> list:
    list = []
    if len(string) == 0:
        return list
    for i in range(len(string)):
        part = string[i:] + string[:i]
        list.append(part.upper())
    return list


print(scrolling_text('robot'))
