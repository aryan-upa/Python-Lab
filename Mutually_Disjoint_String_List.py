def rem(x,e):
    x = list(x)
    e = str(e)
    x.pop(x.index(e))
    return x

ls = list(map(str,input('Enter strings: ').split()))
for q in ls:
    for j in rem(ls,q):
        for p in q:
            if p in j:
                print(False)
                exit()
else:
    print(True)

