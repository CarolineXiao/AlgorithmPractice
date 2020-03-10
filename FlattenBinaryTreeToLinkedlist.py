"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    lastNode = None
    def flatten(self, root):
        # write your code here
        if root == None:
            return
        
        if self.lastNode:
            self.lastNode.left = None
            self.lastNode.right = root
        
        self.lastNode = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
        
