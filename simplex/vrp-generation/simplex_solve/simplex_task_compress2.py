from simplex_functions import min_n, check_simplex_next_f 
from gen_functions import gen_VRP_data
import numpy as np
import pandas as pd
# from simplex_out_f import simplex_out_fnc
from data_io_fnc import data_input_f,to_df

# ---------------input -----------------
file_path_out = "c:/Work/repo/math-code/simplex/vrp-generation/input/data_out3.csv"

A_ij,b_i,c_i,Xbasis_i_in = data_input_f()
Xbasis_i=np.array(Xbasis_i_in)
Xbasis_i = Xbasis_i.astype(int)
Z_0 = []
Z_0.append(0)

delta_i = [0,0,0,0,0]
fi_i = [0,0,0,0,0]

Cbasis_i = []
for i in range(len(Xbasis_i)):
    Cbasis_i.append(float(c_i[Xbasis_i[i][0]-1]))

# ---------------input -----------------
max_iteration = 10
iteration = 0
while (check_simplex_next_f(c_i,Xbasis_i,A_ij) and iteration<=max_iteration):
    iteration+=1
    # 1. C_Basis. Отримуємо стовпчик Cbasis_i, як елементи з коефіцієнтів цільової функції.
    Cbasis_i = []
    for i in range(len(Xbasis_i)):
        Cbasis_i.append(float(c_i[Xbasis_i[i][0]-1]))
    # 2. Z_i Рахуємо значення цільової функції
    Z_i = []
    A_T_ij=np.transpose(A_ij)
    for i in range(len(A_T_ij)):
        Z_i.append(0)
        for j in range(len(A_T_ij[0])):
            Z_i[i]+=float(Cbasis_i[j])*float(A_T_ij[i][j])
    # 3. delta_i.  Обраховуємо дельту: значення елементу цільової функції та коефіцієнту при змінній.
    delta_i=[]
    for i in range(len(A_ij[0])):
        delta_i.append(float(Z_i[i]-c_i[i]))
    # 4. За delta_i знаходимо стовпчик (i)
    basis_i = min_n(delta_i)[1]
    # 5. Знаходимо fi_i, як відношення 
    A_T_ij_basis=np.transpose(A_ij)[basis_i]
    fi_i = np.array([])
    for i in range(len(A_T_ij_basis)):
        fi_i = np.append(fi_i,b_i[i]/A_T_ij_basis[i])
    # 6. Значення ведучого стовпчика як мінімальне значення fi+i
    basis_j=min_n(fi_i)[1]
    # 7. Отримуємо значення ведучого елементу
    basis_element = A_ij[basis_j][basis_i]
    # 8. Вивеодмио LaTex
    # simplex_out_fnc("TASK02",A_ij,b_i,Xbasis_i,c_i,Z_0,delta_i,fi_i,basis_j,basis_i)
    # 9. Переводимо чисельні речі в словник і зберігаємо словник до CSV
    df_out = to_df(c_i,Cbasis_i,Xbasis_i,A_ij,b_i,fi_i,delta_i,Z_0)
    df_out.to_csv(file_path_out ,mode='a',sep=";")
    # Зробити CSV
    # 10. Перераховуємо стовпчик b_i
    b_i[basis_j]=b_i[basis_j]/basis_element    
    # 11. Перераховуємо базовий рядок
    base_string = []
    for j in range(len(A_ij[basis_j])):
        el = A_ij[basis_j][j]/basis_element
        base_string.append(el)
        A_ij[basis_j][j]=el
    # 12. Перераховуємо елементи симплекс-таблиці, які не є базовим рядком
    for i in range(len(A_ij)):
        k = A_ij[i][basis_i]
        if i!=basis_j:
            b_i[i] = b_i[i] - k*b_i[basis_j]
            for j in range(len(A_ij[0])):
                A_ij[i][j] = A_ij[i][j] - k*base_string[j]
    # 13. Змінюємо елементи, що входять до базису.
    Xbasis_i[basis_j]=basis_i+1
    # 14. Змінюємо C базисних елементів відпоівдно до того, які елементи увійшли 
    Cbasis_i = []
    for i in range(len(Xbasis_i)):
        Cbasis_i.append(float(c_i[Xbasis_i[i][0]-1]))
    # 15. Обраховуємо значення цільової функції
    Z_0=0
    for i in range(len(Xbasis_i)):
        Z_0+=b_i[i]*Cbasis_i[i]

    df_out = to_df(c_i,Cbasis_i,Xbasis_i,A_ij,b_i,fi_i,delta_i,Z_0)
    print(df_out)
    # df_out.to_csv(file_path_out ,mode='a',sep=";")   
    # 16. Виводимо значення до консолі
    
    # print(f"b_i = {b_i} Xbasis_i = {Xbasis_i} Cbasis_i = {Cbasis_i} Z_0 = {Z_0}")
    # print("---------------")
    # simplex_out_fnc("TASK02",A_ij,b_i,Xbasis_i,c_i,Z_0,delta_i,fi_i)

print("***************************************")

# print(Cbasis_i)
# print(Xbasis_i)
# print(A_ij)
# print(b_i)
# print(c_i)
# print(Z_0)
# print(delta_i)
# print(fi_i)


# як перевести матрицю в словник із заголовками типу x1,x2,x3,x4,x5,...
# !1. Робимо прикинцеві обрахунки
Cbasis_i = []
for i in range(len(Xbasis_i)):
    Cbasis_i.append(float(c_i[Xbasis_i[i][0]-1]))
# !2. Z_i
Z_i = []
A_T_ij=np.transpose(A_ij)

# Рахуємо значення цільової функції
for i in range(len(A_T_ij)):
    Z_i.append(0)
    for j in range(len(A_T_ij[0])):
        # print(f"Cbasis_i[j] = {Cbasis_i[j]}")
        Z_i[i]+=float(Cbasis_i[j])*float(A_T_ij[i][j])
# 3. delta_i. Обраховуємо дельту: значення елементу цільової функції та коефіцієнту при змінній.

delta_i=[]
for i in range(len(A_ij[0])):
    delta_i.append(float(Z_i[i]-c_i[i]))
# print(f"delta_i = {delta_i}")
fi_i=[0,0,0,0,0]

print(delta_i)
df_out = to_df(c_i,Cbasis_i,Xbasis_i,A_ij,b_i,fi_i,delta_i,Z_0)
df_out.to_csv(file_path_out ,mode='a',sep=";")


# simplex_out_fnc("TASK02",A_ij,b_i,Xbasis_i,c_i,Z_0,delta_i,fi_i,-1,-1)