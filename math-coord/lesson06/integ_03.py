# Функція scipy.integrate.odeint розв’язує систему звичайних диференціальних рівнянь з початковою умовою чисельними методом [11, 14, 25, 31, 45, 53]. У прикладі розв’язується просте диференціальне рівняння з початковою умовою :
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def deriv(y,t): # функція повертає похідну dy/dt в точці t
    return t**2 # значення правої частини рівняння
t = np.linspace(0, 1, 100) # час
y = odeint(deriv, y0=0, t=t) # інтегрує диф. рівняння
plt.plot(t,y,'k-') # рисує залежність y(t)
plt.xlabel('t');plt.ylabel('y');plt.grid();plt.show()