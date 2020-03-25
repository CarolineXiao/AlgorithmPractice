class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        if len(s) == 0 or dict == []:
            return 0
        
        n = len(s)
        s = s.lower()
        lower = set()
        for word in dict:
            lower.add(word.lower())
        #f[i][j] -> how many sentences can form in s[i:j+1]
        f = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i,n):
                word = s[i:j+1]
                if word in lower:
                    f[i][j] = 1
        for i in range(n):
            for j in range(i,n):
                for k in range(i,j):
                    f[i][j] += f[i][k] * f[k+1][j]
        
        return f[0][-1]
            
