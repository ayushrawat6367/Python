from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n - 1]
    
#Example 1
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))

#Example 2
obstacleGrid = [[0,1],[0,0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))

