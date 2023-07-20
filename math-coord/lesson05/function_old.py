# coding=utf-8
import matplotlib.pyplot as plt
from math import * #Берем всі функції що можуть знадобитись
 
print ("Програма побудови графіка")
 
fstring=raw_input("f(x)=")#Вводимо текст функції
 
def f(x):
    return eval(fstring) # ну, і відповідно за ним обчислюємо функцію.
 
print ("На інтервалі [a,b]")# Вводимо інтервал
a=input("a=")
b=input("b=")
 
assert a<b, "a >= b"# Перевіряємо щоб інтервал був правильним
 
delta=(b-a)/1000.0 # Беремо невеликий діаметр розбиття
 
X=[] # Координати графіка
Y=[]
x=a
while x<b: #На всьому інтервалі
    X.append(x)
    Y.append(f(x)) #Табулюємо
    x+=delta
 
plt.rc('text', usetex=True) # Ця опція вказує нам, що треба використати зовнішній парсер LaTeX. Залежності: LaTeX, dvipng, ghostscript
plt.plot(X,Y) # Малюємо графік. Список X не обов'язковий, але тоді замість нього беруть range(0,len(Y))
plt.ylabel("$f(x)$") #Підписи
plt.xlabel("$x$")
label=raw_input("Заголовок функції (LaTeX, не обов'язково) ") 
plt.title(r"$\displaystyle f(x)="+label+"$") # заголовок графіка
plt.grid(True) # сітка
plt.show()     # і нарешті покажемо це користувачу