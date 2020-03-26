import sys
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # 1. traverse
        '''
        if triangle == []:
            return 0
        
        return self.traverse(triangle, 0, 0, 0)
        
    def traverse(self, triangle, x, y, min_sum):
        if x == len(triangle):
            return min_sum
        
        left = self.traverse(triangle, x+1, y, min_sum+triangle[x][y])
        right = self.traverse(triangle, x+1, y+1, min_sum+triangle[x][y])
        return min(left,right)
        '''
        
        # 2. Divide Conquer
        '''
        if triangle == []:
            return 0
        
        return self.divideConquer(triangle, 0, 0)
        
    def divideConquer(self, triangle, x, y):
        if x == len(triangle):
            return 0
        
        left = self.divideConquer(triangle, x+1, y)
        right = self.divideConquer(triangle, x+1, y+1)
        return min(left,right) + triangle[x][y]
        '''
        
        # 3. Memoization
        '''
        if triangle == []:
            return 0
        
        memo = [] 
        visited = []
        for i in range(len(triangle)):
            memo_row = []
            visited_row = []
            for j in range(len(triangle[i])):
                memo_row.append(-1)
                visited_row.append(False)
            memo.append(memo_row)
            visited.append(visited_row)
        
        return self.divideConquer(triangle, 0, 0, memo, visited)
        
    def divideConquer(self, triangle, x, y, memo, visited):
        if x == len(triangle):
            return 0
            
        if visited[x][y] == True:
            return memo[x][y]
        
        left = self.divideConquer(triangle, x+1, y, memo, visited)
        right = self.divideConquer(triangle, x+1, y+1, memo, visited)
        visited[x][y] = True
        memo[x][y] = min(left,right) + triangle[x][y]
        
        return memo[x][y]
        '''
    
    # 4. DP
        if triangle == []:
            return 0
        
        f = [[sys.maxsize] * len(triangle[i]) for i in range(len(triangle))]
        #f[0][0] = triangle[0][0]
        
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i - 1 < 0:
                    f[i][j] = triangle[i][j]
                else:
                    if 0 <= j < len(triangle[i-1]) and 0 <= j - 1 < len(triangle[i-1]):
                        f[i][j] = min(f[i-1][j-1], f[i-1][j]) + triangle[i][j]
                    elif 0 <= j < len(triangle[i-1]):
                        f[i][j] = f[i-1][j] + triangle[i][j]
                    else:
                        f[i][j] = f[i-1][j-1] + triangle[i][j]
        
        min_sum = sys.maxsize
        for s in f[len(triangle)-1]:
            if s < min_sum:
                min_sum = s
        return min_sum
                    
