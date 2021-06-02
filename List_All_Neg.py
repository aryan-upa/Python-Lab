# To print all negative numbers in a given range.

ls = list(map(int,input('Enter start<space>stop<space>step: ').split())); _ = []
for i in range(ls[0],0,ls[2]):
    _.append(i)
print(_)
