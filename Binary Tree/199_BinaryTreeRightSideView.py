# Source : https://leetcode.com/problems/binary-tree-right-side-view/description/

# Algo/DS : Tree

# Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
         
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return [] 
        level = [root]
        d= []
        while level:
            d.append(level[-1].val)             
            temp = [ kid for node in level for kid in [node.left, node.right] if kid]
            level = temp
        return d
    
