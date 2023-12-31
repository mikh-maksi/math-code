# Модель польоту снаряду, випущеного під кутом 45 градусів до горизонту. Систему диференціальних рівнянь другого порядку
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
def deriv(xy,t):
    x=xy[0] # переміщення по x
    x_=xy[1] # швидкість по x
    y=xy[2] # переміщення по y
    y_=xy[3] # швидкість по y
    return np.array([x_, 0.0, y_, -9.8]) # повертає значення функцій dx/dt, dx'/dt, dy/dt, dy'/dt
t = np.linspace(0.0, 10.0, 100) # час
init = np.array([0.0, 50.0, 0.0, 50.0]) # початкові умови для x, x', y, y'
xy = odeint(deriv, init, t) # інтегруємо систему диф. рівнянь, отримуємо масив [x, x', y, y']
plt.plot(xy[:,0], xy[:,2]) # траєкторія
plt.xlabel("x");plt.ylabel("y");plt.grid();plt.show()