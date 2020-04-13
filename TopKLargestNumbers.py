import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        if len(nums) <= k:
            return sorted(nums, reverse=True)
        
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
        
        return sorted(heap, reverse=True)
