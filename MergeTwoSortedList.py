"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        dummy = ListNode(-1)
        head = dummy
        tail = dummy
        
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                tail = p1
                p1 = p1.next
            else:
                tail.next = p2
                tail = p2
                p2 = p2.next
        
        if p1:
            tail.next = p1
        
        if p2:
            tail.next = p2
    
        return head.next
            
