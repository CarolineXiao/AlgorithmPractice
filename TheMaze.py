class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        if maze == None or maze == []:
            return False
        
        queue = []
        visited = set()
        queue.append((start[0],start[1]))
        visited.add((start[0],start[1]))
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while queue:
            x, y = queue.pop(0)
            for delta_x, delta_y in dir:
                next_x, next_y = self.getNext(maze, x, y, delta_x, delta_y)
                if next_x == destination[0] and next_y == destination[1]:
                    return True
                if self.isValid(maze, next_x, next_y, visited):
                    queue.append((next_x,next_y))
                    visited.add((next_x,next_y))
        return False
        
    def isValid(self, maze, x, y, visited):
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and (x, y) not in visited:
            return True
        return False
    
    def getNext(self, maze, x, y, delta_x, delta_y):
        if delta_x == 0:
            while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                y += delta_y
            y -= delta_y
        else:
            while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                x += delta_x
            x -= delta_x
        
        return x, y
                  
