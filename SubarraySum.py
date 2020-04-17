class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        sum = 0
        
        dict = {}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                return [i, i]
            sum = sum + nums[i]
            if sum in dict:
                return [dict[sum]+1, i]
            dict[sum] = i 
            if sum == 0:
                return [0, i]
        return [0, 0]
        
