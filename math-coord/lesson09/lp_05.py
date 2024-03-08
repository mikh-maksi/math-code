import time

from scipy.optimize import linprog

start = time.time()

c = [-1, 3]  # Цільова функція - на мінімум
A_ub = [
    [2, -3],
    [-1, 1],
    [1, 2],
    [-1, 0],
    [0, -1],
]  # Коефіцієнти при нерівностях
b_ub = [7,2,8,0,0]  # Результати при нерівностях
# A_eq = [[1, 1, 1]]  # Кофеціенти при рівняння функциї обмеження
# b_eq = [1]  # Результат при рівняння функциї обмеження

# print(linprog(c, A_ub, b_ub,A_eq,b_eq))  # Оптимізація
print(linprog(c, A_ub, b_ub))  # Оптимізація

stop = time.time()
print("Час :")
print(stop - start)