def next_vertex(in_tree, distance):
    """Helper function to gain the next vertex to
    be used in Prim's and Dijkstra's algorithm"""
    possible_next = [] #Array to hold possible choices for next vertex
    next_vert = None #Initializing next vertex to None
    for index, vertex in enumerate(in_tree): #Looping over vertices in tree
        if not vertex:
            possible_next.append(index) #Vertex is not in tree so is considered for next vertex
    min_weight = distance[possible_next[0]] #Setting initial min weight
    next_vert = possible_next[0]
    for i in possible_next: #Looping over possible next vertices
        weight = distance[i] #Getting weight of current vertex
        if weight < min_weight: #Checking if current vertex has small weight than min weight
            min_weight = weight
            next_vert = i
    return next_vert #Returning next vertex



"""
"Tests"

in_tree = [False, True, True, False, False]
distance =   [float('inf'), 0, 3, 12, 5]
print(next_vertex(in_tree, distance), '\n')

in_tree = [False, False, False]
distance =   [float('inf'), 0, float('inf')]
print(next_vertex(in_tree, distance))

"Expected output"

4

1

for vertex, weight in adj_list[current_vert]:
    if not in_tree[vertex]:
        possible_next.append(vertex)
"""
