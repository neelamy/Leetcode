# Source : https://leetcode.com/problems/palindrome-number/description/

# Algo/DS : Number

# Complexity : O(ns)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 : return False
        temp =  x
        reverse = 0
        while temp:
            reverse = reverse * 10 + temp %10
            temp /= 10
            
        return x == reverse
            
        