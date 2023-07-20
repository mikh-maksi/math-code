m_sm = [
    [0,4,3,0,0],
    [0,0,0,0,3],
    [0,0,0,1,3],
    [0,0,0,0,3],
    [0,0,0,0,0]
] 

q = []
n_max = [0,0,0,0,0]
n_min = [0,0,0,0,0]
q.append(0)
while len(q)>0:
    v = q.pop(0)
    print(v)

    for i in range(len(m_sm[v])):
        if m_sm[v][i]>0:
            q.append(i)
            n_max[i] = n_max[v] + m_sm[v][i]
            if  n_min[i]==0 or (n_min[i]> n_min[v] + m_sm[v][i]):
                n_min[i] = n_min[v] + m_sm[v][i]


print(n_max)
print(n_min)





