"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
"""

class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        def helper(loc, memo):
            """
            19.30 %ile runtime
            53.93 %ile memory

            See optimal solution below for a better way: memoizing the number of paths *to* (i, j) rather than *from* (i, j).
            """
            x, y = loc
            if obstacleGrid[x][y] == 1:
                return 0
            if loc not in memo:
                memo[loc] = 0
                for dx, dy in (1, 0), (0, 1):
                    u, v = x + dx, y + dy
                    try:
                        memo[loc] += helper((u, v), memo)
                    except IndexError:
                        continue
            return memo[loc]

        dest = (len(obstacleGrid)-1, len(obstacleGrid[0])-1)
        memo = {dest: 1}
        return helper((0, 0), memo)

    def uniquePathsWithObstaclesDP(self, obstacleGrid):
        """Optimal solution using DP"""
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] != 0)
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] != 0)
        for i in range(1, m):
            for j in range (1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
        return obstacleGrid[m-1][n-1]

    def uniquePathsWithObstaclesStackDFS(self, obstacleGrid: List[List[int]]) -> int:
        """TLE"""
        stack = [(0, 0, 0, 0)]
        path = [(0, 0)]
        dest = (len(obstacleGrid)-1, len(obstacleGrid[0])-1)
        total = 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[dest[0]][dest[1]] == 1:
            return 0
        while len(stack) > 0:
            x, y, px, py = stack.pop()
            while path[-1] != (px, py):
                u, v = path.pop()
                obstacleGrid[u][v] = 0
            path.append((x, y))
            obstacleGrid[x][y] = 1
            if (x, y) == dest:
                total += 1
            else:
                for dx, dy in (1, 0), (0, 1):
                    u, v = x + dx, y + dy
                    if u < 0 or v < 0 or u > dest[0] or v > dest[1] or obstacleGrid[u][v] == 1:
                        continue
                    stack.append((u, v, x, y))
        return total

