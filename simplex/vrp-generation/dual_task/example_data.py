import numpy as np

A_ij =  np.array([[3,1,1,-1,-1,-1,0],[-2,1,2,-2,2,0,1]])
b_i =  np.array([[-8],[6]])
c_i =  np.array([6,-4,-10,-4,-20,-10,-7])


def dual_task(A_ij,b_i,c_i):
    A_t_ij = np.transpose(A_ij)
    c_i_=np.array([])
    for el in b_i:
        c_i_=np.append(c_i_,el[0])
    b_i_=np.array([])
    for el in c_i:
        el_=np.array([el])
        b_i_=np.append(b_i_,el_)
    return [A_t_ij,c_i_,b_i_]


print(dual_task(A_ij,b_i,c_i))
