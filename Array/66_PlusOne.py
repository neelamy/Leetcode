# Source : https://leetcode.com/problems/plus-one/description/

# Algo/DS : Array

# Complexity : O(n), space = O(1)


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in reversed(range(len(digits))):
            temp = (digits[i] + carry) 
            digits[i] = temp % 10
            carry = temp / 10
        if carry : digits = [carry] + digits   
        return digits
