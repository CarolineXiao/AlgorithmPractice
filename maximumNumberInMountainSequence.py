class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if nums == []:
            return None
        
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid+1] < nums[mid]:
                end = mid
            else:
                start = mid
        
        return max(nums[start], nums[end])
        
