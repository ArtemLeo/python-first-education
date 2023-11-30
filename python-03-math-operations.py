# Math operations: +, -, *, /, **, %, unary minus, rounding
# Comparison operators: >, <, >=, <=, ==, !=, lexical comparison

import math

a = 10
b = 5
print('a = ' + str(a) + '\nb = ' + str(b))
print('-------------')

c = a + b
print('"a + b" = ' + str(c))
print('-------------')

d = a - b
print('"a - b" = ' + str(d))
print('-------------')

e = a * b
print('"a * b" = ' + str(e))
print('-------------')

f = a / b
print('"a / b" = ' + str(f))
print('-------------')

g = a ** 3
print('"' + str(a) + ' in third degree" = ' + str(g))
print('-------------')

h = a % 3
print('"' + str(a) + ' % 3" = ' + str(h))
print('-------------')

i = 10
i = -i
print('"x" = 10\nUnary minus of "x" = ' + str(i))
print('-------------')

j = 1.2345
print('"j" = ' + str(j))
print('Rounding of "j" = ' + str(round(j)))
print('-------------')

print('math.ceil of "j" = ' + str(math.ceil(j)))
print('math.floor of "j" = ' + str(math.floor(j)))
print('-------------')

# Lexical comparison
print('Lexical comparison: ')
print('Test' > 'Text')