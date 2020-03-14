class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        n = len(numbers)
        if numbers == None or n < 4:
            return []
        numbers.sort()
        result = []    
        for i in range(n):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            for j in range(i+1, n):
                if j != i+1 and j > 0 and numbers[j] == numbers[j-1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    twoSum = numbers[left] + numbers[right]
                    newTarget = target - numbers[i] - numbers[j]
                    if twoSum == newTarget:
                        newResult = [numbers[i], numbers[j], numbers[left], numbers[right]]
                        result.append(newResult)
                        while left < right and numbers[left+1] == numbers[left]:
                            left += 1
                        while left < right and numbers[right-1] == numbers[right]:
                            right -= 1    
                        left += 1
                        right -= 1
                    elif twoSum < newTarget:
                        left += 1
                    else:
                        right -= 1
        return result
