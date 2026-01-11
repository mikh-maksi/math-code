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
# coordinates_list(5)
def num_to_letters(n: int) -> str:
    """Перетворює число в буквений код (як у Excel)."""
    result = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        result = chr(65 + r) + result
    return result
# print(num_to_letters(101))

def windows_generate(n):
  import random
  windows_list = []
  for i in range(n):
    cond = True
    while cond:
      a_part = random.randint(0,10)
      b_part = random.randint(6,16)
      if (b_part-a_part)>=6:
        cond = False
    a = a_part * 30
    b = b_part * 30
    windows_list.append([a,b])
  return windows_list
# windows_generate(5)

def service_time(n):
  import random
  service_times = []
  for i in range(n):
    service_times.append(random.randint(1,10))
  return service_times
# print(service_time(5))

def weights(n):
  import random
  service_times = []
  for i in range(n):
    service_times.append((random.randint(1,5)*5))
  return service_times
# print(weights(5))

def orders(nudes_n,orders_n,weight_limit):
  import random, json
  n = 0
  orders = []
  while n <=orders_n:
    start = random.randint(0, nudes_n)
    finish = random.randint(0, nudes_n)
    if start != finish:
      weight = random.randint(1, weight_limit)
      orders.append([start, finish, weight])
      n += 1

  return json.dumps(orders)
# print(orders(8,6,50))

def vechiles(n):
  base_weight = 100
  vechiles_list =[]
  for i in range(n):
    vechiles_list.append(base_weight)
  return vechiles_list
# print(vechiles(5))

def generate(vechiles_list,coords_list,demand_list,windows_list,service_times_list):
  vehicles= []
  for i in range(len(vechiles_list)):
    vehicles.append({"id":i,"capacity":vechiles_list[i],"start": "Depot", "end": "Depot"})
  # print(vehicles)
  locations = []
  locations.append({"id":"Depot","Lat":48.210033,"Lon":16.363449,"demand":0})
  for i in range(5):
    locations.append({"id":i,"Lat":coords_list[i][0],"Lon":coords_list[i][1],"demand":demand_list[i],"a":windows_list[i][0],"b":windows_list[i][1],"service_time":service_times_list[i]})
#   print(locations)
  return {"vehicles":vehicles,"locations":locations,"distance_metric":"euclidean"}
#

# generate(vechiles(5),coordinates_list(5),weights(5),windows_generate(5),service_time(5))

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
# print(gen_balance_matrix(4))

def ln(x1,y1,x2,y2):
    import math
    return math.sqrt( pow((x1-x2),2)+pow((y1-y2),2))

def gen_c_i(n):
    import numpy as np
    c = coordinates_list(n)
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
    x_list_value= np.hstack([x_list_value, I])
    return x_list_value

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