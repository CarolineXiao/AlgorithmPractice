class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        f = [False] * len(A)
        f[0] = True
        
        # f[j] -> whether we can jump to j from i (i<j)
        for j in range(len(A)):
            for i in range(j):
                if f[i] and i + A[i] >= j:
                    f[j] = True
                    break
        return f[len(A)-1]
