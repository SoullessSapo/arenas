from collections import deque
from random import randint
class Graph:
    def __init__(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix

    def bfs(self, start_vertex):
        visited = [False] * len(self.adjacency_matrix)
        queue = deque([start_vertex])
        visited[start_vertex] = True

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[vertex][neighbor] and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs(self, start_vertex):
        visited = [False] * len(self.adjacency_matrix)
        self._dfs_helper(start_vertex, visited)

    def _dfs_helper(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in range(len(self.adjacency_matrix)):
            if self.adjacency_matrix[vertex][neighbor] and not visited[neighbor]:
                self._dfs_helper(neighbor, visited)
adjacency_matrix = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
]

# Creamos un grafo con la matriz de adyacencias
graph = Graph(adjacency_matrix)

v = randint(0,5)
print("Recorrido BFS:")
start_vertex = v
graph.bfs(start_vertex)


print("\n\nRecorrido DFS:")
start_vertex = v
graph.dfs(start_vertex)

