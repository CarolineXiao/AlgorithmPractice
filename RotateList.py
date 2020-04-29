"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head
        
        n, end = self.getLength(head)
        if k >= n:
            k = k % n
        if k == 0:
            return head
            
        target = n - k - 1
        prev = head
        
        for _ in range(target):
            prev = prev.next
        
        new_head = prev.next
        prev.next = None
        end.next = head
        return new_head
    
    def getLength(self, head):
        result = 1
        while head.next != None:
            result += 1
            head = head.next
        return result, head
            
            
