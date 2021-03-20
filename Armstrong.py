a=input()

l = len(a)
Sum=0
for i in a:
    Sum += int(i)**l
if Sum==int(a):
    print(f"{a} is an Armstrong number.")
else:
    print(f"{a} is not an not Armstrong number.")
