n = 4
# list of base variables
x_list = []
for i in range(n):
    for j in range(n):
        if i!=j:
            x_list.append([i,j])
        # print(f"x_{i}_{j}")
print(x_list)
import numpy as np


# Створюємо квадратну матрицю n x n, заповнену нулями
m = (n-1)*n
A = np.zeros((n, m), dtype=int)
for i in range(n):
    for j in range(m):
        if x_list[j][0]==i:
            A[i][j]=1
        # No balance condition to depout
        if x_list[j][1]==i and x_list[j][0]!=0:
            A[i][j]=-1
# print(A)
A2 = np.zeros((n, m), dtype=int)
for i in range(n):
    for j in range(m):
        if x_list[j][0]==i:
            A2[i][j]=1
print(A2)

Q = [0,3,4,5]
# Q - n*

# A
