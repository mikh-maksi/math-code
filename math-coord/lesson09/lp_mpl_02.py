import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 12})

x = np.linspace(0, 10, 100)

f1 = 2*x
f2 = (1/3)*x
f3 = 1-x
f4 = 5/2-(1/2)*x
ff = 0.5*x

# вказуємо в аргументі label текст легенди 
plt.plot(x, f1, ':b', label='x2<2x1')
plt.plot(x, f2, 'k', label='x2>1/3x1')
plt.plot(x, f3, '--b', label='x2>1-x1')
plt.plot(x, f4, '--g', label='x2<5/2-1/2x1')

plt.xlabel(r'$x1$', fontsize=16)
plt.ylabel(r'$x2$', fontsize=16)

plt.xlim([0, 3])
plt.ylim([0, 3])

# виводимо легенду
plt.legend(fontsize=14)

plt.tight_layout()
plt.show()
