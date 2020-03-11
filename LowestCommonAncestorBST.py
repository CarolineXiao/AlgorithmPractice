"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        val = root.val
        pval = p.val
        qval = q.val
        
        if val < pval and val < qval:
            return self.lowestCommonAncestor(root.right, p, q)
        if val > pval and val > qval:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
