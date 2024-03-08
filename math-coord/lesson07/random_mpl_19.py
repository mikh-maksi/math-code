import numpy as np
from scipy import stats
# print np.random.random(3) # випадкова вибірка з інтервалу [0.0, 1.0) рівноімовірного розподілу
n=[1,3,4,6,8,3,5,4,3,3,5]

mean,std = stats.uniform.fit(n)

print(mean,std)

X=np.random.uniform(1,20,10)
print (X.mean(), X.std(), X.var())


X1=np.linspace(1,20,10) 
print(X1)
dist2=stats.uniform(loc=4, scale=100)
print(dist2.pdf(X1))
# plt.plot(X1, dist2.pdf(X1),'k-') 
# print(N)
# print(X)