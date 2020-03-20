class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if nums == None or nums == []:
            return -1
        return self.quickSelelct(nums, n, 0, len(nums) - 1)
        
    def quickSelelct(self, nums, n, start, end):
        if start == end:
            return nums[start]
        left = start
        right = end
        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
        if start + n - 1 <= right:
            return self.quickSelelct(nums, n, start, right)
        if start + n - 1 >= left:
            return self.quickSelelct(nums, n - (left - start), left, end)
        return nums[right+1]
