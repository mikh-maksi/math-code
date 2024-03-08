import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# dist = stats.norm(loc=15, scale=0.5) # нормальний розподіл
# dist=stats.uniform(loc=14,scale=2) # рівномірний розподіл (для порівняння)
# dist=stats.alpha(2) # рівномірний розподіл (для порівняння)
# dist=stats.expon(loc=0, scale=5) # рівномірний розподіл (для порівняння)
dist=stats.bernoulli(0.3) # рівномірний розподіл (для порівняння)


N=10000 # розмір вибірки
X=dist.rvs(size=N) # випадкова вибірка з цього розподілу

mean,std = stats.norm.fit(X) # підігнати криву норм. розп. і отримати її параметри
k2,pvalue = stats.normaltest(X) # тест на нормальний розподіл (k2 - сума квадратів коефіцієнтів асиметрії і ексцесу)
print (k2,pvalue) # наприклад, якщо pvalue < 0.05, то це не нормальний розподіл
d,pvalue = stats.kstest(X, dist.cdf) # тест Колмогорова-Смірнова
#або stats.kstest(X, 'norm', args=(15, 0.5))
print (d,pvalue) # якщо pvalue < 0.05, то ці розподіли не ідентичні

# побудова емпіричної гістограми і теоретичної кривої:
n,x=np.histogram(X, bins=10) # кількість значень у кожному інтервалі, інтервали
xmin=x[:-1] # масив мінімумів інтервалів
dx=x[1]-x[0] # ширина інтервалу
y=n/(N*dx) # емпірична приведена частота

# площа одного прямокутника гістограми дорівнює відносній частоті: p=n/N=dx*n/(N*dx)
xmid=xmin+dx/2 # масив центрів інтервалів
plt.bar(xmid, y, width=dx, color='y') # нарисувати емпіричну гістограму приведених частот
dist2 = stats.norm(loc=mean, scale=std) # нормальний розподіл із параметрами після підгонки

plt.plot(xmid, dist2.pdf(xmid),'ko') # нарисувати точки теоретичної кривої
X1=np.linspace(13,17,100) # аргументи для побудови теоретичної кривої
plt.plot(X1, dist2.pdf(X1),'k-') # нарисувати теоретичну криву густини імовірності
plt.xlabel('x');plt.ylabel('y')

plt.grid()
plt.show()
