class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        if nums == None:
            return []
        nums.sort()
        permutation = []
        results = []
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
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            permutation.append(nums[i])
            visited[i] = 1
            self.dfs(nums, permutation, results, visited)
            visited[i] = 0
            permutation.pop()
