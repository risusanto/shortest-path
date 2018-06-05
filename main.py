#main code: dijkstra algorithm
from dijkstra import dijkstra

graph_list = [   
    [0, 50, 10, 40, 45, float('inf')],
    [float('inf'), 0, 15, float('inf'), 10, float('inf')],
    [20, float('inf'), 0, 15, float('inf'), float('inf')],
    [float('inf'), 20, float('inf'), 0, 35, float('inf')],
    [float('inf'), float('inf'), float('inf'), 30, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 3, float('inf'), 0]
    ]


src = 0
distance, path = dijkstra(graph_list, src)
for key, value in distance.items():
    print((src + 1), " ke ", (key + 1),"adalah ",
    [x + 1 for x in ([src]+path[src][key])], " dengan panjang ", value)