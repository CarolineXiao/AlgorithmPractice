class Solution:
    """
    @param A: A positive integer which has N digits, A is a string
    @param k: Remove k digits
    @return: A string
    """
    def DeleteDigits(self, A, k):
        
        for i in range(k):
            index = 0
            while index < len(A):
                if index == len(A)-1:
                    A = A[:index] + A[index+1:]
                    break
                if A[index] > A[index+1]:
                    A = A[:index] + A[index+1:]
                    break
                else:
                    index += 1
        print(A)
        for char in A:
            if char == '0':
                A = A.replace('0', '', 1)
            else:
                break
        return A
