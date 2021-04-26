# You might think that why this program is so long but, this program works on every size of matrix.
# Invalid Matrix is the one where number of elements does not equate with the order (size) of matrix entered.
def matdef():
    # This function is defined to take input of Matrices.
    t = 2
    MM = []
    while t > 0:
        print('Enter elements <space separated> of Matrix {}'.format(3-t))
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
                del M
        else:
            print('INVALID Matrix')
            exit()
        t -= 1
    for i in MM:
        for q in i:
            print(*q)
        print()
    return MM


def matadd(x):
    # This function is defied to do the addition part.
    mt1 = x[0]
    mt2 = x[1]
    sm = [[0 for m in range(len(mt1[0]))] for r in range(len(mt1))]
    r,c = 0,0
    for i in range(len(mt1)):
        c = 0
        for q in range(len(mt1[0])):
            sm[r][c] = mt1[r][c]+mt2[r][c]
            c+=1
        r+=1
    print('--Sum Matrix--')
    for q in sm:
        for i in q:
            print(str(i).rjust(10), end='')
        print()


# Function Call
matadd(matdef())
