class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if m > n:
            return self.findMedianSortedArrays(B, A)
        
        if A == [] and B == []:
            return -1
        if len(A) == 1 and len(B) == 1:
            return (A[0] + B[0]) / 2
        if A == []:
            if len(B) % 2 == 0:
                return (B[len(B)//2-1] + B[len(B)//2]) / 2
            else:
                return B[len(B)//2]
      
        
        start = 0
        end = m
        partition_a = 0
        partition_b = 0
        
        while start <= end:
            mid = (start + end) // 2
            partition_a = mid
            partition_b = (m + n + 1) // 2 - partition_a
            import sys
            a_partiton_max = -sys.maxsize if partition_a == 0 else A[partition_a-1]
            a_rest_min = sys.maxsize if partition_a == m else A[partition_a]
            print(a_partiton_max)
            print((m+n+1)//2-mid-1)
            
            b_partition_max = -sys.maxsize if partition_b == 0 else B[partition_b-1]
            b_rest_min = sys.maxsize if partition_b == n else B[partition_b]
            
            if a_partiton_max <= b_rest_min and b_partition_max <= a_rest_min:
                if (m+n) % 2 == 0:
                    return (max(a_partiton_max,b_partition_max) + min(a_rest_min,b_rest_min)) / 2
                else:
                    return max(a_partiton_max,b_partition_max)
            elif a_partiton_max > b_rest_min:
                end = mid - 1 
            else:
                start = mid + 1
        
