class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid == None or obstacleGrid == []:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # f[i][j] -> the number of unique paths to (i,j)
        f = [[0] * n for i in range(m)]
        
        for i in range(0,len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if i == 0 and j == 0:
                    f[i][j] = 1 - obstacleGrid[i][j]
                elif i == 0:
                    if obstacleGrid[i][j] == 1:
                        f[i][j] = 0
                    else:
                        f[i][j] = f[i][j-1]
                elif j == 0:
                    if obstacleGrid[i][j] == 1:
                        f[i][j] = 0
                    else:
                        f[i][j] = f[i-1][j]
                else:
                    if obstacleGrid[i][j] != 1:
                        f[i][j] = f[i][j-1] + f[i-1][j]
                         
        return f[m-1][n-1]
        
