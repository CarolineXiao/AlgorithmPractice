class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if board == [] or words == []:
            return []
            
        word_set = set(words)
        # build a prefix dictionary {prefix: is_a_prefix}
        prefix_set = {}
        for w in words:
            pre = ""
            for i in range(len(w)):
                pre += w[i]
                if pre not in prefix_set:
                    prefix_set[pre] = 1
            prefix_set[w] = 0
            
        results = set()
        word = ""
        print(word_set)
        print(prefix_set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.dfs(board, prefix_set, results, word+board[i][j], i, j, set([(i,j)]))
        
        return list(results)
        
    def dfs(self, board, prefix_set, results, word, x, y, visited):
        
        if word != "" and word not in prefix_set:
            return
        
        if word in prefix_set and prefix_set[word] == 0:
            results.add(word)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for delta_x, delta_y in directions:
            next_x = x + delta_x
            next_y = y + delta_y
            if self.isValid(board, next_x, next_y) and (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                next_letter = board[next_x][next_y]
                word += next_letter
                self.dfs(board, prefix_set, results, word, next_x, next_y, visited)
                word = word[:-1]
                visited.remove((next_x, next_y))
            
    def isValid(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
                
               
