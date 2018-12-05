# Source : https://leetcode.com/problems/palindromic-substrings/description/

# Algo/DS : Array, String

# Complexity : O(n) n = no of digits


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        self.count = 0
        
        for i in range(len(s)):
            
            # to check odd length palindrome
            self.checkPalindrome(i,i,s)
            
            # to check even length palindrome
            self.checkPalindrome(i,i + 1,s)
        return self.count
    
    
    def checkPalindrome(self,i,j,s):
        while i>= 0 and j< len(s) and s[i] == s[j ]:
            self.count += 1
            
            # move towards left
            i -= 1
            
            # move towards right
            j += 1
            
    
            
            
        