import heapq
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        if num == []:
            return 0
            
        result = 0    
        hash_set = set()
        for n in num:
            hash_set.add(n)
            
        for n in num:
            if n not in hash_set:
                continue
            consecutive = 1
            left = n - 1
            right = n + 1
            while left in hash_set:
                hash_set.remove(left)
                consecutive += 1
                left -= 1
            while right in hash_set:
                hash_set.remove(right)
                consecutive += 1
                right += 1
            if consecutive > result:
                result = consecutive
        return result
            
