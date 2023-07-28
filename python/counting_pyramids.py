class Solution:
    """Accepted, and apparently one of only a handful of solutions submitted in Python"""

    def countPyramids(self, grid: List[List[int]]) -> int:
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = [grid[i][j], grid[i][j]]
                if grid[i][j][0] == 0:
                    continue
                grid[i][j] = [1, 1]
                if i >= 1:
                    if j >= 2:
                        h = min(grid[i][j - 1][0], grid[i][j - 2][0],
                                grid[i - 1][j - 1][0])
                        total += h
                        grid[i][j][0] += h
                    if j >= 1 and j + 1 < len(grid[0]):
                        h = min(grid[i - 1][j - 1][1], grid[i - 1][j][1],
                                grid[i - 1][j + 1][1])
                        total += h
                        grid[i][j][1] += h
        return total
