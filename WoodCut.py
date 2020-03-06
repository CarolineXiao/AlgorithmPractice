class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        Lsum = 0
        for l in L:
            Lsum += l
        
        start = Lsum // (k + len(L))
        end = Lsum // k
        print(start,end)
        if start == 0 and end == 0:
            return 0
        
        while start + 1 < end:
            mid = start + (end - start) // 2

            if self.numPieces(L, mid) < k:
                end = mid
            else:
                start = mid
        
        if self.numPieces(L, end) >= k:
            return end
        
        if self.numPieces(L, start) >= k:
            return start
        
        return 0
            
    
    def numPieces(self, L, length):
        sum = 0
        for i in range(len(L)):
            sum += L[i] // length
        
        return sum
