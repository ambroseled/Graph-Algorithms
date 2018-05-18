def adjacency_list(graph_str):
    """Making adjacency list from a graph string for both directed and undirected graphs"""
    graph = graph_str.splitlines() #Splitting graph str into lines
    undirected = False #Catch variable if the graph is undirected
    edges = [edge.split() for edge in graph] #Getting edge out of lines
    if edges[0][0] == 'U': #Checking if graph is undirected
        undirected = True
    inc = 2 #Settign increment for an unweighted graph
    if len(edges[0]) == 3:
        inc = 3 #Updating increment for a weighted graph
    adj_lst = [[] for _ in range(int(edges[0][1]))] #Filling empty adjacency list
    edges.pop(0) #Popping graph header
    for edge in edges: #Looping on edges
        vertex = int(edge[0]) #Settign current vertex
        if inc == 2: #Appedning to adjacency list for unweighted
            adj_lst[vertex].append((int(edge[1]), None))
            if undirected and not (vertex, None) in adj_lst[int(edge[1])]:
                adj_lst[int(edge[1])].append((vertex, None)) #Appending edge for undirected
        else: #Appending to adjacency list for weighted graph
            adj_lst[vertex].append((int(edge[1]), int(edge[2])))
            if undirected and not (vertex, int(edge[2])) in adj_lst[int(edge[1])]:
                adj_lst[int(edge[1])].append((vertex, int(edge[2]))) #Appending for undirected
    return adj_lst #Returning adjacency list

def tests():
    "Tests"

    from pprint import pprint

    graph_string = """
    D 3
    0 1
    1 0
    0 2
    """
    print(adjacency_list(graph_string), '\n')

    graph_string = """\
    D 3 W
    0 1 7
    1 0 -2
    0 2 0
    """
    print(adjacency_list(graph_string), '\n')


    graph_string = """\
    D 7
    1 6
    1 2
    1 5
    2 5
    2 3
    5 4
    3 4
    """

    pprint(adjacency_list(graph_string))
    print('')


    # undirected graph from the textbook example
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

    pprint(adjacency_list(graph_string))
    print('')

    "Expected output"
    [[(1, None), (2, None)], [(0, None)], []]

    [[(1, 7), (2, 0)], [(0, -2)], []]

    [[],
     [(6, None), (2, None), (5, None)],
     [(5, None), (3, None)],
     [(4, None)],
     [],
     [(4, None)],
     []]

    [[],
     [(2, None), (5, None), (6, None)],
     [(1, None), (3, None), (5, None)],
     [(2, None), (4, None)],
     [(3, None), (5, None)],
     [(1, None), (2, None), (4, None)],
     [(1, None)]]
