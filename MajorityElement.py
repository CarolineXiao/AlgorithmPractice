class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        """ Boyer-Moore majority vote algorithm implementation
        """
        storedNumber = None 
        counter = 0
        for num in nums:
            if num == storedNumber:
                counter += 1 
            else:
                if counter == 0:
                    storedNumber = num
                    counter = 1 
                else:
                    counter -= 1 
                    
        return storedNumber
