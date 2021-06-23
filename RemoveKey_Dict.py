def dict_make(x):
    dic = {}
    for q in range(x):
        ls = input('Enter key <space> value: ').split()
        dic[ls[0]] = ls[1]
    return dic

dict1 = dict_make(int(input('Enter length of Dictionary: ')))
print('Dictionary before change : ',dict1)

inp = input('Enter the key to be removed: ')
dict1.pop(inp)
print('Dictionary after change : ',dict1)