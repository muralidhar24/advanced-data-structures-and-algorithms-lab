import sys

class TravellingSalesmanProblem:
    def __init__(self, graph):
        """
        Initialize the TSP problem with a given graph.
        
        Parameters:
            graph: A 2D list representing the adjacency matrix of the graph.
        """
        self.graph = graph
        self.n = len(graph)
        self.min_cost = sys.maxsize
        self.best_path = []

    def tsp_branch_and_bound(self):
        """
        Solves the TSP using the Branch and Bound approach.
        
        Returns:
            The minimum cost and the path of the optimal solution.
        """
        # Initialize variables
        visited = [False] * self.n
        visited[0] = True  # Start from the first city
        self._branch_and_bound(0, visited, 1, 0, [0])
        return self.min_cost, self.best_path

    def _branch_and_bound(self, current_city, visited, count, current_cost, current_path):
        """
        Recursive helper function for the Branch and Bound approach.
        
        Parameters:
            current_city: The city currently being visited.
            visited: A list of booleans indicating whether each city has been visited.
            count: Number of cities visited so far.
            current_cost: Cost of the current path.
            current_path: The current path being explored.
        """
        # Base case: If all cities are visited, return to the starting city
        if count == self.n and self.graph[current_city][0] != 0:
            total_cost = current_cost + self.graph[current_city][0]
            if total_cost < self.min_cost:
                self.min_cost = total_cost
                self.best_path = current_path + [0]
            return

        # Explore all possible cities from the current city
        for next_city in range(self.n):
            if not visited[next_city] and self.graph[current_city][next_city] != 0:
                # Calculate the cost of visiting the next city
                new_cost = current_cost + self.graph[current_city][next_city]

                # Prune the branch if the cost exceeds the current minimum
                if new_cost < self.min_cost:
                    visited[next_city] = True
                    self._branch_and_bound(next_city, visited, count + 1, new_cost, current_path + [next_city])
                    visited[next_city] = False  # Backtrack

# Example usage
if __name__ == "__main__":
    # Example adjacency matrix (distance between cities)
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    tsp = TravellingSalesmanProblem(graph)
    min_cost, best_path = tsp.tsp_branch_and_bound()
    print("Minimum Cost:", min_cost)
    print("Optimal Path:", best_path)

