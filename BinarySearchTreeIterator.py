"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    stack = []
    def __init__(self, root):
        # do intialization if necessary
        while root:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        if self.stack:
            return True
        else:
            return False
        

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        node = self.stack.pop()
        nextNode = node
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return nextNode.val
            
        
