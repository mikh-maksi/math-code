import time

from scipy.optimize import linprog

start = time.time()

c = [2, 1,-3,-5]  # Цільова функція - на мінімум
A_ub = [
    [1, 1,2,-1],
    [1, 2,-1,1],
    [-1,0,0,0],
    [0,-1,0,0],
    [0,0,-1,0],
    [0,0,0,-1],

]  # Коефіцієнти при нерівностях
b_ub = [9,2,0,0,0,0]  # Результати при нерівностях
A_eq = [[3, -1, 1,2]]  # Кофеціенти при рівняння функції обмеження
b_eq = [4]  # Результат при рівняння функциї обмеження

print(linprog(c, A_ub, b_ub,A_eq,b_eq))  # Оптимізація


stop = time.time()
print("Час :")
print(stop - start)