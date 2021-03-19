Lst = []
T=500
for i in range(T):
    Lst.append(1)

n = 50
for i in range(1,n+1):
    for p in range(1,T+1):
        if p%i==0:
            if Lst[p-1]==0:
                Lst[p - 1]=1
            else:
                Lst[p - 1]=0
        else:
            pass

for i in range(T):
    if Lst[i]==0:
        print(i,end=' ')
