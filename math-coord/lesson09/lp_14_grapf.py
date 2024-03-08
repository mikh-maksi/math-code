import time

from scipy.optimize import linprog

start = time.time()

c = [-4 , -2, -6]  # Цільова функція - на мінімум
A_ub = [
    [12, 6,2],
    [12, 24,18],
    [12, 12,12],
    [-1, 0,0],
    [0,-1, 0],
    [0,0, -1],
]  # Коефіцієнти при нерівностях
b_ub = [160,360,720,0,0,0]  # Результати при нерівностях
# A_eq = [[1, 1, 1]]  # Кофеціенти при рівняння функциї обмеження
# b_eq = [1]  # Результат при рівняння функциї обмеження

# print(linprog(c, A_ub, b_ub,A_eq,b_eq))  # Оптимізація
print(linprog(c, A_ub, b_ub))  # Оптимізація

stop = time.time()
print("Час :")
print(stop - start)