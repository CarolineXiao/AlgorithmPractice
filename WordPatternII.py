class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        mapping = {}
        used = set()
        return self.dfs(pattern, str, mapping, used)
        
    def dfs(self, pattern, str, mapping, used):
        if pattern == "":
            return not str
        
        char = pattern[0]
        
        if char in mapping:
            word = mapping[char]
            if not str.startswith(word):
                return False
            return self.dfs(pattern[1:], str[len(word):], mapping, used)
        
        for i in range(len(str)):
            word = str[:i+1]
            if word in used:
                continue
            mapping[char] = word
            used.add(word)
            if self.dfs(pattern[1:], str[len(word):], mapping, used):
                return True
            used.remove(word)
            del mapping[char]
            
        return False
        
