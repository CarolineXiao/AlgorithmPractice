class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    result = 0
    def longestIncreasingSubsequence(self, nums):
        # 1. dfs
        '''
        if nums == []:
            return 0
        
        #result = 0
        cur_result = []
        self.helper(nums, 0, cur_result)
        return self.result
        
    def helper(self, nums, startIndex, cur_result):
        if startIndex == len(nums):
            if len(cur_result) > self.result:
                self.result = len(cur_result)
            return
        
        for i in range(startIndex, len(nums)):
            if cur_result != [] and nums[i] > cur_result[-1]:
                cur_result.append(nums[i])
                self.helper(nums, i+1, cur_result)
                cur_result.pop()
                self.helper(nums, i+1, cur_result)
            elif cur_result == []:
                cur_result.append(nums[i])
                self.helper(nums, i+1, cur_result)
                cur_result.pop()
                self.helper(nums, i+1, cur_result)
                '''
        # 2. dp (n^2)
        if nums == []:
            return 0
        
        # f[i] -> the longest increasing subsequence in nums[0:i+1]  
        f = [1] * len(nums)
        pi = [0] * len(nums)
        p = -1
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j] + 1)
                    if f[i] == f[j] + 1:
                        pi[i] = j
        
        m = 0
        for i in range(len(nums)):
            if f[i] > m:
                m = f[i]
                p = i
        
        result = [0] * m
        for i in range(m-1, -1, -1):
            result[i] = nums[p]
            p = pi[p]

        # print the solution
        print(result)
        
        
        return max(f)
            
