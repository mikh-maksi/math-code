import numpy as np
import matplotlib.pyplot as plt
from sympy import diff, symbols, cos, sin
# x, y = symbols('x y')



X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)

# print(diff(cos(x)))
plt.plot(X, Y, c = 'k')
plt.grid(True, lw = 2, ls = '--', c = '.75')
plt.show()
