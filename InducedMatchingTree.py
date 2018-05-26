import networkx as nx
from LexBFS import LexBFS
from BFS import BreadthFirstKLevels
from AdjacencySort import sortadjacencylist
import matplotlib.pyplot as plt

#Tree generator
def _tree_edges(n,r):
    # helper function for trees
    # yields edges in rooted tree at 0 with n nodes and branching ratio r
    nodes=iter(range(n))
    parents=[next(nodes)] # stack of max length r
    while parents:
        source=parents.pop(0)
        for i in range(r):
            try:
                target=next(nodes)
                parents.append(target)
                yield source,target
            except StopIteration:
                break

def makedictionary(maplist):
    dictionary = {}
    for index, value in enumerate(maplist):
        dictionary[value] = index
    return dictionary



def sortlistwithmap(mapping, L):
    sortedlist = []
    for item in sorted(mapping.items(), key=lambda x: (x[1], x[0])):
        sortedlist.append(item[0])
    return sortedlist


def induced_matching(G):
    sigma = LexBFS(G)
    visited = [False]*len(G.nodes)
    M = []
    sigmamapping = makedictionary(sigma)
    adjacencylist = sortadjacencylist(sigma, G)
    # print adjacencylist
    for u in sigma:
        if visited[u]:
            continue
        # neighbors = sortlistwithmap(sigmamapping, list(G.neighbors(u)))
        neighbors = adjacencylist[u]
        for node in neighbors:
            if(sigmamapping[node]<sigmamapping[u] and not visited[node]):
                v = node
                M.append((v, u))
                Nv = G.neighbors(v)
                Nu = G.neighbors(u)
                for node in Nv:
                    visited[node] = True
                for node in Nu:
                    visited[node] = True
                visited[u] = True
                visited[v] = True
                G.remove_nodes_from(Nv)
                G.remove_nodes_from(Nu)
    return M
def distancekmatching(G, k):
    sigma = LexBFS(G)
    visited = [False]*len(G.nodes)
    M = []
    sigmamapping = makedictionary(sigma)
    adjacencylist = sortadjacencylist(sigma, G)
    for u in sigma:
        if visited[u]:
            continue
        # neighbors = sortlistwithmap(sigmamapping, list(G.neighbors(u)))
        neighbors = adjacencylist[u]
        for node in neighbors:
            if(sigmamapping[node]<sigmamapping[u] and not visited[node]):
                v = node
                M.append((v, u))
                Nkv = BreadthFirstKLevels(G,v,k)
                Nku = BreadthFirstKLevels(G,u,k)
                for node in Nkv:
                    visited[node] = True
                for node in Nku:
                    visited[node] = True
                visited[u] = True
                visited[v] = True
                G.remove_nodes_from(Nkv)
                G.remove_nodes_from(Nku)
    return M
#generate the tree graph
n = 200
G = nx.empty_graph(n)
G.add_edges_from(list(_tree_edges(n,4)))
H = G.copy()
nx.write_adjlist(G,"test.adjlist")
IM = induced_matching(H)
k = 3
DkM = distancekmatching(H, k)
