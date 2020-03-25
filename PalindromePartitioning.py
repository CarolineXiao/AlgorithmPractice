class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        if s == "":
            return []
        
        result = []
        palindromes = []
        self.dfs(s, palindromes, result, 0)
        return result
        
    def dfs(self, s, palindromes, result, startIndex):
        if startIndex == len(s):
            result.append(list(palindromes))
            return
        
        for i in range(startIndex, len(s)):
            word = s[startIndex:i+1]
            if not self.isPalindrome(word):
                continue
            palindromes.append(word)
            self.dfs(s, palindromes, result, i+1)
            palindromes.pop()
            
            
    def isPalindrome(self, word):
        left = 0
        right = len(word) - 1 
        while left <= right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
