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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # with recursion
        '''
        result = []
        self.traversal(root, result)
        return result
        
    def traversal(self, root, result):
        if root == None:
            return 
        
        self.traversal(root.left, result)
        self.traversal(root.right, result)
        result.append(root.val)
        '''
        
        # without recursion
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        postorer = []
        
        while stack:
            cur_node = stack.pop()
            if cur_node.right and cur_node.right.val != 0:
                stack.append(cur_node)
                node = cur_node.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                postorer.append(cur_node.val)
                cur_node.val = 0
        return postorer[:-1]
                
