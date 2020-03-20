class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        # Sift down O(n)
        for i in range(len(A)-1, -1, -1):
            self.siftDown(A, i)
        return A
        
        
    def siftDown(self, A, k):
        while k*2 + 1 < len(A): # have left child
            minSon = k*2 + 1
            if k*2 + 2 < len(A): # have right child
                if A[k*2+2] < A[k*2+1]:
                    minSon = k*2 + 2
            if A[minSon] < A[k]:
                A[minSon], A[k] = A[k], A[minSon]
                k = minSon
            else:
                break
            
