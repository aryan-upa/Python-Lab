inp = int(input())
ls = list(map(int,input().split()))
ls.sort()
que = int(input())
for j in range(que):
    num = int(input())
    for q in range(len(ls)):
        if ls[q]>=num:
            print(len(ls[0:q]))
            break
    else:
        print(inp)