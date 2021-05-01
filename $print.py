inp = int(input())
for i in range(1,inp+1): print('$'*i) if i<=int(inp/2) else print('$'*(i-int(inp/2)))