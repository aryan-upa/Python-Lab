st = input()
ls = [st[0]]

for q in range(0,len(st)):
    if q!=len(st)-1:
        if st[q+1]==st[q]:
            ls[-1]+=st[q]
        else:
            ls.append(st[q+1])

print(ls)

# Alternative Approach
# The group by function return a key and list of multiple consecutive elements in a string.
# It also takes a key as an input but if not given 'None' is by default and every changed group creates a new list.
# from itertools import groupby
# st = input()
# ls = ["".join(group) for ele,group in groupby(st)]
# print(ls)

