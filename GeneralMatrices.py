# Identity Matrix: If A is an Identity Matrix then, det(A) = 1
inp = int(input('Enter the size of Matrix: '))
Mat = [[int(q==x) for q in range(inp)] for x in range(inp)]
for i in Mat:
    print(*i)

# X pattern Matrix
inp = int(input('Enter the size of Matrix: '))
Mat = [['*' if(q==x or q+x==inp-1) else ' ' for q in range(inp)] for x in range(inp)]
for i in Mat:
    print(*i)

# Lower Left triangular Matrix
inp = int(input('Enter the size of Matrix: '))
Mat = [['*' if(q<=x) else ' ' for q in range(inp)] for x in range(inp)]
for i in Mat:
    print(*i)

# Upper Left triangular Matrix
inp = int(input('Enter the size of Matrix: '))
Mat = [['*' if(x+q<=inp-1) else ' ' for q in range(inp)] for x in range(inp)]
for i in Mat:
    print(*i)

# Upper Right triangular Matrix
inp = int(input('Enter the size of Matrix: '))
Mat = [['*' if(q>=x) else ' ' for q in range(inp)] for x in range(inp)]
for i in Mat:
    print(*i)

# Lower Right triangular Matrix
inp = int(input('Enter the size of Matrix: '))
Mat = [['*' if(x+q>=inp-1) else ' ' for q in range(inp)] for x in range(inp)]
for i in Mat:
    print(*i)

# Box Matrix
# * * * *
# *     *
# *     *
# * * * *
inp = int(input('Enter the size of Matrix: '))
Mat = [['*' if(x==0 or x==inp-1 or q==0 or q==inp-1) else ' ' for q in range(inp)] for x in range(inp)]
for i in Mat:
    print(*i)

# Diamond Matrix
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
inp = int(input('Enter the size of Matrix: '))
c = 0
Mat = [['' for x in range(2*inp-1)] for q in range(2*inp)]
for i in Mat:
    if c<inp:
        for q in range(2*inp-1):
            i[q] = ' ' if q not in range((2*inp-1) // 2 - c + 1, (2*inp-1) // 2 + c) else '*'
    elif c == inp:
        for q in range(2*inp-1):
            i[q] = '*'
    else:
        for q in range(2*inp-1):
            i[q] = Mat[2*inp-c][q]
    c += 1
Mat.pop(0)
for i in Mat:
    print(*i)
