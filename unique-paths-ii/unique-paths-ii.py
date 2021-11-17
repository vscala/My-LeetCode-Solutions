class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]: return 0
        for i, v in enumerate(obstacleGrid):
            if v[0]: break
            else: v[0] = -1
        obstacleGrid[0][0] = 0
        for j, v in enumerate(obstacleGrid[0]):
            if v: break
            else: obstacleGrid[0][j] = -1
        for i, r in enumerate(obstacleGrid[1:]):
            for j, v in enumerate(r[1:]):
                if v == 0:
                    obstacleGrid[i+1][j+1] += obstacleGrid[i][j+1] * (obstacleGrid[i][j+1] < 0) 
                    obstacleGrid[i+1][j+1] += obstacleGrid[i+1][j] * (obstacleGrid[i+1][j] < 0)
        return -obstacleGrid[-1][-1]