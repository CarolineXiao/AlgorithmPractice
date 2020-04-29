"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        if (head == None and x == 0) or head.next == None:
            return head
        
        leftDummy = ListNode(-1)
        rightDummy = ListNode(-1)
        left = leftDummy
        right = rightDummy
        cur = head
        
        while cur != None:
            if cur.val < x:
                left.next = cur
                left = cur
                cur = cur.next
                left.next = None
            else:
                right.next = cur
                right = cur
                cur = cur.next
                right.next = None 
        if leftDummy.next == None:
            return rightDummy.next
        left.next = rightDummy.next
        return leftDummy.next
