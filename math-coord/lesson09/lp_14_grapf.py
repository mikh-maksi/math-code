import time

from scipy.optimize import linprog

start = time.time()

c = [-4 , -2, -6]  # The objective function is at a minimum
A_ub = [
    [12, 6,2],
    [12, 24,18],
    [12, 12,12],
    [-1, 0,0],
    [0,-1, 0],
    [0,0, -1],
]  # Coefficients with inequalities
b_ub = [160,360,720,0,0,0]  # Results for inequalities
# A_eq = [[1, 1, 1]]  # Coefficient in the constraint function equation
# b_eq = [1]  # The result of the constraint function equation

# print(linprog(c, A_ub, b_ub,A_eq,b_eq))  # Optimisation
print(linprog(c, A_ub, b_ub))  # Optimisation

stop = time.time()
print("Time :")
print(stop - start)