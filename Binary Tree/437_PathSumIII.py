# Source : https://leetcode.com/problems/path-sum-iii/description/

# Algo/DS : Binary Tree

# Complexity : O(n)

# Explanation: https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-:-)

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
        :rtype: int
        """
        self.count = 0
        self.d = {}
        self.d[0] = 1
        self.path(root, sum, 0)
        
        return self.count
    
        
        
    def path(self, node, sum, current_sum):
        if not node: return 0
        
        new_sum = current_sum + node.val
        
        required_val = new_sum -sum
        if required_val in self.d: self.count += self.d[required_val]
        self.d[new_sum] = self.d.get(new_sum, 0) + 1
        
        self.path(node.left, sum, new_sum)
        self.path(node.right, sum, new_sum)
        self.d[new_sum] -=1
        
        
        