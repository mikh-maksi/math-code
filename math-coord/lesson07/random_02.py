# https://docs.python.org/uk/3/library/random.html
import random

# Генеруємо n=100 випадкових подій (підкидання кістки)
n=100
lst = []
for i in range(n):
    lst.append(random.randrange(1,7))

# Виміряємо кількість випадань кожної грані
def cntr(l: list):
    rt = {}
    for i in l:
        if i in rt:
            continue
        else:
            rt[i] = (l.count(i))
    # Доставляємо нолики, якщо нема жодного випадіння цього номеру
    for i in range(1, 7):
        if i not in rt:
            rt[i] = 0
    return rt

# Функція сортиування підсумкового словника
def srt(rt: dict):
    srtr = {}
    for key in sorted(rt.keys()):
        srtr[key] = rt[key]
    return srtr

print(srt(cntr(lst)))
prob = srt(cntr(lst))

import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3]
y = np.array([[1, 2], [3, 4], [5, 6]])
plt(x, y)

plt.show()
