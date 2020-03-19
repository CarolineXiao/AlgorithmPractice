from collections import deque
class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    queue1 = deque()
    queue2 = deque()
    def push(self, x):
        self.queue1.append(x)
    
    def moveItem(self):
        while len(self.queue1) > 1: 
            num = self.queue1.popleft()
            self.queue2.append(num)
        
    def swapQueue(self):
        self.queue1, self.queue2 = self.queue2, self.queue1
    """
    @return: nothing
    """
    def pop(self):
        if self.queue1:
            self.moveItem()
            x = self.queue1.popleft()
            self.swapQueue()
        
    """
    @return: An integer
    """
    def top(self):
        if self.queue1:
            self.moveItem()
            x = self.queue1.popleft()
            self.queue2.append(x)
            self.swapQueue()
            return x
        return None

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return len(self.queue1) == 0
