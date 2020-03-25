class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        if s in dict or len(s) == 0:
            return True
        if dict == []:
            return False
        
        max_length = self.getMaxLength(dict)
        
        f = [False] * (len(s) + 1)
        f[0] = True
        
        for i in range(1,len(s)+1):
            lastWordLength = 1
            while lastWordLength <= max_length and lastWordLength <= i:
                # if 0 to i-lastWordLength cannot be broken
                if not f[i-lastWordLength]:
                    lastWordLength += 1
                    continue
                # if can -> check i-lastWordLength to i whether a word
                word = s[i-lastWordLength:i]
                if word in dict:
                    f[i] = True
                    break
                lastWordLength += 1
        
        return f[len(s)]
        
    
    def getMaxLength(self, dict):
        max_length = 0
        for word in dict:
            if len(word) > max_length:
                max_length = len(word)
        return max_length
