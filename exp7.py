import heapq
import time

def dijkstra_matrix(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    visited = [False] * n
    dist[source] = 0

    for _ in range(n):
        # Find the vertex with the smallest distance
        min_dist = float('inf')
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        
        visited[u] = True

        # Update distances to neighbors
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                dist[v] = min(dist[v], dist[u] + graph[u][v])
    
    return dist

def dijkstra_list(graph, source):
    n = len(graph)
    dist = [float('inf')] * n
    dist[source] = 0
    pq = [(0, source)]  # Priority queue: (distance, vertex)

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    
    return dist

# Example usage
if __name__ == "__main__":
    # Dense graph (adjacency matrix)
    graph_matrix = [
        [0, 10, 0, 0, 0],
        [10, 0, 5, 15, 0],
        [0, 5, 0, 10, 20],
        [0, 15, 10, 0, 25],
        [0, 0, 20, 25, 0]
    ]

    # Sparse graph (adjacency list)
    graph_list = {
        0: [(1, 10)],
        1: [(0, 10), (2, 5), (3, 15)],
        2: [(1, 5), (3, 10), (4, 20)],
        3: [(1, 15), (2, 10), (4, 25)],
        4: [(2, 20), (3, 25)]
    }

    source = 0

    # Measure time for adjacency matrix
    start = time.time()
    print("Adjacency Matrix:", dijkstra_matrix(graph_matrix, source))
    print("Matrix Time:", time.time() - start)

    # Measure time for adjacency list
    start = time.time()
    print("Adjacency List:", dijkstra_list(graph_list, source))
    print("List Time:", time.time() - start)

