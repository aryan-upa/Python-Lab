import itertools

S = set(map(int,input('Enter Numerical space separated elements : ').split()))
n = int(input('Enter size of subset : '))

v = list(itertools.combinations(S,n))
ls = []
for q in v:
    ls.append(set(q))
print(ls)
