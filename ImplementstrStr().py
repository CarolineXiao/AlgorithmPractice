class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Write your code here
        len_t = len(needle)
        len_s = len(haystack)
        
        if len_t > len_s: 
            return -1
        
        if needle == "":
            return 0
        
        for i in range(0, len_s):
            if haystack[i] == needle[0]:
                j = 0
                while j < len_t:
                    if i+j >= len_s:
                        return -1
                    if haystack[i+j] != needle[j]:
                        break
                    j = j + 1
                if j == len_t:
                    return i
        
        return -1
