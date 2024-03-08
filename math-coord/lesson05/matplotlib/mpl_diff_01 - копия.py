import matplotlib.pyplot as plt
import numpy as np




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


x = [1,2,3,4,5]
y = [5,6,7,8,9]


ax.plot(x,y)

# Додамо проміжні лінії
ax.grid(True, linestyle='-.')

# Сформуємо функцію y = x**2+2



# Запускаємо малювання графіку
plt.show()