class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        if digits == "":
            return []
            
        dict = {}
        dict['2'] = ["a", "b", "c"]
        dict['3'] = ["d", "e", "f"]
        dict['4'] = ["g", "h", "i"]
        dict['5'] = ["j", "k", "l"]
        dict['6'] = ["m", "n", "o"]
        dict['7'] = ["p", "q", "r", "s"]
        dict['8'] = ["t", "u", "v"]
        dict['9'] = ["w", "x", "y", "z"]
        
        results = []
        combination = ""
        self.dfs(dict, digits, combination, results, 0)
        return results
        
    def dfs(self, dict, digits, combination, results, index):
        if len(combination) == len(digits):
            results.append(combination)
            return
        
        for i in range(index, len(digits)):
            chars = dict[digits[i]]
            for char in chars:
                combination += char
                self.dfs(dict, digits, combination, results, i+1)
                combination = combination[:-1]
        
