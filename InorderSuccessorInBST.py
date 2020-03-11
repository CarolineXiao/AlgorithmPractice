"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        
        
        while stack:
            node = stack.pop()
            Mynode = node
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if Mynode == p:
                if stack == []:
                    return None
                return stack[-1]
        return None
                        
