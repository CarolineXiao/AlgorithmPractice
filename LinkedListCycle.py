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
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        if head == head.next:
            return head
        # write your code here
        slow = head
        fast = head.next
        hasCycle = True
        while fast != slow:
            if fast == None or fast.next == None:
                hasCycle = False
                break
            slow = slow.next
            fast = fast.next.next
        
        if hasCycle:
            while fast.next != head:
                head = head.next
                fast = fast.next
        else:
            return None
        return head
