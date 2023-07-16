import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
mu_params = [-1, 0, 1]
sd_params = [0.5, 1, 1.5]
x = np.linspace(-7, 7, 200)
_, ax = plt.subplots(len(mu_params), len(sd_params), sharex=True,
 sharey=True,
 figsize=(9, 7), constrained_layout=True)
for i in range(3):
 for j in range(3):
   mu = mu_params[i]
   sd = sd_params[j]
   y = stats.norm(mu, sd).pdf(x)
   ax[i,j].plot(x, y)
   ax[i,j].plot([], label="μ = {:3.2f}\nσ = {:3.2f}".format(mu,sd), alpha=0)
   ax[i,j].legend(loc=1)
ax[2,1].set_xlabel('x')
ax[1,0].set_ylabel('p(x)', rotation=0, labelpad=20)
ax[1,0].set_yticks([])
