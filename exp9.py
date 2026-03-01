def knapsack_dp(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using Dynamic Programming.
    
    Parameters:
        weights: List of item weights.
        values: List of item values.
        capacity: Maximum weight capacity of the knapsack.
        
    Returns:
        Maximum value that can be obtained and the items included.
    """
    n = len(weights)
    # Create a 2D DP table with dimensions (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include the item or exclude it, take the max value
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the items included in the optimal solution
    max_value = dp[n][capacity]
    w = capacity
    included_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i - 1)  # Include this item (index starts at 0)
            w -= weights[i - 1]

    included_items.reverse()  # Reverse to get the items in the original order
    return max_value, included_items


# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, included_items = knapsack_dp(weights, values, capacity)
print("Maximum Value:", max_value)
print("Items Included (Indices):", included_items)

