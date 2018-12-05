# Source : https://leetcode.com/problems/number-of-1-bits/description/

# Algo/DS : Bits

# Complexity : O(n) n = no of bits


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        
        i = 1
        while n:
            
            if i & n : count += 1
            n = n>> 1
        return count
            
        