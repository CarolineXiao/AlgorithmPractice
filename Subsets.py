class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if nums == None:
            return []
        
        nums.sort()
        result = []
        subset = []
        self.dfs(nums, subset, result, 0)
        return result
    
    def dfs(self, nums, subset, result, index):
        if index == len(nums):
            result.append(list(subset))
            return
            
        
        subset.append(nums[index])
        self.dfs(nums, subset, result, index+1)
        subset.remove(nums[index])
        self.dfs(nums, subset, result, index+1)
