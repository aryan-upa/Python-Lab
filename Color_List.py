def miss(x):
    Col = ['R','G','B']
    for q in Col:
        if q not in x:
            return q


ls = eval(input())
flag=1; q = 0
while flag == 1:
    if ls.count(ls[0])==len(ls):
        break
    if ls[q]!=ls[q+1]:
        flag=1
        val = miss([ls[q],ls[q+1]])
        ls.pop(0);ls.pop(0)
        ls.insert(q,val)
        q = 0
    else:
        q+=1
print(f'"{ls[0]}"')
