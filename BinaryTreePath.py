"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [str(root.val)]
        
        leftPath = self.binaryTreePaths(root.left)
        rightPath = self.binaryTreePaths(root.right)
        
        path = []
        
        for p in leftPath + rightPath:
            path.append(str(root.val) + '->' + p)
        
        return path
        
