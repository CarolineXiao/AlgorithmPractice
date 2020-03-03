class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None:
            return 0
        
        island = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    self.bfs(grid, visited, i, j)
                    island += 1
                    
        return island
    
    def bfs(self, grid, visited, x, y):
        queue = []
        queue.append((x,y))
        visited.add((x,y))
        
        while queue:
            x, y = queue.pop(0)
            for delta_x, delta_y in [(-1,0), (1,0), (0,-1), (0,1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                
                if self.isValid(grid, visited, next_x, next_y):
                    queue.append((next_x,next_y))
                    visited.add((next_x,next_y))
                    
        
    def isValid(self, grid, visited, x, y):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        if (x,y) in visited:
            return False
        if grid[x][y] == "1":
            return True
        else:
            return False
        
