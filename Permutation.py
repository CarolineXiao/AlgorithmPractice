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
        visited = [0] * len(nums)
        self.dfs(nums, permutation, results, visited)
        return results
        
    def dfs(self, nums, permutation, results, visited):
        if len(permutation) == len(nums):
            results.append(list(permutation))
            return
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            permutation.append(nums[i])
            visited[i] = 1
            self.dfs(nums, permutation, results, visited)
            visited[i] = 0
            permutation.pop()
        
