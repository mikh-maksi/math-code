def min_n(lst):
  i_min = 0
  min = lst[0]
  for i in range(len(lst)):
    if lst[i]<min:
      min = lst[i]
      i_min = i
  return [min,i_min]

def check_delta(delta_i):
  for i in delta_i:
    print()