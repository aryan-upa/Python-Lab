def dict_make(x):
    dic = {}
    for q in range(x):
        ls = input('Enter key <space> value: ').split()
        dic[ls[0]] = ls[1]
    return dic

dc = dict_make(int(input('Enter the number of elements in the Dictionary : ')))
# dc = {'a':'1','b':'2','c':'3'}

k = list(map(int,dc.values()))
print('Minimum value is : ',min(k))
print('Maximum value is : ',max(k))
