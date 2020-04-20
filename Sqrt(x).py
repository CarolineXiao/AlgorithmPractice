class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x == 0:
            return 0
        if x == 1:
            return 1
            
        start = 1
        end = x
        
        while start + 1 < end:
            mid = (start + end) // 2
            if mid == x / mid:
                return mid
            elif mid < x / mid:
                start = mid
            else:
                end = mid
        
        if end > end / mid:
            return start
        
        return end 
