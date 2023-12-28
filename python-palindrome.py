# Palindrome
string = "Rotat or"


def is_werewolf(target: str) -> bool:
    new_target = ''
    for i in target:
        if i.isalnum():
            new_target += i
    reverse = new_target[::-1]
    if reverse.lower() == new_target.lower():
        return True
    else:
        return False


print(is_werewolf(string))
