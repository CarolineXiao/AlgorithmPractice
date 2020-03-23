"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq
ListNode.__lt__ = lambda x, y: (x.val < y.val)
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    #O(nlogk)
    def mergeKLists(self, lists):
        # heap
        '''
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, node)
            
            
        dummy = ListNode(0)
        end = dummy
        while heap:
            min_node = heapq.heappop(heap)
            end.next = min_node
            end = min_node
            if min_node.next != None:
                heapq.heappush(heap, min_node.next)
                min_node.next = None
                
        return dummy.next
        '''
        if lists == []:
            return []
        
        return self.merge_lists(lists, 0, len(lists)-1)
        
    def merge_lists(self, lists, start, end):
        if start >= end:
            return lists[start]
            
        mid = (start + end) // 2
        left = self.merge_lists(lists, start, mid)
        right = self.merge_lists(lists, mid+1, end)
        return self.merge_two_lists(left, right)
    
    def merge_two_lists(self, head1, head2):
        dummy = ListNode(0)
        tail = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                tail.next = head1
                tail = head1
                head1 = head1.next
            else:
                tail.next = head2
                tail = head2
                head2 = head2.next
        while head1:
            tail.next = head1
            tail = head1
            head1 = head1.next
        while head2:
            tail.next = head2
            tail = head2
            head2 = head2.next
        
        return dummy.next
            
            
