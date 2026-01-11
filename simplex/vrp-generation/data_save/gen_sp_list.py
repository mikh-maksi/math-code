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


def gen_VRP_data(n):
    import numpy as np
    m = (n-1)*n
    A = gen_balance_matrix(n)
    I = np.eye(n, dtype=float)
    A_ij = np.hstack([A, I])

    b_i=np.full((n, 1), 1.0)

    Xbasis_i_arr = []
    for i in range(n):
        Xbasis_i_arr.append([m+1+i])
    Xbasis_i = np.array(Xbasis_i_arr)
    c_i = gen_c_i(n)
    return [A_ij,b_i,Xbasis_i,c_i]

print(gen_VRP_data(4))