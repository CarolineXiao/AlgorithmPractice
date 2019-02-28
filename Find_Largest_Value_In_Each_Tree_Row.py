# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        result = []
        
        result.append(root.val)
        row = []
        row.append(root)
        self.getLargest(row, result) 
        return result
    
    def getLargest(self, row, result):
        cr = []
        next_row = []
        for node in row:
            if node.left != None:
                cr.append(node.left.val)
                next_row.append(node.left)
            if node.right != None:
                cr.append(node.right.val)
                next_row.append(node.right)
        if cr != []:
            result.append(max(cr))
        if next_row != []:
            self.getLargest(next_row, result)
