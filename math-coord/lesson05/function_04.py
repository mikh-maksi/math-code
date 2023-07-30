import numpy as np
import matplotlib.pyplot as plt
from sympy import diff, symbols, cos, sin

x, y = symbols('x y')
dx = diff((x*x))
print(dx)
k = dx.subs(x,4)
print(k)
x = np.linspace(-6, 6, 10)
print(x)
a = np.where(x, dx, np.nan)

plt.plot(x, a)
# Y1 = z.subs(xn,4)
# Y2 =diff(xn**2)

# print(Y1)
# print(Y2)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.plot(X, Y1, c = 'k', lw = 3., label = 'sin(X)')
# plt.plot(X, Y2, c = '.5', lw = 3., ls = '--', label = 'cos(X)')
# plt.legend()
plt.show()