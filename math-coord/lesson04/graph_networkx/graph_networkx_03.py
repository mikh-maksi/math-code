import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import biadjacency_matrix

G=nx.Graph() # створити неорієнтований граф
G.add_node('a') # додати вузол
G.add_node('b') # додати вузол
G.add_node('c') # додати вузол
G.add_node('d') # додати вузол
G.add_edge('a','b') 
G.add_edge('a','c') 
G.add_edge('b','c') 
G.add_edge('c','d') 
# G.add_nodes_from([2,3,4]) # додати вузли
# G.add_edge(1,2) # додати ребро
# G.add_edges_from([(2,3),(3,4),(4,2)]) # додати ребра

print (G.number_of_nodes(), G.number_of_edges()) # кількість вузлів і ребер
print ('nodes', G.nodes) # вузли
print ('edges', G.edges) # ребра
print ('adj', G.adj) # сусіди вершин
print ('degree', G.degree) # степені вершин (кількість ребер вершин)

nx.draw(G, with_labels = True) # рисувати граф за допомогою matplotlib
# nx.draw_circular(G, with_labels = True) # інші способи візуалізації графа
# nx.draw_spectral(G, with_labels = True)
plt.show(); 
print ("Рисунок - Візуалізація графа")

print(biadjacency_matrix(G))