class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        # method 1:
        # length = len(s)
        # for i in range(length//2):
        #     s = s[:i] + s[length-1-i] + s[i+1:length-1-i] + s[i] + s[length-i:]
        # return s
        
        # method 2:
        return s[::-1]
        
        # method 3:
        # reversed_str = ""
        # for i in range(len(s)-1, -1, -1):
        #     reversed_str += s[i]
        
        # return reversed_str
