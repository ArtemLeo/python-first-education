# Own methods
# Operator "return"

# create method (without arguments)
def show_info():
    print('Displayed some information!')


# use current method
show_info()
print('---------------------------')

# create method (with arguments)
number = float(input('Enter any number: '))


def show_input_num(value):
    print('Your input is ' + str(value))


# use current method
show_input_num(number)
print('---------------------------')


# operator "return"
def multiply(value1, value2):
    return value1 * value2


# use current method
result = multiply(2, 2)
print('Result of multiply method = ' + str(result))
print('---------------------------')


# create method min_max
def show_max_number(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2


# use current method
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
result = show_max_number(x, y)
print('Result of "show_max_number" method = ' + str(result))
