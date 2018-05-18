from Next_vertex import next_vertex
import copy

def floyd(adjacency_matrix):
    """Implementing Floyd's algortihm"""
    n_vert = len(adjacency_matrix) #Getting num ber of vertices
    through_k = 0 #Initializing through_k to 0
    output = copy.copy(adjacency_matrix)

    for k in range(n_vert): #Looping over all vertices with k
        for i in range(n_vert): #Looping over all vertices with i
            for j in range(n_vert):#Looping over all vertices with j
                through_k = output[i][k] + output[k][j]
                if through_k < output[i][j]:
                    output[i][j] = through_k
    return output



"""
"Tests"

graph_str = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

print(floyd(adjacency_matrix(graph_str)), '\n')

import pprint

# example from the textbook - figure 6.3

graph_str = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2
"""

pprint.pprint(floyd(adjacency_matrix(graph_str)))


"Expected output"

[[0, 1, 3], [6, 0, 2], [4, 5, 0]]

[[0, 5, 7, 11, 11, 10, 12],
 [5, 0, 9, 13, 7, 9, 11],
 [7, 9, 0, 4, 4, 3, 5],
 [11, 13, 4, 0, 8, 7, 9],
 [11, 7, 4, 8, 0, 2, 4],
 [10, 9, 3, 7, 2, 0, 2],
 [12, 11, 5, 9, 4, 2, 0]]
"""
