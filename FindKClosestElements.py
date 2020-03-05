class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []
        index = self.findClosestNum(arr, x)
        left = index - 1
        right = index + 1
        result.append(arr[index])
        while len(result) < k:
            if left < 0:
                result.append(arr[right])
                right += 1
                continue
            if right >= len(arr):
                result.append(arr[left])
                left -= 1
                continue
            diff_left = x - arr[left]
            diff_right = arr[right] - x
            if diff_left <= diff_right:
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
           
        return sorted(result)
        
        
    def findClosestNum(self, A, target):
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
                
        dif1 = target - A[start]
        dif2 = A[end] - target
        
        if dif1 > dif2:
            return end
        else:
            return start
