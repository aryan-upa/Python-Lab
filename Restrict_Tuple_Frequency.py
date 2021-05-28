inp = int(input('Enter number of values: '))
ls = [tuple(map(int,input().split())) for q in range(inp)]
K = int(input('Enter K: '))
# ls = eval(input('Enter Data: '))
# K = int(input('Enter K: '))
n = [q[0] for q in ls]
for p in n:
    while n.count(p)-K>0:
        n.remove(p)
nls = []
for q in ls:
    for j in n:
        if q[0]==j:
            nls.append(q)
            n.remove(j)
            break
print(nls)