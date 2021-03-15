a=list(input())
b=[]
for i in range(0,len(a)):
    if a[i]=='{' or a[i]==',' or a[i]=='}' or a[i]==' ':
        pass
    else:
        b.append(a[i])
c=[]
for i in range(0,len(b)):
    q= b[i]
    flag=1
    for k in range(0,len(c)):
        if q==c[k]:
            flag=0
            break
        else:
            pass
    if flag==1:
        c.append(b[i])
    else:
        pass

print(c)
print(len(c))