from collections import defaultdict

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(list)  # Adjacency list representation
        self.time = 0  # Timer used in DFS

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # DFS utility to find biconnected components
    def biconnected_components_util(self, u, parent, visited, disc, low, stack, result):
        # Mark the current node as visited
        visited[u] = True
        disc[u] = low[u] = self.time
        self.time += 1
        child_count = 0

        # Iterate over all neighbors of u
        for v in self.graph[u]:
            # If v is not visited, process it
            if not visited[v]:
                child_count += 1
                stack.append((u, v))  # Push the edge to the stack
                self.biconnected_components_util(v, u, visited, disc, low, stack, result)

                # Update low value of u
                low[u] = min(low[u], low[v])

                # Check if u is an articulation point
                if (parent is None and child_count > 1) or (parent is not None and low[v] >= disc[u]):
                    # Pop all edges from the stack until (u, v) is found
                    biconnected_component = []
                    while stack[-1] != (u, v):
                        biconnected_component.append(stack.pop())
                    biconnected_component.append(stack.pop())
                    result.append(biconnected_component)

            elif v != parent:  # Update low value for a back edge
                low[u] = min(low[u], disc[v])
                if disc[v] < disc[u]:
                    stack.append((u, v))  # Push the edge to the stack

    # Function to find all biconnected components
    def find_biconnected_components(self):
        visited = [False] * self.V
        disc = [-1] * self.V
        low = [-1] * self.V
        stack = []
        result = []

        # Call the utility function for all unvisited vertices
        for i in range(self.V):
            if not visited[i]:
                self.biconnected_components_util(i, None, visited, disc, low, stack, result)

        # Pop any remaining edges in the stack as a component
        if stack:
            biconnected_component = []
            while stack:
                biconnected_component.append(stack.pop())
            result.append(biconnected_component)

        return result


# Example Usage
if __name__ == "__main__":
    # Create a graph
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(5, 6)

    # Find and print biconnected components
    bcc = g.find_biconnected_components()
    print("Biconnected Components:")
    for component in bcc:
        print(component)
