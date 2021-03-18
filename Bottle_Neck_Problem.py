#I had previously solved this question in C as well, so it was just change of Syntax only.
n = int(input("N: ")) #Total Numbers of Bottles.

bottle =[] #List contaning all Bottles.
Dist = [] #Distinct elements of List Bottles.

for i in range(n):
    inp = eval(input(": "))
    bottle.append(inp)
    for p in range(i):
        if bottle[p]==inp:
            break
    else:
        Dist.append(inp)

count = [] #List containing Frequency of each Dist element.
for i in Dist:
    _ = 0
    for p in bottle:
        if i==p:
            _ = _+1
        else:
            pass
    count.append(_)

print("Minimum no. of Visible Bottles:",max(count))