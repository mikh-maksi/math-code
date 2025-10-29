def delivery_orders_out(nudes_n,orders_n,weight_limit):
  # generating orders_n (number of orders) pairs for service: start and finish is less than nudes_n (number of nudes). Weight for order is less than weight_limit
  import random, json
  # nudes_n = 8
  # orders_n = 6
  # weight_limit = 50
  n = 0
  orders = []
  while n <=orders_n:
    start = random.randint(0, nudes_n)
    finish = random.randint(0, nudes_n)
    if start != finish:
      weight = random.randint(1, weight_limit)
      orders.append({"start":start, "finish":finish, "weight":weight})
      n += 1

  return json.dumps(orders)
# Only wiegthed pairs
print(delivery_orders_out(8,6,50))


def delivery_length_out(nudes_n,orders_n,weight_limit):
  import random, json
  # nudes_n = 8
  # orders_n = 6
  # weight_limit = 50
  n = 0
  orders = []
  for i in range(nudes_n):
    # l.append([])
    for j in range(nudes_n):
      weight= random.randint(0, weight_limit)
      if i == j:
        weight=0
      orders.append({"start":i, "finish":j, "weight":weight})

  return json.dumps(orders)
# All pairs
print(delivery_length_out(6,6,50))


# Decoration format

def delivery_length_json(in_json):
  import json
  # print("Delivery orders")
  y = json.loads(in_json)
  max_start = 0
  for i in range(len(y)):
    if max_start < y[i]["start"]:
      max_start = y[i]["start"]
  rang = max_start +1
  print(rang)
  table_caption = "Delivery orders"
  column_list = []
  header_list = []

  for i in range(rang):
    header_list.append(i)
    column_list.append(i)
  # base_matrix = []


  # y = json.loads(delivery_orders_out(6,6,50))
  base_matrix = []
  for i in range(rang):
    string_out = ""
    string_matrix = []
    for j in range(rang):
      for k in range(len(y)):
        n = 0
        if y[k]["start"] == i and y[k]["finish"] == j:
          n = y[k]['weight']
          break
      string_matrix.append(n)
      string_out+= f"{n:^6d}|"
    base_matrix.append(string_matrix)
    # print(string_out)
    # print()
  json_out = {"table_caption":table_caption,"header_list":header_list, "column_list":column_list, "base_matrix":base_matrix}
  return json.dumps(json_out)

print(delivery_length_json(delivery_length_out(6,6,10)))