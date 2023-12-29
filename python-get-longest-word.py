# Get the longest word in list

words = ["one", "two", "three", "four", "five"]


def get_the_longest_word(value):
    if len(words) == 0:
        return ""
    longest = words[0]
    for i in range(1, len(words)):
        if len(words[i]) > len(longest):
            longest = words[i]
    return longest


print(f'The longest word is: {get_the_longest_word(words)}')
