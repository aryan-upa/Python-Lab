inp = int(input('Enter the length of dictionary: '))
lsk = list(map(str, input('Enter list of space separated keys: ').split()))
lsv = list(map(str, input('Enter list of space separated values: ').split()))

# we can do this using zip function.
dic = dict(zip(lsk,lsv))
print(dic)
