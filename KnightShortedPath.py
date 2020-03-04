"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        
        if source == destination:
            return 0
        
        queue = []
        start = (source.x, source.y, 0)
        queue.append(start)
        visited = set()
        
        while queue:
            t = queue.pop(0)
            x = t[0]
            y = t[1]
            dis = t[2]
            
            for delta_x, delta_y in [(-1,-2), (1,-2), (-2,-1), (2,-1), (-2,1), (2,1), (-1,2), (1,2)]:
                next_x = x + delta_x
                next_y = y + delta_y
                
                
                if next_x == destination.x and next_y == destination.y:
                    return dis+1
                
                if self.isValid(grid, next_x, next_y, visited):
                    queue.append((next_x,next_y,dis+1))
                    visited.add((next_x,next_y))
                
        return -1
                
        
    def isValid(self, grid, x, y, visited):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        if (x,y) in visited:
            return False
        
        return not grid[x][y]
