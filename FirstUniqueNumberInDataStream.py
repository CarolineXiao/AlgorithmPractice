class DataStream:
    
    def __init__(self):
        dummy = ListNode(-1)
        self.head = dummy
        self.tail = dummy
        self.num_to_prev = {}
        self.duplicates = set()
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        if num in self.duplicates:
            return
        if num not in self.num_to_prev:
            node = ListNode(num)
            self.num_to_prev[num] = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.duplicates.add(num)
            prev = self.num_to_prev[num]
            if prev.next == self.tail:
                self.tail = prev
                del self.num_to_prev[prev.next.val]
                prev.next = None
                return
            cur = prev.next
            prev.next = cur.next
            cur.next = None
            self.num_to_prev[prev.next.val] = prev
            del self.num_to_prev[cur.val]
            
    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        if self.head.next == None:
            return -1
        return self.head.next.val
