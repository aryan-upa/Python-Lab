inp = int(input())
s1 = set()
s2 = set()
for q in range(2*inp):
    if q%2==0:
        s1.add(q)
    else:
        s2.add(q)
print('Even Set: ',s1)
print('Odd Set: ',s2)