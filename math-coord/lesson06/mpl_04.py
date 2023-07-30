
import numpy as np
from scipy.optimize import minimize, fmin_l_bfgs_b

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x): # функція двох змінних
    return x[0]**2+x[1]**2
res=minimize(f, x0=[1.0, 1.0], method="L-BFGS-B", bounds=[(-5,5),(-5,5)])
print (res.x)
# argmin = fmin_l_bfgs_b(f, x0=[1.0, 1.0], bounds=[(-5,5),(-5,5)], approx_grad=True) # або так
# print (argmin[0])


ax=Axes3D(plt.figure()) # система координат
X, Y = np.meshgrid(np.linspace(-5,5), np.linspace(-5,5)); 
Z=f([X,Y])
ax.plot_wireframe(X, Y, Z) # каркасна поверхня
ax.scatter(res.x[0], res.x[1], res.fun, c='k') # мінімум
ax.set_xlabel('X0'),ax.set_ylabel('X1'),ax.set_zlabel('Y');

ax.show()