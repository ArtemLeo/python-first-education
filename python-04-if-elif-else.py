# Conditional operators: if, else, elif
# Operators: and, or, not

# if
a = 10
if a == 10:
    print('a == 10')

# if-else
b = 5
if b >= 10:
    print('b == 10')
else:
    print('b != 10')

# if-elif
c = 10
if c == 20:
    print('c == 20')
elif c == 15:
    print('c == 15')
elif c == 10:
    print('c == 10')
else:
    print('None of the choices')
print('--------------------------------')

# Operators: and, or, not
x = 1
y = 2

if x == 1 and y == 2:
    print('x = 1, y = 2')

if x == 1 or y == 2:
    print('x = 1, y = 2')

if x == 1 and (y == 1 or y == 2):
    print('x = 1, y = 2')

if not x == 2:
    print('x = 1, y = 2')
print('--------------------------------')

# ternary operator
age = 18
ternary = "Adult" if age >= 18 else "Child"
print(ternary)
