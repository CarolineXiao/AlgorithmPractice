class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        if S == None or S == []:
            return 0
        S.sort()
        n = len(S)
        counter = 0
        for i in range(n):
            max_side = S[i]
            left = 0
            right = i - 1
            while left < right:
                if S[left] + S[right] > max_side:
                    counter += right - left
                    right -= 1
                else:
                    left += 1
        return counter
                    
