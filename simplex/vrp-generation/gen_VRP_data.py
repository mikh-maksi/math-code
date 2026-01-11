import numpy as np
from gen_functions import gen_balance_matrix, gen_c_i
from data_io_fnc import data_input_f,to_df

# 1. Визначаємо порядок материці, що відповідає кількості точок обслуговування
n=4
# 2. Визначаємо розмірність матриці, як (n-1)*n
m = (n-1)*n
# 3. Визначаємо малансову матрицю, яка визначається як n груп по n-1 одиничних стовпчиків, яка відображає матрицю зв'язності   
A = gen_balance_matrix(n)

# 4. Створюємо одиничну матрицю 4x4 для додавання в кінець матриці зв'язності
I = np.eye(n, dtype=float)

# 5. Приписуємо справа → результат матриця 4x16
A_ij = np.hstack([A, I])
# 6. Визначаємо матрицю правих частин (одиниці)
b_i=np.ones((n, 1), dtype=float)


# 7. Визначаємо номера базисних стовпчиків: від (n-1)*n до n*n
Xbasis_i_arr = []
for i in range(n):
    Xbasis_i_arr.append([m+1+i])
Xbasis_i = np.array(Xbasis_i_arr)

# 8. Генерцємо набір коефіцієнтів при цільовій функції.
c_i = gen_c_i(n)

# 9. Додаємо значення елементів за замовчванням.
Cbasis_i = Xbasis_i
fi_i=[0,0,0,0,0]
delta_i = [9.0, 0.0, 0.0, 0.0, 2.0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Z_0 = [0]

# 10. Переводимо згенеровані математичні елементи в numpy до словника в pandas.
df_out = to_df(c_i,Cbasis_i,Xbasis_i,A_ij,b_i,fi_i,delta_i,Z_0)
print(df_out)
print(A_ij)
print(b_i)
print(c_i)


# file_path_out = "c:/Work/repo/math-code/simplex/vrp-generation/input/data_out4.csv"
# df_out.to_csv(file_path_out ,mode='a',sep=";")