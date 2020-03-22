
class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        dummy = ListNode(0)
        self.head = dummy
        self.tail = dummy
        self.cur_sum = 0
        self.counter = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        node = ListNode(val)
        self.tail.next = node
        self.tail = node
        self.cur_sum += val
        if self.counter < self.size:
            self.counter += 1
        else:
            kick_node = self.head.next
            kick_val = kick_node.val
            self.head.next = kick_node.next
            self.cur_sum -= kick_val
        return self.cur_sum / self.counter
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
