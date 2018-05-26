"""BFS.py

Breadth First Search. See also LexBFS.py.

D. Eppstein, May 2007.
"""
import networkx as nx
def BreadthFirstLevels(G,root):
    """
    Generate a sequence of bipartite directed graphs, each consisting
    of the edges from level i to level i+1 of G. Edges that connect
    vertices within the same level are not included in the output.
    The vertices in each level can be listed by iterating over each
    output graph.
    """
    visited = set()
    currentLevel = [root]
    while currentLevel:
        for v in currentLevel:
            visited.add(v)
        nextLevel = set()
        levelGraph = {v:set() for v in currentLevel}
        for v in currentLevel:
            for w in G[v]:
                if w not in visited:
                    levelGraph[v].add(w)
                    nextLevel.add(w)
        print levelGraph
        currentLevel = nextLevel
        return nodes
def BreadthFirstKLevels(G,root,k):
    visited = set()
    currentLevel = [root]
    level = 0
    nodelist = []
    while (currentLevel and level<=k):
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
        nodelist = nodelist + levelGraph.keys()
        level = level + 1
        if level==k:
            break
        currentLevel = nextLevel
    return nodelist

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
#generate the tree graph
n = 100
G = nx.empty_graph(n)
G.add_edges_from(_tree_edges(n,4))
nodes = BreadthFirstKLevels(G,0,2)
