def dict_make(x):
    dic = {}
    for q in range(x):
        ls = input('Enter key <space> value: ').split()
        dic[ls[0]] = ls[1]
    return dic

dict1 = dict_make(int(input('Enter length of Dictionary: ')))

for key,value in dict1.items():
    print(f'{key} has the value {value}.')
