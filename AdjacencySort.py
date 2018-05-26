"""
Sorting the adjacency lists of a graph.

Input: The unsorted adjacency lists of a graph G = (V, E)
and a order of vertices
Output: The sorted adjacency lists

The Algorithm is represented by Martin Charles Golumbic in 2004.
Golumbic, Martin Charles. Algorithmic graph theory and perfect graphs.
Vol. 57. Elsevier, 2004.
"""
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
# G = nx.Graph.karate_club_graph()
