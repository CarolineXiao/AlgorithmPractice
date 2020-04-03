"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        isBST, myMax, myMin = self.helper(root)
        return isBST
    
    
    def helper(self, root):
        if root == None:
            return True, -sys.maxsize, sys.maxsize
        
        left, leftMax, leftMin = self.helper(root.left)
        right, rightMax, rightMin = self.helper(root.right)
        
        curMax = max(root.val, leftMax, rightMax)
        curMin = min(root.val, leftMin, rightMin)
        
        isBST = left and right and leftMax < root.val < rightMin
        
        return isBST, curMax, curMin
