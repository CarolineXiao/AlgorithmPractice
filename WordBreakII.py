class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        if len(s) == 0 or wordDict == []:
            return []
        # 1. DFS - Time Limit Exceed
        '''
        result = []
        word = ""
        max_length = self.getMaxLength(wordDict)
        memo = []
        visited = []
        for i in range(len(s)):
            memo_end = []
            visited_end = []
            for j in range(len(s)):
                memo_end.append([])
                visited_end.append(False)
        
        self.dfs(s, wordDict, 0, word, result, max_length, memo, visited)
        return result
        
        
    def dfs(self, s, wordDict, startIndex, word, result, max_length, memo, visited):   
        if startIndex == len(s):
            word = word[:-1]
            result.append(word)
            return
        
        
        for i in range(startIndex, len(s)):
            if i > startIndex + max_length:
                break
            nextWord = s[startIndex:i+1]
            if nextWord in wordDict:
                pre = word
                word += nextWord + " "
                self.dfs(s, wordDict, i+1, word, result, max_length, memo, visited)
                word = pre
                '''
        # Memoization + dfs        
        memo = {}

        return self.helper(s, wordDict, memo)
        
    def helper(self, s, wordDict, memo):
        partition = []
        
        if s in memo:
            return memo[s]
        
        if s in wordDict:
            partition.append(s)
        
        for i in range(1, len(s)):
            word = s[:i]
            if word not in wordDict:
                continue
            
            sub_partition = self.helper(s[i:], wordDict, memo)
            for p in sub_partition:
                partition.append(word + " " + p)
        
        memo[s] = partition
        return memo[s]

  
                
    def getMaxLength(self, wordDict):
        max_length = 0
        for word in wordDict:
            if len(word) > max_length:
                max_length = len(word)
        return max_length
                
