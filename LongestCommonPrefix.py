class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]
            
        index = 0
        while 1:
            if self.ifithequal(strs, index):
                index += 1
                continue
            break
        
        return strs[0][:index]
                
    def ifithequal(self, strs, i):
        if i >= len(strs[0]):
            return False
        char = strs[0][i]
        for str in strs:
            if i >= len(str):
                return False
            if str[i] != char:
                return False
        return True
                
