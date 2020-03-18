class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        if n == 0:
            return []
        if n == 1:
            return [["Q"]]
        results = []
        col = []
        visited = [0] * n
        self.permuation(n, results, col, visited)
        return results
    
    def permuation(self, n, results, col, visited):
        if len(col) == n:
            results.append(self.drawBoard(col))
        for i in range(n):
            if visited[i]:
                continue
            if self.isValid(col, i):
                col.append(i)
                visited[i] = 1
                self.permuation(n, results, col, visited)
                visited[i] = 0
                col.pop()
    
    def drawBoard(self, col):
        n = len(col)
        board = []
        for i in range(n):
            row = ""
            for j in range(n):
                if j == col[i]:
                    row += "Q"
                else:
                    row += "."
            board.append(row)
        return board
                    
        
    def isValid(self, col, column):
        rowIndex = len(col)
        for i in range(rowIndex):
            if i + col[i] == rowIndex + column:
                return False
            if i - col[i] == rowIndex - column:
                return False
        return True
              
