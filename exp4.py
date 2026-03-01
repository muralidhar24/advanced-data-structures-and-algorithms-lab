from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]  # Adjacency matrix
        self.adj_list = defaultdict(list)  # Adjacency list 

    # Add an edge for adjacency matrix and adjacency list
    def add_edge(self, u, v):
        # For adjacency matrix
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # For undirected graph

        # For adjacency list
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # For undirected graph

    # Breadth-First Traversal using adjacency matrix
    def bft_matrix(self, start):
        visited = [False] * self.V
        queue = deque([start])
        visited[start] = True
 
        print("BFT using Adjacency Matrix:")
        while queue:
            node = queue.popleft()
            print(node, end=" ")

            # Traverse all vertices connected to the current node
            for i in range(self.V):
                if self.adj_matrix[node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print()

    # Breadth-First Traversal using adjacency list
    def bft_list(self, start):
        visited = [False] * self.V
        queue = deque([start])
        visited[start] = True

        print("BFT using Adjacency List:")
        while queue:
            node = queue.popleft()
            print(node, end=" ")

            # Traverse all neighbors of the current node
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

    # Depth-First Traversal using adjacency matrix
    def dft_matrix(self, start):
        visited = [False] * self.V
        print("DFT using Adjacency Matrix:")
        self._dft_matrix_util(start, visited)
        print()

    def _dft_matrix_util(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        # Traverse all vertices connected to the current node
        for i in range(self.V):
            if self.adj_matrix[node][i] == 1 and not visited[i]:
                self._dft_matrix_util(i, visited)

    # Depth-First Traversal using adjacency list
    def dft_list(self, start):
        visited = [False] * self.V
        print("DFT using Adjacency List:")
        self._dft_list_util(start, visited)
        print()

    def _dft_list_util(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        # Traverse all neighbors of the current node
        for neighbor in self.adj_list[node]:
            if not visited[neighbor]:
                self._dft_list_util(neighbor, visited)


# Example Usage
if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    # Perform Breadth-First Traversal
    g.bft_matrix(0)  # Using adjacency matrix
    g.bft_list(0)    # Using adjacency list

    # Perform Depth-First Traversal
    g.dft_matrix(0)  # Using adjacency matrix
    g.dft_list(0)    # Using adjacency list