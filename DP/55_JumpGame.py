
# Source : https://leetcode.com/problems/jump-game/description/

# Algo/DS : Array, DP

# Complexity : O(n)


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2: return True
        
        if nums[0] == 0 : return False
        
        max_length = 0
        
        for index, val in enumerate(nums[:-1]):
            if max_length < index : return False
            max_length = max(max_length, index+ val)
            
            
        #print max_length
        return max_length >= len(nums) - 1 
            