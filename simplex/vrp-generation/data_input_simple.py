import pandas as pd
import csv
import numpy as np

# Шлях до CSV-файлу
file_path = "c:/Work/repo/math-code/simplex/vrp-generation/input/data.csv"
file_path_out = "c:/Work/repo/math-code/simplex/vrp-generation/input/data_out.csv"
# Читання CSV
df = pd.read_csv(file_path,sep=";")
cols = len(df.columns)-1
rows = len(df)-1

print(cols)
print(rows)

cols_name = []
cols_name.append("C_i")
cols_name.append("Xbase_i")

for ii in range(cols):
    i = ii+1
    x_n_name="x"+str(i)
    cols_name.append(x_n_name)

for i in range(rows):
    x_n = i+cols+1
    x_n_name = "x"+str(x_n)
    cols_name.append(x_n_name)
    df.loc[i+1,"Xbase_i"]=x_n
    df.loc[i+1,"C_i"]=0
    df.loc[0,x_n_name]=0
    for jj in range(rows):
        j=jj+1
        n_out =0
        if i == jj:
            n_out=1
        df.loc[j,x_n_name]=n_out

cols_name.append("bi")

# print(cols_name)  
df = df[cols_name]
print(df)

all = np.array([])

A = np.array([df["x1"][1:].to_numpy(), df["x2"][1:].to_numpy(), df["x3"][1:].to_numpy(), df["x4"][1:].to_numpy(), df["x5"][1:].to_numpy()])
A_t = np.transpose(A)
# print(A_t)

bi_num = df["bi"][1:].to_numpy()
# print(b_i)
# print(bi_num)
bi_num_shape =  bi_num.reshape(-1, 1)
# print(bi_num_shape)

Xbasis_i = np.array([[3],[4],[5]])
# c_i = np.array([5,2,0,0,0])

c_i_arr=[]
c_i_arr.append(df['x1'][0])
c_i_arr.append(df['x2'][0])
c_i_arr.append(df['x3'][0])
c_i_arr.append(df['x4'][0])
c_i_arr.append(df['x5'][0])

# print(c_i_arr)
c_i_num=np.array(c_i_arr)
# print(c_i_num)
# print(c_i)

A_ij = A_t
b_i = bi_num_shape
c_i = c_i_num
# print([A_ij,b_i,c_i])


# A_ij = np.array([[7,3,1,0,0],[9,2,0,1,0],[7,1,0,0,1]])
# b_i = np.array([[1533],[1044],[371]])
# c_i = np.array([5,2,0,0,0])


df.to_csv(file_path_out ,mode='a',sep=";")

# all = 
# A_ij = np.array([[7,3,1,0,0],[9,2,0,1,0],[7,1,0,0,1.0]])
# b_i = np.array([[1533],[1044],[371]])
# Xbasis_i = np.array([[3],[4],[5]])
# c_i = np.array([5,2,0,0,0])
# Z_0 = 0

# delta_i = [0,0,0,0,0]
# fi_i = [0,0,0,0,0]

# C_i
# Xbase_i
# fi_i

# Перегляд перших 5 рядків
# print(df.head())
# print(df.columns)
# print(df['x1'][0])
# df = pd.read_csv(
#     file_path,
#     sep=";",
#     header=1,
#     skiprows=0,
#     na_values=["NA", "null", ""]
# )

# print(df.head())

# with open(file_path, newline="\n", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)