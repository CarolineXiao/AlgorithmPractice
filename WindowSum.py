class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if nums == [] or k == 0 or k > len(nums):
            return []
            
        n = len(nums)
        sum = [0] * (n - k + 1)
        for i in range(k):
            sum[0] += nums[i]

        for i in range(1, (n-k+1)):
            sum[i] = sum[i-1] - nums[i-1] + nums[i+k-1]
        
        return sum
