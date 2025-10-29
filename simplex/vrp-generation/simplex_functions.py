import numpy as np
def min_n(lst):
  i_min = 0
  min = lst[0]
  for i in range(len(lst)):
    if lst[i]<min:
      min = lst[i]
      i_min = i
  return [min,i_min]

# def check_delta(delta_i):
#   for i in delta_i:
#     print()


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
    print(f"Z_i = {Z_i}")
    delta_i=[]
    for i in range(len(A_ij[0])):
        delta_i.append(float(Z_i[i]-c_i[i]))
    check_simplex_next=0
    print(f"delta_i= {delta_i}")
    for i in range(len(delta_i)):
        if delta_i[i] < 0:
            check_simplex_next=1
    return check_simplex_next