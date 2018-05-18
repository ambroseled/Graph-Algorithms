def dfs_tree(adj_list, start):
    """Performing a depth first search on an adjacency list"""
    n_vert = len(adj_list) #Number of vertices
    states_array = ["Undiscovered"]*n_vert #State array
    parent_array = [None]*n_vert #Parrent array
    states_array[start] = "Discovered" #Assigning start state to discovered
    parent_array = dfs_loop(adj_list, start, states_array, parent_array) #Calulating dfs_helper
    #to performing the recursion of the dfs
    return parent_array #Returning parent array


def dfs_loop(adj_list, vert, states_array, parent_array):
    """Helper for dfs_tree which performs recusion to perform dfs"""
    for edge in adj_list[vert]: #Looping over vertices adjacent to current vertex
        vertex = edge[0] #Setting new current vertex
        if states_array[vertex] == "Undiscovered": #Checking state of current vertex
            states_array[vertex] = "Discovered" #Setting state of current vertex
            parent_array[vertex] = vert #Setting parent of current vertex
            parent_array = dfs_loop(adj_list, vertex, states_array, parent_array) #Performing a
            #DFS loop on current vertex
        states_array[vertex] = "Processed" #Setting current vertex to Processed
    return parent_array #Returning parent array


"""
"Tests"

# an undirected graph

adj_list = [
    [(1, None), (2, None)],
    [(0, None), (2, None)],
    [(0, None), (1, None)]
]

print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1))
print(dfs_tree(adj_list, 2), '\n')

# a directed graph (note the asymmetrical adjacency list)

adj_list = [
[(1, None)],
[]
]

print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1), '\n')

# graph from the textbook example
graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(dfs_tree(adjacency_list(graph_string), 1), '\n')

gstring = """\
U 4
2 3
2 1
0 3
1 0
"""

print(dfs_tree(adjacency_list(gstring), 0), '\n')


"Expected output"

[None, 0, 1]
[1, None, 0]
[2, 0, None]

[None, 0]
[None, None]

[None, None, 1, 2, 3, 4, 1]

[None, 2, 3, 0]
"""
