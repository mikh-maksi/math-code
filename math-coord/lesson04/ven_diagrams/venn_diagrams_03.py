import matplotlib.pyplot as plt
from matplotlib_venn import venn3

set1 = set([11,12,13,14,15,16,17,18,19])
set2 = set([2,4,6,8,10,12,14,16,18])
set3 = set([3,6,9,12,15,18])

venn3([set1, set2, set3], ('>10', 'Парні', 'Кратні 3'))

plt.show()