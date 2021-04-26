# This Program takes input of Matrix in form of nested list and then prints it.
t = 2
MM = []
while t > 0:
    lst = list(map(int, input().split()))
    r, c = map(int, input('Enter No. of rows <space> Column: ').split())
    if r*c == len(lst):
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
        else:
            MM.append(M)
            M = []
    else:
        print('INVALID Matrix')
    t -= 1
for i in MM:
    for q in i:
        print(*q)
    print()

print(MM)
