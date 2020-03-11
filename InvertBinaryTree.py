"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        stack = []
        node = root
        visited = set()
        while node:
            stack.append(node)
            node = node.left
        
        while stack:
            node = stack.pop()
            if node.right and node.right not in visited:
                stack.append(node)
                node = node.right
                visited.add(node)
                while node:
                    stack.append(node)
                    node = node.left
            elif node.right and node.right in visited:
                temp = node.left
                node.left = node.right
                node.right = temp
            elif node.left:
                node.right = node.left
                node.left = None
        return root
                          
