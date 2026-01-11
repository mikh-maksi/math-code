import numpy as np
import pandas as pd

# Simplex functions
def min_n(lst):
  i_min = 0
  min = lst[0]
  for i in range(len(lst)):
    if lst[i]<min:
      min = lst[i]
      i_min = i
  return [min,i_min]

def check_simplex_next_f(c_i,Xbasis_i,A_ij):
    Cbasis_i = []
    for i in range(len(Xbasis_i)):
        Cbasis_i.append(float(c_i[Xbasis_i[i][0]-1]))
    print(f"Cbasis_i = {Cbasis_i}")
    Z_i = []
    A_T_ij=np.transpose(A_ij)
    # print(A_T_ij)
    for i in range(len(A_T_ij)):
        Z_i.append(0)
        for j in range(len(A_T_ij[0])):
            # print(f"Cbasis_i[j] = {Cbasis_i[j]}")
            Z_i[i]+=float(Cbasis_i[j])*float(A_T_ij[i][j])
    # print(f"Z_i = {Z_i}")
    delta_i=[]
    for i in range(len(A_ij[0])):
        delta_i.append(float(Z_i[i]-c_i[i]))
    check_simplex_next=0
    print(f"delta_i= {delta_i}")
    for i in range(len(delta_i)):
        if delta_i[i] < 0:
            check_simplex_next=1
    return check_simplex_next

# data_io
def to_df(c_i,Cbasis_i,Xbasis_i,A_ij,b_i,fi_i,delta_i,Z_0):
    import pandas as pd
    import numpy as np
    data = {}
    df = pd.DataFrame(data)
    df.loc[0,'x1']="0"
    for i in range(len(Xbasis_i)):
        ii = i+1
        df.loc[ii,'Xbase_i']=Xbasis_i[i][0]
        df.loc[ii,'C_i']=Cbasis_i[i]
        df.loc[ii,'b_i']=b_i[i]
        df.loc[ii,'fi_i']=fi_i[i]

    A_T_ij=np.transpose(A_ij)
    # print(len(A_T_ij))
    arr_x=[]
    for i in range(len(A_T_ij)):
        ii = i+1
        # print()
        col_name = "x"+str(ii)
        arr_x.append(col_name)
        df.loc[0,col_name]=c_i[i]
        df.loc[4,col_name]=delta_i[i]
        for j in range(len(A_T_ij[0])):
            jj = j+1
            # print(A_T_ij[i][j])
            df.loc[jj,col_name]=A_T_ij[i][j]
                            

    line_plus = len(Xbasis_i)+1

    df.loc[line_plus,"b_i"] = Z_0[0]
    # delta =  | "x1", "x2","x3","x4","x5"
    # Z = | b_i
    arr = []
    arr.append("C_i")
    arr.append("Xbase_i")
    arr.extend(arr_x)
    arr.append("b_i")
    arr.append("fi_i")
    
    df = df[arr]

    # print(df)
    return df

def pre_simplex(A_ij,b_i,c_i):
    import numpy as np
    rows = len(A_ij)
    cols = len(A_ij[0])
    I = np.eye(rows, dtype=float)
    A_ij = np.hstack([A_ij, I])

    Xbasis_i_arr = []
    for i in range(rows):
        Xbasis_i_arr.append([cols+1+i])
        c_i=np.append(c_i,0)
    Xbasis_i = np.array(Xbasis_i_arr)

    Cbasis_i = []
    for i in range(len(Xbasis_i)):
        Cbasis_i.append(float(c_i[Xbasis_i[i][0]-1]))

    # cols for 0
    delta_i = []
    fi_i = []
    for i in range(rows):
        delta_i.append(0)
        fi_i.append(0)
    Z_0 = [0]
    return [A_ij,b_i,c_i,Xbasis_i,Cbasis_i,delta_i,fi_i,Z_0]

def data_input_file(n_file):
    import pandas as pd
    import csv
    import numpy as np

    # Шлях до CSV-файлу
    file_path = f"c:/Work/repo/math-code/simplex/vrp-generation/input/data_{n_file}.csv"

    # 1. Читання CSV
    df = pd.read_csv(file_path,sep=";")
    print(df)
    # 2. Отримуємо кількість рядків та стовпчиків.
    cols = len(df.columns)-1-1
    print(cols)
    rows = len(df)-1
    # print(rows,cols)

    # 3. Формуємо імена стовпчиків, відповідно до їх кількості
    cols_name = []
    for ii in range(cols):
        i = ii+1
        x_n_name="x"+str(i)
        cols_name.append(x_n_name)

    # 4. Формуємо матрицю A та рядок C_i
    a_arr = []
    c_i_arr=[]
    for col in cols_name:
        a_arr.append(df[col][1:])
        c_i_arr.append(df[col][0])
    A=np.array(a_arr)
    A_ij = np.transpose(A) 
    c_i=np.array(c_i_arr)

    # 5. Формуємо рядок b_i
    bi_num = df["b_i"][1:].to_numpy()
    b_i =  bi_num.reshape(-1, 1)

    # 6. Повертаємо список елементів у потрібній послідовності
    return [A_ij,b_i,c_i]

# ---------------input -----------------
file_path_out = "c:/Work/repo/math-code/simplex/vrp-generation/input/data_out_file.csv"

A_ij,b_i,c_i = data_input_file(3)
A_ij,b_i,c_i,Xbasis_i,Cbasis_i,delta_i,fi_i,Z_0=pre_simplex(A_ij,b_i,c_i)

# ---------------input -----------------
max_iteration = 10
iteration = 0

print(f"check = {check_simplex_next_f(c_i,Xbasis_i,A_ij)}")
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

    # df_out = to_df(c_i,Cbasis_i,Xbasis_i,A_ij,b_i,fi_i,delta_i,Z_0)
    # df_out.to_csv(file_path_out ,mode='a',sep=";")   
    # 16. Виводимо значення до консолі
    
    print(f"b_i = {b_i} Xbasis_i = {Xbasis_i} Cbasis_i = {Cbasis_i} Z_0 = {Z_0}")
    # print("---------------")
    # simplex_out_fnc("TASK02",A_ij,b_i,Xbasis_i,c_i,Z_0,delta_i,fi_i)

print("***************************************")

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
print(df_out)
# df_out.to_csv(file_path_out ,mode='a',sep=";")


# simplex_out_fnc("TASK02",A_ij,b_i,Xbasis_i,c_i,Z_0,delta_i,fi_i,-1,-1)