import networkx as nx
import matplotlib.pyplot as plt
DG = nx.DiGraph()



DG.add_weighted_edges_from([('a', 'b', 0.5), ('a', 'c', 0.75),('b', 'c', 0.75),('c', 'd', 0.75)])
DG.out_degree('a', weight='weight')

DG.degree('a', weight='weight')

list(DG.successors('a'))

list(DG.neighbors('a'))
nx.draw(DG, with_labels = True)
plt.show(); 

