import time

from scipy.optimize import linprog

start = time.time()

c = [-10, -14, -12]  # Цільова функція - на мінімум
A_ub = [
    [2, 4, 5],
    [1, 8, 6],
    [7, 4, 5],
    [4, 6, 7],
]  # Коефіцієнти при нерівностях
b_ub = [120, 280,240,360]  # Результати при нерівностях
# A_eq = [[1, 1, 1]]  # Кофеціенти при рівняння функциї обмеження
# b_eq = [1]  # Результат при рівняння функциї обмеження

# print(linprog(c, A_ub, b_ub,A_eq,b_eq))  # Оптимізація
print(linprog(c, A_ub, b_ub))  # Оптимізація

stop = time.time()
print("чАС :")
print(stop - start)