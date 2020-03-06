class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == [] or matrix[0] == []:
            return False
            
        counter = 0    
        end = len(matrix[0]) - 1
        top = 0
        
        while  0 <= top < len(matrix) and 0 <= end < len(matrix[0]):
            num = matrix[top][end]
            if num == target:
                counter += 1
                top += 1
                end -= 1
            elif num < target:
                top += 1
            else:
                end -= 1
        
        return counter > 0
        
