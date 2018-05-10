import networkx as nx
from LexBFS import LexBFS

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
def node_index(map, u):
    return map.index(u)

def makedictionary(map, L):
    dict = {}
    for u in L:
        dict[u] = node_index(map, u)
    return dict

def sortlistwithmap(map, L):
    return makedictionary(map, L)

def induced_matching(G):
    sigma = LexBFS(G)
    visited = [False]*n
    M = []
    for u in sigma:
        neighbors = sortlistwithmap(sigma, list(G.neighbors(u)))
        for node in neighbors:
            if(node_index(sigma, node)<node_index(sigma, u) and not visited[node]):
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
#generate the tree graph
n = 100
G = nx.empty_graph(n)
G.add_edges_from(_tree_edges(n,4))
IM = induced_matching(G)
