import itertools 
s = "ABC" 
com_set = itertools.combinations(s, 2) 
for elem in com_set: 
    print(elem)

