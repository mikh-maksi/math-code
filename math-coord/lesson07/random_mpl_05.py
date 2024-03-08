import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import random

dist = stats.norm(loc=15, scale=0.5) # нормальний розподіл

N=1000 # розмір вибірки
# Створюємо розподіл на N-елементів
X=dist.rvs(size=N) 
X = []

for i in range(1000):
    # X.append(random.uniform(1,10))
    # X.append(random.normalvariate(10,5))
    # X.append(random.expovariate(10))
    # triangular(low, high, mode) Неперервне від low до high, із найчастішим значенням що дорівнює mode
    # X.append(random.triangular(1,5,4))
    # X.append(random.gauss(10,3)) # нормальний розподіл, працює трохи швидше ніж normalvariate
    X.append(random.paretovariate(1.16)) # нормальний розподіл, працює трохи швидше ніж normalvariate

print(X)





# побудова емпіричної гістограми 
print(np.histogram(X, bins=10))
n,x=np.histogram(X, bins=10) # кількість значень у кожному інтервалі, інтервали
pareto20 = n[0]+n[1]
percent=pareto20/sum(X)
print(percent)
print(sum(X))
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
