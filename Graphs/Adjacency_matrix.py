def adjacency_matrix(graph_str):
    """Making an adjacency matrix from a graph string"""
    graph = graph_str.split() #Converting graph str in to list
    edge_list = [] #Initializing edge list
    adj_matrix = [] #Initializing adjacency matrix
    for k in range(int(graph[1])): #Filling adjacency matrix with inf
        adj_matrix.append([float('inf')]*int(graph[1]))
    for i in range(3, len(graph), 3): #Creating edge list
        edge_list.append((int(graph[i]), int(graph[i+1]), int(graph[i+2])))
    for j in range(int(graph[1])): #Filling values that corrospond to its self in matrix \n
        adj_matrix[j][j] = 0 #As every vertex can reach its self
    for index, edge in enumerate(edge_list): #Looping over edges to fill matrix
        adj_matrix[edge[0]][edge[1]] = edge[2]
        if graph[0] == 'U': #Adding reverse edge as graph is undirected
            adj_matrix[edge[1]][edge[0]] = edge[2]
    return adj_matrix #Returning adjacency matrix



"""
"Tests"

graph_str = """\
U 3 W
0 1 5
2 1 7
"""

print(adjacency_matrix(graph_str))

# more readable output (less readable code):
print("\nEach row on a new line:")
print("\n".join(str(lst) for lst in adjacency_matrix(graph_str)), '\n')

graph_str = """\
D 2 W
0 1 4
"""

print(adjacency_matrix(graph_str))


"Expected output"

[[0, 5, inf], [5, 0, 7], [inf, 7, 0]]

Each row on a new line:
[0, 5, inf]
[5, 0, 7]
[inf, 7, 0]

[[0, 4], [inf, 0]]
"""
