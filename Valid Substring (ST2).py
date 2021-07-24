st = input()
count = 0
an = [0]; ln = 0
for q in st:
    if q==')':
        if count<=0:
            an.append(ln)
            count = 0
            ln = 0
        else:
            ln+=1
            count-=1
    else:
        ln+=1
        count+=1
else:
    if count==0:
        an.append(ln)
    else:
        an.append(ln-count)
print(max(an))