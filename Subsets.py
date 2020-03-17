class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        nums.sort()
        subset = [None] * len(nums)
        result = []

        self.helper(nums, subset, result, 0)
        return result
        
    def helper(self, nums, subset, result, i):
        if i == len(nums):
            result.append(list(filter(lambda x: x is not None, subset)))
        else:    
            subset[i] = None
            self.helper(nums, subset, result, i+1)
            subset[i] = nums[i]
            self.helper(nums, subset, result, i+1)
