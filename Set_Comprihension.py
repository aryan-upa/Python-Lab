S1 = set(map(int,input('Enter Numerical space separated elements in set 1: ').split()))
S2 = set(map(int,input('Enter Numerical space separated elements in set 2: ').split()))

S3 = {q for q in S2 if q not in S1}
print(S3)