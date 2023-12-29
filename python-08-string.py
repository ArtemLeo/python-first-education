# String

name = "John"
age = 20

# concatenation / interpolation
print(name, "is", age)
print(name + " is " + str(age))
print(f"{name} is {age}")
print("--------------------------")

# multiline string
print('''This is ->
        -> multiline string!''')
print("--------------------------")

# len
a = "Michael"
b = "John"
print(a if len(a) > len(b) else b)
print("--------------------------")

# string index
s = "Hello World"
print(s[0])  # first letter
print(s[-len(s)])  # first letter
print(s[-1])  # last letter
print(s[len(s) - 1])  # last letter
print("--------------------------")

# string iteration
text = 'Hello world!'
for i in text:  # H e l l o   w o r l d !
    print(i, end=' ')
print()

for i in range(len(text) - 1, -1, -1):  # ! d l r o w   o l l e H
    print(text[i], end=' ')
print()
print("--------------------------")

# substring
a = 'abcd'
b = 'bc'
print(b in a)  # b in a ? True/False
print(a.index(b))  # what is the first index 'b' in 'a' ? if not = exception
print(a.find(b, 0, 5))  # what is the first index 'b' in 'a' ? if not = -1
print(a.rindex(b, 0, 4))  # what is the last index 'b' in 'a' ? if not = exception
print(a.rfind(b))  # what is the last index 'b' in 'a' ? if not = -1
print(a.startswith(b))  # start of 'a' = 'b'
print(a.endswith(b))  # finish of 'a' = 'b'
print("--------------------------")

# upper/lower
string = 'hello python!'
print(string.upper())
print(string.lower())
print(string.capitalize())
print("--------------------------")

# slices
string_numbers = '0123456789'
print(string_numbers[1:5])  # 1234
print(string_numbers[1:])  # 123456789
print(string_numbers[:-2])  # 01234567
print(string_numbers[0:8:2])  # 0246
print(string_numbers[::-1])  # reverse 9876543210
print("--------------------------")

# int to str
num = 12345  # 12345
string_num = str(num)  # '12345'
print(string_num)
print("--------------------------")

# count (quantity of this value in the string)
number = '10111011011110'
print(f'Count of 1 in string = {number.count('1')}')
print('-------------------------')

# input()
print(input("Enter your text: "))  # input is always = 'str'
print(int(input("Enter your number: ")))  # so, if you need to get input 'int'
