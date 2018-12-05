# Source : https://leetcode.com/problems/sum-of-two-integers/description/

# Algo/DS : Bit Manipulation

# Complexity : O(n), space = O(1)


import numpy as np
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        # for solution refer CTCI Pg 541
        if b == 0 : return int(a)  
        # use numpy to change to int32 else for -ve number it exceeds number range and wont work
        sum = np.int32(a ^ b)
        carry = np.int32((a&b) << 1)
        return self.getSum(sum, carry)