inp = int(input('Enter No. of Tuples: '))
ls = []; sp = []
for q in range(inp):
    ls.append(tuple(map(int,input().split())))
    sp.append(tuple(sorted(ls[q])))
sp = set(sp)
ls = list(sp)
print(ls)