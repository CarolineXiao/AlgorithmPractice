class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        myStr = sorted(str)
        results = []
        permuation = ""
        visited = [0] * len(myStr)
        self.dfs(myStr, permuation, results, visited)
        return results
    
    def dfs(self, myStr, permuation, results, visited):
        if len(permuation) == len(myStr):
            results.append(permuation)
        
        for i in range(len(myStr)):
            if visited[i]:
                continue
            if i > 0 and myStr[i] == myStr[i-1] and not visited[i-1]:
                continue
            
            permuation = permuation + myStr[i]
            visited[i] = 1
            self.dfs(myStr, permuation, results, visited)
            visited[i] = 0
            permuation = permuation[:-1]
