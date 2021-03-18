inp = int(input("Enter Input: "))
C = 2*inp - 1
c= C//2
for i in range(inp):
    if i==0:
        print(" "*(c)+'*'+" "*(c))
    elif i!=inp-1:
        print(" "*(c-i)+f"*{' '*(C-2*(c-i)-2)}*"+" "*(c-i))
    else:
        print("*"*C)
