# Source : https://leetcode.com/problems/reverse-integer/description/

# Algo/DS : Numbers

# Complexity : O(1)

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            
            reverse_x = -int(str(abs(x))[::-1])
        else:
            reverse_x = int(str(abs(x))[::-1])
                    
        if -(2**31) <= reverse_x <= (2**31)-1 :
            return reverse_x
        else:
            return 0
        