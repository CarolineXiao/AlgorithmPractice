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
        # write your code here
        node, a_exist, b_exist = self.helper(root, A, B)
        if a_exist and b_exist:
            return node
        return None
        
    def helper(self, root, A, B):
        if root == None:
            return None, False, False
        
        left, left_a_exist, left_b_exist = self.helper(root.left, A, B)
        right, right_a_exist, right_b_exist = self.helper(root.right, A, B)
        
        a_exist = left_a_exist or right_a_exist or root == A
        b_exist = left_b_exist or right_b_exist or root == B
        print(a_exist, b_exist)
        
        if root == A or root == B:
            return root, a_exist, b_exist
        if left != None and right != None:
            return root, a_exist, b_exist
        if left != None:
            return left, a_exist, b_exist
        if right != None:
            return right, a_exist, b_exist
        if left == None and right == None:
            return None, a_exist, b_exist
        
