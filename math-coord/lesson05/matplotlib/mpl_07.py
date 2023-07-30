import matplotlib.pyplot as plt
import numpy as np
from sympy import diff, symbols, cos, sin



fig, ax = plt.subplots()

# Перемістимо лівий і нижній стовпчики до x = 0 і y = 0 відповідно.
ax.spines[["left", "bottom"]].set_position(("data", 0))

# Сховати верхню та праву лінію
ax.spines[["top", "right"]].set_visible(False)

# Намалюємо стрілки (як чорні трикутники: ">k"/"^k") на кінцях осей. 
# Також вимкнемо відсікання (clip_on=False) стрілок.
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

# Сформуємо ряд значень x. 100 елементів від -2 до 2. 


x, y = symbols('x y')
dx = diff((x*x+2*x+10))
k = []
n = []
l = []
for i in range(1000):
    j = i-500
    k.append(0.01*j)
    n.append(dx.subs(x,0.01*j))
    l.append((0.01*j)**2+2*(0.01*j)+10)


print(k)

print(n)

ax.plot(k,n)
ax.plot(k,l)
# Додамо проміжні лінії
ax.grid(True, linestyle='-.')

# Сформуємо функцію y = x**2+2



# Запускаємо малювання графіку
plt.show()