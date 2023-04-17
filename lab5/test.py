from main import Graph
graph = Graph(4)
graph.add_edge(0, 1, 2)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 2, 1)
graph.add_edge(1, 3, 5)
graph.add_edge(2, 3, 1)

print('DFS:')
graph.dfs(0)
print()

print('BFS:')
graph.bfs(0)
print()

print('Dijkstra:')
print(graph.dijkstra(0))

print('Kruskal:')
print(graph.kruskal())

print('Prim:')
print(graph.prim())

print('Floyd-Warshall:')
print(graph.floyd_warshall())