ls1 = list(map(str,input('Enter element of List 1: ').split()))
ls2 = list(map(str,input('Enter element of List 2: ').split()))

if len(ls1)!=len(ls2):
    if len(ls1)<len(ls2):
        ind = 0
        for i in range(len(ls2)-len(ls1)):
            ls1.append(ls1[ind])
            ind+=1
    else:
        ind = 0
        for i in range(len(ls1)-len(ls2)):
            ls2.append(ls2[ind])
            ind+=1

nls = []
for i,j in zip(ls1,ls2):
    nls.extend([i,j])

print(nls)