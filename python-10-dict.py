# Dictionary (Map)

# create dict
dict = {'John': '25', 'Sam': '21'}
print(dict)
print('--------------------------------')

# len()
print('len of dict = ' + str(len(dict)))
print('--------------------------------')

# add element (key:value)
dict['Kate'] = 27
print(dict)
print('--------------------------------')

# get a value by key
print('John is ' + str(dict['John']) + ' years')
dict['John'] = 26
print('And now, John is ' + str(dict['John']) + ' years')
print('--------------------------------')

# for loop
for key, value in dict.items():
    print('Key: ' + str(key) + '; Value: ' + str(value))
print('--------------------------------')
