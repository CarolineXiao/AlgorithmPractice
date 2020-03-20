class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        if dict == []:
            return []
        dict.add(start)
        dict.add(end)
        
        queue = []
        visited = {}
        visited[end] = 0
        queue.append((end,0))
        
        while queue:
            word, dist = queue.pop(0)
            neighbour_list = self.getNextWord(word)
            for neighbour in neighbour_list:
                if neighbour in dict and neighbour not in visited:
                    queue.append((neighbour, dist+1))
                    visited[neighbour] = dist+1
        results = []
        path = [start]
        self.dfs(visited, results, path, end, start)
        return results
        
    def dfs(self, visited, results, path, end, cur_word):
        if path[-1] == end:
            results.append(list(path))
            return
        
        word_list = self.getNextWord(cur_word)
        for word in word_list:
            if word not in visited or visited[word] != visited[cur_word] - 1:
                continue
            path.append(word)
            self.dfs(visited, results, path, end, word)
            path.pop()
        
        
        
            
    def getNextWord(self, word):
        word_list = set()
        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:]
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c != word[i]:
                    next_word = left + c + right
                    word_list.add(next_word)
        return word_list
