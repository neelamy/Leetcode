# Source : https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Algo/DS : Binary Tree

# Complexity : O(n log n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.sumpath(root, 0, sum1) == True
    
    def sumpath(self,root, val, sum1):
        if not root: return 0
        if not root.left and not root.right :
            return ( val + root.val) == sum1
        return self.sumpath(root.left,  val + root.val, sum1) or self.sumpath(root.right,  val + root.val, sum1)
