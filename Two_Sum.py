class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        # using hashset
        dict = {}
        for i in range(len(numbers)):
            n = target - numbers[i]
            if n in dict:
                return [dict[n], i]
            dict[numbers[i]] = i
        
                
# Complexity: O(n)
