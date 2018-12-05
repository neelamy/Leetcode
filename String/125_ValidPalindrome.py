# Source : https://leetcode.com/problems/valid-palindrome/description/

# Algo/DS : string, palindrome

# Complexity : O(n)

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()
        
        start, end = 0 , len(s) -1
        
        while start < end:
            while start < end and not s[start].isalnum(): start += 1
            while  start < end and not s[end].isalnum() : end -= 1
            if s[start] != s[end] : return False
            start += 1
            end -= 1
        return True
        