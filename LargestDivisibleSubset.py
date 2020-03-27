class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        if nums == []:
            return 0
        nums.sort(reverse = True)
        result = 0
        f = [1] * len(nums)
        pi = [0] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] % nums[i] == 0: 
                    f[i] = max(f[i], f[j]+1)
                    if f[i] == f[j] + 1:
                        pi[i] = j
        
        max_length = 0
        p = -1

        for i in range(len(nums)):
            if f[i] > max_length:
                max_length = f[i]
                p = i
        result = [0] * max_length
        for i in range(max_length-1, -1, -1):
            result[i] = nums[p]
            p = pi[p]
        
        
        return result
