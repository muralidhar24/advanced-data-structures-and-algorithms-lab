def knapsack_backtracking(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using backtracking.
    
    Parameters:
        weights: List of item weights.
        values: List of item values.
        capacity: Maximum weight capacity of the knapsack.
        
    Returns:
        Maximum value that can be obtained and the items included.
    """
    n = len(weights)
    max_value = 0
    best_combination = []

    def backtrack(index, current_weight, current_value, included_items):
        nonlocal max_value, best_combination

        # Base case: reached the end of the items
        if index == n:
            if current_value > max_value:
                max_value = current_value
                best_combination = included_items[:]
            return

        # Exclude the current item
        backtrack(index + 1, current_weight, current_value, included_items)

        # Include the current item if it doesn't exceed capacity
        if current_weight + weights[index] <= capacity:
            included_items.append(index)  # Add the current item
            backtrack(index + 1, 
                      current_weight + weights[index], 
                      current_value + values[index], 
                      included_items)
            included_items.pop()  # Backtrack (remove the item)

    # Start the backtracking process
    backtrack(0, 0, 0, [])
    
    return max_value, best_combination


# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, included_items = knapsack_backtracking(weights, values, capacity)
print("Maximum Value:", max_value)
print("Items Included (Indices):", included_items)

