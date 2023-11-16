# Calculator

print('Welcome to the Calculator 1.0')
print('-----------------------------')
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print('-----------------------------')
operation = input('What operation we will do?\nEnter (+, -, *, /): ')
print('-----------------------------')

if operation == '+':
    result = a + b
    print('RESULT = ' + str(result))
    print('-----------------------------')
elif operation == '-':
    result = a - b
    print('RESULT = ' + str(result))
    print('-----------------------------')
elif operation == '*':
    result = a * b
    print('RESULT = ' + str(result))
    print('-----------------------------')
elif operation == '/':
    if b != 0:
        result = a * b
        print('RESULT = ' + str(result))
        print('-----------------------------')
    else:
        print('Can`t divide dy "0"')
        print('------------------- ')
else:
    print('Incorrect operation selected!\nPlease enter (+, -, *, /):')
    print('----------------------------')

print('To perform another operation - RESTART the program!\nSee you later!')
input()
