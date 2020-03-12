"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        '''
        if head == None:
            return None
        
        list = []
        node = head
        while node.next:
            list.append(node)
            node = node.next
        list.append(node)
        n = len(list)
        if n % 2 == 0:
            return list[(n // 2) - 1]
        else:
            return list[(n // 2)]
        '''
        
        if head == None:
            return None
            
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
