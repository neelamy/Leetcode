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
    
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumpath(root, 0)
        
        
    def sumpath(self,root, val):
        if not root: return 0
        if not root.left and not root.right :
            return 10 * val + root.val
        return self.sumpath(root.left, 10 * val + root.val) + self.sumpath(root.right, 10 * val + root.val)
