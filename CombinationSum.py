class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        if candidates == []:
            return [[]]
        
        candidates.sort()
        combination = []
        curSum = 0
        results = []
        self.getCombinations(candidates, target, combination, results, curSum, 0)
        return results
    
    def getCombinations(self, candidates, target, combination, results, curSum, start):
        if curSum == target:
            if combination not in results:
                results.append(list(combination))
            return
        
        if curSum > target:
            return
        
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
            self.getCombinations(candidates, target, combination, results, curSum+candidates[i], i)
            combination.pop()
