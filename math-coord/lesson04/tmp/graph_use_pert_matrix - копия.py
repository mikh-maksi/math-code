m_sm = [
    [0,4,3,0,0],
    [0,0,0,0,3],
    [0,0,0,1,3],
    [0,0,0,0,3],
    [0,0,0,0,0]
] 

a = [0,0,0,0,0]
n=0

a[1] = m_sm[0][1]
a[2] = m_sm[0][2]
a[3] = m_sm[0][3]
a[4] = m_sm[0][4]

print(a)
if m_sm[1][2]>0:
    a[2] = a[1] + m_sm[1][2]
if m_sm[1][3]>0:
    a[3] = a[1] + m_sm[1][3]

if m_sm[1][4]>0:
    a[4] = a[1] + m_sm[1][4]
print(a)


if m_sm[2][3]>0:
    a[3] = a[2] + m_sm[2][3]
if m_sm[2][4]>0:
    a[4] = a[2] + m_sm[2][4]

print(a)
if m_sm[3][4]>0:
    a[4] = a[3] + m_sm[3][4]

print(a)



# for i in range(len(m_sm)):
#     n = a[i]
#     for j in range(len(m_sm[i])):
#         a[j] += n+m_sm[i][j]


print(a)