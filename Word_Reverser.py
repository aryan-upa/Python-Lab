inp = input("Enter the string: ")
print("Which Type to use for word reverse: "
      "\n1.: With loop"
      "\n2.: Without loop")
choice = int(input("Enter Type: "))
if choice==1:
    for i in range(len(inp)):
        print(inp[len(inp)-i-1],end='')

elif choice==2:
    print(inp[len(inp)::-1])

else:
    print("Invalid Input!")