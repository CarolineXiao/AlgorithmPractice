class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        if nums == []:
            return 0
        
        slow = 1
        fast = 1
        
        while fast < len(nums):
            if nums[fast] != nums[fast-1]:
                if slow != fast:
                    nums[slow] = nums[fast]
                slow += 1
                fast += 1
            else:
                fast += 1
        
        nums = nums[:slow]
        return len(nums)
                
