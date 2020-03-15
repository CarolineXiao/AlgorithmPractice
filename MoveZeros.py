class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if nums == []:
            return []
        slow = 0
        fast= slow + 1
        
        while fast < len(nums):
            while fast < len(nums) and nums[slow] != 0:
                slow += 1
                fast += 1
            while fast < len(nums) and nums[fast] == 0:
                fast += 1
            if fast < len(nums) and slow < fast:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast += 1
        return nums
