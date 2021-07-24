ls = list(input())
R = U = 1
L = D = -1
val = 0
for q in ls: val+=eval(q)
print('false') if val else print('true')
