import pandas as pd
import csv
import numpy as np

# Шлях до CSV-файлу
file_path = "c:/Work/repo/math-code/simplex/vrp-generation/input/data.csv"
file_path_out = "c:/Work/repo/math-code/simplex/vrp-generation/input/data_out.csv"
# Читання CSV
df = pd.read_csv(file_path,sep=";")
# df.to_csv(file_path_out ,mode='a',sep=";")
# df['x1'][0]=5
# df['x2'][0]=2
# df.loc[1,'x2']=6


df.loc[1,'C_i']=0
df.loc[2,'C_i']=0
df.loc[3,'C_i']=0

df.loc[1,'x3']=1
df.loc[2,'x3']=0
df.loc[3,'x3']=0

df.loc[1,'x4']=0
df.loc[2,'x4']=1
df.loc[3,'x4']=0

df.loc[1,'x5']=0
df.loc[2,'x5']=0
df.loc[3,'x5']=1

df.loc[1,'Xbase_i']=3
df.loc[2,'Xbase_i']=4
df.loc[3,'Xbase_i']=5

df = df[["C_i","Xbase_i", "x1", "x2","x3","x4","x5", "bi"]]

print(df["C_i"][1:].to_numpy())
print(df["x1"][1:].to_numpy())
print(df["x2"][1:].to_numpy())
print(df["x3"][1:].to_numpy())
print(df["x4"][1:].to_numpy())
print(df["x5"][1:].to_numpy())
print(df["bi"][1:].to_numpy())
x5_numpy = df["x1"][1:].to_numpy()
# print(x5_numpy.transpose)
print(np.transpose(x5_numpy))
x3_np = np.array(df["x3"][1:].to_numpy())
all = np.array([])
# np.insert(all,x5_numpy)
print(all)
A = np.array([df["x1"][1:].to_numpy(), df["x2"][1:].to_numpy(), df["x3"][1:].to_numpy(), df["x4"][1:].to_numpy(), df["x5"][1:].to_numpy()])
A_ij = np.array([[7,3,1,0,0],[9,2,0,1,0],[7,1,0,0,1]])
b_i = np.array([[1533],[1044],[371]])
A_t = np.transpose(A)
print(A_t)
print(A_ij)

bi_num = df["bi"][1:].to_numpy()
print(b_i)
# print(bi_num)
bi_num_shape =  bi_num.reshape(-1, 1)
print(bi_num_shape)

Xbasis_i = np.array([[3],[4],[5]])
c_i = np.array([5,2,0,0,0])

c_i_arr=[]
c_i_arr.append(df['x1'][0])
c_i_arr.append(df['x2'][0])
c_i_arr.append(0)
c_i_arr.append(0)
c_i_arr.append(0)
print(c_i_arr)
c_i_num=np.array(c_i_arr)
print(c_i_num)
print(c_i)
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