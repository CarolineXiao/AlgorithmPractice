"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # recursion
        '''
        result = []
        self.traversal(root, result)
        return result
    
    def traversal(self, root, result):
        if root == None:
            return
        
        result.append(root.val)
        self.traversal(root.left, result)
        self.traversal(root.right, result)
        '''
        # without recursion
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        preorder = []
        while stack:
            cur_node = stack.pop()
            if cur_node.right:
                node = cur_node.right
                while node:
                    stack.append(node)
                    preorder.append(node.val)
                    node = node.left
        
        return preorder
