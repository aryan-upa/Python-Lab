inp = int(input('Enter number of elements in the Dictionary: '))
print('Enter element as "Key"<space>"Value"'); Dic = {}
for q in range(inp):
    inp = list(input().split())
    d = {inp[0]:int(inp[1])}
    Dic.update(d)
print(Dic)
print(sum([q for q in Dic.values()]))
