class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if nums == None:
            return []
        nums.sort()
        subset = []
        results = []
        self.dfs(nums, subset, results, 0)
        return results
    
    def dfs(self, nums, subset, results, startIndex):
        results.append(list(subset))
        for i in range(startIndex, len(nums)):
            if i != 0 and nums[i] == nums[i-1] and i > startIndex:
                continue
            subset.append(nums[i])
            self.dfs(nums, subset, results, i+1)
            subset.remove(nums[i])
