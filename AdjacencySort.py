import networkx as nx
def sortadjacencylist(order, G):
    # Another Files
    adjacency = {}
    for node in order:
        adjacency[node] = []
    for node in order:
        for adjnode in G.neighbors(node):
            adjacency[adjnode].append(node)
    return adjacency
