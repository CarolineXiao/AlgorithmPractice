class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == [] or matrix[0] == []:
            return False
            
        top = 0
        bot = len(matrix) - 1
        last = len(matrix[0]) - 1
        row = 0
        
        while top + 1 < bot:
            mid = top + (bot - top) // 2
            if matrix[mid][last] == target:
                top = mid
            elif matrix[mid][last] < target:
                top = mid
            else:
                bot = mid
    
        if matrix[top][last] >= target:
            row = top
        elif matrix[bot][last] >= target:
            row = bot

        start = 0
        end = last
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[row][mid] == target:
                start = mid
            elif matrix[row][mid] < target:
                start = mid
            else:
                end = mid
        
        if matrix[row][start] == target:
            return True
        if matrix[row][end] == target:
            return True
        
        return False
            
        
