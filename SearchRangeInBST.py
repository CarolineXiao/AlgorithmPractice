"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        
        result = []
        lowStack = []
        node = root
        while node:
            if node.val < k1:
                node = node.right
            else:
                lowStack.append(node)
                node = node.left
        
        if lowStack == []:
            return []
        
        while lowStack and lowStack[-1].val <= k2:
            node = lowStack.pop()
            result.append(node.val)
            if node.right:
                node = node.right
                while node:
                    if node.val >= k1:
                        lowStack.append(node)
                        node = node.left
        
        return result
     
