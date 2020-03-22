import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        if n == 1:
            return 1
        ugly_number = [1]
        counter = 1
        visited = set()
        while counter < n:
            num = heapq.heappop(ugly_number)
            for factor in [2, 3, 5]:
                if num*factor not in visited:
                    visited.add(num*factor)
                    heapq.heappush(ugly_number, num*factor)
            heapq.heapify(ugly_number)
            counter += 1
        return heapq.heappop(ugly_number)
       
