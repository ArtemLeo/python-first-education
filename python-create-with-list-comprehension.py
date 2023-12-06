# Create list with list comprehension
# Example with int
list = [num * 2 for num in range(10, 1, -1) if num % 2 == 0]
print(list)

# Example with string
words = ['hello', 'hey', 'goodbye', 'guitar', 'piano']
words_filtered = [word + '.' for word in words if len(word) > 5]
print(words_filtered)
