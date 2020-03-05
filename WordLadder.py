class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, wordList):
        # write your code here
        #dict.add(end)
        #dist = 0
        if end not in wordList or not end or not start or not wordList:
            return 0
        
        dict = set()
        for i in range(len(wordList)):
            dict.add(wordList[i])
        
        queue = []
        visited = set()
        queue.append((start,1))
        while queue:
            word, dist = queue.pop(0)
            word_list = self.getNextWord(word)
            for next_word in word_list:
                if next_word in dict and next_word not in visited:
                    if next_word == end:
                        return dist+1
                    queue.append((next_word,dist+1))
                    visited.add(next_word)
        
        return 0
    
    
    def getNextWord(self, word):
        word_list = set()
        for i in range(len(word)):
            left = word[:i]
            right = word[i+1:len(word)]

            for char in "abcdefghijklmnopqrstuvwxyz":
                if char != word[i]:
                    new_word = left + char + right
                    word_list.add(new_word)

        return word_list
