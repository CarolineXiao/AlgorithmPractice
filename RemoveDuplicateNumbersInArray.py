class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        # O(n)
        
        hash_set = set()
        counter = 0
        for num in nums:
            if num not in hash_set:
                hash_set.add(num)
                nums[counter] = num
                counter += 1
        return counter
        
        
        '''
        # O(nlogn) -> order not correct
        if nums == []:
            return 0
            
        nums.sort()
        result = 1
        for i in range(1, len(nums) - 1):
            if nums[i-1] != nums[i]:
                nums[result] = nums[i]
                result += 1
        return result
        '''
