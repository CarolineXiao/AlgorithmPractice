class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        upperBound = self.findUpperBound(reader, target)
        #print(upperBound)
        if upperBound == 0:
            return 0
        start = 0
        end = upperBound
        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) == target:
                end = mid
            elif reader.get(mid) < target:
                start = mid
            else:
                end = mid
            
        if reader.get(start) == target:
            return start
            
        if reader.get(end) == target:
            return end
            
        return -1
            

        
    def findUpperBound(self, reader, target):
        if reader.get(0) == target:
            return 0
            
        k = 1
        while reader.get(k) <= target and reader.get(k) != None:
            if reader.get(k) == target:
                return k
            k = 2 * k
        
        return k
        
