class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        dict = {}
        n = len(nums)
        for i in range(n):
            if nums[i] + target in dict:
                return [dict[nums[i]+target]+1, i+1]
            if nums[i] - target in dict:
                return [dict[nums[i]-target]+1, i+1]
            dict[nums[i]] = i
        
