class Solution:
    """
    @param array: an integer array
    @return: nothing
    """
    def pancakeSort(self, array):
        # Write your code here
        size = len(array)
        while size > 0:
            maxIndex = self.findMax(array[:size])
            FlipTool.flip(array, maxIndex)
            FlipTool.flip(array, size - 1)
            size -= 1
        return array
        
    def findMax(self, array):
        index = 0
        for i in range(len(array)):
            if array[i] >= array[index]:
                index = i
        return index
