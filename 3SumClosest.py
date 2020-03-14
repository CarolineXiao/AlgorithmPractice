import sys
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        if numbers == None or len(numbers) < 3:
            return 0
        
        numbers.sort()
        n = len(numbers)
        ans = 0
        diff = sys.maxsize
        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                twoSum = numbers[left] + numbers[right]
                newTarget = target - numbers[i]
                threeSum = twoSum + numbers[i]
                if twoSum == newTarget:
                    return threeSum
                elif twoSum < newTarget:
                    if abs(threeSum - target) < diff:
                        diff = abs(threeSum - target)
                        ans = threeSum
                    left += 1
                else:
                    if abs(threeSum - target) < diff:
                        diff = abs(threeSum - target)
                        ans = threeSum
                    right -= 1
        return ans
                          
