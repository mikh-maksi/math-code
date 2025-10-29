import numpy as np
from gen_functions import gen_balance_matrix, gen_c_i
n=4
m = (n-1)*n
A = gen_balance_matrix(n)


# Створюємо одиничну матрицю 4x4
I = np.eye(n, dtype=float)

# Приписуємо справа → результат матриця 4x16
A_ij = np.hstack([A, I])
print(A_ij)

b_i=np.ones((n, 1), dtype=float)
print(b_i)

Xbasis_i_arr = []
for i in range(n):
    Xbasis_i_arr.append([m+1+i])
print(Xbasis_i_arr)
Xbasis_i = np.array(Xbasis_i_arr)
print(Xbasis_i)
c_i = gen_c_i(n)
print(c_i)
