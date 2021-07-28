ls1 = eval(input())
ls2 = eval(input())
c = 0
for q in ls1:
    for j in ls2:
        if len(q) ==  len(j):
            if set(q) == set(j):
                c+=1
else:
    print(c)