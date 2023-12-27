# Remove vowels letters

string = "captain"


def remove_vowels(document: str) -> str:
    result = ''
    for i in document:
        if i not in "aeiouyAEIOUY":
            result += i
    return result


print(remove_vowels(string))  # cptn
