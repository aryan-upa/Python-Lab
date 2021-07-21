ls = list(input().split(','))
ls.sort()
p = [ls.count(q) for q in ls]
print(ls[p.index(max(p))])

# Alternate Solution

ls = sorted(input().split(',')); _ = ''
for q in ls : _ = q if ls.count(q) > ls.count(_) else _
print(_)
