import numpy as np
from gen_functions import gen_balance_matrix, gen_c_i
from data_io_fnc import data_input_f,to_df


n=4
m = (n-1)*n
A = gen_balance_matrix(n)

# Створюємо одиничну матрицю 4x4
I = np.eye(n, dtype=float)

# Приписуємо справа → результат матриця 4x16
A_ij = np.hstack([A, I])
b_i=np.ones((n, 1), dtype=float)

Xbasis_i_arr = []
for i in range(n):
    Xbasis_i_arr.append([m+1+i])

Xbasis_i = np.array(Xbasis_i_arr)
c_i = gen_c_i(n)

Cbasis_i = Xbasis_i


fi_i=[0,0,0,0,0]
delta_i = [9.0, 0.0, 0.0, 0.0, 2.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Z_0 = [0]

df_out = to_df(c_i,Cbasis_i,Xbasis_i,A_ij,b_i,fi_i,delta_i,Z_0)
print(df_out)
# file_path_out = "c:/Work/repo/math-code/simplex/vrp-generation/input/data_out4.csv"
# df_out.to_csv(file_path_out ,mode='a',sep=";")