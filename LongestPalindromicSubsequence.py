class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        if s == "":
            return 0
        if len(s) == 1:
            return 1
            
        # dp[i][j] -> the longest palidromic subsequence from s[i:j+1]    
        dp = [[0] * len(s) for _ in range(len(s))]
        
        for i in range(1, len(s)):
            dp[i][i] = 1
            for j in range(i-1, -1, -1):
                if s[j] == s[i]:
                    dp[j][i] = dp[j+1][i-1] + 2
                else:
                    dp[j][i] = max(dp[j+1][i], dp[j][i-1])
                
        return dp[0][len(s)-1]        
