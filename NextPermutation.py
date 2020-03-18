class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        if nums == None:
            return None
        if len(nums) == 1:
            return nums
            
        i = len(nums) - 1 
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i == 0:
            return sorted(nums)
        target = i - 1
        j = len(nums) -1
        while nums[j] <= nums[target]:
            j -= 1
        nums[target], nums[j] = nums[j], nums[target]
        newlist = sorted(nums[i:len(nums)])
        return nums[:i] + newlist
            
