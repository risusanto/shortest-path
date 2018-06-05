#dijkstra algorithm
def dijkstra(graph,src):
    length = len(graph)
    nodes = [i for i in range(length)]

    visited = [src]
    path = {src:{src:[]}}
    nodes.remove(src)
    distance_graph = {src:0}
    pre = next = src

    while nodes:
        distance = float('inf')
        for v in visited:
             for d in nodes:
                new_dist = graph[src][v] + graph[v][d]
                if new_dist <= distance:
                    distance = new_dist
                    next = d
                    pre = v
                    graph[src][d] = new_dist


        path[src][next] = [i for i in path[src][pre]]
        path[src][next].append(next)

        distance_graph[next] = distance

        visited.append(next)
        nodes.remove(next)

    return distance_graph, path