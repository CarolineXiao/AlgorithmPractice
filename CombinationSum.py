class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        if candidates == None:
            return []
        candidates.sort()
        results = []
        sumset = []
        self.dfs(candidates, sumset, results, 0, target)
        return results
        
    def dfs(self, candidates, sumset, results, startIndex, target):
        if target < 0:
            return
        if target == 0:
            results.append(list(sumset))
            return
        for i in range(startIndex, len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1] and i > startIndex:
                continue
            sumset.append(candidates[i])
            self.dfs(candidates, sumset, results, i, target-candidates[i])
            sumset.pop()
        
