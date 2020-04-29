"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        '''
        if head.next == None:
            return None
        counter = 0
        ptr = head
        while ptr != None:
            counter += 1
            ptr = ptr.next
        
        if counter-n == 0:
            return head.next
        
        ptr = head
        for _ in range(counter-n-1):
            ptr = ptr.next
        ptr.next = ptr.next.next
        
        return head
        '''
        end = head
        target = head
        cur_len = 1
        while cur_len <= n:
            end = end.next
            cur_len += 1
        
        if end == None:
            return head.next
        
        while end.next != None:
            end = end.next
            target = target.next
            
        target.next = target.next.next
        return head
        
