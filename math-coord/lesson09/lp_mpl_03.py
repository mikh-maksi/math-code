import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 12})

x = np.linspace(0, 10, 100)
x1 = []
for i in range(100):
    x1.append(3)
y1 = np.linspace(0, 10, 100)
f1 = (5/2)*x+1
f2 = 2+0*x
f3 = 11/2+x
ff = 2.5847*x

# указываем в аргументе label содержание легенды 
plt.plot(x, f1, ':b', label='x2<(5/2)*x3+1')
plt.plot(x1, y1, 'k', label='x2>3')
plt.plot(x, f2, '--b', label='x3<2')
plt.plot(x, f3, 'y', label='x2<11/2+x3')
plt.plot(x, ff, 'r', label='Funtion')

plt.xlabel(r'$x2$', fontsize=16)
plt.ylabel(r'$x3$', fontsize=16)

plt.xlim([0, 10])
plt.ylim([0, 10])

# выводим легенду
plt.legend(fontsize=14)

plt.tight_layout()
plt.show()
