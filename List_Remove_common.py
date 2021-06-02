ls1 = input().split()
ls2 = input().split()

nls = ls1.copy()
for q in nls:
    if q in ls2:
        while ls2.count(q):
            ls2.remove(q)
        while ls1.count(q):
            ls1.remove(q)

print(*ls1)
print(*ls2)
