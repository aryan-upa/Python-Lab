ls1 = eval(input())
ls2 = eval(input())
cnt=0
for q in ls1:
    for j in ls2:
        if len(j)==len(q):
            if sorted(j)==sorted(q):
                cnt+=1
else:
    print(cnt)
