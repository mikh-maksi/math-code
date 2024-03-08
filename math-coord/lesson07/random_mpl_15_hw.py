import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats

N=100 # розмір вибірки
X = [] # Пустий масив для наповнення

# Цикл зі 1000 ітерацій, на кожній з яких додаємо 1 випадковий  
# елемент з нормальним розподілом, із середнім 10 та стандартним відхиленням 5.
for i in range(N):
    k = random.normalvariate(10,3)
    X.append(float('%.2f' % (k)) )

print(X)
