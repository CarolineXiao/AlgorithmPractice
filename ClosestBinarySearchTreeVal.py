"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        lower = root
        upper = root
        while root:
            if root.val == target:
                return root.val
            if root.val < target:
                lower = root
                root = root.right
                continue
            if root.val > target:
                upper = root
                root = root.left
        if abs(target - lower.val) < abs(upper.val - target):
            return lower.val
        
        return upper.val
