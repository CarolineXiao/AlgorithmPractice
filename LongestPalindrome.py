class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        result = 0
        has_odd = False
        
        if s == "":
            return 0
        
        while len(s):
            char = s[0]
            occur = s.count(char)
            if occur % 2 == 0:
                result = result + occur
            else:
                result = result + occur - 1
                has_odd = True
            
            s = s.replace(char, '')
        
        if has_odd:
            result = result + 1
        return result
