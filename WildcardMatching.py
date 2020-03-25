class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        memo = [[False] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        return self.helper(s, p, 0, 0, visited, memo)
        
    def helper(self, s, p, sIndex, pIndex, visited, memo):
        if pIndex == len(p):
            return sIndex == len(s)
        
        if sIndex == len(s):
            return p[pIndex:].count('*') + len(p[:pIndex]) == len(p)
            
        if visited[sIndex][pIndex]:
            return memo[sIndex][pIndex]
            
        
        if p[pIndex] != '*':
            if s[sIndex] != p[pIndex] and p[pIndex] != '?':
                return False
            visited[sIndex][pIndex] = True
            memo[sIndex][pIndex] = self.helper(s, p, sIndex+1, pIndex+1, visited, memo)
        else:
            visited[sIndex][pIndex] = True
            memo[sIndex][pIndex] = self.helper(s, p, sIndex, pIndex+1, visited, memo) or self.helper(s, p, sIndex+1, pIndex, visited, memo)
        return memo[sIndex][pIndex]

        
