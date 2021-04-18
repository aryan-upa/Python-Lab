def next_date(d, m, y):
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        # Leap Yr
        feb = 29
    else:
        feb = 28
    if m == 2:
        md = feb
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        md = 31
    else:
        md = 30
    if d != md:
        d += 1
    else:
        d = 1
        m += 1
        if m == 13:
            m = 1
            y += 1
    p = [d, m, y]
    return p


count=0
inp = input('Enter Date as DD MM YYYY: ')
ls = list(map(int, inp.split()))
while next_date(ls[0],ls[1],ls[2]) != [31,12,ls[2]]:
    ls = next_date(ls[0],ls[1],ls[2])
    count+=1
print(count)
