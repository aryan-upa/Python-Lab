ls = list(map(str,input('Enter List Elements: ').split()))
nls = []

for i in ls:
    s = set(i)
    for q in s:
        if i.count(q)==1:
            pass
        else:
            break
    else:
        nls.append(i)

nls = list(map(int,nls))
print(nls)
