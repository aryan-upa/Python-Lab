def set_make(x):
    s = set()
    for q in range(x):
        s.add(input('Enter element: '))
    return s

inp = int(input('Enter number of elements in the set : '))
S = set_make(inp)
print(S)

st = 'a'
while st != '':
    st = input('enter the element to delete, (just press enter to exit) : ')
    S.discard(st)

print(S)
