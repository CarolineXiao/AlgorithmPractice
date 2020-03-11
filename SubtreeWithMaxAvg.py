"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        mySum, myNodeNum, myMaxAvg, myMaxNode = self.helper(root)
        return myMaxNode
        
    
    def helper(self, root):
        if root == None:
            return 0, 0, -sys.maxsize, None
        
        leftSum, leftNodeNum, leftMaxAvg, leftMaxNode = self.helper(root.left)
        rightSum, rightNodeNum, rightMaxAvg, rightMaxNode = self.helper(root.right)
        
        curSum = leftSum + rightSum + root.val
        curNodeNum = leftNodeNum + rightNodeNum + 1
        curAvg =  curSum / curNodeNum
        curMaxAvg = max(curAvg, leftMaxAvg, rightMaxAvg)
        
        if curMaxAvg == curAvg:
            return curSum, curNodeNum, curMaxAvg, root
        if curMaxAvg == leftMaxAvg:
            return curSum, curNodeNum, curMaxAvg, leftMaxNode
        if curMaxAvg == rightMaxAvg:
            return curSum, curNodeNum, curMaxAvg, rightMaxNode
        
