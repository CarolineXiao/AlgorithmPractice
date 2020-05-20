class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        s_arr = s.split()

        ans = ''
        for i in range(len(s_arr)-1, -1, -1):
            ans = ans + s_arr[i] + " "
        
        return ans[:-1]
