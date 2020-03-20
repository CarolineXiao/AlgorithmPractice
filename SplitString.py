class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        if s == "":
            return [[]]
        
        results = []
        strings = []
        
        self.dfs(s, strings, results, 0)
        
        return results
    
    def dfs(self, s, strings, results, index):
        if self.getWholeString(strings) == s:
            results.append(list(strings))
            return
        
        strings.append(s[index])
        self.dfs(s, strings, results, index+1)
        strings.pop()
            
        if index + 1 < len(s):
            strings.append(s[index] + s[index+1])
            self.dfs(s, strings, results, index+2)
            strings.pop()
                
    
    def getWholeString(self, slist):
        string = ""
        for s in slist:
            string += s
        return string
            
