#include <stdio.h>
#include <limits.h>
#include <stdbool.h>

#define MAX 20 // Maximum number of cities

int n; // Number of cities
int cost[MAX][MAX]; // Cost matrix
int visited[MAX]; // Visited cities
int minCost = INT_MAX; // Minimum cost found
int path[MAX]; // Path taken

// Function to find the minimum cost path using Branch and Bound
void tsp(int currentPos, int count, int costSoFar) {
    // If all cities are visited and we return to the starting city
    if (count == n && cost[currentPos][0]) {
        if (costSoFar + cost[currentPos][0] < minCost) {
            minCost = costSoFar + cost[currentPos][0];
            path[count] = 0; // Return to starting city
        }
        return;
    }

    // Explore all possible paths
    int i;
    for (i = 0; i < n; i++) {
        // If the city is not visited and there is a path
        if (!visited[i] && cost[currentPos][i]) {
            // Mark the city as visited
            visited[i] = true;
            path[count] = i;

            // Recur to the next city
            tsp(i, count + 1, costSoFar + cost[currentPos][i]);

            // Backtrack
            visited[i] = false;
        }
    }
}

int main() {
    printf("Enter the number of cities: ");
    scanf("%d", &n);

    printf("Enter the cost matrix:\n");
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            scanf("%d", &cost[i][j]);
        }
    }

    // Initialize visited array
    for (i = 0; i < n; i++) {
        visited[i] = false;
    }

    // Start from the first city
    visited[0] = true;
    path[0] = 0;

    // Call the TSP function
    tsp(0, 1, 0);

    // Print the minimum cost and path
    printf("Minimum cost: %d\n", minCost);
    printf("Path: ");
    for (i = 0; i <= n; i++) {
        printf("%d ", path[i]);
    }
    printf("\n");

    return 0;
}

