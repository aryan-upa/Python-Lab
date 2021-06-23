def dict_make(x):
    dc = {}
    for q in range(x):
        ls = input('Enter key <space> value: ').split()
        dc[ls[0]] = ls[1]
    return dc


dic = dict_make(int(input('Enter length of Dictionary: ')))

print('The sum of all the values are: ',sum([int(q) for q in dic.values()]))
print('The sum of all the keys are: ',sum([int(q) for q in dic.keys()]))
