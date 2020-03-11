"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        ancestorA = []
        ancestorB = []
        self.findAncestor(A, ancestorA)
        self.findAncestor(B, ancestorB)
        
        i = len(ancestorA) - 1
        j = len(ancestorB) - 1
        while i>= 0 and j>=0:
            if ancestorA[i] != ancestorB[j]:
                break
            i -= 1
            j -= 1
        return ancestorA[i+1]
        
        
    def findAncestor(self, node, lst):
        while node:
            lst.append(node)
            node = node.parent
