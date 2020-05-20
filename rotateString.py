class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        if len(s) == 0:
            return s
        if offset > len(s):
            offset = offset % len(s)
        if offset == 0:
            return s
        
        temp = s[-offset:] + s[:-offset]
        for i in range(len(s)):
            s[i] = temp[i]
    
