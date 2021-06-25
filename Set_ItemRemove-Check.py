def set_make(x):
    s = set()
    for q in range(x):
        s.add(input('Enter element: '))
    return s

inp = int(input('Enter number of elements in the set : '))
S = set_make(inp)
print('Set elements before deletion : \n',S)

st = 'a'
while st != '':
    st = input('enter the element to delete, (just press enter to exit) : ')
    if st != '':
        if st in S:
            ch = input('Item is present, want to delete (Y/N) ? ')
            if ch == 'Y' or ch == 'y':
                S.discard(st)
                print('\t\tItem Deleted!')
                print()
            else:
                print('\t\tItem Not Deleted!')
                print()
        else:
            print('\tItem is not present')
            print()
print('\nSet elements after deletion : \n',S)
