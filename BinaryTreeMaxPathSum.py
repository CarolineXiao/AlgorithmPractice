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
    @return: An integer
    """
    def maxPathSum(self, root):
        max_path_sum, max_single_path_sum = self.pathSum(root)
        return max_path_sum
        
    def pathSum(self, root):
        import sys
        if root == None:
            return -sys.maxsize, 0
            
        left_max, left_single_max = self.pathSum(root.left)
        right_max, right_single_max = self.pathSum(root.right)
        
        max_sum = max(left_max, right_max, left_single_max+right_single_max+root.val)
        single_max_sum = max(left_single_max+root.val, right_single_max+root.val, 0)
        
        return max_sum, single_max_sum
