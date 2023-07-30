
import numpy as np
from scipy.optimize import minimize_scalar, fminbound
def f(x): # функція однієї змінної (цільова функція)
    return np.sin(x)+np.cos(x**2)
res = minimize_scalar(f, bounds=(-3, 3), method='bounded') # знайти мінімум f(x) в заданих границях. Критерій пошуку - мінімум, допустима множина x від -3 до 3
print ("argmin=",res.x)

argmin = fminbound(f, -3, 3) # або так
print ("argmin=", argmin)
argmax = fminbound(lambda x: -f(x), -3, 3) # знайти максимум f(x) в заданих границях
print ("argmax=", argmax)

import matplotlib.pyplot as plt
x=np.linspace(-3,3,100)
plt.plot(x,f(x),'k') # графік
plt.scatter([argmin,argmax], [f(argmin),f(argmax)], linewidths=[3,3]) # локальні екстремуми
plt.xlabel('x');plt.ylabel('y');plt.grid();plt.show()