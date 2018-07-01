# Source : https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Algo/DS : Binary Tree

# Complexity : O(n), space = O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root : return  []        
        q = []
        q.append(root)
        levels = []
        while q and root:           
            levels.append([node.val for node in q])
            q = [ kid for node in q for kid in (node.left, node.right) if kid]                      
        return levels[::-1]
            
        