# Source : 	https://leetcode.com/problems/missing-number/description/

# Algo/DS : Array, bit manipulation

# Complexity : O(n)

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        xor = reduce(lambda x, y : x ^ y, range(n + 1))
        xor ^= reduce(lambda x, y : x ^ y, nums)
        return xor