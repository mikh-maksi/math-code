import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

mean, var, skew, kurt = uniform.stats(moments='mvsk')

x = np.linspace(uniform.ppf(0.01),
                uniform.ppf(0.99), 100)

                
ax.plot(x, uniform.pdf(x),
       'r-', lw=5, alpha=0.6, label='uniform pdf')

plt.show()