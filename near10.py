inp = int(input("Enter the number: "))

md = inp%10
if md>5:
    if 10-md>2:
        print(False)
    else:
        print(True)
else:
    if md<3:
        print(True)
    else:
        print(False)
