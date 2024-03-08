import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

dist = stats.norm(loc=15, scale=0.5) # нормальний розподіл

N=1000 # розмір вибірки
# Створюємо розподіл на N-елементів
X=dist.rvs(size=N) 

print(X)





# побудова емпіричної гістограми 
print(np.histogram(X, bins=20))
n,x=np.histogram(X, bins=20) # кількість значень у кожному інтервалі, інтервали

print(sum(n))
# масив початків інтервалів (прибрали останнє, найбільше значення)
xmin=x[:-1] 

# ширина інтервалу (різниця двох послідовних стовпчиків).
dx=x[1]-x[0] 
print(n)
print(N*dx)
# y=n/(N*dx) # емпірична приведена частота
y=n/N 
# площа одного прямокутника гістограми дорівнює відносній частоті: p=n/N=dx*n/(N*dx)
xmid=xmin+dx/2 # масив центрів інтервалів
plt.bar(xmid, y, width=dx, color='y') # нарисувати емпіричну гістограму приведених частот

plt.xlabel('x');plt.ylabel('y')

plt.grid()
plt.show()
