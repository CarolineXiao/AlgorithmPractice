"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
            
        cur = head
        prev = head
        while cur != None:
            if cur == head:
                cur = cur.next
                continue
            if cur.val == prev.val:
                cur = cur.next
            else:
                prev.next = cur
                prev = cur
                cur = cur.next
        prev.next = None
            
        return head
