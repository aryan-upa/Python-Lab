inp = 2**int(input()) - 1
c=0
while inp>0:
    st = bin(inp)[2:].zfill(inp)
    if '11' not in st:
        c+=1
    inp-=1
print(c)
