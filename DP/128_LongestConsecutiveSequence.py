
# Source : https://leetcode.com/problems/longest-consecutive-sequence/description/

# Algo/DS : Array, LIS, DP

# Complexity : O(n) n = no of digits

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # convert nums to set so that searching is O(1)
        nums = set(nums)
        best = 0       
        for no in nums:

            # if its previous number already exists then ignore
            # as this number has been considered
            if no - 1 in nums: continue
            next = 0

            # check for consecutive numbers starting from this number
            while no + next in nums:
                best = max(best, no + next - no + 1)
                next += 1
        # return best
        return best
            
        
        
        
        