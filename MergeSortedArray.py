class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        if A == []:
            return B
        if B == []:
            return A
        result = [0] * (m+n)
        pa = m-1
        pb = n-1
        index = m+n-1
        while pa >= 0 and pb >= 0:
            if A[pa] >= B[pb]:
                A[index] = A[pa]
                pa -= 1
            else:
                A[index] = B[pb]
                pb -= 1
            index -= 1
            
        while pa >= 0:
            A[index] = A[pa]
            pa -= 1
            index -= 1

        while pb >= 0:
            A[index] = B[pb]
            pb -= 1
            index -= 1
        
            
