class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        if nums == None or nums == []:
            return -1
        return self.quickSelect(nums, 0, len(nums) - 1, k)
        
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        left = start
        right = end
        pivot = nums[(right + left) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
        if start + k - 1 <= right:
            return self.quickSelect(nums, start, right, k)
        if start + k - 1 >= left:
            return self.quickSelect(nums, left, end, k - (left - start))
        return nums[right+1]
                                    
