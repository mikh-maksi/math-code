def min_n(lst):
  i_min = 0
  min = lst[0]
  for i in range(len(lst)):
    if lst[i]<min:
      min = lst[i]
      i_min = i
  return [min,i_min]

# результат = np.dot(matrix1, matrix2)
# transpose = np.transpose(matrix1)
# large_matrix = np.zeros((1000, 1000))
# elementwise_product = matrix1 * matrix2
# matrix = np.array([[7,3],[9,2],[7,1]])

import numpy as np

matrix = np.array([[7,3,1,0,0],[9,2,0,1,0],[7,1,0,0,1.0]])
b_i = np.array([[1533],[1044],[371]])
fi = np.array([[219],[116],[53]])
ci_base = np.array([[0],[0],[0]])
xi_base = np.array([[3],[4],[5]])
ci = np.array([5,2,0,0,0])
zi_ci=np.array([-5,-2,0,0,0])
z=0
# print(matrix,b)

print(ci)
arr = np.concatenate((ci_base, xi_base,matrix,b_i,fi), axis=1)
print(arr)
dd = np.array([9999,0])
arr1=np.array([np.hstack((dd,zi_ci))])
print(arr1)

ii = len(matrix) #3
jj = len(matrix[0]) #5
# for i in range(ii):
#   for j in range(jj):
#     print(matrix[i,j])
zi = np.array([0,0,0,0,0])
for j in range(jj):
  for i in range(ii):
    zi[j]+=ci_base[i].item()*matrix[i,j]
  zi_ci[j] = zi[j]-ci[j]
print(zi)
print(zi_ci)

min,i_min = min_n(zi_ci)
print(min,i_min)
# fi = []
a_i = np.array([0,0,0])
fi_i = np.array([0,0,0])
for i in range(ii):
  a_i[i]=matrix[i,i_min].item()
  fi_i[i] = float(b_i[i].item()/a_i[i].item())
print(fi_i)
min,i_min = min_n(fi_i)
print(min,i_min)



import numpy as np

# A_{ij} – матриця відстаней
# b_j – стовпчик правих частин обмежень
# C_i – рядок коефіцієнтів при цільовій функції
n = 3
m = 5

A_ij = np.array([[7,3,1,0,0],[9,2,0,1,0],[7,1,0,0,1.0]])
b_i = np.array([[1533],[1044],[371]])
ci = np.array([5,2,0,0,0])
Xbasis_i = np.array([[3],[4],[5]])

# -------------------
Cbasis_i = []
delta_i=[]
for i in range(len(xi_base)):
  Cbasis_i.append(int(ci[Xbasis_i[i][0]-1]))
  delta_i.append(int(Cbasis_i[i]-ci[i]))
print(Cbasis_i)
print(delta_i)

# Номер стовпчика, що виводиться з базису.
print(min_n(delta_i)[1])
basis_i = min_n(delta_i)[1]

# -----------------

print(np.transpose(A_ij)[basis_i])
A_T_ij=np.transpose(A_ij)[basis_i]
fi_i = np.array([])
for i in range(len(A_T_ij)):
  print(A_T_ij[i])
  print(b_i[i])
  fi_i = np.append(fi_i,b_i[i]/A_T_ij[i])
print(fi_i)
print(min_n(fi_i))
basis_j=min_n(fi_i)[1]
print(basis_j)

# -------------------------
# A_ij = np.array([[7,3,1,0,0],[9,2,0,1,0],[7,1,0,0,1.0]])

# print(basis_i,basis_j)


basis_element = A_ij[basis_j][basis_i]
print(basis_element)

# ------------------------
print(A_ij[2])
print(A_ij)
base_string = []
for j in range(len(A_ij[basis_j])):
  el = A_ij[basis_j][j]/basis_element
  base_string.append(el)
  A_ij[basis_j][j]=el
print(A_ij)
for i in range(len(A_ij)):
  k = A_ij[i][basis_i]
  for j in range(len(A_ij[0])):
    if i!=basis_j:
      A_ij[i][j] = A_ij[i][j] - k*base_string[j]
print(A_ij)