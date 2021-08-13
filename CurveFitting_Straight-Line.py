import numpy as np
from matplotlib import pyplot as plt

n_obsrv = int(input("Enter number of observation : "))
x = [0 for q in range(n_obsrv)]
y = [0 for q in range(n_obsrv)]
for q in range(n_obsrv):
    x[q],y[q] = map(eval,input(f"Enter x{q+1} and y{q+1} : ").split())
p = sum(y)
q = sum(x)
r = sum([a*b for a,b in zip(x,y)])
s = sum([q*q for q in x])

b = (n_obsrv*r - p*q)/(n_obsrv*s - q*q)
a = (p - b*q)/n_obsrv

print(f"The required equation is : y = {a:.2f} + {b:.2f}x")
# Plotting of the graph.
plt.scatter(x,y)
plt.plot(x,y,'--b')
x = np.linspace(min(x),max(x),20)
y = a + b*x
plt.plot(x, y, '-r', label=f'y = {a:.2f} + {b:.2f}x')
plt.title('Fitting Curve to a straight line.')
plt.legend(loc='upper left')
plt.show()

"""
5
1 14
2 27
3 40
4 55
5 68
"""

"""
5
0 1
1 1.8
2 3.3
3 4.5
4 6.3
"""