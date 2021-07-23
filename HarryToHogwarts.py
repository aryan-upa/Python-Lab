n = input()
s = 0
while n!='6174':
    s+=1
    n = str(n)
    x = int(''.join(sorted(n, reverse=True)))
    y = int(''.join(sorted(n)))
    if x-y==6174:
        break
    else:
        n = x-y
print(s)

