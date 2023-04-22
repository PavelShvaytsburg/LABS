from typing import List, Dict
from collections import defaultdict

# алгоритм Тарьяна для топологической сортировки
def topological_sort(graph: Dict[str, List[str]]) -> List[str]:    
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for child in graph[node]:
            in_degree[child] += 1

    queue = [node for node in in_degree if in_degree[node] == 0]

    sorted_nodes = []
    while queue:
        node = queue.pop(0)
        sorted_nodes.append(node)

        for child in graph[node]:
            in_degree[child] -= 1

            if in_degree[child] == 0:
                queue.append(child)

    if len(sorted_nodes) != len(graph):
        raise ValueError("The graph contains a cycle and cannot be sorted topologically.")

    return sorted_nodes

# алгоритм Флёри
def fleury_algorithm(graph, start_node):
    def dfs(graph, node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

    def is_bridge(graph, u, v):
        visited = set()
        dfs(graph, u, visited)
        if v in visited:
            return False
        return True

    def remove_edge(graph, u, v):
        graph[u].remove(v)
        graph[v].remove(u)

    def fleury_util(graph, node, path):
        for neighbor in graph[node]:
            if not is_bridge(graph, node, neighbor):
                temp = dict(graph)
                remove_edge(temp, node, neighbor)
                fleury_util(temp, neighbor, path)
        path.append(node)

    visited = set()
    dfs(graph, start_node, visited)
    if len(visited) != len(graph):
        raise ValueError("Graph is not connected")
    if sum(len(graph[node]) % 2 != 0 for node in graph) > 2:
        raise ValueError("Graph has no Eulerian path")
    path = []
    fleury_util(graph, start_node, path)
    return path[::-1]


#  алгоритм поиска эйлерова цикла на основе объединения циклов
def find_euler_path(graph):    
    path = []
    edges = defaultdict(list)
    for vertex in graph:
        for neighbor in graph[vertex]:
            edges[vertex].append(neighbor)
    start_vertex = None
    for vertex in graph:
        in_degree = len(edges[vertex])
        out_degree = len(graph[vertex])
        if in_degree - out_degree == 1:
            if start_vertex is not None:
                return None 
            start_vertex = vertex
        elif out_degree - in_degree == 1:
            if start_vertex is not None:
                return None
            start_vertex = vertex
    if start_vertex is None:
        start_vertex = next(iter(graph))
    
    def visit(vertex):
        while edges[vertex]:
            neighbor = edges[vertex].pop()
            visit(neighbor)
        path.append(vertex)
    visit(start_vertex)
    for vertex in graph:
        if edges[vertex]:
            return None 
    return path[::-1]


# алгоритм Косарайю
def kosaraju(graph: List[List[int]]) -> List[List[int]]:
    """
    Функция для поиска компонент сильной связности в ориентированном графе
    с помощью алгоритма Косарайю.

    Аргументы:
    - graph: список смежности графа

    Возвращает:
    - компоненты сильной связности в графе в виде списка списков вершин
    """

    # функция для обхода графа в глубину
    def dfs(node: int, visited: List[bool], stack: List[int]):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(node)

    def dfs_reverse(node: int, visited: List[bool], scc: List[int]):
        visited[node] = True
        scc.append(node)
        for neighbor in reverse_graph[node]:
            if not visited[neighbor]:
                dfs_reverse(neighbor, visited, scc)

    n = len(graph)

    reverse_graph = [[] for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            reverse_graph[j].append(i)

    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, stack)

    visited = [False] * n
    scc_list = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc = []
            dfs_reverse(node, visited, scc)
            scc_list.append(scc)

    return scc_list
