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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        curSum, minSum, minNode = self.helper(root)
        return minNode
        
    def helper(self, root):
        if root == None:
            return 0, sys.maxsize, None
        
        sumLeft, minSumLeft, minNodeLeft = self.helper(root.left)
        sumRight, minSumRight, minNodeRight = self.helper(root.right)
        sumRoot = root.val + sumLeft + sumRight
        
        minSum = min(sumRoot, minSumLeft, minSumRight)
        
        if minSum == sumRoot:
            return sumRoot, minSum, root
        elif minSum == minSumLeft:
            return sumRoot, minSum, minNodeLeft
        else:
            return sumRoot, minSum, minNodeRight

