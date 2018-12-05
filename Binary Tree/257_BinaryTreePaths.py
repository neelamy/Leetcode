# Source : https://leetcode.com/problems/binary-tree-paths/description/

# Algo/DS : Tree

# Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.path =[]
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.findpath(root, "")        
        return self.path
    
    def findpath(self, root, temp):
        if not root : return        
        if not root.left and not root.right:
            self.path.append(temp + str(root.val))
            return
        self.findpath( root.left, temp + str(root.val) + "->" )
        self.findpath( root.right, temp + str(root.val) + "->" )
        
