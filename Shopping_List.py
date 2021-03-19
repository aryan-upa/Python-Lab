Loop=[1]
Name=[]
Quan=[]
for i in Loop:
    name= input("Enter Item name: ")
    if name!='':
        Name.append(name)
        quan = input("Enter Quantity (Just Enter for 1): ")
        if quan=='':
            quan=1
        else:
            pass
        Quan.append(quan)
        Loop.append(1)
    else:
        print("-------------Shopping List--------------------")
        count=0
        for q in Name:
            print(f"Item name: {q} --> Quantity : {Quan[count]}")
            count+=1
        exit()
