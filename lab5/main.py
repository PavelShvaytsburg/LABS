# класс для представления графа в виде списков смежности
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = [[] for _ in range(num_vertices)]
        self.edges = []

    def add_edge(self, u, v, weight=None):
        self.adjacency_list[u].append((v, weight))
        self.edges.append((u, v, weight))

    def dfs(self, start_vertex):
        visited = [False] * self.num_vertices
        self._dfs_util(start_vertex, visited)

    def _dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')

        for neighbor, _ in self.adjacency_list[vertex]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited)

    def bfs(self, start_vertex):
        visited = [False] * self.num_vertices
        queue = [start_vertex]

        visited[start_vertex] = True

        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex, end=' ')

            for neighbor, _ in self.adjacency_list[current_vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    def dijkstra(self, start_vertex):
        # инициализация расстояний вершин до начальной вершины бесконечностью
        distances = [float('inf')] * self.num_vertices
        # начальная вершина имеет расстояние 0 до самой себя
        distances[start_vertex] = 0

        # создание списка посещенных вершин
        visited = set()

        # цикл по всем вершинам графа
        for _ in range(self.num_vertices):
            # поиск вершины с минимальным расстоянием среди не посещенных вершин
            min_distance = float('inf')
            for vertex in range(self.num_vertices):
                if vertex not in visited and distances[vertex] < min_distance:
                    min_distance = distances[vertex]
                    current_vertex = vertex

            # добавление найденной вершины в список посещенных
            visited.add(current_vertex)

            # обновление расстояний до соседних вершин
            for neighbor, weight in self.adjacency_list[current_vertex]:
                distance = distances[current_vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances

    def kruskal(self):
        # создание списка ребер и сортировка их по весу
        edges = sorted(self.edges, key=lambda x: x[2])
        # создание списка подмножеств, каждое изначально содержит только одну вершину
        subsets = [{i} for i in range(self.num_vertices)]

        # инициализация списка ребер остовного дерева
        mst = []

        for edge in edges:
            # поиск подмножеств, к которым принадлежат вершины ребра
            u_subset = None
            v_subset = None
            for subset in subsets:
                if edge[0] in subset:
                    u_subset = subset
                if edge[1] in subset:
                    v_subset = subset

        # проверка наличия цикла
        if u_subset != v_subset:
            # объединение подмножеств
            subsets.remove(u_subset)
            subsets.remove(v_subset)
            subsets.append(u_subset.union(v_subset))

            # добавление ребра в список ребер остовного дерева
            mst.append(edge)

        return mst

    def prim(self):
        # выбор начальной вершины
        start_vertex = 0

        # создание списка вершин, включенных в остовное дерево
        mst_vertices = set([start_vertex])

        # создание списка ребер, исходящих из вершин, включенных в остовное дерево
        mst_edges = []

        # цикл по всем вершинам графа
        while len(mst_vertices) != self.num_vertices:
            # поиск минимального ребра, соединяющего вершины остовного дерева с не входящей в него вершиной
            min_edge = None
            min_weight = float('inf')
            for vertex in mst_vertices:
                for neighbor, weight in self.adjacency_list[vertex]:
                    if neighbor not in mst_vertices and weight < min_weight:
                        min_edge = (vertex, neighbor)
                        min_weight = weight

            # добавление найденного ребра в список ребер остовного дерева и в список вершин, включенных в него
            mst_edges.append((min_edge[0], min_edge[1], min_weight))
            mst_vertices.add(min_edge[1])

        return mst_edges

    def floyd_warshall(self):
        # инициализация матрицы расстояний
        distances = [[float('inf') for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
        for u in range(self.num_vertices):
            distances[u][u] = 0
        for u, v, weight in self.edges:
            distances[u][v] = weight

        # поиск кратчайшего пути между всеми парами вершин через промежуточные вершины
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        return distances