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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # recursion
        '''
        result = []
        self.traversal(root, result)
        return result
    
    def traversal(self, root, result):
        if root == None:
            return
        
        self.traversal(root.left, result)
        result.append(root.val)
        self.traversal(root.right, result)
        '''
        # without recursion
        
        dummy = TreeNode(0)
        dummy.right = root
        
        stack = [dummy]
        inorder = []
        
        while stack:
            cur_node = stack.pop()
            inorder.append(cur_node.val)
            if cur_node.right:
                node = cur_node.right
                while node:
                    stack.append(node)
                    node = node.left
                    
        return inorder[1:]
        
