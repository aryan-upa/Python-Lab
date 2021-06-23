def dict_make(x):
    dc = {}
    for q in range(x):
        ls = input('Enter key <space> value: ').split()
        dc[ls[0]] = ls[1]
    return dc

dic = dict_make(int(input('Enter the length of dictionary: ')))
print(dic)

lis = sorted(dic.keys())
ndic = {Q: dic[Q] for Q in lis}
print(ndic)
