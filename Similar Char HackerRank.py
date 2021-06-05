inp = int(input())
ls = input()
que = int(input())
for j in range(que):
    pos = int(input())
    ch = ls[pos-1]
    print(ls[0:pos-1].count(ch))
