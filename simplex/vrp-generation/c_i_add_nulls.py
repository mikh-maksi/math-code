from gen_functions import coordinates_list,ln
import numpy as np
def gen_c_i(n):
    import numpy as np
    c = coordinates_list(n)
    A = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            A[i][j] = ln(c[i][0],c[i][1],c[j][0],c[j][1])
    print(A)
    x_list_value = np.array([])
    for i in range(n):
        for j in range(n):
            if i!=j:
                x_list_value = np.append(x_list_value,A[i][j])
    # I = np.zeros(n, dtype=float)
    # x_list_value= np.hstack([A, I])
    return x_list_value
print(gen_c_i(4))
c_i = gen_c_i(4)
I = np.zeros(4, dtype=float)
print(I)
x_list_value_null= np.hstack([c_i, I])
print(x_list_value_null)