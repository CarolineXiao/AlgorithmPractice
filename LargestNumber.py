from functools import cmp_to_key
class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        nums = sorted(nums, key=cmp_to_key(lambda x, y: self.compare(x,y)))

        result = ''.join([str(i) for i in nums])
        if result[0] == "0":
            return "0"
        return result
    
    def compare(self, x, y):
        if str(x) + str(y) < str(y) + str(x):
            return 1
        return -1
            
        
