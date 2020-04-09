class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if numbers == []:
            return []
            
        numbers.sort()
        results = []
        for i in range(len(numbers)):
            target = numbers[i]
            self.twoSum(numbers, target, i+1, len(numbers)-1, results)
            
        return results
            
            
    def twoSum(self, numbers, target, left, right, results):
        while left < right:
            if numbers[left] + numbers[right] + target == 0:
                result = [target, numbers[left], numbers[right]]
                
                if result not in results:
                    results.append(result)
                left += 1
                right -= 1
            elif numbers[left] + numbers[right] + target < 0:
                left += 1
            else:
                right -= 1
