# BFS / DFS

Classic problem: [https://leetcode.com/problems/number-of-islands/](https://leetcode.com/problems/number-of-islands/)

```python
def num_islands(matrix):
    if not matrix or not matrx[0]
        return 0

    m, n = len(matrix), len(matrix[0])
    count = 0
    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def bfs(i, j):
        # improves performance 4x if you check bounds before each recursive call
        if i < m and i >= 0 and j < n and j >= 0 and matrix[i][j] == "1":
            matrix[i][j] = "0"
            for di, dj in neighbors:
                bfs(i + di, j + dj)

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                count += 1
                bfs(i, j)
    return count

```