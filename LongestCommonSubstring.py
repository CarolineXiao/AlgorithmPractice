class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        if A == "" or B == "":
            return 0
        
        
        # dp[i][j] -> longestCommonSubstring in A[0-i] and B[0-j] ending with A[i] and B[j]
        dp = [[False] * len(B) for _ in range(len(A))]
        
        for j in range(len(B)):
            dp[0][j] = int(B[j] == A[0])
        
        for i in range(len(A)):
            dp[i][0] = int(A[i] == B[0])
            
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                if A[i] == B[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
        
        max_len = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
        
        return max_len
