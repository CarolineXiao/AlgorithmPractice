class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        if A == []:
            return 0
        
        left = 0
        right = len(A) - 1
        
        while left <= right:
            while left <= right and A[left] != elem:
                left += 1
            while left <= right and A[right] == elem:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        while A:
            if A[-1] == elem:
                A.pop()
            else:
                break
        
        return len(A)
                
