# Source : https://leetcode.com/problems/divide-two-integers/description/

# Algo/DS : Maths

# Complexity : 

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = (dividend < 0 and  divisor > 0) or (dividend > 0 and  divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        
        while dividend >= divisor:
            temp, count = divisor, 1
            while dividend >= temp:
                result += count
                dividend -= temp
                count = count << 2
                temp = temp << 2
                
        if negative : result = -result
        
        return min(max(result,-2147483648),2147483647)
        