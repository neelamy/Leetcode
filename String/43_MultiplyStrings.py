# Source : https://leetcode.com/problems/multiply-strings/description/

# Algo/DS : Tree

# Complexity : O(n1 * n2)

class Solution(object):
    
    def add(self, num1, num2):
        ans = ""
        result = ""
        carry = 0
        while num1 or num2 or carry:
            n1 = ord(num1[-1]) - ord('0') if num1 else 0
            n2 = ord(num2[-1]) - ord('0') if num2 else 0
            result = str((n1+n2 + carry)%10) + result 
            carry = (n1+n2 + carry) / 10
            num1 = num1[0: len(num1) -1 ] if num1 else []
            num2 = num2[0: len(num2) -1 ] if num2 else []
        return result
    
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """      
        if num1 == '0' or num2 == '0' : return '0'
        if len(num1) < len(num2):
            num1, num2 = num2, num1      
        result = ""
        iter = 0
        while num1:
            number1 = ord(num1[-1]) - ord('0')
            temp = num2
            remainder = ""           
            carry = 0
            while temp:
                number2 = ord(temp[-1]) - ord('0')
                remainder = str(((number2 * number1) + carry) % 10) + remainder
                carry = ((number2 * number1) + carry) / 10 
                temp =temp[0 : len(temp) - 1]
            if carry : remainder = str(carry) + remainder
            remainder  = remainder +"0"*iter
            result = self.add(result, remainder)
            num1 =num1[0 : len(num1) - 1]
            iter += 1
        return result
                
                
                
        