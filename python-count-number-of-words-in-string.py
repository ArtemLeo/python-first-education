# Count the number of words in a string

text = 'Hello bye python java program new bye adult python'
list = text.split(' ')
print(list)
print('-------------------------------')

dict = {}
count = 0
for i in list:
    if i not in dict:
        count += 1
        dict[i] = count
print(dict)
print(str(count) + ' words in this dictionary')
print('--------------------------------')

text2 = 'Hello bye python java program new bye adult python'
dict2 = {}
for i in text2.split(' '):
    if i not in dict2:
        dict2[i] = 1
    else:
        dict2[i] += dict2[i]
print(dict2)

count = 0
for k, v in dict2.items():
    if v == 1:
        count += v
    else:
        count += 1
print(str(count) + ' words in this dictionary')
