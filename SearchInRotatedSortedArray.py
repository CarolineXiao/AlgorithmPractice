class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if A == []:
            return -1
        
        start = 0
        end = len(A) - 1
        first = A[start]
        last = A[end]

        while start + 1 < end:
            mid = (start + end) // 2
            if target > last:
                if A[mid] >= last:
                    if target > A[mid]:
                        start = mid
                    else:
                        end = mid
                else:
                    end = mid
            else:
                if A[mid] >= last:
                    start = mid
                else:
                    if target > A[mid]:
                        start = mid
                    else:
                        end = mid
                        
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
                    
