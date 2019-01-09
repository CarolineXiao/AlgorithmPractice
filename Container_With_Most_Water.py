class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        start = 0
        end = len(height) - 1
        while start < end:
            area = (end - start) * min(height[start], height[end])
            if area > max_area:
                max_area = area
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area
    
        
