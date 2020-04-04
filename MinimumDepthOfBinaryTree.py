"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if root == None:
            return 0
        
        #depth = 0
        queue = []
        queue.append((root,1))
        
        while queue:
            node, depth = queue.pop(0)
            print(node.val)
            print(queue)
            if node.left == None and node.right == None :
                return depth
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        
