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
        zero_counter = 0
        for i in range(len(numbers)):
                newN = numbers[:i] + numbers[i+1:]
                self.twoSum(newN, -numbers[i], result)
        return result
    
    def twoSum(self, numbers, target, result):
        dict = {}
        for n in numbers:
            if target - n in dict:
                if dict[target-n] == 1:
                    a = [n, target-n, -target]
                    mymax = max(a)
                    mymin = min(a)
                    a.remove(mymax)
                    a.remove(mymin)
                    mid = a[0]
                    r = [mymin, mid, mymax]
                    if r not in result:
                        result.append(r)
                dict[target-n] += 1
            dict[n] = 1
        
