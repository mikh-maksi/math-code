# n = 4
# list of base variables
def gen_balance_matrix(n):
    import numpy as np
    x_list = []
    for i in range(n):
        for j in range(n):
            if i!=j:
                x_list.append([i,j])
    m = (n-1)*n
    A = np.zeros((n, m), dtype=int)
    for i in range(n):
        for j in range(m):
            if x_list[j][0]==i:
                A[i][j]=1
    return(A)

print(gen_balance_matrix(4))