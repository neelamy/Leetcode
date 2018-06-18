# Source : https://leetcode.com/problems/3sum/description/

# Algo/DS : Array

# Complexity : O(n^2)

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        str = str.strip()
        if str == "": return 0
    
        sign = -1 if str[0] == "-" else 1
            
        if str[0] in ['+', '-'] : 
            str = str[1:]
        
        i, ans =0 ,0
        
        while i < len(str) and str[i].isdigit():         
            ans = (ans* (10)) + (ord(str[i]) - ord('0'))
            i += 1
        
        return max(-(2**31), min(sign * ans, (2**31) - 1 ))