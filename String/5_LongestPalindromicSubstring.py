# Source : https://leetcode.com/problems/longest-palindromic-substring/description/

# Algo/DS : Array, String

# Complexity : O(n^2)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
  
        result = ""       
        for i in range(len(s)):          
            # to check odd length palindrome
            temp = self.checkPalindrome(i,i,s)
            if len(result) < len(temp):
                result = temp
            
            # to check even length palindrome
            temp = self.checkPalindrome(i,i + 1,s)
            if len(result) < len(temp):
                result = temp
        return result
    
    
    def checkPalindrome(self,i,j,s):
        while i>= 0 and j< len(s) and s[i] == s[j ]:
           
            # move towards left
            i -= 1
            
            # move towards right
            j += 1
            
        return s[i+1: j]
    
            
