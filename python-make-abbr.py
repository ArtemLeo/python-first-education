# Make abbr

string = "national aeronautics space administration"


def make_abbr(words: str) -> str:
    if len(words) == 0:
        return ''
    result = words[0].upper()
    for i in range(len(words)):
        if words[i] != ' ':
            continue
        else:
            result += words[i + 1].upper()
    return result


print(make_abbr(string))
