inp = int(input())
st = ''
cnt = 0
for q in range(2**inp):
    st = str(bin(q))
    st = st[2:]
    if '11' in st:
       cnt+=1
print(cnt)
