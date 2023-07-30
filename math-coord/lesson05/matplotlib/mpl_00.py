import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(-50, 50, 0.01)
y = x**2

fig, ax = plt.subplots()
ax.plot(x,y)

ax.set(xlabel='x', ylabel='y',
       title='xy Graph')
ax.grid()

fig.savefig("test.png")
plt.show()