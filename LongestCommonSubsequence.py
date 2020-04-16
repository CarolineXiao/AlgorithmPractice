class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        if A == "" or B == "":
            return 0
            
        f = [[0] * len(A) for _ in range(len(B))]
        f[0][0] = int(A[0] == B[0])
        
        for i in range(1, len(A)):
            f[i][0] = f[i-1][0]
            if A[i] == B[0]:
                f[i][0] = 1
        
        for j in range(1, len(B)):
            f[0][j] = f[0][j-1]
            if A[0] == B[j]:
                f[0][j] = 1
        
        for i in range(1, len(A)):
            for j in range(1, len(B)):
                f[i][j] = max(f[i-1][j], f[i][j-1])
                if A[i] == B[j]:
                    f[i][j] = f[i-1][j-1] + 1
        
        return f[len(A)-1][len(B)-1]
                
