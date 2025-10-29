import numpy as np
from gen_functions import gen_balance_matrix, gen_c_i

def gen_VRP_data(n):
    import numpy as np
    m = (n-1)*n
    A = gen_balance_matrix(n)
    I = np.eye(n, dtype=float)
    A_ij = np.hstack([A, I])

    b_i=np.ones((n, 1), dtype=float)

    Xbasis_i_arr = []
    for i in range(n):
        Xbasis_i_arr.append([m+1+i])
    Xbasis_i = np.array(Xbasis_i_arr)
    c_i = gen_c_i(n)
    return [A_ij,b_i,Xbasis_i,c_i]
print(gen_VRP_data(4))