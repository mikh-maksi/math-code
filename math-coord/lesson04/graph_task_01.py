import graph

for tp in graph.tops:
    graph.top(tp['x'],tp['y'],tp['n'])

graph.edge_n(1,2)
graph.edge_n(0,1)
graph.edge_n(0,2)
graph.edge_n(0,3)
graph.edge_n(0,4)


adj_matrix = [
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0],
]
import numpy as np
a = np.array(adj_matrix)
a = a.transpose()
print(a)


# adj_matrix = [
#     [0,0,0,1,1],
#     [1,0,0,0,1],
#     [0,1,0,0,1],
#     [0,1,0,1,0],
#     [1,1,0,0,0],
#     [0,1,1,0,0],
#     [0,0,1,1,0]
# ]

# for i in range(len(adj_matrix)):
#     print(adj_matrix[i])



for i in range(len(a)):
    # print(f"-->{a[i]}")
    n1 = 0
    n2 = 0
    for j in range(len(a[i])):
        # print(f"{a[i][j]}-{n1}-{n2}")
        if a[i][j] == 1 and n1!=0:
            n2 = j
        if a[i][j] == 1 and n1==0:
            n1 = j

    print(f"n1 = {n1}, n2= {n2}")



    # n1 = 0
    # n2 = 0
    # for j in range(len(adj_matrix[i])):
    #     if adj_matrix[i][j] == 1 and n1==0:
    #         n1 = j
    #     if adj_matrix[i][j] == 1 and n1!=0:
    #         n2 = j
    # print(n1,n2)
    # graph.edge_n(n1,n2)




graph.root.mainloop()