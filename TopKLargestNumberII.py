import heapq
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.number = []
        self.size = k

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        if len(self.number) < self.size:
            self.number.append(num)
        else:
            heapq.heapify(self.number)
            min_num = heapq.heappop(self.number)
            if num > min_num:
                self.number.append(num)
            else:
                self.number.append(min_num)
        heapq.heapify(self.number)
            

    """
    @return: Top k element
    """
    def topk(self):
        self.number.sort(reverse=True)
        return self.number
