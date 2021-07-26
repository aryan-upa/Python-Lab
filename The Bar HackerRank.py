s = ''
st = ''
while s!='}':
    s = input()
    st+=s
dic: dict = eval(st)
# print(dic)
nls = []
for q in dic.values(): nls.extend(q)
ndic = dict.fromkeys(nls,0)
for q in ndic.keys():
    for j in dic.keys():
        if q in dic[j]:
            ndic[q]+=1
# print(ndic)
Cust = dict.fromkeys(dic.keys(),False)
cal = sorted(ndic, key = lambda x: ndic[x],reverse = True)
ans = 0
for q in cal:
    _ = list(Cust.values()).count(True)
    flag = 0
    for j in dic.keys():
        if q in dic[j]:
            if not Cust[j]:
                Cust[j] = True
                flag = 1
    if flag==1:
        ans+=1
print(ans)

# Another Test case
{
    0: [0,1],
    4: [0,1],
    1: [4,5,6],
    2: [4,5,6],
    3: [6,7,8]
}

# TestCase01
{
    0: [0,3,6],
    1: [1,4,7],
    2: [2,4,7,5],
    3: [3,2,5],
    4: [5,8]
}
