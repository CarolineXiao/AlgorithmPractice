class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub not in num_dict:
                num_dict[nums[i]] = i
            else:
                return {num_dict[sub], i}
                
# Complexity: O(n)
