def bfs_tree(adj_list, start):
    """Perfoming a breadth first search"""
    parent_array = [None]*len(adj_list) #Initializing parent array filled with None
    cur_node = adj_list[start] #Gettign initial vertex
    state = ['Undiscovered']*len(adj_list) #Filling state array with Undiscovered
    to_check = [start] #Adding initial vertex to queue
    return bfs_loop(adj_list, to_check, state, parent_array) #Performing BFS loop and returning result


def bfs_loop(adj_list, to_check, state, parent_array):
    """helper for bfs function performing loop"""
    while to_check: #Looping until there are no more vertices to check
        node = to_check.pop(0) #Getting current vertex
        for edge in adj_list[node]: #Looping over vertices adjacent to current vertex
            if state[edge[0]] == 'Undiscovered': #Checking state of adjacent vertex
                state[edge[0]] = 'Discovered' #Setting state of adjacent vertex
                parent_array[edge[0]] = node #Adding current node as parent of adjacent vertex
                to_check.append(edge[0]) #Adding adjacent vertex to queue
        state[node] = 'Processed' #Setting current vertex state to Processed
    return parent_array #Returning parent array


"""
"Tests"

# an undirected graph

adj_list = [
    [(1, None)],
    [(0, None), (2, None)],
    [(1, None)]
]

print(bfs_tree(adj_list, 0))
print(bfs_tree(adj_list, 1), '\n')

# a directed graph (note the asymmetrical adjacency list)

adj_list = [
[(1, None)],
[]
]

print(bfs_tree(adj_list, 0))
print(bfs_tree(adj_list, 1), '\n')

graph_string = """\
D 2
0 1
"""

print(bfs_tree(adjacency_list(graph_string), 0), '\n')

graph_string = """\
D 2
0 1
1 0
"""

print(bfs_tree(adjacency_list(graph_string), 1), '\n')

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

print(bfs_tree(adjacency_list(graph_string), 1), '\n')

graph_string = """\
D 2 W
0 1 99
"""

print(bfs_tree(adjacency_list(graph_string), 0), '\n')

"Expected output"
[None, 0, 1]
[1, None, 1]

[None, 0]
[None, None]

[None, 0]

[1, None]

[None, None, 1, 2, 5, 1, 1]

[None, 0]
"""
