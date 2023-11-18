# String

# String output/display
print('Hello Python!')
print("Hello Python!")
print('-----------------')

# To the new line
print('Hello\nPython!')
print('''Hello
Python
!''')
print('-----------------')

# Shielding
print("Hello \"Python\"")
print('Hello "Python"')
print('-----------------')

# String concatenation
name = 'John'
age = 20
print('Hello!\nMy name is ' + name + '.\nI`m ' + str(age) + ' years old!')
print('-----------------')

# Multiplication by string
string = 'Hello'
print(string * 5)

name = input('What is your name?: ')
count = input('How many times need to show this information?: ')
print('Your name is ' + name + '!')
print('And I show this information ' + count + ' times:\n' + name * int(count))
print('-----------------')

# input()
name = input('Enter your name: ')
age = input('How old are you: ')
print('Your name is ' + name + '.\nYou are ' + age + ' yeas old!\nWelcome ' + name + '!')
print('-----------------')
