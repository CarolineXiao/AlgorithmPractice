class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        if nums == None:
            return []
        
        results = []
        permutation = []
        visited = [False] * len(nums)
        self.dfs(nums, permutation, results, visited)
        return results
        
    def dfs(self, nums, permutation, results, visited):
        if len(permutation) == len(nums):
            results.append(list(permutation))
            return
        
        for i in range(len(nums)):
            if not visited[i]:
                permutation.append(nums[i])
                visited[i] = True
                self.dfs(nums, permutation, results, visited)
                visited[i] = False
                permutation.remove(nums[i])
        
