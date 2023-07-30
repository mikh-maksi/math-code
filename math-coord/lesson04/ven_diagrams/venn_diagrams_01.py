import pylab as plt
from matplotlib_venn import venn3, venn3_circles

v = venn3(subsets=(1,1,0,1,0,0,0))
v.get_label_by_id('100').set_text('First')
v.get_label_by_id('010').set_text('Second')
v.get_label_by_id('001').set_text('Third')
plt.title("Not a Venn diagram")
plt.show()