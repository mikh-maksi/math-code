from simplex_functions import min_n, check_simplex_next_f 
from gen_functions import gen_VRP_data
import numpy as np
from simplex_out_f import simplex_out_fnc

# ---------------input -----------------
A_ij = np.array([[7,3,1,0,0],[9,2,0,1,0],[7,1,0,0,1.0]])
b_i = np.array([[1533],[1044],[371]])
Xbasis_i = np.array([[3],[4],[5]])
c_i = np.array([5,2,0,0,0])
Z_0 = 0
delta_i = [0,0,0,0,0]
fi_i = [0,0,0,0,0]
# A_ij,b_i,Xbasis_i,c_i = gen_VRP_data(4)

# print(A_ij)
# print(b_i)
# print(Xbasis_i)
# print(c_i)
# ---------------input -----------------
max_iteration = 10
iteration = 0
while (check_simplex_next_f(c_i,Xbasis_i,A_ij) and iteration<=max_iteration):
    iteration+=1
    print(f"----iteration {iteration}----")
    # 1. C_Basis.
    # Отримуємо стовпчик Cbasis_i, як елементи з коефіцієнтів цільової функції.
    Cbasis_i = []
    for i in range(len(Xbasis_i)):
        Cbasis_i.append(float(c_i[Xbasis_i[i][0]-1]))

    # 2. Z_i
    Z_i = []
    A_T_ij=np.transpose(A_ij)
    # print(A_T_ij)
    print(A_ij)
    print(f"b_i={b_i}")

    # Рахуємо значення цільової функції
    for i in range(len(A_T_ij)):
        Z_i.append(0)
        for j in range(len(A_T_ij[0])):
            # print(f"Cbasis_i[j] = {Cbasis_i[j]}")
            Z_i[i]+=float(Cbasis_i[j])*float(A_T_ij[i][j])
    print(f"Z_i = {Z_i}")
    # Для поточного базису
    # 3. delta_i
    # Обраховуємо дельту: значення елементу цільової функції та коефіцієнту при змінній.
    
    delta_i=[]
    for i in range(len(A_ij[0])):
        delta_i.append(float(Z_i[i]-c_i[i]))
    print(f"delta_i = {delta_i}")
    # За delta_i знаходимо стовпчик (i)
    basis_i = min_n(delta_i)[1]
    print(f"basis_i = {basis_i}")
    # -----------------fi_i, basis_j
    A_T_ij_basis=np.transpose(A_ij)[basis_i]
    fi_i = np.array([])
    for i in range(len(A_T_ij_basis)):
        fi_i = np.append(fi_i,b_i[i]/A_T_ij_basis[i])
    print(f"fi_i = {fi_i}")
    basis_j=min_n(fi_i)[1]
    print(f"basis_j = {basis_j}")
    # --------- matrix recumputing
    # ---------- take base element
    basis_element = A_ij[basis_j][basis_i]
    simplex_out_fnc("TASK02",A_ij,b_i,Xbasis_i,c_i,Z_0,delta_i,fi_i,basis_j,basis_i)
    
    # print(f"Prog:{basis_j} {basis_i}, Math: {basis_j+1} {basis_i+1} {basis_element}")
    # ---------- Base string
    # print(b_i)
    # print(f"b_i[basis_j] = {b_i[basis_j]}")
    # print(f"{basis_j} {basis_element} b_i = {b_i} b_i[basis_j]= {b_i[basis_j]}")
    b_i[basis_j]=b_i[basis_j]/basis_element

    base_string = []
    for j in range(len(A_ij[basis_j])):
        el = A_ij[basis_j][j]/basis_element
        base_string.append(el)
        A_ij[basis_j][j]=el

    # print(f"b_i[basis_j] = {b_i[basis_j]}")
    # ---------- non base string
    for i in range(len(A_ij)):
        k = A_ij[i][basis_i]
        if i!=basis_j:
            # print(f"b_i[i] = {b_i[i]} basis_j = {basis_j} basis_i = {basis_i} k = {k} b_i[basis_j]={b_i[basis_j]}")
            b_i[i] = b_i[i] - k*b_i[basis_j]
            for j in range(len(A_ij[0])):
                A_ij[i][j] = A_ij[i][j] - k*base_string[j]

    # --------------- Change basis (Xbasis_i, C)

    # Як замінити Xbasis_i 
    # print(Xbasis_i)
    Xbasis_i[basis_j]=basis_i+1
    # print(A_ij)
    Cbasis_i = []

    for i in range(len(Xbasis_i)):
        Cbasis_i.append(float(c_i[Xbasis_i[i][0]-1]))
    Z_0=0

    for i in range(len(Xbasis_i)):
        Z_0+=b_i[i]*Cbasis_i[i]

    print(f"b_i = {b_i} Xbasis_i = {Xbasis_i} Cbasis_i = {Cbasis_i} Z_0 = {Z_0}")
    print("---------------")
    # simplex_out_fnc("TASK02",A_ij,b_i,Xbasis_i,c_i,Z_0,delta_i,fi_i)

Cbasis_i = []
for i in range(len(Xbasis_i)):
    Cbasis_i.append(float(c_i[Xbasis_i[i][0]-1]))

# 2. Z_i
Z_i = []
A_T_ij=np.transpose(A_ij)
# print(A_T_ij)
print(A_ij)
print(f"b_i={b_i}")

# Рахуємо значення цільової функції
for i in range(len(A_T_ij)):
    Z_i.append(0)
    for j in range(len(A_T_ij[0])):
        # print(f"Cbasis_i[j] = {Cbasis_i[j]}")
        Z_i[i]+=float(Cbasis_i[j])*float(A_T_ij[i][j])
print(f"Z_i = {Z_i}")
# Для поточного базису
# 3. delta_i
# Обраховуємо дельту: значення елементу цільової функції та коефіцієнту при змінній.

delta_i=[]
for i in range(len(A_ij[0])):
    delta_i.append(float(Z_i[i]-c_i[i]))
print(f"delta_i = {delta_i}")
fi_i=[0,0,0,0,0]
simplex_out_fnc("TASK02",A_ij,b_i,Xbasis_i,c_i,Z_0,delta_i,fi_i,-1,-1)

# print(Xbasis_i)

# print(basis_j)
# print(basis_i)