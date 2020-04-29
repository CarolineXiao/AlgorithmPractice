"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
            
        hash_map = {}
        dummy = RandomListNode(-1)
        pre = dummy
        
        while head != None:
            new_node = None
            if head in hash_map:
                new_node = hash_map[head]
            else:
                n = RandomListNode(head.label)
                hash_map[head] = n
                new_node = n
            
            pre.next = new_node
            pre = new_node
            
            node = head.random
            if node != None:
                if node in hash_map:
                    new_node.random = hash_map[node]
                else:
                    n = RandomListNode(node.label)
                    hash_map[node] = n
                    new_node.random = n
            else:
                new_node.random = None
            head = head.next
                
    
        return dummy.next
                
                
