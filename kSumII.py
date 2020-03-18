class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        if A == None:
            return []
        results = []
        sumSet = []
        self.dfs(A, k, target, sumSet, results, 0)
        return results
        
    def dfs(self, A, k, target, sumSet, results, startIndex):
        if target < 0:
            return
        if len(sumSet) > k:
            return
        if target == 0 and len(sumSet) == k:
            results.append(list(sumSet))
        for i in range(startIndex, len(A)):
            sumSet.append(A[i])
            self.dfs(A, k, target - A[i], sumSet, results, i+1)
            sumSet.pop()
