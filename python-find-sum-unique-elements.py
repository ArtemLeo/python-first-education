# Find the sum of unique elements in the list
my_list = [1, 1, 2, 5, 10, 10, 10]

my_set = set(my_list)
result = 0
for i in my_set:
    result += i
print('Sum of unique elements in the list = ' + str(result))

# or one-line solution
result = sum(set(my_list))
print('One-line solution = ' + str(result))
