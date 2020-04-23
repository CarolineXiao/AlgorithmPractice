class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        counter = 0
        
        while n > 0:
            counter += n // 5
            n //= 5
        return counter
