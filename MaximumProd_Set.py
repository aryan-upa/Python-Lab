S = set(map(int,input('Enter Numerical space separated elements : ').split()))
ls = sorted([q for q in S])
ls = ls[-1:-3:-1]
print('maximum product is formed by the pair:',set(ls))
