# Source : https://leetcode.com/problems/subsets/description/

# Algo/DS : DP

# Complexity : O(n *2^n)


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        
        for number in nums:
            result += [ current + [number] for current in result]
        return result
        