class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        '''
        # simple recursion
        if nums == None:
            return []
        nums.sort()
        result = []
        subset = []
        self.dfs(nums, result, subset, 0)
        return result
    
    def dfs(self, nums, result, subset, index):
        if index == len(nums):
            result.append(list(subset))
            return
        
        subset.append(nums[index])
        self.dfs(nums, result, subset, index+1)
        subset.remove(nums[index])
        self.dfs(nums, result, subset, index+1)
        '''
        
        # DFS - backtracking
        if nums == None:
            return []
        nums.sort()
        result = []
        subset = []
        self.dfs(nums, subset, result, 0)
        return result
    
    def dfs(self, nums, subset, result, startIndex):
        result.append(list(subset))
        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, subset, result, i+1)
            subset.remove(nums[i])
            
