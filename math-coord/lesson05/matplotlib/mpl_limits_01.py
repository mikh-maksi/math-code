import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(50, 500, 0.01)
y = (7*(x**2)+7*x-2)/(x**2-2*x+3)

fig, ax = plt.subplots()
ax.plot(x,y)

ax.set(xlabel='x', ylabel='y',
       title='xy Graph')
ax.grid()

plt.show()