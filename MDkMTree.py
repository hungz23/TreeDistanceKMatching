def distancekmatching(G, k):
    sigma = LexBFS(G)
    visited = [False]*n
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
                Nkv = BreadthFirstKLevels(G,v,k-1)
                Nku = BreadthFirstKLevels(G,u,k-1)
                for node in Nkv:
                    visited[node] = True
                for node in Nku:
                    visited[node] = True
                visited[u] = True
                visited[v] = True
                G.remove_nodes_from(Nkv)
                G.remove_nodes_from(Nku)
    return M
