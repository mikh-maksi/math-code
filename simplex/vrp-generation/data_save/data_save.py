import numpy as np
from data_io_fnc import to_df_start,save_data

A_ij =  np.array([[3,1,1,-1,-1,-1,0],[-2,1,2,-2,2,0,1]])
b_i =  np.array([[-8],[6]])
c_i =  np.array([6,-4,-10,-4,-20,-10,-7])

# print(A_ij)
# print(b_i)
# print(c_i)

# flip minus
# print(A_ij[1])
# A_ij[1]=-A_ij[1]
# print(A_ij[1])
# b_i[1]=-b_i[1]

A_t_ij = np.transpose(A_ij)
# print(A_t_ij)
print()

# print(A_ij)
# print(b_i)
# print(c_i)

c_i_=np.array([])
for el in b_i:
    c_i_=np.append(c_i_,el[0])
b_i_=np.array([])
for el in c_i:
    el_=np.array([el])
    b_i_=np.append(b_i_,el_)
print(A_t_ij)
print(c_i_)
print(b_i_)

# m = 2, n = 7
print(len(A_t_ij))
print(len(A_t_ij[0]))
# 1. Визначаємо m та n
m = len(A_t_ij[0])
n = len(A_t_ij)
print(n,m)

# 2. Генеруємо назви стовпчиків.
col_names_arr = []
for i in range(n):
    ii=i+1
    col_name = 'x'+str(ii)
    col_names_arr.append(col_name)

df = to_df_start(A_t_ij,b_i_,c_i_)
save_data(df)
print(df)