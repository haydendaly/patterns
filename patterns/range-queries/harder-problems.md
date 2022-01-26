# Challenge Problems

## Minimum Sub-matrix Sum

Given an `m * n` matrix of integers, find the minimum sum sub-matrix of size `k * l`.

### Starter Code

```python
def find_min_sum_submatrix(grid, k, l):
    """Takes integer matrix, returns position and sum of the sub-matrix of size k * l with minimum sum"""
    pass
```

### Solution

```python
def find_min_sum_submatrix(grid, k, l):
    if not grid or not grid[0]:
        return -1, -1, 0
    # Create variables for size of grid
    m, n = len(grid), len(grid[0])

    # Transform to prefix grid
    for i in range(1, m):
        grid[i][0] = grid[i - 1][0] + grid[i][0]
    for j in range(1, n):
        grid[0][j] = grid[0][j - 1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1] + grid[i][j]
    
    # Define variables for minimums
    min_i, min_j, min_sum = 0, 0, grid[m - 1][n - 1]
    
    # Helper function to get range sum
    def range_sum(i, j):
        if i > m - k or j > n - l:
            return float("inf")
        sum_val = grid[i + k - 1][j + l - 1]
        sum_val -= grid[i - 1][j + l - 1] if i > 0 else 0
        sum_val -= grid[i + k - 1][j - 1] if j > 0 else 0
        sum_val += grid[i - 1][j - 1] if i > 0 and j > 0 else 0
        return sum_val

    # Iterate over grid to find min sum
    for i in range(m):
        for j in range(n):    
            temp_sum = range_sum(i, j)
            if temp_sum < min_sum:
                min_i, min_j, min_sum = i, j, temp_sum

    return (min_i, min_j, min_sum)
```



