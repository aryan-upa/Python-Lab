lst = eval(input())
r, c = map(int, input().split('x'))
if r * c == len(lst):
    M = list()
    ls = list()
    C = 0
    for i in lst:
        if C < c:
            C += 1
            ls.append(i)
        if C == c:
            C = 0
            M.append(ls)
            ls = []
    for i in M:
        print(*i)
else:
    print('None')

