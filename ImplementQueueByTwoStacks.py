class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        self.stack2.append(element)

    """
    @return: An integer
    """
    def pop(self):
        if self.stack1 == [ ] and self.stack2 == []:
            return None
        if self.stack1 == []:
            while len(self.stack2) > 0:
                self.stack1.append(self.stack2[-1])
                self.stack2.pop()
        val = self.stack1[-1]
        self.stack1.pop()
        return val
            

    """
    @return: An integer
    """
    def top(self):
        if self.stack1 == [ ] and self.stack2 == []:
            return None
        if self.stack1 != []:
            return self.stack1[-1]
        return self.stack2[0]
        
