class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        if p == '.*':
            return True
        m = len(s)
        n = len(p)
        memo = [[False] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        return self.helper(s, p, 0, 0, memo, visited)
        
    def helper(self, s, p, sIndex, pIndex, memo, visited):
        if pIndex == len(p):
            return sIndex == len(s)
        
        if sIndex == len(s):
            return self.isRemainingValid(p, pIndex)
        
        if visited[sIndex][pIndex]:
            return memo[sIndex][pIndex]
            
        if pIndex+1 < len(p) and p[pIndex] != '*' and p[pIndex+1] == '*':
            if s[sIndex] == p[pIndex] or p[pIndex] == '.':
                memo[sIndex][pIndex] = self.helper(s, p, sIndex, pIndex+2, memo, visited) or self.helper(s, p, sIndex+1, pIndex, memo, visited)
            else:
                memo[sIndex][pIndex] = self.helper(s, p, sIndex, pIndex+2, memo, visited)
        else:
            if s[sIndex] != p[pIndex] and p[pIndex] != '.':
                return False
            memo[sIndex][pIndex] = self.helper(s, p, sIndex+1, pIndex+1, memo, visited)
            
        
        visited[sIndex][pIndex] = True
        return memo[sIndex][pIndex]
            
            
            
    def isRemainingValid(self, p, pIndex):
        for i in range(pIndex, len(p)-1):
            if p[i] != '*' and p[i+1] == '*':
                continue
            else:
                return False
        return True
