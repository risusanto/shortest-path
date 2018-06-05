#prim algorithm
def prim(graph, root):
    assert type(graph)==dict

    nodes = list(graph)
    nodes.remove(root)
    
    visited = [root]
    path = []
    next = None

    while nodes:
        distance = float('inf') 
        for s in visited:
            for d in graph[s]:
                if d in visited or s == d:
                    continue
                if graph[s][d] < distance:
                    distance = graph[s][d]
                    pre = s
                    next = d
        path.append((pre, next))
        visited.append(next)
        try:
            nodes.remove(next)
        except Exception as e:
            return path

    return path


graph_dict = {  "s1":{"s1": 0, "s2": 50, "s3": 10, "s4": 40, "s5":45,"s6":float("inf")},
    "s2":{"s1": float("inf"), "s2": 0, "s3": 15, "s4": float("inf"), "s5":10,"s6":float("inf")},
    "s3":{"s1": 20, "s2": float("inf"), "s3": 0, "s4":15, "s5":35,"s6":float("inf")},
    "s4":{"s1": float("inf"), "s2": 20, "s3": float("inf"), "s4":0,"s5":35,"s6":float("inf")},
    "s5":{"s1": float("inf"), "s2": float("inf"), "s3": float("inf"), "s4":30,"s5":0,"s6":float("inf")},
    "s6":{"s1": float("inf"), "s2": float("inf"), "s3": float("inf"), "s4":3,"s5":float("inf"),"s6":0}
}

path = prim(graph_dict, 's6')
print ("Jalur terpendek dari s6 ke s1 adalah melalui: ",path)