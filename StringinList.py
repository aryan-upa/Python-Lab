ls = ['abc','xyz','aba','1221']
ls = [q for q in ls if len(q)>2 and q[0]==q[-1]]
print(len(ls))
