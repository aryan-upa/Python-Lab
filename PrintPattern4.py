inp = int(input("Enter the input: "))
for i in range(2*inp-1):
    if i<inp:
        print("* "*(i+1))
    else:
        print("* "*((2*inp-1)-i))
