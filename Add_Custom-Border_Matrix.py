ls: list[list] = eval(input())
bord = input('Enter Border: ')
for q in ls:
    q.insert(0,bord)
    q.insert(len(q),bord)
    print(*q)
