from data_io_fnc import data_input_f,to_df,data_input_file
import numpy as np
# print(data_input_file(1))

r_f = data_input_f()
# print(r_f)

# Xbasis_i_in - [cols-2,cols-2+1,cols-2+2...cols-2+m-1)
A_ij,b_i,c_i,Xbasis_i_in = data_input_f()
print(A_ij)
A_ij,b_i,c_i = data_input_file(1)




print(pre_simplex(A_ij,b_i,c_i))
# додати елементи до A_ij
# формувати Xbasis_i_in
