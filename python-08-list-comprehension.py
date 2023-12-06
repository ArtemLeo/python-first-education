# List comprehension
# Change current list
a = [1, 2, 3, 4, 5]
print('Current list: ' + str(a))

a1 = []
for i in a:  # with for (hard)
    a1.append(i * 2)
print('List create with for loop: ' + str(a1))

a2 = [i * 2 for i in a]  # list comprehension
print('List create with list comprehension: ' + str(a2))
print('------------------------------')

# Create by range()
b1 = [i * 3 for i in range(1, 6)]  # list comprehension
print('List create with list comprehension: ' + str(b1))

b2 = []  # with for (hard)
for i in range(1, 6):
    b2.append(i * 3)
print('List create with for loop: ' + str(b2))
print('------------------------------')

# Element filtration
c = [1, 10, 12, 4, 3, 20, 55]
c1 = []
for i in c:
    if i < 10:
        c1.append(i)
print('List create with for loop: ' + str(c1))

c2 = [i for i in c if i < 10]
print('List create with list comprehension: ' + str(c2))
print('------------------------------')

# Combination (filtration + changing list elements)
d = [i ** 2 for i in range(1, 10) if i > 5]
print('List create with list comprehension: ' + str(d))
