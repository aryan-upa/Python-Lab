inp = int(input("Enter the number of lines: "))
val = 65
for i in range(1, inp+1):
    for p in range(1, i+1):
        print(chr(val), end='')
        val += 1
    print()
