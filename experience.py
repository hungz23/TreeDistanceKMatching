import time
import networkx as nx
from LexBFS import LexBFS
# from BFS import BreadthFirstKLevels
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

def BreadthFirstKLevels(G,root,k):
    visited = set()
    currentLevel = [root]
    level = 0
    nodelist = []
    while (currentLevel):
        for v in currentLevel:
            visited.add(v)
        nextLevel = set()
        levelGraph = {v:set() for v in currentLevel}
        for v in currentLevel:
            for w in G[v]:
                if w not in visited:
                    levelGraph[v].add(w)
                    nextLevel.add(w)
        # yield levelGraph
        # print levelGraph.keys()
        nodelist = nodelist + levelGraph.keys()
        level = level + 1
        if level>k:
            break
        currentLevel = nextLevel
    return nodelist

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
                break
    return M
def distancekmatching(G, k):
    sigma = LexBFS(G)
    # print sigma
    visited = [False]*len(G.nodes)
    M = []
    sigmamapping = makedictionary(sigma)
    adjacencylist = sortadjacencylist(sigma, G)
    complex = 0
    for u in sigma:
        if not visited[u]:
            # neighbors = sortlistwithmap(sigmamapping, list(G.neighbors(u)))
            neighbors = adjacencylist[u]
            for node in neighbors:
                if(sigmamapping[node]<sigmamapping[u] and not visited[node]):
                    v = node
                    M.append((v, u))
                    Nkv = BreadthFirstKLevels(G,v,k-1)
                    Nku = BreadthFirstKLevels(G,u,k-1)
                    complex = complex + len(Nkv) + len(Nku)
                    for node in Nkv:
                        visited[node] = True
                    for node in Nku:
                        visited[node] = True
                    # visited[u] = True
                    # visited[v] = True
                    # G.remove_nodes_from(Nkv)
                    # G.remove_node(v)
                    # G.remove_nodes_from(Nku)

                    # print "::::::::::::::::::::::::::::::----------------"
                    # print str((u,v))
                    # print str(G.edges)
                    # # print visited
                    # print "::::::::::::::::::::::::::::::-----------------"
                    break
    print complex
    return M
# generate the tree graph
n = 100
G = nx.empty_graph(n)
G.add_edges_from(list(_tree_edges(n,3)))

# G = nx.balanced_tree(4,9)

# G = nx.random_powerlaw_tree(n=10000, gamma=3, seed=None, tries=1000000)

# G = nx.degree_sequence_tree([1,2,3,4,1,1,1,1])

H = G.copy()
nx.write_adjlist(G,"test.adjlist")
start_time = time.time()
# IM = induced_matching(H)
k=3
DkM = distancekmatching(H, k)
print(str(len(G.nodes))+"---"+str(len(G.edges))+"---"+str(len(DkM))+"--- %s seconds ---" % (time.time() - start_time))
Try = BreadthFirstKLevels(G,0,k-1)

#Testing




# # Adding colors
sigma = LexBFS(G)
edges = G.edges()
for u,v in edges:
    G[u][v]['color']='black'
for edge in DkM:
    G[edge[0]][edge[1]]['color']='red'
colors = [G[u][v]['color'] for u,v in edges]
nx.draw(G, pos=nx.spring_layout(G), edges=edges, edge_color=colors, node_size=10)
 # with_labels = True)
plt.savefig("Tree_100_3.png", format="PNG")
print sigma
