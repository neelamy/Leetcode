# Source : https://leetcode.com/problems/roman-to-integer/description/

# Algo/DS : String

# Complexity : O(1)

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ans = 0      
        d ={"I" :1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M": 1000}
        n = len(s)
        i = 0
        for i in xrange(n):           
            if i < n - 1 and d[s[i]] < d[s[i+1]]:
                ans -=  d[s[i]]                
            else:
                ans += d[s[i]]             
        return ans