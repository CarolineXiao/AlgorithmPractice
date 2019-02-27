# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        
        current = root
        self.tr(current.left, result)
        result.append(current.val)
        self.tr(current.right, result)
        
        return result
            
            
    def tr(self, node, result):
        if node == None:
            return
        if node.left == None:
            result.append(node.val)
            self.tr(node.right, result)
        else:
            self.tr(node.left, result)
            result.append(node.val)
            self.tr(node.right, result)
            
