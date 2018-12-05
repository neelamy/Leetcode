# Source : https://leetcode.com/problems/add-strings/description/

# Algo/DS : String

# Complexity : O(n + m)


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        carry = 0
        ans = ""
        while carry or num1 or num2:
            sum = carry
            sum += int(num1[-1]) if num1 else 0
            sum += int(num2[-1]) if num2 else 0
            ans =  str(sum%10) + ans
            carry = sum /10
            num1 = num1[0:-1]
            num2 = num2[0:-1]
        return ans
            
        