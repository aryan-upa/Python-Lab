n=[7]
for i in n:
    if i%7==0:
        if i%6==i%5==i%4==i%3==i%2==1:
            print(f'Number is: {i}')
            break
        else:
            n.append(i+1)
    else:
        n.append(i+1)
