inp = int(input('Enter no. of elements: '))
ls = [tuple(map(int,input().split())) for q in range(inp)]
# ls = eval(input())
# inp = len(ls)
for i in range(inp):
    ls[i] = list(ls[i])
    i = ls[i]
    if i[0]<0:
        i[0]=-1*i[0]
    if i[1]>0:
        i[1]=-1*i[1]
ls = [tuple(i) for i in ls]
print(ls)
