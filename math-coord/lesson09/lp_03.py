import time

from scipy.optimize import linprog

start = time.time()

c = [30, 30, 45]  # Целевая функция
A_ub = [
    [0.03, 0.01, -0.01],
    [-1.25, 0.75, -0.25],
]  # Коэффициенты первых 2-х функций ограничения
b_ub = [0, 0]  # Результат первых 2-х функций ограничения
A_eq = [[1, 1, 1]]  # Коэффициенты 3-й функции ограничения
b_eq = [1]  # Результат 3-й функции ограничения

print(linprog(c, A_ub, b_ub, A_eq, b_eq))  # Оптимизация

stop = time.time()
print("Время :")
print(stop - start)