class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        arr = []
        for _ in range(m):
            row = []
            for _ in range(n):
                row.append(0)
            arr.append(row)
        arr[0][0] = grid[0][0]
        for i in range(1, m):
            arr[i][0] = arr[i - 1][0] + grid[i][0]
        for j in range(1, n):
            arr[0][j] = arr[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = grid[i][j] + min(arr[i - 1][j], arr[i][j - 1])

        return arr[-1][-1]
