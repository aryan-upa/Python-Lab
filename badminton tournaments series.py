ls = list(input().split(','))
ls.sort()
p = [ls.count(q) for q in ls]
print(ls[p.index(max(p))])