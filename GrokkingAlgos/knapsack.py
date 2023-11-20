# Using recursion
def knapsack(capacity, weights, values, number_items):
    if number_items == 0 or capacity == 0:
        return 0
    
    if (weights[number_items-1] > capacity): # last item too heavy
        return knapsack(capacity, weights, values, number_items-1)
    else: # last item add or not
        return max( 
            values[number_items-1] + knapsack(capacity-weights[number_items-1], weights, values, number_items-1),
            knapsack(capacity, weights, values, number_items-1)       
        )

# Using DP
def knapsack(capacity, weights, values, number_items):
    Cell = [[0 for x in range(capacity + 1)] for x in range(number_items + 1)]

    for i in range(number_items + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                Cell[i][j] = 0
            elif weights[i - 1] <= j: # item can be added
                Cell[i][j] = max(values[i-1] + Cell[i-1][j-weights[i-1]], Cell[i-1][j])
            else:
                Cell[i][j] = Cell[i-1][j]
    
    print(Cell)
    return Cell[number_items][capacity]

if __name__ == '__main__':
    N = 5
    W = 6
    values = [10, 3, 9, 5, 6]
    weights = [3, 1, 2, 2, 1]
    print(knapsack(W, weights, values, N))
    