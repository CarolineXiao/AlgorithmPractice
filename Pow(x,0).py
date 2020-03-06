class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n == 0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = -n
        
        result = 1
        temp = x
        
        while n != 0:
            if n % 2 == 1:
                result = result * temp
            temp = temp * temp
            n = n // 2
                
            
        return result
        
