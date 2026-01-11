import numpy as np
# from data_io_fnc import to_df_start,save_data
import pandas as pd
file_path = "c:/Work/repo/math-code/simplex/vrp-generation/input/sp_list.csv"
df = pd.read_csv(file_path)
print(df)
coord_arr =[]
for i in range(4):
    base_arr=[df['lon'][i],df['lat'][i]]
    coord_arr.append(base_arr)
print(coord_arr)
# Створюємо матрицю A_ij

def coordinates_list_csv(n):
    import pandas as pd
    file_path = "c:/Work/repo/math-code/simplex/vrp-generation/input/sp_list.csv"
    df = pd.read_csv(file_path)
    print(df)
    coord_list =[]
    for i in range(n):
        base_arr=[df['lon'][i],df['lat'][i]]
        coord_list.append(base_arr)
    # print(coord_list)
    return coord_list

print(coordinates_list_csv(4))

def coordinates_list(n):
  import random
  import math
  coord_list = []
  coord_box= {"north_west_lat":48.34,"north_west_lon":16.18,"south_east_lat":48.12,"south_east_lon":16.59}
  # Згенерувати випадкову
  for i in range(n):
    a = coord_box["north_west_lat"]
    b = coord_box["south_east_lat"]
    lat = round(random.uniform(a, b),2)
    a = coord_box["north_west_lon"]
    b = coord_box["south_east_lon"]
    lon =  round(random.uniform(a, b),2)
    coord_list.append([lat,lon])
  return coord_list

def ln(x1,y1,x2,y2):
    import math
    return math.sqrt( pow((x1-x2),2)+pow((y1-y2),2))

def gen_c_i(n):
    import numpy as np
    # c = coordinates_list(n)
    c = coordinates_list_csv(n)
    coordinates_list_csv
    A = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            A[i][j] = ln(c[i][0],c[i][1],c[j][0],c[j][1])
    # print(A)
    x_list_value = np.array([])
    for i in range(n):
        for j in range(n):
            if i!=j:
                x_list_value = np.append(x_list_value,A[i][j])
    I = np.zeros(n, dtype=float)
    # x_list_value= np.hstack([x_list_value, I])
    return x_list_value
# print(coordinates_list(4))
# print(gen_c_i(4))

def gen_balance_matrix(n):
    import numpy as np
    x_list = []
    for i in range(n):
        for j in range(n):
            if i!=j:
                x_list.append([i,j])
    m = (n-1)*n
    A = np.zeros((n, m), dtype=float)
    for i in range(n):
        for j in range(m):
            if x_list[j][0]==i:
                A[i][j]=1
    return(A)

def to_df_start(A_ij,b_i,c_i):
    import pandas as pd
    import numpy as np
    data = {}
    df = pd.DataFrame(data)
    df.loc[0,'x1']="0"
    print(f"len(b_i)={len(b_i)}")
    for i in range(len(b_i)):
        ii = i+1
        df.loc[ii,'b_i']=b_i[i][0]

    A_T_ij=np.transpose(A_ij)
    arr_x=[]
    print(len(A_T_ij))
    print(f"c_i={c_i}")
    for i in range(len(A_T_ij)):
        ii = i+1
        # print()
        col_name = "x"+str(ii)
        arr_x.append(col_name)
        df.loc[0,col_name]=c_i[i]
        for j in range(len(A_T_ij[0])):
            jj = j+1
            df.loc[jj,col_name]=A_T_ij[i][j]
                            
    arr = []
    arr.extend(arr_x)
    arr.append("b_i")
    
    df = df[arr]

    # print(df)
    return df

def save_data(df):
    import pandas as pd
    file_path_all = "c:/Work/repo/math-code/simplex/vrp-generation/input/all_data.csv"
    data_info = pd.read_csv(file_path_all,sep=";")
    n = len(data_info)
    file_name = f"data_{n}.csv"
    file_path_save = f"c:/Work/repo/math-code/simplex/vrp-generation/input/{file_name}"
    print(file_path_save)
    print(df)
    df.to_csv(file_path_save ,mode='w',sep=";")
    f = open(file_path_all, "a")
    str_out = f"{n};{file_name};\n"
    f.write(str_out)
    f.close()



def gen_VRP_data(n):
    import numpy as np
    m = (n-1)*n
    A = gen_balance_matrix(n)
    I = np.eye(n, dtype=float)
    # A_ij = np.hstack([A, I])
    A_ij = A
    b_i=np.full((n, 1), 1.0)

    Xbasis_i_arr = []
    for i in range(n):
        Xbasis_i_arr.append([m+1+i])
    Xbasis_i = np.array(Xbasis_i_arr)
    c_i = gen_c_i(n)
    return [A_ij,b_i,c_i]

print(gen_VRP_data(4))

A_ij,b_i,c_i=gen_VRP_data(4)

A_t_ij = np.transpose(A_ij)

c_i_=np.array([])
for el in b_i:
    c_i_=np.append(c_i_,el[0])
b_i_=np.array([])
for el in c_i:
    el_=np.array([el])
    b_i_=np.append(b_i_,el_)


print(len(b_i))
df = to_df_start(A_ij,b_i,c_i)
print(df)
save_data(df)