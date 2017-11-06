# Source : https://leetcode.com/problems/binary-number-with-alternating-bits/description/

# Algo/DS : Bits

# Complexity : O(n)

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = 2
        while n:
            bit = n % 2
            
            if bit == temp : return False
            
            temp = bit
            
            n = n/2
            
        return True
            