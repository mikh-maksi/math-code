import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph() # створити неорієнтований граф
G.add_node(1) # додати вузол
G.add_nodes_from([2,3,4]) # додати вузли
G.add_edge(1,2) # додати ребро
G.add_edges_from([(2,3),(3,4),(4,2)]) # додати ребра

print (G.number_of_nodes(), G.number_of_edges()) # кількість вузлів і ребер
print ('nodes', G.nodes) # вузли
print ('edges', G.edges) # ребра
print ('adj', G.adj) # сусіди вершин
print ('degree', G.degree) # степені вершин (кількість ребер вершин)

nx.draw(G, with_labels = True) # рисувати граф за допомогою matplotlib
plt.show(); 
print ("Рисунок - Візуалізація графа")

nx.draw(G, pos=nx.nx_agraph.graphviz_layout(G)) # нарисувати граф
