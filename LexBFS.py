import networkx as nx
from Sequence import Sequence
from Util import arbitrary_item
from partition_refinement import PartitionRefinement
def LexBFS(G):
    """Find lexicographic breadth-first-search traversal order of a graph.
    G should be represented in such a way that "for v in G" loops through
    the vertices, and "G[v]" produces a sequence of the neighbors of v; for
    instance, G may be a dictionary mapping each vertex to its neighbor set.
    Running time is O(n+m) and additional space usage over G is O(n).
    """
    P = PartitionRefinement(G)
    S = Sequence(P, key=id)
    sigma = []
    while S:
        set = S[0]
        v = arbitrary_item(set)

        sigma.append(v)

        P.remove(v)
        if not set:
            S.remove(set)
        for new,old in P.refine(G.neighbors(v)):
            S.insertBefore(old,new)
    return sigma
