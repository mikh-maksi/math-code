import matplotlib.pyplot as plt

n = [0.1,0.2,0.3,0.4]
print(n)
plt.stairs(n, fill=True, label='Filled histogram\nw/ automatic edges')
plt.grid(True)
plt.show()