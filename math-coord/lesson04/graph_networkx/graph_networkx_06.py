import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_nodes_from([
    (0, {"pos": (0, 0)}),
    (1, {"pos": (3, 0)}),
    (2, {"pos": (8, 0)}),
])
print(nx.geometric_edges(G, radius=1))

print(nx.geometric_edges(G, radius=4))

print(nx.geometric_edges(G, radius=6))

print(nx.geometric_edges(G, radius=9))
