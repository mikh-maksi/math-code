import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 12})

x = np.linspace(0, 10, 100)
x1 = []
for i in range(100):
    x1.append(3)
y1 = np.linspace(0, 10, 100)
f1 = 2*x
f2 = (1/4)*x
f3 = 1-x


# вказуємо в аргументі label текст легенди 
plt.plot(x, f1, ':b', label='$x_2>2x_1$')
plt.plot(x, f2, '--b', label='$x_2<\\frac{1}{4}x_1$')
plt.plot(x, f3, 'y', label='$x_2>1-x_1$')


plt.xlabel(r'$x1$', fontsize=16)
plt.ylabel(r'$x2$', fontsize=16)

plt.xlim([0, 2])
plt.ylim([0, 2])




polygon_2 = matplotlib.patches.Polygon([(0, 0),
                                            (0.33, 0.67),
                                            (0.8, 0.2),
                                            (0, 0)],
                                           fill='blue',
                                           closed=True)
axes = plt.gca()
axes.set_aspect("equal")
axes.add_patch(polygon_2)
# plt.text(-1.0, -0.1, "Polygon", horizontalalignment="center")
plt.scatter(0.33, 0.67, marker='^')
plt.scatter(0.8, 0.2, marker='^')
plt.scatter(0, 0, marker='^')

plt.arrow (x= 0 , y= 0 , dx=0.2 , dy= 0.2 , facecolor= 'red',edgecolor= 'none', width= .018 )
plt.annotate('Objective', xy = (0.5, 0.5)) 

# виводимо легенду
plt.legend(fontsize=14)
plt.grid()
plt.tight_layout()
plt.show()
