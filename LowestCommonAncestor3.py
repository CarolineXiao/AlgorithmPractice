"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        res, a_exists, b_exists = self.helper(root, A, B)
        if a_exists and b_exists:
            return res
        return None
        
        
    def helper(self, root, A, B):
        if root == None:
            return None, False, False
        
        left, a_exists_left, b_exists_left = self.helper(root.left, A, B)
        right, a_exists_right, b_exists_right = self.helper(root.right, A, B)
        
        a_exists = a_exists_left or a_exists_right or root == A
        b_exists = b_exists_left or b_exists_right or root == B
        
        if root == A or root == B:
            return root, a_exists, b_exists
            
        if left != None and right != None:
            return root, a_exists, b_exists
        if left != None:
            return left, a_exists, b_exists
        if right != None:
            return right, a_exists, b_exists
        
        return None, a_exists, b_exists
        
        
