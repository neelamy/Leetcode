# Source : https://leetcode.com/problems/increasing-triplet-subsequence/description/

# Algo/DS : LIS, DP

# Complexity : O(n)

# explanation : https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        head, tail = float("Inf"), float("Inf")
        
        for i in nums:
            if i <= head: head = i
            elif i <= tail : tail = i
            else: return True
        return False