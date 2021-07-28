st = eval(input())
pr = [q for q in st if q in ('2','3','5','7')]
nr = [q for q in st if q not in ('2','3','5','7')]
pr = sorted(pr)
st = ''.join(pr)+''.join(nr)
print(f'"{st}"')
