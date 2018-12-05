# Source : https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Algo/DS : Tree

# Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.get_depth(root) 
    
    def get_depth(self,root):
        if root:          
            l = self.get_depth(root.left)
            r = self.get_depth(root.right)
            return min(l,r) + 1 if l>0 and r >0 else max(l,r)+1
        
        
        return 0