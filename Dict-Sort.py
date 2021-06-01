Dic = {'a':1,'d':0,'b':3,'c':2}
# Sort by key
ls = [q for q in Dic.keys()]
print(ls)
ls.sort()
nDic = {}
for j in range(len(ls)):
    d = {ls[j]:Dic.get(ls[j])}
    nDic.update(d)
print(nDic)
# Sort by Value
ls = [q for q in Dic.values()]
ls.sort()
print(ls)
nls = [q for q in Dic.keys()]
nDic = {}
for j in ls:
    d = {nls[j]:j}
    nDic.update(d)
print(nDic)

