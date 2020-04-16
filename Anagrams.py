class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        if strs == []:
            return []
        
        dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in dict:
                dict[sorted_word] += [word]
            else:
                dict[sorted_word] = [word]

        results = []
        for items in dict:
            if len(dict[items]) > 1:
                results += dict[items]
        
        return results
