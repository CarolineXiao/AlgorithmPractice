class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        if nums == []:
            return 0
            '''
        import sys
        max_sum = -sys.maxsize
        for i in range(len(nums)):
            j = i
            cur_sum = 0
            while j < len(nums):
                cur_sum += nums[j]
                if cur_sum > max_sum:
                    max_sum = cur_sum
                j += 1
        return max_sum
        '''
        
        import sys
        max_sum = -sys.maxsize
        prefix_min = sys.maxsize
        cur_sum = 0
        
        for i in range(len(nums)):
            cur_sum += nums[i]
            max_sum = max(cur_sum-prefix_min, cur_sum, max_sum)
            prefix_min = min(prefix_min,cur_sum)
            
        return max_sum
            
        
