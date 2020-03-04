class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        if prerequisites == None:
            return True
        
        inDegree = {}
        neighbors = {}
        for i in range(numCourses):
            inDegree[i] = 0
            neighbors[i] = []
        
        for req in prerequisites:
            inDegree[req[0]] += 1
            neighbors[req[1]].append(req[0])
        
        start = []
        
        for course in inDegree:
            if inDegree[course] == 0:
                start.append(course)
                
        if len(start) == 0:
            return False
            
        # bfs
        queue = []
        order = []
        for c in start:
            queue.append(c)
        
        while queue:
            course = queue.pop(0)
            order.append(course)
            for n in neighbors[course]:
                inDegree[n] -= 1
                if inDegree[n] == 0:
                    queue.append(n)
                    
        return len(order) == numCourses
            

