
import numpy as np
from scipy.optimize import minimize_scalar, fminbound
def f(x): # функція однієї змінної (цільова функція)
    return -3*(x-2)**2+30*x
res = minimize_scalar(f, bounds=(0,8), method='bounded') # знайти мінімум f(x) в заданих границях. Критерій пошуку - мінімум, допустима множина x від -3 до 3
print ("argmin=",res.x)

argmin = fminbound(f, 0, 8) # або так
print ("argmin=", argmin)
argmax = fminbound(lambda x: -f(x), 0,8) # знайти максимум f(x) в заданих границях
print ("argmax=", argmax)

import matplotlib.pyplot as plt
x=np.linspace(0,8,100)
plt.plot(x,f(x),'k') # графік
plt.scatter([argmin,argmax], [f(argmin),f(argmax)], linewidths=[3,3]) # локальні екстремуми
plt.xlabel('x');plt.ylabel('y');plt.grid();plt.show()