# Math operations: +, -, *, /, //, **, %, unary minus, rounding
# Comparison operators: >, <, >=, <=, ==, !=, lexical comparison
# Operator priority

import math

a = 10
b = 5
print('a = ' + str(a) + '\nb = ' + str(b))
print("a =", a, "b =", b)
print('-------------')

# addition
c = a + b
print('"a + b" = ' + str(c))
print('-------------')

# subtraction
d = a - b
print('"a - b" = ' + str(d))
print('-------------')

# multiplication
e = a * b
print('"a * b" = ' + str(e))
print('-------------')

# division
f = a / b
print('"a / b" = ' + str(f))
print('-------------')

# integer division
g = a // b
print('"a // b" = ' + str(g))
print('-------------')

# exponentiation
h = a ** 3
print('"' + str(a) + ' in third degree" = ' + str(h))
print('-------------')

# remainder of the division
i = a % 3
print('"' + str(a) + ' % 3" = ' + str(i))
print('-------------')

j = 10
j = -j
print('"x" = 10\nUnary minus of "x" = ' + str(j))
print('-------------')

k = 1.2345
print('"j" = ' + str(k))
print('Rounding of "j" = ' + str(round(k)))
print('-------------')

print('math.ceil of "j" = ' + str(math.ceil(k)))
print('math.floor of "j" = ' + str(math.floor(k)))
print('-------------')

# lexical comparison
print('Lexical comparison: ')
print('b' > 'a')  # True
print('abc' > 'aba')  # True
print('Test' > 'Text')  # False
print('sunny' > 'sun')  # True
print('a' > 'A')  # True
print('A' > 'a')  # false

# Operator priority:
# 1. ( )
# 2. **
# 3. *, /
# 4. +, -
