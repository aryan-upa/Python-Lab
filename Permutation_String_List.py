from itertools import permutations

ls = list(map(str,input('Enter String: ').split()))
lis = list(permutations(ls))
print('No. of Permutations :',len(lis))
for i in lis:
    print(*i)
