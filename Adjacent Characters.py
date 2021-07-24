inp = input()
if len(inp)&1==1:
    print('Odd length.')
else:
    nst = ''
    for q in range(0,len(inp),2): nst+= inp[q+1]+inp[q]
    print(nst)
