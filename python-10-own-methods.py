# Own methods
# Operator "return"
# """ Documentation comment """

# create method (without arguments)
def show_info():
    """Method show_info"""
    print('Displayed some information!')


# use current method
print(show_info.__doc__)
show_info()
print('---------------------------')


# create method (with arguments)
def show_input_num(value):
    """Method show_input_num"""
    print('Your input is ' + str(value))


# use current method
print(show_input_num.__doc__)
number = float(input('Enter any number: '))
show_input_num(number)
print('---------------------------')


# operator "return"
def multiply(value1, value2):
    """Method multiply"""
    return value1 * value2


# use current method
print(multiply.__doc__)
result = multiply(2, 2)
print('Result of multiply method = ' + str(result))
print('---------------------------')


# create method min_max
def show_max_number(num1, num2):
    """Method show_max_number"""
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2


# use current method
print(show_max_number.__doc__)
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
result = show_max_number(x, y)
print('Result of "show_max_number" method = ' + str(result))
print('---------------------------')


# method as an argument
def show_name(name):
    """Method show_name"""
    print('Hi, ' + name + '!')


def input_name():
    name = input('Enter your name: ')
    return name


print(show_name.__doc__)
show_name(input_name())
