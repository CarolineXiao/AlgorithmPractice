"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        dummy = TreeNode(0)
        dummy.left = None
        dummy.right = root
        stack = []
        stack.append(dummy)
        inorder = []

        for i in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                
                while node:
                    stack.append(node)
                    node = node.left
            if not stack:
                return None
                
        return stack[-1].val
            
