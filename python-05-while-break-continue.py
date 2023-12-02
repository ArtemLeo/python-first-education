# Loops: while
# Operators: break, continue

# while
x = 1
while x <= 5:
    print('x = ' + str(x))
    x += 1
print('----------------------')

# break
y = 15
count = 1
while True:
    print('while "True", count = ' + str(count))
    count += 1
    y -= 1
    if y <= 1:
        break
print('----------------------')

# continue
i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        print(i)
    else:
        continue
print('----------------------')

# walk of list
numbers = [34, 12, -93, 48, 72, -4]
i = 0
sum = 0
while i < len(numbers):
    if numbers[i] < 0:
        sum += numbers[i]
    i += 1
print(sum)
