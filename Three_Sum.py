class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i in range(0, len(nums)-2):
            a = nums[i]
            pre = i + 1
            post = len(nums) - 1
            
            while pre < post:
                b = nums[pre]
                c = nums[post]
                sum = a + b + c
                if sum == 0:
                    if [a, b, c] not in result:
                        result.append([a, b, c])
                    pre += 1
                    post -= 1
                elif sum < 0:
                    pre += 1
                else:
                    post -= 1
        return result
        
        
