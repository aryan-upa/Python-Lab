def dict_make(x):
    " A Function to define dictionaries. "
    dic = {}
    for q in range(x):
        ls = input('Enter key <space> value: ').split()
        dic[ls[0]] = ls[1]
    return dic

dict1 = dict_make(int(input('Enter length of 1st Dictionary: ')))
print(dict1)
dict2 = dict_make(int(input('Enter length of 2nd Dictionary: ')))
print(dict2)

# dict1 = {'A': '1', 'B': '2'}
# dict2 = {'C': '3', 'D': '4'}

# Method 1
dict3 = {}
dict3.update(dict1)
dict3.update(dict2)
print(dict3)

# Method 2
dict3 = {**dict1,**dict2}
print(dict3)

