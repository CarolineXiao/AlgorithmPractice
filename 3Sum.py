class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if numbers == None or numbers == []:
            return []
        
        result = []
        numbers.sort()
        n = len(numbers)
        for i in range(n):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            self.twoSum(numbers, -numbers[i], i, result)
        
        return result
        
    def twoSum(self, numbers, target, i, result):
        left = i + 1
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == -numbers[i]:
                result.append([numbers[i], numbers[left], numbers[right]])
                while left < right and numbers[left] == numbers[left+1]:
                    left += 1
                while left < right and numbers[right] == numbers[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif numbers[left] + numbers[right] < -numbers[i]:
                left += 1
            else:
                right -= 1
                
        
