class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # p[i] -> the product of A[i] ... A[n-1]
        p = [0] * (len(nums) + 1)
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            prod *= nums[i]
            p[i] = prod
        p[len(nums)] = 1
        
        B = [0] * len(nums)   
        pre_prod = 1
        for i in range(len(B)):
            B[i] = p[i+1] * pre_prod
            pre_prod *= nums[i]
        
        return B
