class Solution:
    """
    @param nums: An array of integers
    @return: nothing
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
            nums.reverse()
            return nums
        target = i - 1
        j = len(nums) -1
        while nums[j] <= nums[target]:
            j -= 1
        nums[target], nums[j] = nums[j], nums[target]
        left = i
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
            
