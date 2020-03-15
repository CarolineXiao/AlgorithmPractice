class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        if colors == []:
            return []
        
        return self.rainbowSort(colors, 0, len(colors) - 1, 1, k)
    
    def rainbowSort(self, colors, left, right, colorFrom, colorTo):
        start = left
        end = right
        if start >= end:
            return 
        if colorFrom == colorTo:
            return
       
        colorMid = (colorFrom + colorTo) // 2
        while start <= end:
            while start <= end and colors[start] <= colorMid:
                start += 1
            while start <= end and colors[end] > colorMid:
                end -= 1
            if start <= end:
                colors[start], colors[end] = colors[end], colors[start]
                start += 1
                end -= 1
        self.rainbowSort(colors, left, end, colorFrom, colorMid)
        self.rainbowSort(colors, start, right, colorMid+1, colorTo)
