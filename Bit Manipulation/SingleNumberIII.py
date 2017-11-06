# Source : https://leetcode.com/problems/single-number-iii/description/

# Algo/DS : Array

# Complexity : O(n)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        xor = reduce(lambda x, y: x ^ y, nums)
              
       # Get the rightmost set bit in set_bit_no
        set_bit = xor & ~(xor - 1)

        x = reduce(lambda x, y : x^y ,[i for i in nums if set_bit & i])

        y = reduce(lambda x, y : x^y ,[i for i in nums if not set_bit & i])

        return x , y
                      