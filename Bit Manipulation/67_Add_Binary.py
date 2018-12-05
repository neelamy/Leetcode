# Source : https://leetcode.com/problems/add-binary/description/

# Algo/DS : Bit manipulation

# Complexity : O(n)

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res = ""
        while carry or a or b:
            sum = carry
            sum += int(a[-1]) if a else 0
            sum += int(b[-1] ) if b else 0
            
            res =  str(sum%2) + res
            carry = sum/2
           
            a = a[:-1]
            b= b[:-1]
        return res
        