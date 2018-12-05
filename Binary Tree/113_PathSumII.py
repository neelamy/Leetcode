# Source : https://leetcode.com/problems/path-sum-ii/description/

# Algo/DS : Binary Tree

# Complexity : O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.result = []
        
        self.getpath(root, [], 0, sum)
        
        return self.result
    
    def getpath(self, root, path,temp_sum, final_sum ):
        if not root: return 
        if not root.left and not root.right:
            if temp_sum + root.val == final_sum : self.result.append(path + [root.val])
        
        self.getpath(root.left, path + [root.val] ,temp_sum + root.val , final_sum ) 
        self.getpath(root.right, path + [root.val] ,temp_sum + root.val , final_sum )
            
            
            
            
