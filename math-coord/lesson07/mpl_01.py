import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

dist = stats.norm(loc=15, scale=1) # ВВ з нормальним розподілом
X = np.linspace(10,20,100) # область значень ВВ
Xs=dist.rvs(size=1000) # випадкова вибірка значень ВВ розміром 1000
print (Xs.mean(), Xs.std(), Xs.var()) # середнє, середньоквадратичне відхилення, дисперсія
plt.hist(Xs, bins=20,  color='y') # гістограма вибірки
plt.plot(X, dist.pdf(X),'k') # функція густини імовірності розподілу ВВ
plt.plot(X, dist.cdf(X),'k--') # функція розподілу ВВ (імовірність того, що ВВ буде мати значення менше або рівне x)
print (dist.cdf(15)-dist.cdf(0)) # імовірність попадання в інтервал значень (0,15)
plt.xlabel('x');plt.ylabel('y, Y');plt.grid();plt.show()
print ("Рисунок - Гістограма, функція густини імовірностей y(x) (-) та функція розподілу Y(x) (--)")

plt.figure()
Y=np.linspace(0,1,100) # область значень функції розподілу
plt.plot(Y, dist.ppf(Y),'k') # квантільна функція (інверсна до cdf)
print (dist.ppf(0.5)) # значення ВВ, якому відповідає cdf=0.5
cdf1=stats.norm().cdf(3) # 0.998650101968
cdf2=stats.norm().cdf(-3) # 0.00134989803163
print (cdf1-cdf2) # імовірність попадання в інтервал (-3*std,+3*std)
# квантілі стандартного нормального розподілу:
print (stats.norm().ppf(cdf1)) # з рівнем cdf1
print (stats.norm().ppf(0.5)) # з рівнем 0.5
plt.xlabel('Y');plt.ylabel('x');plt.grid();plt.show()
print ("Рисунок - Квантільна функція x(Y)")