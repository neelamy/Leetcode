# Source : https://leetcode.com/problems/valid-palindrome-ii/description/

# Algo/DS : String

# Complexity : O(n)

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0 , len(s) - 1
        while l < r:
            if  s[l] != s[r]:
               # print s[l: r], s[l + 1: r + 1]
                return (s[l: r] ==s[l: r][::-1]) or (s[l + 1: r + 1] ==s[l+1: r + 1][::-1])
            l += 1
            r -=1
        
        return True
                    
        