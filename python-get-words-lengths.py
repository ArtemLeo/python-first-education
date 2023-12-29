# Get words lengths

words = ['one', 'two', 'three', 'four', 'five']


def get_words_lengths(self: words):
    result = []
    for i in words:
        result.append(len(i))
    return result


print(get_words_lengths(words))
