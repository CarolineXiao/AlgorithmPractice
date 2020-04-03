"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        if root == None:
            return []
            
        result = []
        path = []
        self.traverse(root, target, path, result, 0)
        return result
    
    def traverse(self, root, target, path, result, path_sum):
        print(path)
        if root == None:
            return
        
        path.append(root.val)
        path_sum += root.val
        
        if root.left == None and root.right == None and path_sum == target:
            result.append(list(path))
            
        
        self.traverse(root.left, target, path, result, path_sum)
        self.traverse(root.right, target, path, result, path_sum)
        
        path.pop()
    
