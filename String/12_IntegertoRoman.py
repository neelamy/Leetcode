# Source : https://leetcode.com/problems/integer-to-roman/description/
# Given an integer, convert it to a roman numeral, and return a string corresponding to its roman numeral version

# Algo/DS : String

# Complexity :

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        ans = ""
        
        A =[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1]
        B =['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX' ,'V', 'IV', 'I']
        
        for index, number in enumerate(A):
            while num >= number:
                ans += B[index]
                num -=number
                
        return ans
        
        