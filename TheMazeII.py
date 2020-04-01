class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        if maze == None or maze == []:
            return False
        
        queue = []
        visited = set()
        queue.append((start[0],start[1],0))
        visited.add((start[0],start[1]))
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        import sys
        result = sys.maxsize
        
        while queue:
            x, y, cur_dist = queue.pop(0)
            print((x,y,cur_dist))
            for delta_x, delta_y in dir:
                next_x, next_y, dist = self.getNext(maze, x, y, delta_x, delta_y)
                if next_x == destination[0] and next_y == destination[1]:
                    d = cur_dist + dist
                    if d < result:
                        result = d
                if self.isValid(maze, next_x, next_y, visited):
                    queue.append((next_x,next_y,cur_dist+dist))
                    visited.add((next_x,next_y))
                    
        if result == sys.maxsize:
            return -1
        return result
        
    def isValid(self, maze, x, y, visited):
        if 0 <= x < len(maze) and 0 <= y <len(maze[0]) and (x,y) not in visited:
            return True
        return False
    
    
    def getNext(self, maze, x, y, delta_x, delta_y):
        dist = 0
        if delta_x == 0:
            while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                y += delta_y
                dist += 1
            y -= delta_y
            dist -= 1
        else:
            while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                x += delta_x
                dist += 1
            x -= delta_x
            dist -= 1
        return x, y, dist
            
