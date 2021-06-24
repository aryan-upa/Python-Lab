def dict_make(x):  # Function to declare user defined dictionaries.
    dc = {}
    for q in range(x):
        ls = input('Enter key <space> value: ').split()
        dc[ls[0]] = ls[1]
    return dc

# This method works for values which are mutable, but here we create a new dictionary
'Method 1'

dic = {'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
nls = set(dic.values())
ndc = {}
for j in nls:
    for k in dic.keys():
        if dic[k]==j:
            ndc[k] = j
            break
print(ndc)

# This method works the way preferred, no new dictionary formed and any type of value will be fine.
'Method 2'

dic = {'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
nls = set(dic.values())
pop = []
for k in dic.keys():
    if dic[k] in nls:
        nls.discard(dic[k])
    else:
        pop.append(k)
for j in pop: dic.pop(j)
print(dic)

# This code will only work with the given condition that values are also of immutable type.
'Method 3'

dic = {'gfg' : 10, 'is' : 15, 'best' : 20, 'for' : 10, 'geeks' : 20}
print(f'The dictionary is : {dic}')
ndc = dict(zip(dic.values(), dic.keys()))
dic = dict(zip(ndc.values(), ndc.keys()))
print(dic)
