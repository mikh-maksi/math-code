from gen_functions import generate,vechiles,orders,weights,service_time,windows_generate,num_to_letters,coordinates_list
import math
import numpy as np
# generate(vechiles(5),coordinates_list(5),weights(5),windows_generate(5),service_time(5))
n=4
def ln(x1,y1,x2,y2):
    return math.sqrt( pow((x1-x2),2)+pow((y1-y2),2))

def gen_c_i(n):
    c = coordinates_list(n)
    A = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            A[i][j] = ln(c[i][0],c[i][1],c[j][0],c[j][1])
    print(A)
    x_list_value = []
    for i in range(n):
        for j in range(n):
            if i!=j:
                x_list_value.append(A[i][j])
    return x_list_value

print(gen_c_i(4))