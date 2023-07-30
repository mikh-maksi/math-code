import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz

X=np.linspace(-5,3)
Y=X**2+4*X # функція
plt.plot(X,Y,'k-')

Y1=np.diff(Y)/np.diff(X) # похідна
plt.plot(X[:-1],Y1,'k--')
Y1=np.gradient(Y,X[1]-X[0]) # або
plt.plot(X,Y1,'k--')

Y_int=cumtrapz(Y, X, initial=0) # первісна
plt.plot(X,Y_int,'k:')
plt.xlabel('$x$');plt.ylabel('$y, \dot{y}, Y$');plt.grid();plt.show()