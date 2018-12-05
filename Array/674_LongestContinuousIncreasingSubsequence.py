# Source : https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

# Algo/DS : Array, LIS

# Complexity : O(n)

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 0: return 0
        res = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1                
            else:
                count = 1
            res = max(res, count)
        return res
            
        