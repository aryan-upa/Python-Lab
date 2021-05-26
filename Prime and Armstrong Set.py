from math import ceil, sqrt
def prime(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        val = ceil(sqrt(x))
        for p in range(2, val+1):
            if x % p == 0:
                return 0
        else:
            return 1

s1 = set()
for i in range(100,1000):
    if prime(i):
        s1.add(i)

s2 = set()
for i in range(100,1000):
    s = str(i)
    sm = int(s[0])**3 + int(s[1])**3 + int(s[2])**3
    if sm==i:
        s2.add(i)

print(f'Set of Prime numbers in b/w 100 and 999 are:\nNo. of elements : {len(s1)}\n', s1)
print(f'Set of Armstrong numbers in b/w 100 and 999 are:\nNo. of elements : {len(s2)}\n',s2)