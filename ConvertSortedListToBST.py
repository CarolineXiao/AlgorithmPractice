"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        if head == None:
            return None
        # find middle node
        mid = head
        end = head
        prev = None
        while end.next != None and end.next.next != None:
            end = end.next.next
            prev = mid
            mid = mid.next
        
        if end == head and head.next != None:
            end = end.next
        
        if prev != None:
            prev.next = None
            
        node = TreeNode(mid.val)
        
        if mid == head:
            node.left = None
        else:
            node.left = self.sortedListToBST(head)
        if mid == end:
            node.right = None
        else:
            node.right = self.sortedListToBST(mid.next)
        
        return node
