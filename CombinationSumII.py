class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        if num == None:
            return []
        num.sort()
        results = []
        sumSet = []
        visited = [0] * len(num)
        self.dfs(num, sumSet, results, target, visited, 0)
        return results
        
    def dfs(self, num, sumSet, results, target, visited, startIndex):
        if target < 0:
            return
        if target == 0:
            results.append(list(sumSet))
        
        for i in range(startIndex, len(num)):
            if visited[i]:
                continue
            if i > 0 and num[i] == num[i-1] and not visited[i-1]:
                continue
            sumSet.append(num[i])
            visited[i] = 1
            self.dfs(num, sumSet, results, target-num[i], visited, i+1)
            visited[i] = 0
            sumSet.pop()
