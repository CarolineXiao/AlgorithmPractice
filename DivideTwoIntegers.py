class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        max_int = 2147483647
            
        is_neg = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            is_neg = True
        dividend = abs(dividend)
        divisor = abs(divisor)

        ans = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << shift):
                shift += 1
            dividend -= (divisor << (shift-1))
            ans += (1 << (shift-1))
        
        if is_neg:
            return -ans
        if ans > max_int:
            return max_int
        return ans
