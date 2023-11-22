# Own methods

# Create method (without arguments)
def show_info():
    print('Displayed some information!')


# Use current method
show_info()
print('---------------------------')

# Create method (with arguments)
number = float(input('Enter any number: '))


def show_input_num(value):
    print('Your input is ' + str(value))


# Use current method
show_input_num(number)
print('---------------------------')
