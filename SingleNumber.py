class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        A = sorted(A);
        if A == []:
            return -1
        i = 0
        while i < len(A):
            if (i+1) == len(A):
                return A[i]
            if A[i+1] != A[i]:
                return A[i]
            else:
                i += 2
        return A[0]
