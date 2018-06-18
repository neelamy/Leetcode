
# Source : https://leetcode.com/problems/implement-strstr/description/

# Algo/DS : String

# Complexity : O(n ^2)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h = len(haystack)
        n = len(needle)
        
        if   n == 0: return 0
        
        for i in range(h):
            if i + n > h : return -1
            l = 0
            while( i + l < h and l < n  and haystack[i+ l] == needle[l]): 
                l += 1
            if l == n  : return i
            
        return -1
            
        
        