import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats
import statistics 


n = [0.0016,0.0256,0.1536,0.4096,0.4096]
mean,std = stats.norm.fit(n)
print(mean,std)

print(statistics.variance(n))
print(statistics.stdev(n))
print(statistics.pvariance(n))
print(statistics.pstdev(n))
