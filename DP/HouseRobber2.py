# Source : https://leetcode.com/problems/house-robber/description/

# Algo/DS : DP

# Complexity : O(n)

class Solution(object):
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len (nums)
        if n == 0: return 0
        dp = [0] * (n)
        for i in xrange(n):            
            selected = nums[i] + dp[i - 2] if (i-2) >-1 else nums[i]
            notSelected = dp[i - 1] if (i-1) >-1 else 0
            dp[i] = max(selected , notSelected)            
        return dp[-1]

print Solution().rob([1])
