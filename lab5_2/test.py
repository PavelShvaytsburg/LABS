from main import *

graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": []
}
sorted_nodes = topological_sort(graph)
print("алгоритм Тарьяна для топологической сортировки\n",sorted_nodes,"\n")  # Output: ['a', 'c', 'b', 'd', 'e']


graph = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: [3]}
start_node = 0
print("алгоритм Флёри")
print(fleury_algorithm(graph, start_node),"\n") # [0, 1, 2, 3, 4]


graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
print("алгоритм поиска эйлерова цикла на основе объединения циклов\n",find_euler_path(graph),"\n") # [0, 1, 2, 3, 3]

graph = [
    [1],     # 0 -> 1
    [2],     # 1 -> 2
    [0,3],   # 2 -> 0,3
    [4],     # 3 -> 4
    [5],     # 4 -> 5
    [3,6],   # 5 -> 3,6
    [7],     # 6 -> 7
    [5,8],   # 7 -> 5,8
    [6],     # 8 -> 6
]
scc_list = kosaraju(graph)
print("алгоритм Косарайю\n",scc_list)  # должно вывести [[0, 2], [1], [3, 5, 6], [4], [7], [8]]




