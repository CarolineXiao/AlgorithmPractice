import sys
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # 1. bfs
        '''
        if grid == None or grid == []:
            return -1
            
        n = len(grid)
        m = len(grid[0])
        
        path = 0
        queue = []
        next_dir = [(1,2),(-1,2),(2,1),(-2,1)]
        queue.append((0,0,0))
        
        while queue:
            point = queue.pop(0)
            x = point[0]
            y = point[1]
            cur_length = point[2]
            if x == n -1 and y == m -1:
                return cur_length
            for delta_x, delta_y in next_dir:
                new_x = x + delta_x
                new_y = y + delta_y
                
                if self.isValid(grid, new_x, new_y):
                    queue.append((new_x,new_y,cur_length+1))
        
        return -1
    
    
        '''
        
        # 2. dp
        if grid == None or grid == []:
            return -1
            
        n = len(grid)
        m = len(grid[0])
        
        f = [[sys.maxsize] * m for _ in range(n)]
        
        f[0][0] = 1
        for j in range(m):
            for i in range(n):
                if i == 0 and j == 0:
                    continue
                if grid[i][j] == 1:
                    f[i][j] = 0
                    continue
                cur_min = sys.maxsize
                if self.isValid(grid, i-2, j-1) and f[i-2][j-1] > 0:
                    if f[i-2][j-1] < cur_min:
                        cur_min = f[i-2][j-1]
                if self.isValid(grid, i-1, j-2) and f[i-1][j-2] > 0:
                    if f[i-1][j-2] < cur_min:
                        cur_min = f[i-1][j-2]
                if self.isValid(grid, i+1, j-2) and f[i+1][j-2] > 0:
                    if f[i+1][j-2] < cur_min:
                        cur_min = f[i+1][j-2]
                if self.isValid(grid, i+2, j-1) and f[i+2][j-1] > 0:
                    if f[i+2][j-1] < cur_min:
                        cur_min = f[i+2][j-1]
                if cur_min == sys.maxsize:
                    f[i][j] = 0
                else:
                    f[i][j] = cur_min + 1
        
        return f[n-1][m-1]-1
                
        
        
    def isValid(self, grid, x, y):
        n = len(grid)
        m = len(grid[0])
        if 0 <= x < n and 0 <= y < m and grid[x][y] == 0:
            return True
        return False    
        
