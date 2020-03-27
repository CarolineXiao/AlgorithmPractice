class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        if grid == []:
            return 0
        f = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    f[i][j] = grid[i][j]
                elif i == 0:
                    f[i][j] = f[i][j-1] + grid[i][j]
                elif j == 0:
                    f[i][j] = f[i-1][j] + grid[i][j]
                else:
                    f[i][j] = min(f[i][j-1], f[i-1][j]) + grid[i][j]
                    
        return f[len(grid)-1][len(grid[0])-1]
