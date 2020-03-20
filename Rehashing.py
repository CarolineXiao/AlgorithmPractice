"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        nums = []
        capacity = len(hashTable) * 2
        newHash = [None] * capacity
        for i in hashTable:
            while i != None:
                nums.append(i.val)
                i = i.next
                
        for i in range(len(nums)-1, -1, -1):
            node = ListNode(nums[i])
            index = self.hashCode(nums[i], capacity)
            if newHash[index] == None:
                newHash[index] = node
            else:
                preHead = newHash[index]
                node.next = preHead
                newHash[index] = node
        
        return newHash
        
    def hashCode(self, key, capacity):
        return key % capacity
