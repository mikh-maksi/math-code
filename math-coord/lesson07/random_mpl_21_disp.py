import numpy as np
import math
import statistics as st
x = [17,15,23,7,9,13]

X=np.array(x)
print(X)

avg_x = np.average(X)
print(avg_x)
x_minus_avg = X - np.average(X)
print(x_minus_avg)
x_minus_avg2 = (X - np.average(X))**2
print(x_minus_avg2)
sum_2 = sum(x_minus_avg2)

s2 = sum_2/(len(X)-1)
print(s2)
print(math.sqrt(s2))

print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))


