class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        top = self.getFirstDiffTop(image, x, y)
        bot = self.getFirstDiffBot(image, x, y)
        left = self.getFirstDiffLeft(image, x, y)
        right = self.getFirstDiffRight(image, x, y)
        print(top, bot, left, right)
        
        return (bot - top + 1) * (right - left + 1)
        
    def getFirstDiffTop(self, image, x, y):
        start = 0
        end = x
        while start + 1 < end:
            mid = start + (end - start) // 2
            isvalid = 0
            for i in range(len(image[mid])):
                if image[mid][i] == "1":
                    isvalid = 1
                    break
            if isvalid:
                end = mid
            else:
                start = mid
        
        isvalid = x
        for i in range(len(image[start])):
            if image[start][i] == "1":
                isvalid = start
                break
            if image[end][i] == "1":
                isvalid = end
            
        return isvalid
    
    def getFirstDiffBot(self, image, x, y):
        start = x
        end = len(image) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            isvalid = 0
            for i in range(len(image[mid])):
                if image[mid][i] == "1":
                    isvalid = 1
                    break
            if isvalid:
                start = mid
            else:
                end = mid

        isvalid = x
        for i in range(len(image[end])):
            if image[end][i] == "1":
                isvalid = end
                break
            if image[start][i] == "1":
                isvalid = start
            
        return isvalid

            
    def getFirstDiffLeft(self, image, x, y):
        
        start = 0
        end = y
        while start + 1 < end:
            mid = start + (end - start) // 2
            isvalid = 0
            for i in range(len(image)):
                if image[i][mid] == "1":
                    isvalid = 1
                    break
            if isvalid:
                end = mid
            else:
                start = mid
            
        isvalid = y
        for i in range(len(image)):
            if image[i][start] == "1":
                isvalid = start
                break
            if image[i][end] == "1":
                isvalid = end
            
        return isvalid
        
    
    def getFirstDiffRight(self, image, x, y):
        start = y
        end = len(image[0]) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            isvalid = 0
            for i in range(len(image)):
                if image[i][mid] == "1":
                    isvalid = 1
                    break
            if isvalid:
                start = mid
            else:
                end = mid
        
        isvalid = y
        for i in range(len(image)):
            if image[i][end] == "1":
                isvalid = end
                break
            if image[i][start] == "1":
                isvalid = start
            
        return isvalid
