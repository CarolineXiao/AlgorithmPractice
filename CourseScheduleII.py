class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        indegree_map = {}
        prerequisite_map = {}
        for i in range(numCourses):
            indegree_map[i] = 0
            prerequisite_map[i] = []
        
        for pre in prerequisites:
            indegree_map[pre[0]] += 1
            prerequisite_map[pre[1]].append(pre[0])
            
        start = []
        
        for i in range(len(indegree_map)):
            if indegree_map[i] == 0:
                start.append(i)
        
        if len(start) == 0:
            return []
        
        result = []
        queue = []
        for c in start:
            queue.append(c)
        while queue:
            cur_course = queue.pop(0)
            result.append(cur_course)
            for course in prerequisite_map[cur_course]:
                indegree_map[course] -= 1
                if indegree_map[course] == 0:
                    queue.append(course)
                    
        if len(result) < numCourses:
            return []
        
        return result
            
