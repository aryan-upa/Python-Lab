ls = list(map(int,input('Enter List Data: ').split()))
K = int(input('Enter K: '))
nls = []
for i in range(1,len(ls)-1):
    if ls[i]-ls[i-1]>=4 and ls[i]-ls[i+1]>=4:
        nls.append(ls[i])

print(nls)
