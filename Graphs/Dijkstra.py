from Next_vertex import next_vertex
from Adjacency_list import adjacency_list


def dijkstra(adj_list, start):
    """Dijkstra algorithm"""
    n_verts = len(adj_list)
    in_tree = [False]*n_verts
    distance = [float("inf")]*n_verts
    parent = [None]*n_verts
    distance[start] = 0
    vertex = start

    while not all(in_tree):
        vertex = next_vertex(in_tree, distance)
        #print(vertex)
        if vertex == None:
            break
        in_tree[vertex] = True
        for v, weight in adj_list[vertex]:
            if in_tree[v] == False and distance[vertex] + weight < distance[v]:
                distance[v]= distance[vertex] + weight
                parent[v] = vertex
    return parent, distance


city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(dijkstra(adjacency_list(city_map), 0))
