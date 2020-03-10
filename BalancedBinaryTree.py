"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        rootDepth, rootisBalanced = self.maxDepth(root)
        return rootisBalanced
        
    def maxDepth(self, root):
        if root == None:
            return 0, True
        
        leftDepth, leftisBalanced = self.maxDepth(root.left)
        rightDepth, rightisBalanced = self.maxDepth(root.right)
        
        if not leftisBalanced or not rightisBalanced:
            return 0, False
        
        if abs(leftDepth - rightDepth) > 1:
            return 0, False
        
        return max(leftDepth, rightDepth) + 1 , True
        
