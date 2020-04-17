class Solution:
    """
    @param A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        number = set()
        for num in A:
            number.add(num)
        
        n = 1
        while 1:
            if n not in number:
                return n
            n += 1
