# Source : https://leetcode.com/problems/single-number/description/
# Given an array of integers, every element appears twice except for one. Find that single one.

# Algo/DS : Bit Maniputlation

# Complexity : O(n)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return reduce(lambda x, y : x ^ y , nums)
 