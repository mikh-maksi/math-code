# for i in range(6000):
#     x = -1+ i/1000
#     y = 6*x**5 + 10*x**4 - 120*x**3 + 48*x**2 - 24*x + 1
#     print(x,y)
#     if y<0.01:
#         print(y)

for i in range(6000):
    x = -1+ i/1000
    y = 6*x**5 + 10*x**4 - 120*x**3 + 48*x**2 - 24*x + 1
    if abs(y)<0.01:
        print(y,x)

for i in range(6000):
    x = 2+ i/1000
    y = 6*x**5 + 10*x**4 - 120*x**3 + 48*x**2 - 24*x + 1
    if abs(y)<1:
        print(y,x)

