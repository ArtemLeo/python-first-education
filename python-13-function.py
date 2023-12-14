# Methods
# Annotation of arguments
# Operator "return"
# Operator "pass"
# """ Documentation comment """

# create function (without arguments)
def show_info():
    """function (without arguments)"""
    print('Displayed some information!')


# use function (without arguments)
print(show_info.__doc__)
show_info()
print('---------------------------')


# create function (with arguments)
def show_input_num(value):
    """function (with arguments)"""
    print('Your input is ' + str(value))


# use function (with arguments)
print(show_input_num.__doc__)
number = float(input('Enter any number: '))
show_input_num(number)
print('---------------------------')


# annotation of arguments
# operator "pass"
def show_annotation(name: str, age: int) -> int:
    pass


# create function with one "return" operator
def multiply(value1, value2):
    """function with one "return" operator"""
    return value1 * value2


# use function with one "return" operator
print(multiply.__doc__)
result = multiply(2, 2)
print('Result of multiply method = ' + str(result))
print('---------------------------')


# create function with several operators "return"
def show_max_number(num1, num2):
    """function with several operators "return"""
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2


# use function with several operators "return"
print(show_max_number.__doc__)
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
result = show_max_number(x, y)
print('Result of "show_max_number" method = ' + str(result))
print('---------------------------')


# create function as an argument
def show_name(name):
    """function as an argument"""
    print('Hi, ' + name + '!')


def input_name():
    name = input('Enter your name: ')
    return name


# use function as an argument
print(show_name.__doc__)
show_name(input_name())
print('---------------------------')

# find body mass index
name1 = 'John'
height1 = 1.90
weight1 = 82

name2 = 'Ben'
height2 = 1.72
weight2 = 93

name3 = 'Sam'
height3 = 1.61
weight3 = 78


def bmi_calculator(name, height, weight):
    bmi = int(weight / (height ** 2))
    if bmi < 25:
        return "bmi = " + str(bmi) + ',so ' + name + " doesn't have"
    else:
        return "bmi = " + str(bmi) + ',so ' + name + " has a fat"


bmi1 = bmi_calculator(name1, height1, weight1)
bmi2 = bmi_calculator(name2, height2, weight2)
bmi3 = bmi_calculator(name3, height3, weight3)

print(bmi1)
print(bmi2)
print(bmi3)
